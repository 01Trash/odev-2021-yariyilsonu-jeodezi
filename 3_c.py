"""Python3"""
import math

# Verilen değerler
W_P = 6.262129752474 * pow(10, 7)  # Gravite potansiyel (8. değer) m²/s²
W_0 = 62636856.0  # Referans potansiyel m²/s²
gama_0 = 980.6199203 / 100  # Gal
G_P = 9.796232618985 * pow(10, 5) / 100000  # Yer gravite (Gal) (7. değer)
enlem_derece = 38 + (45 / 60) + (0 / 3600)
enlem_radyan = enlem_derece * (math.pi / 180)
boylam_derece = 32 + (30 / 60) + (0 / 3600)
boylam_radyan = boylam_derece * (math.pi / 180)
h = 1625
r = h

# Sabit değerler
a = 6378137
b = 6356752.3141
f = 1 / 298.257222101
m = 0.00344978600308
k = 0.001931851353
e_Kare = 0.006694380023
e_Ussu_Kare = 0.006739496775
gama_ekvator = 9.7803267715
w = 7.292115 * pow(10, (-5))  # rad/s
GM = 3986005 * pow(10, 8)  # m^3/s^2
w = 7.292115 * pow(10, (-5))  # rad/s
J_2 = 1.08263000 * pow(10, (-3))
J_4 = -2.37091222 * pow(10, (-6))
J_6 = 6.0834706 * pow(10, (-9))
J_8 = -1.427 * pow(10, (-11))


"""# Bozucu Potansiyel hesabı (T)"""
# c değerinin hesabı
c = pow(a, 2) / b

# N değerinin hesabı
N = c / pow((1 + e_Ussu_Kare * pow(math.cos(enlem_radyan), 2)), 0.5)
# print(N)

# x hesabı
x = (N + r) * math.cos(enlem_radyan) * math.cos(boylam_radyan)
# y hesabı
y = (N + r) * math.cos(enlem_radyan) * math.sin(boylam_radyan)
# z hesabı
z = ((1 - e_Kare) * N + r) * math.sin(enlem_radyan)
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
#yeni_enlem_radyan=yeni_enlem * (180 / math.pi)
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
#print("U: ", U)

# Bozucu Potansiyel hesabı (T)
T = W_P - U
print("Bozucu Potansiyel: %.4f" % T)


"""#Yükseklik Anomalisi hesabı (zita)"""
# Jeopotansiyel sayı hesabı
C_P = W_0 - W_P
# print(C_P)

# Dinamik yükseklik hesabı
H_D = C_P / gama_0
# print(H_D)

# Helmert ortometrik yükseklik hesabı
H_D = H_D / 1000
g_cizgi = G_P + 0.0424 * H_D
H_O = C_P / g_cizgi
# print(H_O)

# Normal yükseklik hesabı
gama_cizgi = gama_0 * (1 - (1 + f + m - 2 * f *
                            pow(math.sin(enlem_radyan), 2)) * H_O / a + pow(H_O, 2) / pow(a, 2))

N_1 = r - H_O
# Yükseklik Anomalisi hesabı (zita)
Zita = N_1 - ((g_cizgi - gama_cizgi) / gama_cizgi) * H_O
print("Yükseklik Anomalisi: %.4f" % Zita)


"""Gravite Bozukluğu hesabı (sigma_g)"""
# Gama 0 değerinin hesabı
gama_0 = gama_ekvator * ((1 + k * pow(math.sin(enlem_radyan), 2)) /
                         pow(1 - e_Kare * pow(math.sin(enlem_radyan), 2), 0.5))
# print(gama_0)

# Gama h değerinin hesabı
gama_h = gama_0 * (1 - (2 * h) / a * (1 + f + m - 2 * f *
                                      pow(math.sin(enlem_radyan), 2)) + (3 / pow(a, 2)) * pow(h, 2))
# print(gama_h)

# Gravite bozukluğu hesabı (sigma_g)
sigma_g = (G_P - gama_h) * 1000
print("Gravite bozukluğu: %.4f" % sigma_g)


"""Gravite Anomalisi hesabı (Delta_g)"""
g_0 = G_P + 0.3086 * H_O
# Delta_g hesabı
Delta_g = g_0 - gama_0
print("Gravite Anomalisi: %.4f" % Delta_g)
