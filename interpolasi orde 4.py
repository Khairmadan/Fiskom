i = [0.25, 0.75, 1.25, 1.5 , 2.0]
v = [-0.45, -0.6 , 0.7 , 1.88, 6.0 ]
a0 = v[0]
def aa1(v0,v1,i0,i1):
    return (v1-v0)/(i1-i0)
a1 = aa1(v[0],v[1],i[0],i[1])
def aa2(v0,v1,v2,i0,i1,i2):
    return (aa1(v1,v2,i1,i2)-aa1(v0,v1,i0,i1))/(i2-i0)
a2 = aa2(v[0],v[1],v[2],i[0],i[1],i[2])
def aa3(v0,v1,v2,v3,i0,i1,i2,i3):
    return (aa2(v1,v2,v3,i1,i2,i3)-aa2(v0,v1,v2,i0,i1,i2))/(i3-i0)
a3 = aa3(v[0],v[1],v[2],v[3],i[0],i[1],i[2],i[3])
def aa4(v0,v1,v2,v3,v4,i0,i1,i2,i3,i4):
    return (aa3(v1,v2,v3,v4,i1,i2,i3,i4)-aa3(v0,v1,v2,v3,i0,i1,i2,i3))/(i4-i0)
a4 = aa4(v[0],v[1],v[2],v[3],v[4],i[0],i[1],i[2],i[3],i[4])
y = a0 + a1*(1.15-i[0]) + a2 * (1.15-i[0])*(1.15-i[1]) + a3 * (1.15-i[0])*(1.15-i[1])*(1.15-i[2]) + a4 * (1.15-i[0])*(1.15-i[1])*(1.15-i[2])*(1.15-i[3])
print(y)
