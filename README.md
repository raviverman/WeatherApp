# WeatherApp
A Python Script to fetch weather data for requested city.

## How to execute?
1. Change working directory to `WeatherApp`.
2. Run script by typing `python3 WeatherApp.py`.
3. Enter city name.
4. Weather description appears after a short while.

## Problems?
> No module name 'requests'
1. Script requires `requests` module to run.
2. Install `requests` module by typing `sudo pip install requests`.
3. If using proxy, type `sudo pip install requests --proxy 'http://username:password@proxyip:proxyport'`
4. Run script again.

> Unable to fetch data under proxy
1. Open script in a text editor.
2. Comment out existing dummy proxy `proxy = {}`.
3. Modify commented proxy `proxy = {"http" : "http://username:password@proxyip:proxyport"}` and uncomment it.
4. Try running it again.
