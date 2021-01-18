"""Python3"""
import math

# Verilen değerler
W_0 = 62636856.0  # Referans potansiyel m²/s²
W_P = 6.262129752474 * pow(10, 7)  # Gravite potansiyel (8. değer) m²/s²

# Jeopotansiyel sayı (yükseklik) hesabı
C_P = W_0 - W_P
print("Jeopotansiyel yükseklik: %.4f" % C_P)
