import fetch from 'node-fetch';

async function getToken(clientID){
    const data = await fetch('https://api.orange.com/oauth/v3/token', {
        method: 'POST',
        headers: {
            'Authorization': `Basic ${clientID}`,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        },
        body: 'grant_type=client_credentials'
    }).then( response => response.json())

    return data['access_token'];
}

async function sendSMS(senderAdress, address, message, token){
    const data = await fetch(`https://api.orange.com/smsmessaging/v1/outbound/tel:${senderAdress}/requests`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "outboundSMSMessageRequest":{
                "address":`tel:${address}`,
                "senderAddress" : `tel:${senderAdress}`,
                "outboundSMSTextMessage":{
                    "message": message
                }
            }
        })
    })
    .then( response => response.json())

    return data
}

async function getUsageStats(token){
    const stats = await fetch('https://api.orange.com/sms/admin/v1/statistics', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then( response => response.json())

    return stats
}

async function showBalanceSMS(token) {
    const balance = fetch('https://api.orange.com/sms/admin/v1/contracts', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    }).then( response => response.json());

    return balance
}

export {
    sendSMS, showBalanceSMS, getToken, getUsageStats
}