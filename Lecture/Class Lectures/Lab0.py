x ='acegikmoqsuwy'
y ='+bdfhjlnprtvxz'
z=''

for i in range(len(x)):
    print(i)
    if(y[i].isalpha() == True):
        z=z+y[i]
    else:
        z=z+x[i]
        continue
    z= z+x[i]
print(z)