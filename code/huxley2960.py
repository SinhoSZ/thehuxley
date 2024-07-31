f = float(input())

t_celsius = ((f - 32) * 5) / 9
t_kelvin = t_celsius + 273.15

print(f"Convertendo {f:.1f} graus Fahrenheit temos:")
print(f"{t_celsius} graus Celsius e {t_kelvin} Kelvin")