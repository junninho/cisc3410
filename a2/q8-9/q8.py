def f_to_c(temp):
  celsius = (temp - 32) * (5/9)
  return celsius

def c_to_f(temp):
  fahrenheit = (temp * 9/5) + 32
  return fahrenheit


print(f'{f_to_c(70)} C')
print(f'{c_to_f(23)} F')