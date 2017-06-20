#import libraries
import sys
from bs4 import BeautifulSoup

if sys.version_info[0] < 3:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen


# Use the exact URL you want to scrape
faulk = 'http://library.austintexas.gov/faulk-central-library'

# Use urllib2 or urllib to pull the html to the variable 'site'
site = urlopen(faulk)

# Parse the site
soup = BeautifulSoup(site, 'html.parser')

# Retrieve data
name = soup.find('h2', attrs = {'pane-title'}).text
address = soup.find('div', attrs = {'views-field-field-address'}).text

print(name)
print(address)