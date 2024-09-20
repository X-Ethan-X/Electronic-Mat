import numpy as np
import pyqtgraph.opengl as gl
from queue import Queue

SIZE_X = 25
SIZE_Y = 34


class matPlot(gl.GLViewWidget):
    def __init__(self) -> None:
        super().__init__()
        self.data_q = Queue()
        ## Add a grid to the view
        g = gl.GLGridItem()
        g.setSize(SIZE_X, SIZE_Y, 500)
        # g.scale(1, 1, 1)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        self.addItem(g)
        space_x = np.linspace(-(SIZE_X / 2), (SIZE_X / 2), SIZE_X)
        space_y = np.linspace(-(SIZE_Y / 2), (SIZE_Y / 2), SIZE_Y)
        self.plot = gl.GLSurfacePlotItem(
            x=space_x,
            y=space_y,
            shader="heightColor",
            # drawEdges=True,
            computeNormals=False,
            smooth=True,
        )
        """
        colors fragments by z-value.
        This is useful for coloring surface plots by height.
        This shader uses a uniform called "colorMap" to determine how to map the colors:
           red   = pow(colorMap[0]*(z + colorMap[1]), colorMap[2])
           green = pow(colorMap[3]*(z + colorMap[4]), colorMap[5])
           blue  = pow(colorMap[6]*(z + colorMap[7]), colorMap[8])
        """
        self.plot.shader()["colorMap"] = np.array(
            [0.7, -0.1, 1, 0.2, -0.1, 1, -0.7, -0.2, 1]
        )
        # self.plot.translate(0, 0, 0)
        self.addItem(self.plot)

    def update_plot(self):
        if not self.data_q.empty():
            data = self.data_q.get()
            z = data / 50
            self.plot.setData(z=z)
