import time
from traceback import print_exc
import numpy as np
from serial import Serial
from serial.tools.list_ports import comports
from threading import Thread
from queue import Queue

from datetime import datetime

SIZE = 48


class Mat(Thread):
    from .plot import SIZE_X, SIZE_Y

    Values = np.zeros((SIZE_X, SIZE_Y), dtype=int)

    def __init__(self) -> None:
        super().__init__(daemon=True)
        self.data_q = Queue()
        self.temp_Values = self.Values.copy()
        self.ser = Serial(port=self.find_dev(), baudrate=115200, timeout=3.0)
        time.sleep(1)
        self.ser.write(b"S")
        self.run_flag = True
        self.last = time.perf_counter()
        from plot import SIZE_X, SIZE_Y

        self.x, self.y = SIZE_X, SIZE_Y
        self.index_x, self.index_y = SIZE - SIZE_X, SIZE - SIZE_Y
        self.start()

    @staticmethod
    def find_dev():
        devices = comports()
        for device in devices:
            if device.pid == 0x0483 and device.vid == 0x16C0:
                return device.device
        else:
            raise Exception("Device not found")

    def _ReceiveMap(self):
        points = int.from_bytes(self.ser.read(2), byteorder="big")
        Values = np.zeros((self.x, self.y), dtype=int)
        self.ser.read(2)
        for _ in range(points):
            y = self.ser.read()[0]
            x = self.ser.read()[0]
            data = int.from_bytes(self.ser.read(2), byteorder="big")
            if x < self.index_x or y < self.index_y:
                continue
            Values[x - self.index_x, y - self.index_y] = data
        self.temp_Values = Values

    def run(self):
        self.ser.flush()
        self.task2 = Thread(target=self.send_data)
        self.task2.start()
        try:
            while self.run_flag:
                time.sleep(0.002)
                self.ser.write(b"R")
                if self.ser.read() == b"\x4e":  # 0x48
                    self.ser.read()
                    self._ReceiveMap()
                else:
                    self.ser.flush()
        except Exception:
            self.run_flag = False

    def send_data(self):
        start = time.perf_counter()
        gap = 0.0
        while self.run_flag:
            time.sleep(0.002)
            # print(time.perf_counter()-last)
            if (time.perf_counter() - start) > gap:
                # interval = time.perf_counter() - self.last
                # print(f"FS: {1/interval},{datetime.now()},")
                # self.last = time.perf_counter()
                gap += 1 / 8
                self.data_q.put(
                    (
                        datetime.now().strftime("%Y%m%d %H:%M:%S.%f")[:-3],
                        np.fliplr(self.temp_Values).copy(),
                    )
                )
                # print(np.max(self.temp_Values))

    def close_dev(self):
        self.run_flag = False
        self.join()
        self.task2.join()
        try:
            self.ser.close()
        except Exception:
            print_exc()
