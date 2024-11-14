import requests
from bs4 import BeautifulSoup
import time

url = "https://ggplot2.tidyverse.org/reference/index.html"  
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


response = requests.get(url, headers=headers)


# 檢查 HTTP 請求是否成功
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
    
# 檢查網頁內容是否存在
if response.content:
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 例子：提取所有的標題 (h1 標籤)
    titles = soup.find_all('h1')
    
    if titles:
        print("Titles found:")
        for title in titles:
            print(title.get_text())
    else:
        print("No titles found.")
else:
    print("Failed to retrieve content from the page.")

# 提取所有的連結
links = soup.find_all('a', href=True)

if links:
    print("Links found:")
    for link in links:
        href = link['href']
        text = link.get_text().strip()
        print(f"Text: {text}, URL: {href}")
else:
    print("No links found.")

# 添加延遲以防止過度請求
print("Waiting for 2 seconds...")
time.sleep(2)

import csv

# 開啟 CSV 文件以寫入模式
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'URL'])  # 寫入表頭

    # 寫入每一個連結
    for link in links:
        text = link.get_text().strip()
        href = link['href']
        writer.writerow([text, href])

print("Data saved to data.csv")