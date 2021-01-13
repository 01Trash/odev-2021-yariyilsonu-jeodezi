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
b = 6356752.3141
e_Kare = 0.006694380023
e_Ussu_Kare = 0.006739496775
GM = 3986005 * pow(10, 8)  # m^3/s^2
w = 7.292115 * pow(10, (-5))  # rad/s
J_2 = 1.08263000 * pow(10, (-3))
J_4 = -2.37091222 * pow(10, (-6))
J_6 = 6.0834706 * pow(10, (-9))
J_8 = -1.427 * pow(10, (-11))

# c değerinin hesabı
c = pow(a, 2) / b

# N değerinin hesabı
N = c / pow((1 + e_Ussu_Kare * pow(math.cos(enlem_radyan), 2)), 0.5)
# print(N)

# x hesabı
x = (N + h) * math.cos(enlem_radyan) * math.cos(boylam_radyan)
# y hesabı
y = (N + h) * math.cos(enlem_radyan) * math.sin(boylam_radyan)
# z hesabı
z = ((1 - e_Kare) * N + h) * math.sin(enlem_radyan)
# print(x)
# print(y)
# print(z)

# r hesabı (radyal bileşen)
r = pow((x * x + y * y + z * z), 0.5)
# Jeosantrik boylam hesabı
yeni_boylam = math.atan(y / x)
#yeni_boylam_radyan = yeni_boylam * (180 / math.pi)
# Kutup uzunluğu hesabı
yeni_enlem = math.atan(pow((x * x + y * y), 0.5) / z)
#yeni_enlem_radyan = yeni_enlem * (180 / math.pi)
#print("r: ", r)
# print(yeni_boylam)
# print(yeni_enlem)


""" ∀ n ≥ 2, m = 0
Pn(t) == P_n_t
Pn-1(t) == P_n_1_t
Pn-2(t) == P_n_2_t """
# P_n_t = ((2 * n - 1) / n) * t * P_n_1_t - ((n - 1) / n) * P_n_2_t
P_0_t = 1
P_1_t = math.cos(yeni_enlem)
n = 2
P_2_t = ((2 * n - 1) / n) * math.cos(yeni_enlem) * \
    P_1_t - ((n - 1) / n) * P_0_t
a_r_2 = pow((a / r), (n))
# Çarpım kısmı
C_2 = P_2_t * J_2 * a_r_2
# print(C_2)
# print(a_r_2)
#print("P_2_t: ", P_2_t)
n = 3
P_3_t = ((2 * n - 1) / n) * math.cos(yeni_enlem) * \
    P_2_t - ((n - 1) / n) * P_1_t
# print(P_3_t)
n = 4
P_4_t = ((2 * n - 1) / n) * math.cos(yeni_enlem) * \
    P_3_t - ((n - 1) / n) * P_2_t
a_r_4 = pow((a / r), (n))
# Çarpım kısmı
C_4 = P_4_t * J_4 * a_r_4
# print(C_4)
# print(a_r_4)
# print(P_4_t)
n = 5
P_5_t = ((2 * n - 1) / n) * math.cos(yeni_enlem) * \
    P_4_t - ((n - 1) / n) * P_3_t
# print(P_5_t)
n = 6
P_6_t = ((2 * n - 1) / n) * math.cos(yeni_enlem) * \
    P_5_t - ((n - 1) / n) * P_4_t
a_r_6 = pow((a / r), (n))
# Çarpım kısmı
C_6 = P_6_t * J_6 * a_r_6
#print("C_6: %.13f" % C_6)
# print(P_6_t)
# print(a_r_6)

# Çarpım kısmının hesabı için;
carpim = C_2 + C_4 + C_6
# print(carpim)

# U değeri hesabı
U = (GM / r) * (1 - carpim) + (pow(w, 2) / 2) * \
    pow(r, 2) * pow(math.sin(yeni_enlem), 2)

print("U: %.4f m²/s²" % U)
