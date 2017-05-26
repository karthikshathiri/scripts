from twilio.rest import TwilioRestClient

accountSID = 'AC05beb96c094a6f87f8a01517bba41fba'
authToken ='cf4228e8f0528e51c3fc1215465958eb'

twilioCli = TwilioRestClient(accountSID, authToken)

myTwilioNumber = '+12013316514'

print('please input phone no with international code: ')
myCellPhone=input()

print('Body of the messege: ')
text=input()

message = twilioCli.messages.create(body=text , from_=myTwilioNumber, to=myCellPhone)

print(message.status)
print(message.sid)
updatedMessage = twilioCli.messages.get(message.sid)
print(updatedMessage.status)
print(updatedMessage.date_sent)
