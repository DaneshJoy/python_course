
from bs4 import BeautifulSoup


with open('battery-report.html', 'r') as f:
    html_text = f.read()
    
soup = BeautifulSoup(html_text, 'html.parser')

labels = soup.find_all('span', class_='label')

for item in labels:
    if item.text.strip() == 'DESIGN CAPACITY':
        design_capacity = item.find_next('td').text.strip()
    if item.text.strip() == 'FULL CHARGE CAPACITY':
        current_capacity = item.find_next('td').text.strip()
        
design_capacity = design_capacity.split()[0]
design_capacity = int(design_capacity.replace(',', ''))

current_capacity = current_capacity.split()[0]
current_capacity = int(current_capacity.replace(',', ''))

percent = 100 - (1 - current_capacity/design_capacity)*100
print(f'Battery Health: {percent:0.2f}%')




        