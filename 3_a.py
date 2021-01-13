"""Python3"""
import math

# Verilen değerler
W_P = 6.262710435224 * pow(10, 7)  # Gravite potansiyel (16. değer) m^2/s^2
G = 9.797976534719 * pow(10, 5) / 100000  # Gravite (15. değer) (Gal)

# Sabit değerler
W_0 = 62636856.0  # Referans potansiyel m^2/s^2

# Jeopotansiyel sayı hesabı
C_P = W_0 - W_P
print("Jeopotansiyel sayı: %.4f" % C_P)

# Jeopotansiyel yükseklik hesabı
H = C_P / G
print("Jeopotansiyel yükseklik: %.4f" % H)
