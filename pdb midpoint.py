import pandas as pd
R = 1.5
L = 1
dt = 1
I = 0.5
t0 = 0
tf = 10
t = t0
waktu = [t]
arus = [I]
def fungsi(L,r,i):
    return -r*i/L
while t < tf :
    tm = t +dt/2
    im = I + dt/2 * fungsi(L,R, I)
    t = t + dt
    I = I + dt * fungsi(L, R, im)
    waktu.append(t)
    arus.append(I)
data = {
    "waktu" : waktu,
    "arus" : arus
}
print(pd.DataFrame(data))