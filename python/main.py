import json
import requests

clientID="{{clientID}}"

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


def getUsageStats(token):
    response = requests.get('https://api.orange.com/sms/admin/v1/statistics',
        headers={
            'Authorization': f'Bearer {token}'
        }
    )
    stats = response.json()

    return stats


def showBalanceSMS(token):
    response = requests.get('https://api.orange.com/sms/admin/v1/contracts', 
        headers={
            'Authorization': f"Bearer {token}"
        }
    )
    balance = response.json()
    print(balance)

    return balance


def sendSMS(senderAddress, receiverAddress, message, token):
    url = f'https://api.orange.com/smsmessaging/v1/outbound/tel:{senderAddress}/requests'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    data = {
        "outboundSMSMessageRequest":{
            "address": f"tel:{receiverAddress}",
            "senderAddress":f"tel:{senderAddress}",
            "outboundSMSTextMessage":{
                "message": message
        }     
    }}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    return response.json()

token = getToken(clientID)
# code here