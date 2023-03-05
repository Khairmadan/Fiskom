# newton raphson method
import math
def Fungsi(x):
    return ((667.38) * (1 - (math.e ** (-( x / 6.81 )) ) )) - (40 * x)  #fungsi dapat disesuaikan dnegan fungsi yang diberikan
def Turunan(x):
    return 667.38 * ((-1/6.81) * (math.e**(-(x/6.81)))) - 40 #sesuaikan jga turunan dengan fungsi jika fungsi berubah

i = 0
xi = float(input("Masukkan tebakan = "))
error = 100
print("No     xi       error")
while error > 10**(-6)  : # operator while juga dapat diubah jadi for
    xold = xi
    if i == 0 :
        error = "None"
        print("%0.1i   " %i + "%10.5f  " %xi + "   " + error )
    i = i + 1

    xi = xi - (Fungsi(xi)/Turunan(xi))
    error = abs((xi - xold)/xi) * 100
    print("%0.1i" % i + "%10.5f  " % xi + "%8.5f" %error+"%")
print("akar persamaannya adalah %0.5f" %xi)