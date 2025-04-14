def isSumOfTwoPRIMES(number):
  if number%2==1:
    return False
  for i in range(2, number):
    good=True
    # check if i is a prime
    x = 2
    while(x<i):
      if(i%x==0):
        good= False
      x += 1
    if good:
      # i is a prime, now check if j=x-i is prime
      j=number-i
      if(j>=2):#j must be greater or equal 2 to be prime
        good2 =True
        x = 2
        while(x<j):
          if(j%x==0):
            good2= False
          x += 1
        if good2:
          print(f"The number {number} equals to the sum of {i} and {j}")
  return True


Number=int(input("Enter a number:"))
isSumOfTwoPRIMES(Number)
