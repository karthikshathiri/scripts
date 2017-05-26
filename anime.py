import requests , os, bs4
url='www.mangatown.com'
os.makedirs('anime',exist_ok=True)
while not url.endswith('calling'):
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text,"html.parser")
	
	comicElem = soup.select('#comic img')
	
	if comicElem == []:
		print('Could not find comic image.')
	else:
		comicUrl = comicElem[0].get('src')
		# Download the image.
		print(comicUrl)
		print('Downloading image %s...' % (comicUrl))
		
		res = requests.get('http:' + comicUrl)
		res.raise_for_status()

		
		imageFile = open(os.path.join('zenpencils', os.path.basename(comicUrl)), 'wb')

		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
	
	# Get the Prev button's url.
	
	prevLink = soup.select('a[title="< Prev"]')[0]
	url = prevLink.get('href')

print('Done.')


