import requests
import pywhatkit
import json
import datetime
import telebot
import time
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
district = [770,160,179]
final_message = []
knownpincodes = []
knowndates = []
skippincode = ""
skipdate = ""

api_id = '4081179'
api_hash = 'b230a9d343079e204a69719a79cbecce'
token = '1813049791:AAEQwqA1AsRHofLLIp0zW9bDVcw1mikVewQ'
phone = '+917016062635'


xtime = datetime.datetime.now()
myTuple = (xtime.strftime("%d"),xtime.strftime("%m"),xtime.strftime("%Y"))
loopstatus = False
looptrack = 1
while not loopstatus:
    for i in range(0,len(district)):
        try:
            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district[i])+"&date="+("-".join(myTuple))
            response = requests.get(url,headers=header)
            #print(response.json())
            data = response.json()['centers']
            if len(data)!=0:
                for x in data:
                    ses = x['sessions']
                    fee_type = x['fee_type']
                    for s in ses:
                        if ((x['pincode'] in knownpincodes) and (s['date'] in knowndates)):
                            skippincode = x['pincode']
                            skipdate = str(s['date'])
                        if ((s['available_capacity_dose1']>0) and (fee_type=='Free') and (s['min_age_limit']==45) and ((skippincode!=x['pincode']) or (skipdate!=s['date']))):
                            message = "\n For Pincode "+str(x['pincode'])+"("+str(x['district_name'])+") and date "+str(s['date'])+" total availablility of age group above 45 is "+str(s['available_capacity'])+"\n Dose 1 are "+str(s['available_capacity_dose1'])+" and Dose 2 are "+str(s['available_capacity_dose2'])
                            final_message.append(message)
                            pin = x['pincode']
                            knownpincodes.append(pin)
                            d = s['date']
                            knowndates.append(d)
                            #loopstatus = True
                            #print(loopstatus)
        except json.decoder.JSONDecodeError:
            try:
                print("<---------- For pincode "+str(x['name'])+" and date "+str(x['date'])+" ----------->\n No Appoinments")
            except KeyError:
                pass
        except KeyError:
            pass
    print(looptrack,"times", xtime)
    looptrack = looptrack + 1
    time.sleep(80)

    #telegram code

    listToStr = '\n'.join([str(elem) for elem in final_message]) 
    client = TelegramClient('session', api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input('Enter the code: '))
    entity=client.get_input_entity('jaypatel8914')  
    try:
        client.send_message(entity, listToStr)
    except Exception as e:
        print(e)
    final_message.clear()
    client.disconnect()