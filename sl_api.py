import requests #pip install requests
from dotenv import load_dotenv #pip install python-dotenv
import os

load_dotenv()
DEP_KEY = os.getenv('DEP_KEY')
PLACE_KEY = os.getenv('PLACE_KEY')

# place_search = "Nacka Strand"
# plats_url = f"https://api.sl.se/api2/typeahead.JSON?key={PLACE_KEY}&searchstring={place_search}"
# response = requests.get(plats_url)
# print(response)
# answer = response.json()
# print(answer)

time = "20"
slussen = "9192"
nacka_strand = "4031"
realtid = f"https://api.sl.se/api2/realtimedeparturesV4.JSON?key={DEP_KEY}&siteid={nacka_strand}&timewindow={time}"

response = requests.get(realtid)
print(response)
answer = response.json()
#print(answer)

for line in answer['ResponseData']['Buses']:
    print(line['LineNumber'], line['Destination'], line['DisplayTime'])










headers = response.headers # represents the headers as a dictionary
print("Headers is: ", headers, newLines(10))
text = response.text    # represents the response body as a strings
print("Body as string is: ", text, newLines(10))
content = response.content # represents the response body as a binary
print("Body as binary is: ", content, newLines(10))
json_format = response.json()  # parses the response body in JSON format
print("Json format of respose body is: ", json_format, newLines(10))
request = response.request # represents the request as requests.models.PreparedRequest
print("Request I sent is: ", request, newLines(10))





