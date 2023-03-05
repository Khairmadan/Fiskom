from prettytable import PrettyTable
import math
table = PrettyTable()
def f(x):
    return (math.sqrt(0.01) * x * 5.0 / (0.02)) * (x*5.0/(5.0+(2*x)))-12

a = float(input("bilangan tebakan bawah = "))
b = float(input("bilangan tebakan atas= "))

z = f(a) * f(b)
i = 0
while z >= 0 :
    print("akar tidak berada di antara tebakan")
    print("coba dengan tebakan lain")
    a = float(input("bilangan tebakan bawah = "))
    b = float(input("bilangan tebakan atas= "))
table.field_names = ["no", "xl", "xu", "xm","error" , "f(xl)", "f(xm)"]
xm = (a + b) / 2
error = 100
while error > 0.0000001 and abs(f(xm)) > 0.0000001  and abs(a-b) > 0.000000001 : # while dapat diganti dengan for
    # dan dapat juga kondisinya yang diganti dengan berapa persen error yang diinginkan
    xold = xm
    xm = (a + b) / 2

    if i == 0 :
        error = 100
        print(error)
        table.add_row([i + 1, a, b, xm, "none", f(a), f(xm)])
    else :
        error = abs((xold - xm) / xm) * 100
        table.add_row([i + 1, a, b, xm, error, f(a), f(xm)])
    if f(a) * f(xm) < 0:
        a = a
        b = xm
    elif f(a) * f(xm) > 0:
        a = xm
        b = b


    i = i + 1
print(table)
print("akar persamaan = %0.5f" %xm)