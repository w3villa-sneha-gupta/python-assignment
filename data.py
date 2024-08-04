import pandas as pd
import requests
from bs4  import BeautifulSoup
url = "https://www.amazon.in/s?k=samsung&crid=3OKL8GJHJ7CRB&sprefix=samsung%2Caps%2C284&ref=nb_sb_noss_1"
proxies = {
    "http" : "http://149.20.253.126"
}
# Create lists to store the data
product_names = []
product_prices = []

response = requests.get(url, proxies=proxies)
soup = BeautifulSoup(response.text , "html.parser")
# print(soup.find_all(class_="KzDlHZ"))
for data in soup.find_all(class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2") :
    product_names.append(data.text)
for data in soup.find_all(class_="a-price-whole") :
    product_prices.append(data.text)


# Create a DataFrame from the lists
df = pd.DataFrame({
    "Product Name": product_names,
    "Price": product_prices
})

# Save the DataFrame to a CSV file (optional)
df.to_csv("amazon_samsung_products.csv", index=False)

# Print the DataFrame
print(df)