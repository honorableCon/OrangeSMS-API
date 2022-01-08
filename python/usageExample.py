from orangeSMS import sendSMS, getToken


clientID = "aklGYUdsYjdhY2VpM...Hkxdg=="
token = getToken(clientID)
senderAdress = "+2210000"
address = "+221781234567"

result = sendSMS(senderAdress, address, "Salam from python", token)
print(result)