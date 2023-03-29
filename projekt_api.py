import requests
response = requests.get("https://randomuser.me/api/")

def newLines(number):
    for i in range(number):
        print('')


print(type(response))
status_code = response.status_code 
print("Status code is: ", status_code,newLines(10))


#Plocka ut relevanta delar ur requests body för att manipulera på något sätt
#Skapa relevanta klasser och arv som kan uppta den omvandlade informationen
#Test cases; Försök få full code coverage(testen går igenom alla kodrader)
#Skapa någon typ av GUI(Valbart))