# OrangeSMS-API

[![Made-In-Senegal](https://github.com/GalsenDev221/made.in.senegal/blob/master/assets/badge.svg)](https://github.com/GalsenDev221/made.in.senegal)

> Orange Sms is a client library that allow you to send sms with Javascript and Python using the [Orange Sms API](https://developer.orange.com/apis/sms-sn/overview)

## Disclaimer
This gem is not an official client of Orange, in order to use the client you need to create a [Orange Sms API](https://developer.orange.com/apis/sms-sn/overview) and to register an app in the developer dashboard that orange provide to you. After registering your app you can ask for sms integration approval (this process can take time :)).
The registration process is detailed [here](https://developer.orange.com/apis/sms-sn/overview)
## Motivation
Instead of reading and trying to understand once again how the Orange Sms API work this gem aims to let you quickly send sms from Javascript and Python using the [Orange Sms API](https://developer.orange.com/apis/sms-sn/overview).

### javascript
```javascript
const clientID = process.env.clientID
const token = await getToken(clientID)
let senderAdress = "+2210000"
let address = "+221{{receiver}}"
sendSMS(senderAdress, address, 'message')
```
## Getting Started
writing..

### Generate Access token
writing..

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/honorableCon/OrangeSMS-API.


## License

This is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
