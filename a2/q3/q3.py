# define function to read in numbers to list accepting filenamne as parameter

def num_to_list(file):
  nums = [] # initialize list to store numbers

  # open file
  with open(file) as f:
    # read each line in file
    for num in f:
      num = num.strip() # remove whitespaces
      # convert number to int and add to array until it reaches -1
      try:
        n = int(num)
        if n == -1:
          break
        else:
          nums.append(n)
      except ValueError:
        print('Invalid entry in file')

  return nums # return array

# main function
def main():
  print(num_to_list('./numbers.txt')) # call function and print results

if __name__ == '__main__':
    main()