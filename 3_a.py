"""Python3"""
import math

# Verilen değerler
G = 9.796232618985 * pow(10, 5) / 100000  # Gravite (7. değer) (Gal)

W_P = 6.262129752474 * pow(10, 7)  # Gravite potansiyel (8. değer) m²/s²
# Sabit değerler

# Jeopotansiyel sayı hesabı
W_0 = 62636856.0  # Referans potansiyel m²/s²
C_P = W_0 - W_P
print("Jeopotansiyel sayı: %.4f" % C_P)

# Jeopotansiyel yükseklik hesabı
H = C_P / G
print("Jeopotansiyel yükseklik: %.4f" % H)
