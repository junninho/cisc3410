# function defined that accepts number n as a parameter
def add_it_up(n):
  # test that the value is an int
  try:
    num = int(n)
    sum = 0 # declare sum variable and assign value to 0
    # loop through every number from 0 to n
    for i in range(num):
      sum += i # add i in range to current value of sum

    return sum #return value of sum
  
  # if ValueError is returned, print message
  except ValueError:
    return 0

def validation_sum(n):
  # test that the value is an int
  try:
    n = int(n)
    sum = n*(n-1)/2

    return sum # return value of sum

  # if ValueError is returned, print message
  except ValueError:
    print("Invalid Number")

# main function
def main():
  test_number = 8 # test number used as a parameter for both previously defined functions
  func_sum = add_it_up(test_number)
  check_sum = validation_sum(test_number)

  # print sum alongside validation check result
  print(f'Sum: {func_sum} \nValidation Check: {func_sum == check_sum}')
  
if __name__ == '__main__':
    main()