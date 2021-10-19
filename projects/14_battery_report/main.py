from lxml import html
from bs4 import BeautifulSoup
import os


''' Read local html file '''
os.system('powercfg /batteryreport')
html_data = html.parse('battery-report.html')
html_text = html.tostring(html_data)

''' Scrape the file '''
soup = BeautifulSoup(html_text, 'html.parser')
labels = soup.find_all('span', class_='label')

for item in labels:
    if item.text.strip() == 'DESIGN CAPACITY':
        d_c = item.find_next('td').text.strip()
    if item.text.strip() == 'FULL CHARGE CAPACITY':
        f_c = item.find_next('td').text.strip()

d_c = d_c.split()[0]
d_c = int(d_c.replace(',', ''))

f_c = f_c.split()[0]
f_c = int(f_c.replace(',', ''))

battery_percent = 100 - ((d_c - f_c) / d_c) * 100
print(f'Battery Health: {int(battery_percent)}%')
