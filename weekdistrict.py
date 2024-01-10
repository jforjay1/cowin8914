import requests
import json
import datetime
import time
from telethon.sync import TelegramClient
from keepalive import keepalive
import pytz


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


district = [160]
final_message = []
knownpincodes = []
knowndates = []
skippincode = ""
skipdate = ""
IST = pytz.timezone('Asia/Kolkata')
api_id = '4082179' #Replace with your CoWIN API
api_hash = 'b230a9d343079e204a69719a79cdscce' #Replace with your CoWIN hash
token = '1813049791:AAEQwqA1AsRHofLLIp0zW3daDVcw1mikVewQ' #Replace with your Telegram token
phone = '+911234567890' #Replace with your phone number

loopstatus = False
looptrack = 1
keepalive()
while not loopstatus:
    for i in range(0,len(district)):
        try: 
            xtime = datetime.datetime.now(IST)
            myTuple = (xtime.strftime("%d"),xtime.strftime("%m"),xtime.strftime("%Y"))
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
                        if ((s['available_capacity_dose2']>0) and (fee_type=='Free') and (s['min_age_limit']==45) and ((skippincode!=x['pincode']) or (skipdate!=s['date']))):
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
    print("login")
    listToStr = '\n'.join([str(elem) for elem in final_message]) 
    client = TelegramClient('session', api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input('Enter the code: '))
    entity=client.get_input_entity('your_username')  #Replace with your Telegram Username
    try:
        client.send_message(entity, listToStr)
    except Exception as e:
        print(e)
    final_message.clear()
    client.disconnect()
    print("logout")
