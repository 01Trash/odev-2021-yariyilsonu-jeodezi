"""Python3"""
import math

# Verilen değerler
enlem_derece = 38 + (45 / 60) + (0 / 3600)
enlem_radyan = enlem_derece * (math.pi / 180)
boylam_derece = 39 + (30 / 60) + (0 / 3600)
boylam_radyan = boylam_derece * (math.pi / 180)
h = 1025

# Sabit değerler
a = 6378137
e_Kare = 0.006694380023
f = 1 / 298.257222101
k = 0.001931851353
m = 0.00344978600308
gama_ekvator = 9.7803267715
GM = 3986005 * pow(10, 8)  # m^3/s^2
w = 7.292115 * pow(10, (-5))  # rad/s
J_2 = 1.08263000 * pow(10, (-3))
J_4 = -2.37091222 * pow(10, (-6))
J_6 = 6.0834706 * pow(10, (-9))
J_8 = -1.427 * pow(10, (-11))


# Gama 0 değerinin hesabı
gama_0 = gama_ekvator * ((1 + k * pow(math.sin(enlem_radyan), 2)) /
                         pow(1 - e_Kare * pow(math.sin(enlem_radyan), 2), 0.5))
print(gama_0)

# Gama h değerinin hesabı
gama_h = gama_0 * (1 - (2 * h) / a * (1 + f + m - 2 * f *
                                      pow(math.sin(enlem_radyan), 2)) + (3 / pow(a, 2)) * pow(h, 2))
print(gama_h)
