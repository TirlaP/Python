from bs4 import BeautifulSoup
import requests

site_map = "http://www.pngmart.com/sitemapindex.xml/"

response = requests.get(site_map)

xml = response.text
soup = BeautifulSoup(xml, 'xml')

site_maps = []
for loc in soup.find_all('loc'):
    url = loc.text
    if 'part' in url:
        print(loc.text)
        site_maps.append(url)

site_map_1 = site_maps[0]
response = requests.get(site_map_1)

soup = BeautifulSoup(response.text, 'xml')

master_list = []
for loc in soup.find_all('loc'):
    url = loc.text
    master_list.append(url)

for image_url in master_list[0:10]:
    print(image_url)
    response = requests.get(image_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    break

png_url = soup.find('a', class_ = 'download')['href']
print(png_url)
image = requests.get(png_url)
image_title = image_url.split('/')[-1] + '-' + png_url.split('/')[-1]

with open(f'posts/{image_title}', 'wb') as file:
    file.write(image.content)



