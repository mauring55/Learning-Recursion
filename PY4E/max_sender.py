#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

filhandle = input('Enter filename: ')
file = open(filhandle)

# Input is a file - Output will be the maximum sender email 
def max_sender(file):
  sender_count = dict()
  
  for line in file:
    if not line.startswith('From '):
      continue

    else:
      email = line.split()[1]
      sender_count[email] = sender_count.get(email, 0) + 1
  
  max_email = None
  max_sent = None
  
  for key,value in sender_count.items():
    if max_sent is None or max_sent < value:
      max_sent = value
      max_email = key
      
    else:
      continue

  print(max_email, max_sent)
  return None

max_sender(file)