from django.shortcuts import render

def home(request):

	import requests
	import json

	# Grab Crypto Price Data
	#Select currencies
	coins = "BTC,ETH,XLM,XRP,LTC,XMR,BCH,BNB,ZB,ZEC,ETC,DASH,NEO,ADA,BTT,USDT,BGG,TRX,EOS"
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + coins + "&tsyms=USD")
	price = json.loads(price_request.content)


	# Grab Crypto News
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
	import requests
	import json
	if request.method == 'POST':		
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		quote = request.POST['quote']
		return render(request, 'prices.html', {'quote': quote, 'crypto': crypto })

	else:
		notfound = "Enter a crypto currency symbol into the form above..."
		return render(request, 'prices.html', {'not found': notfound })

# Create your views here.
