a = int(input("Digite o valore de a: "))
b = int(input("Digite o valore de b: "))
c = 1

na = a
nb = b
while(c != 0):
    c = na%nb
    
    na = nb
    nb = c

print(f"MDC({a}, {b}) = {na}")