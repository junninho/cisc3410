# define fahrenheit to celcius function
def f_to_c(temp):
  celsius = (temp - 32) * (5/9) # celsius formula
  return celsius # return value

# define celsius to fahrenheit function
def c_to_f(temp):
  fahrenheit = (temp * 9/5) + 32 # fahrenheit formula
  return fahrenheit # return value

# call functions (commented out as these are for testing purposes only)
# print(f'{f_to_c(70)} C')
# print(f'{c_to_f(23)} F')