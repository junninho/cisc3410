def add_it_up(n):
  try:
    num = int(n)
    sum = 0
    for i in range(0, num):
      sum += i

    return sum

  except ValueError:
    return 0

def validation_sum(n):
  try:
    n = int(n)
    sum = n*(n-1)/2

    return sum

  except ValueError:
    print("Invalid Number")

def main():
  user_input = input("Enter a number: ")
  func_sum = add_it_up(user_input)
  check_sum = validation_sum(user_input)

  print(f'Sum: {func_sum} \nValidation Check: {func_sum == check_sum}')
  
if __name__ == '__main__':
    main()
    