# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import helpers as hp

def problematique():

    wc_pb = 2 * np.pi * 700
    wc_pb2 = 2 * np.pi * 5000

    wc_ph = 2 * np.pi * 1000
    wc_ph2 = 2 * np.pi * 7000

    num_pb, den_pb = signal.butter(2, wc_pb, 'low', analog=True)
    num_ph, den_ph = signal.butter(2, wc_ph, 'high', analog=True)

    z_pb, p_pb, k_pb = signal.tf2zpk(num_pb, den_pb)
    z_ph, k_ph, k_ph = signal.tf2zpk(num_ph, den_ph)

    num_pb2, den_pb2 = signal.butter(2, wc_pb2, 'low', analog=True)
    num_ph2, den_ph2 = signal.butter(2, wc_ph2, 'high', analog=True)

    z_pb2, p_pb2, k_pb2 = signal.tf2zpk(num_pb2, den_pb2)
    z_ph2, p_ph2, k_ph2 = signal.tf2zpk(num_ph2, den_ph2)


    mag, ph, w, fig, ax = hp.bodeplot(num_pb, den_pb,'')
    mag, ph, w, fig, ax = hp.bodeplot(num_ph, den_ph,'')
    mag, ph, w, fig, ax = hp.bodeplot(num_pb2, den_pb2,'')
    mag, ph, w, fig, ax = hp.bodeplot(num_ph2, den_ph2, '')


    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problematique()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
