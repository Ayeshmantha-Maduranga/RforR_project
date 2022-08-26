import requests 
from requests.structures import CaseInsensitiveDict

url = "http://3.131.152.241:8080/api/donators/by-index/TE88616"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1c2VyIiwiYXV0aCI6IlJPTEVfVVNFUiIsImV4cCI6Mjc1ODEyNzQwMzl9.P7wkR88Uon0qxqcBzSOApY7PTP3I6yY8dxlUTnDRqJw2DndTfiC7zEMpHoOG2S-egnxz5gV5uPmu7cbSxHpaUA"


resp = requests.get(url, headers=headers)
print(resp.status_code)
print(resp.json())