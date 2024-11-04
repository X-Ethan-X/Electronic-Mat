import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


def LFA_Calculate(data, low, high):
    low_freq_amplitude_matrix = np.zeros((data.shape[1], data.shape[2]))
    fs = 20
    # 计算低频振幅
    for x in range(data.shape[1]):
        for y in range(data.shape[2]):
            column_data = data[:, x, y]
            mean_value = np.mean(column_data)
            normalized_data = (column_data / mean_value) - mean_value if mean_value > 0 else column_data
            fft_data = np.fft.fft(normalized_data)
            n = len(normalized_data)
            f = np.fft.fftfreq(n, d=1/fs)
            fft_magnitude = np.abs(fft_data)
            low_freq_indices = np.where((f >= low) & (f <= high))[0]
            low_freq_amplitude_matrix[x, y] = np.mean(fft_magnitude[low_freq_indices])
    low_freq_amplitude_matrix[np.isnan(low_freq_amplitude_matrix)] = np.nanmean(low_freq_amplitude_matrix)
    plt.imshow(low_freq_amplitude_matrix.T, aspect='auto', cmap='jet')
    plt.colorbar()
    plt.title('低频振幅 (0.01-0.08 Hz) 热力图')
    plt.xlabel('传感器列')
    plt.ylabel('传感器行')
    plt.show()
