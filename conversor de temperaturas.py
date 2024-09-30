graus = float(input('quanto em temperatura em C: '))
grau = float(input('quantos em temperatura em F: '))
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print('convertido para Celsius C: {:.1f}'.format(celsius_para_fahrenheit(grau)))
print('convertido para Fahrenheut F: {:.1f}'.format(fahrenheit_para_celsius(graus)))


