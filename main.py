#Author: Xinyi Yang xvy5166@psu.edu


def digit_sum(n):
  if n == 0:
    return 0
  else:
    return n%10+digit_sum(n//10)


def run():
  i = int(input("Enter an int: "))
  num_sum = digit_sum(i)
  print(f"sum of digits of {i} is {num_sum}.")


if __name__ == "__main__":
  run()




