import requests,time

time = time.strftime("%c")
split = time.split()
date = split[2]
month = split[1]
year = split[4]

if int(date)<10 :
	num=int(date)
else :
	num=int(date)%10
	

if num==1 :
	suffix="st"
	
elif num==2 :
	suffix="nd"
	
elif num==3 :
	suffix="rd"

else :
	suffix="th"

url='http://172.20.0.202/nitw_prm/News/' + date + suffix + ' ' + month + ' ' + year + '.pdf' 

res = requests.get(url)

try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem: %s' % (exc))

filename = date + suffix + ' ' + month + '.pdf'

RO = open( os.path.join('Desktop/RO', os.path.basename(filename)) , 'wb')

for chunk in res.iter_content(100000):
	RO.write(chunk)

print ('Download done. :') 

RO.close()
