import fileinput, math

# Lee entradas
lines = []
for line in fileinput.input():
    lines.append(line)

def compute(a,b,A,B):
    M = (a*b)-1
    e = (A*M)+a
    d = (B*M)+b
    n = int(((e*d)-1)/M)
    return e, d, n 

def cifra(m, e, n):
    temp = m * e 
    return temp % n 

def decifra(m, d, n):
    temp = m * d
    return temp % n 


# Obtener las llaves y texto plano, limpiando el input
mode = lines[0].replace("\n","")
in_a = int(lines[1].replace("\n",""))
in_b = int(lines[2].replace("\n",""))
in_A = int(lines[3].replace("\n",""))
in_B = int(lines[4].replace("\n",""))
mess = int(lines[5].replace("\n",""))

# Algoritmo main
out_e, out_d, out_n = compute(in_a,in_b,in_A,in_B)
print(out_e, out_d, out_n)
if(mode == 'E'):
    print(cifra(mess, out_e, out_n))
if(mode == 'D'):
    print(decifra(mess, out_d, out_n))