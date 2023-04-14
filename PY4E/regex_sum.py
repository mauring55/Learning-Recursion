import re

file = open(input('Enter filename: '))


def regex_sum(file):
  total_list = list()
  total = 0
  for line in file:
    number = re.findall('[0-9]+', line)
    
    if len(number) == 0:
      continue
    elif len(number) > 1:
      for x in number:
        temptotal = 0
        temptotal += int(x)

        total_list.append(temptotal)
    else:
      total_list.append(int(number[0]))

  for num in total_list:
    total += int(num)

  return total


print(regex_sum(file))
