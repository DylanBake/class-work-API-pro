import requests

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"
query = ""
url = url_host + endpoint# + query

response = requests.get(url)
print(response.json()["message"]

#get a list of all breeds from the API call
all_breeds = breeds.keys()

# loop and print out each Key 
for breed in all_breeds:
  print(breed)


# display all retreiver subbreeds
retriever_subbreeds = breeds["retriever"]
input("\nPress enter to get all subbreeds")
for sub in retriever_subbreeds:
  print(sub)