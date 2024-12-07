import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.baraasallout.com/test.html"
response = requests.get(url)

if response.status_code == 200:
    print("Page loaded successfully.")
else:
    print(f"Error: Unable to load the page (Status code: {response.status_code})")
    exit()

page = BeautifulSoup(response.text, "html.parser")

headers = page.find_all(["h1", "h2"])
print("Headers:")
for header in headers:
    print(header.get_text())

paragraph = page.find("p")
if paragraph:
    print("Paragraph:")
    print(paragraph.get_text())
else:
    print("No paragraph found.")

lists = page.find_all("li")
print("List items:")
for item in lists:
    print(item.get_text())

table = page.find("table")

if table:
    rows = table.find_all("tr")

    with open("web_scraping.csv", mode="w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Stock Status"])

        for row in rows:
            cols = row.find_all("td")
            if len(cols) > 0:
                product_name = cols[0].text.strip()
                price = cols[1].text.strip()
                stock_status = cols[2].text.strip()

                print(f"Product: {product_name}, Price: {price}, Stock Status: {stock_status}")
                writer.writerow([product_name, price, stock_status])

    print("Data has been saved to 'web_scraping.csv'.")
else:
    print("No table found on the page.")

            