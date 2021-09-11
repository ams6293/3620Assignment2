numList = []

for num in range(1,101):
    numList.append(num)


only_odd = [num for num in numList if num % 2 == 1]
  
print(only_odd)
                    