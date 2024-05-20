# Initialisation
import requests, json
token = 'secret_frHHTxg46cnG0Hwqaa18G45RcARsUrccAzpKPPs6VU2'
databaseID ="1f071a6dddc346afa9250b3acee4ea2f"
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}

# Response a Database
def responseDatabase(databaseID,headers):
    readUrl=f"https://api.notion.com/v1/databases/{databaseID}"
    res=requests.request("GET",readUrl,headers=headers)
    print(res.status_code)

def readDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return data
  
if __name__ == "__main__":
    data = readDatabase(databaseID, headers)
    print(data)