import requests

url = "https://content.guardianapis.com/search?page=2&q=debate&api-key=test"

payload = {}
headers = {
  'Cookie': 'AWSALB=SU1EnV4H8lOuBqnwVniSq9if5vFtQ3gTLX4+vYmJ6j49dFNJYiNaUtJmWp/cNQ3YPyNEYeuy/Wb82DK/5d74usX77fChGchdgc3n8tEbH4yowMNr+td6CarWYo/5; AWSALBCORS=SU1EnV4H8lOuBqnwVniSq9if5vFtQ3gTLX4+vYmJ6j49dFNJYiNaUtJmWp/cNQ3YPyNEYeuy/Wb82DK/5d74usX77fChGchdgc3n8tEbH4yowMNr+td6CarWYo/5'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
