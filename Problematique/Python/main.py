# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import helpers as hp
from helpers import bodeplot


def problematique():

    wc_pb = 2 * np.pi * 700
    wc_pb2 = 2 * np.pi * 5000

    wc_ph2 = 2 * np.pi * 1000
    wc_ph = 2 * np.pi * 7000

    num_pb, den_pb = signal.butter(2, wc_pb, 'low', analog=True)
    num_ph, den_ph = signal.butter(2, wc_ph, 'high', analog=True)


    z_pb, p_pb, k_pb = signal.tf2zpk(num_pb, den_pb)
    #hp.pzmap1(z_pb, p_pb, 'Passe bas')

    z_ph, p_ph, k_ph = signal.tf2zpk(num_ph, den_ph)
    #hp.pzmap1(z_ph, p_ph, 'Passe haut')

    num_pb2, den_pb2 = signal.butter(2, wc_pb2, 'low', analog=True)
    num_ph2, den_ph2 = signal.butter(2, wc_ph2, 'high', analog=True)

    z_pb2, p_pb2, k_pb2 = signal.tf2zpk(num_pb2, den_pb2)
    z_ph2, p_ph2, k_ph2 = signal.tf2zpk(num_ph2, den_ph2)

    zs, ps, ks = hp.seriestf(z_pb2, p_pb2, k_pb2, z_ph2, p_ph2, k_ph2)
    hp.pzmap1(zs, ps, 'passe bande')

    num_s, den_s = signal.zpk2tf(zs,ps,ks)
    hp.bodeplot(num_s, den_s, 'lieu de bode du passe bande')

    zp, pp, kp = hp.paratf(z_pb, p_pb, k_pb*-1, z_ph, p_ph, k_ph*-1)

    num_f, den_f = [], []
    for i in range(5,25):
        zf, pf, kf = hp.paratf(zp, pp, kp, zs, ps, ks * (1-i/100))

        num_f, den_f = signal.zpk2tf(zf, pf, kf)
        hp.bodeplot(num_f, den_f, '')

    # pour un graphique sans simulation de plusieurs valeurs de gains
    # zf, pf, kf = hp.paratf(zp, pp, kp, zs, ps, ks )

   #  num_f, den_f = signal.zpk2tf(zf, pf, kf)


    mags, phs, ws, fig, ax = hp.bodeplot(num_f, den_f, '')
    hp.grpdel1(ws, -np.diff(phs)/np.diff(ws), 'H1^H2^H3^H4')

    plt.show()



def phase_calc():

    r = -np.arctan((8.88*10e3*2500)/((-2500*2500)+3.94*10e7))
    r2 = -np.arctan((4.44*10e4*2500)/((-2500*2500)+9.86*10e8))

    print(r2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problematique()
    #phase_calc()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
