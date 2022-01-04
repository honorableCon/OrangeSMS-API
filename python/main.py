import requests

clientID = "{{idclient}}"
senderAdress = "+2210000"
address = "+221{{receiver}}"

def getToken(clientID):
    response = requests.post('https://api.orange.com/oauth/v3/token', 
        headers={
                'Authorization': f"Basic {clientID}",
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
        }, data={
            'grant_type': 'client_credentials'
        }
    )
    response = response.json()
    return response['access_token']
