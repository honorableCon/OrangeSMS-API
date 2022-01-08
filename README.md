# Orange SMS API 📬

[![Made-In-Senegal](https://github.com/GalsenDev221/made.in.senegal/blob/master/assets/badge.svg)](https://github.com/GalsenDev221/made.in.senegal)

> Orange SMS is a client library that allow you to send SMS with Javascript and Python using the [Orange SMS API](https://developer.orange.com/apis/sms-sn/overview)

## Disclaimer ⛔

This gem is not an official client of Orange, in order to use the client you need to create a [Orange SMS API](https://developer.orange.com/apis/sms-sn/overview) and to register an app in the developer dashboard that orange provide to you.  
After registering your app you can ask for SMS integration approval (this process can take time :)  
The registration process is detailed [here](https://developer.orange.com/apis/sms-sn/overview)

Instead of reading and trying to understand once again how the Orange SMS API work this gem aims to let you quickly send SMS from JavaScript and Python using the [Orange SMS API](https://developer.orange.com/apis/sms-sn/overview).

## Usage ✅

writing...

### JavaScript 💛

```javascript
const clientID = process.env.clientID
const token = await getToken(clientID)
let senderAdress = "+2210000"
let address = "+221{{receiver}}"
sendSMS(senderAdress, address, 'message')
```

### Python 🐍

```python
```

#### Contributing 🤝

Bug reports and Pull Requests are welcome 👋🏽  
You can tell me **[HERE](https://github.com/honorableCon/OrangeSMS-API/issues)**

#### License 🔖

This project is under **[MIT License](https://opensource.org/licenses/MIT)**.
