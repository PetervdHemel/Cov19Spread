import requests

url = "https://covid-19-data.p.rapidapi.com/country/all"

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "undefined"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
