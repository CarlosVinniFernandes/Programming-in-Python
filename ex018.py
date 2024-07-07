import math
m = float(input('Insira um ângulo'))
seno = math.sin(math.radians(m))
cos = math.cos(math.radians(m))
tan = math.tan(math.radians(m))
print("O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}".format(seno, cos, tan))
