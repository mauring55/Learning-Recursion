#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

file = open(input('Enter filename: '))

def email_time(file):
  hr_list = list()
  hr_with_count = dict()
  
  for line in file:
    if not line.startswith('From '):
      continue

    else:
      #takes the time of day (hr only)
      hour = line[line.find(':') - 2:line.find(':')]
      hr_list.append(hour)

  #create a dictionary with hrs and how many times did it occur
  for hour in hr_list:
    hr_with_count[hour] = hr_with_count.get(hour, 0) + 1

  #Use hr_with_count dictionary to and reverse the key-value pair     to sort them by occurence in descending order
  hr_list = list()
  
  for key, val in hr_with_count.items():
    hr_list.append([key, val])

  #sort it
  hr_list = sorted(hr_list)
  
  
  return hr_list

for k,v in email_time(file):
  print(k, v)
  

  
  