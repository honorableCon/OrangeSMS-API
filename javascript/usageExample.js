import {getToken, sendSMS} from './orangeSMS.js';

const clientID = "aklGYUdsYjdhY...QVRBOVVkVTFqRHkxdg=="
const token = await getToken(clientID)
let senderAdress = "+2210000"
let address = "+221781234567"

sendSMS(senderAdress, address, "bonjour from node", token)
    .then(result => {
        console.log(result);
    });