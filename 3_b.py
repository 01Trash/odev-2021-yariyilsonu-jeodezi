"""Python3"""
import math

# Verilen değerler
W_0 = 62636856.0  # Referans potansiyel m²/s²
gama_0 = 980.6199203 / 100  # Gal
G_P = 9.816907178897 * pow(10, 5) / 100000  # Yer gravite (Gal)
W_P = 6.262129752474 * pow(10, 7)  # Gravite potansiyel (8. değer) m²/s²
enlem_derece = 38 + (45 / 60) + (0 / 3600)
enlem_radyan = enlem_derece * (math.pi / 180)

# Sabit değerler
a = 6378137
f = 1 / 298.257222101
m = 0.00344978600308

# Jeopotansiyel sayı hesabı
C_P = W_0 - W_P
# print(C_P)

# Dinamik yükseklik hesabı
H_D = C_P / gama_0
print("Dinamik yükseklik: %.4f" % H_D)

# Helmert ortometrik yükseklik hesabı
H_D = H_D / 1000
g_cizgi = G_P + 0.0424 * H_D
H_O = C_P / g_cizgi
print("Helmert ortometrik yükseklik: %.4f" % H_O)

# Normal yükseklik hesabı
gama_cizgi = gama_0 * (1 - (1 + f + m - 2 * f *
                            pow(math.sin(enlem_radyan), 2)) * H_O / a + pow(H_O, 2) / pow(a, 2))
# print(gama_cizgi)
H_N = C_P / gama_cizgi
print("Normal yükseklik: %.4f" % H_N)
