def primenumbers():
  num = 0
  while 0 <= num <= 100:
    if num == 0 or num == 1:
      num += 1
      continue
    elif num == 2:
      print(num)
    else:
      for i in range(2,num):
        if num % i == 0:
          break
      else:
          print(num)
    num += 1
primenumbers()
