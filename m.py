def fungsi(T):
    Ta = 20
    k = 1/60
    return -k*(T-Ta)
import pandas as pd
T0 = 90
Tf = 40
dt = 0.25
T = T0
listT = [T]
listt = [0]
t = 0
while T > Tf:
    T = T + fungsi(T) * dt
    listT.append(T)
    t = t+dt
    listt.append(t)
data = {
    "waktu" : listt,
    "suhu" : listT
}
dataa = pd.DataFrame(data)
print(dataa)