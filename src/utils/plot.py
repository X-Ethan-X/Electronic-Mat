# coding=UTF-8

import os
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from queue import Queue

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

SIZE_X = 32
SIZE_Y = 32


def get_matrix(data):

    row, col = SIZE_Y, SIZE_X
    matrix = data.values[:, -(SIZE_X * SIZE_Y):].astype(float)
    matrix.resize(matrix.shape[0], row, col)
    return matrix


def matrix_analysis(matrix):
    # Mean Value
    mean_matrix = np.mean(matrix, axis=0)
    # Standard Deviation
    std_matrix = np.std(matrix, axis=0)
    # Difference coefficient
    coe_matrix = (std_matrix / (mean_matrix + 1e-7)) * 100
    # Zeros Crossing
    zc_matrix = np.sum(np.sign(matrix - 25), axis=0)
    return mean_matrix, std_matrix, coe_matrix, zc_matrix


def matrix2pictures(matrix, file_path):
    matrix = matrix.T
    row, column = matrix.shape
    x = np.linspace(0, column, column)
    y = np.linspace(0, row, row)
    X, Y = np.meshgrid(x, y)
    fig, ax = plt.subplots()
    fig.set_size_inches(14.8, 12.8)
    ax.set_position([0.05, 0.05, 0.93, 0.93])
    # Plot grid.
    ax.grid(c='k', ls='-', alpha=0.3)
    ax.set(xlim=(0, column), xticks=np.arange(0, column + 1, 1),
           xticklabels=['C' + str(i) for i in range(0, column + 1, 1)],
           ylim=(0, row), yticks=np.arange(0, row + 1, 1),
           yticklabels=['R' + str(i) for i in range(0, row + 1, 1)])
    cs = ax.contourf(X, Y, matrix, cmap="cool")
    fig.colorbar(cs)
    plt.savefig(file_path)
    plt.close()


class MatMatrix(FigureCanvasQTAgg):
    def __init__(self):
        self.fig = Figure(
            figsize=(2, 2), dpi=70, facecolor="#f0f0f0", edgecolor="#f0f0f0"
        )
        self.axes = self.fig.add_subplot(111, position=[0.05, 0.05, 0.93, 0.93])
        super().__init__(self.fig)
        self._get_animation(np.zeros((SIZE_X, SIZE_Y)))

    def _get_animation(self, matrix):
        plt.rcParams["figure.figsize"] = (6, 8.16)
        matrix = matrix.T
        row, column = matrix.shape
        x = np.linspace(0, column, column)
        y = np.linspace(0, row, row)
        X, Y = np.meshgrid(x, y)
        self.axes.set(
            xlim=(0, column),
            xticks=np.arange(0, column + 1, 1),
            xticklabels=["C" + str(i) for i in range(0, column + 1, 1)],
            ylim=(0, row),
            yticks=np.arange(0, row + 1, 1),
            yticklabels=["R" + str(i) for i in range(0, row + 1, 1)],
        )
        self.axes.grid(True, linestyle='-.', color='k')
        cs = self.axes.contourf(X, Y, matrix, cmap="cool")
        return cs

    def _get_artist(self, i):
        pass


class MatMatrixPlot(MatMatrix):
    def __init__(self):
        super().__init__()
        self.matrix_queue = Queue()
        self.index = 0
        self.animation = None

    def _get_artist(self, i):
        while self.matrix_queue.empty():
            time.sleep(0.5)
        data = self.matrix_queue.get()
        return self._get_animation(data),

    def plot_start(self):
        self.clear()
        self.animation = anim.FuncAnimation(
            self.fig, func=self._get_artist, frames=None, blit=True, repeat=False, cache_frames=False,
        )

    def plot_stop(self):
        self.animation.event_source.stop()


class MatMatrixRecord(MatMatrix):
    def __init__(self):
        super().__init__()
        self.file_path = None
        self.matrix = None
        self.mean_matrix, self.std_matrix, self.coe_matrix, self.zc_matrix = [None for _ in range(4)]

    def upload_data(self, file_path):
        df = pd.read_csv(file_path)
        self.file_path = file_path[:-4] + '/'
        self.matrix = get_matrix(df)
        self.mean_matrix, self.std_matrix, self.coe_matrix, self.zc_matrix = matrix_analysis(self.matrix)

    def _get_artist(self, i):
        return self._get_animation(self.matrix[i])

    def show(self, i):
        self.draw_idle()
        self.axes.set_title("Replay")
        self._get_artist(i)

    def analysis(self, value):
        self.draw_idle()
        if value == 0:
            self.axes.set_title("Mean Value")
            self._get_animation(self.mean_matrix)
        elif value == 1:
            self.axes.set_title("Standard Deviation")
            self._get_animation(self.std_matrix)
        elif value == 2:
            self.axes.set_title("Coefficients Value")
            self._get_animation(self.coe_matrix)
        elif value == 3:
            self.axes.set_title("Zero Crossing Value")
            self._get_animation(self.zc_matrix)

    def generate_original_pictures(self):
        from PySide6.QtWidgets import QProgressDialog
        from PySide6.QtCore import QCoreApplication

        os.makedirs(self.file_path, exist_ok=True)
        num = self.matrix.shape[0]

        progressDialog = QProgressDialog('Generating...', 'Terminate', 0, num)
        progressDialog.setWindowTitle("Pictures Generation")
        for i in range(num):
            try:
                matrix2pictures(self.matrix[i], self.file_path + str(i) + '.png')
                progressDialog.setValue(i)
                QCoreApplication.processEvents()
                if progressDialog.wasCanceled():
                    break
            except ValueError:
                raise ValueError

    def generate_analysed_pictures(self):
        os.makedirs(self.file_path, exist_ok=True)
        matrix2pictures(self.mean_matrix, self.file_path + '_mean_matrix.png')
        matrix2pictures(self.std_matrix, self.file_path + '_std_matrix.png')
        matrix2pictures(self.coe_matrix, self.file_path + '_coe_matrix.png')
        matrix2pictures(self.zc_matrix, self.file_path + '_zc_matrix.png')
