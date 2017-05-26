#! python3

import json, requests, sys
# Compute location from command line arguments.

url ="https://graph.facebook.com/v2.9/256389754771285?fields=feed.limit(5)&access_token=EAAZAqbJrNGSYBAA47PeI9yhvlw3lz0NWSHnFU7hJTDuXqdgnZB5SWnFFrO1pjVZCAZBvbTBomrry9iW9T5UODGjJVcnLrznPrVxDQguvYW9dTEoLTgucPYXakapr8BKJpG5irAxz6TRhbwzq4x1ZBphOJ9ZClbDTMZD"
response = requests.get(url)
response.raise_for_status()

feed = json.loads(response.text)
f = feed['feed']['data']

k=1
for i in range(len(f)):
	if 'message' in f[i] :
		print("MESSAGE : " + str(k),'\n')
		print( f[i]['message'],'\n')
		print('-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')
		k=k+1
print ( " END " )




