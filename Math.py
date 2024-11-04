from math import sin, cos, tan, radians

an = float(input('Informe o ângulo: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('O ângulo de {} tem seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(an, seno, cosseno, tangente))
