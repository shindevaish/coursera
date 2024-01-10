#9.4 Write a program to read through the mbox-short.txt
#and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines
#and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the
#sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary
#using a maximum loop to find the most prolific committer.

file_name=input("Enter name of file:")
file=open(file_name)
mail_dict={}

for line in file:
    words=line.split()
    if words[0]=='From':
        mails=words[1]
        mail_dict[mails]=mail_dict.get(mails,0)+1
        
mail=None
most=None
for key,value in mail_dict.items():
    if most is None or value>most:
        most=value
        mail=key

print(mail,most)

