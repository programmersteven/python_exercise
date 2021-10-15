CODE_TO_EMAILS = {}
count = 0
email = input("Email:")
email_list = []
name_list = []
while not email == " ":
    email_list.append(email)
    email = input("Email:")
def get_name():
    for text in email_list:
        name = text.split("@")
        print("Is your name{}?(Y/n)".format(name[0].title()),end=" ")
        choice = input().lower()
        if choice =="y":
            name_list.append(name[0].title())
        else:
            name[0] = input("Name:")
            name_list.append(name[0].title())
get_name()
for message in email_list:
    if message not in CODE_TO_EMAILS:
        CODE_TO_EMAILS[message] = name_list[count]
    count += 1
for code in CODE_TO_EMAILS:
    print(CODE_TO_EMAILS[code], '(', code, ')')







