from django.http import HttpResponse
import urllib.request
import json, datetime

# Create your views here.
def index(request):
    date = int(datetime.datetime.now().strftime("%d"))
    if isPrime(date):
        city = request.GET.get('city')
        key = "9c0190ecee8a6b6946e6332abfffc24b"
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+key
        data = json.loads(urllib.request.urlopen(url).read())
        html = "<html><body>This is the json data = </body></html>" % data
    else:
        html = "<html><body>Date is not prime so no data.</body></html>"
    return HttpResponse(html)


def isPrime(n) : 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True
	if (n % 2 == 0 or n % 3 == 0) : 
		return False

	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6
	return True
