entries = int(input())

phonebook = {}
for i in range(entries):
    entry = input().split()
    phonebook[entry[0]] = entry[1]

while True:
    person = None
    
    try:
        person = input()
    except EOFError:
        break
    
    if person in phonebook.keys():
        print(person + "=" + phonebook[person])
    else:
        print("Not found")