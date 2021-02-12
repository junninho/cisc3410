def num_to_list(file):
  nums = []
  with open(file) as f:
    for num in f:
      num = num.strip()
      print(num)
      try:
        n = int(num)
        if n == -1:
          break
        else:
          nums.append(n)
      except ValueError:
        print('Invalid entry in file')

  return nums

def main():
  print(num_to_list('./numbers.txt'))


if __name__ == '__main__':
    main()