from bs4 import BeautifulSoup as bs
import requests as r
import smtplib


AMAZON_URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
PRICE = 200

FROM_EMAIL = "ethanbundles@gmail.com"
TO_EMAIL = "euseand@gmail.com"
PASSWORD = "ethan_bundles_testing_passwords"
SMTP_ADDRESS = "smtp.gmail.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

page = r.get(AMAZON_URL, headers=headers).text
soup = bs(page, "html.parser")

title = " ".join(soup.find("span", id="productTitle").getText().strip().split())
price = float(soup.find("span", id="priceblock_ourprice").getText()[1:])

if price < PRICE:
    message = f"{title} is now at price {price}."

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{AMAZON_URL}"
        )
