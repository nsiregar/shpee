# shpee

Python Wrapper for Shopee Affiliate API

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pprof.

```bash
pip install shpee
```

## Usage

```python
# shopee_client.py

from shpee import ShopeeAffiliate


APP_ID = "12345"
APP_SECRET = "APPSECRET"

url = "https://shopee.co.id/some-long-url-from-shopee-product-page?params=with-tracking-params"
sub_ids = ["ProductName", "Twitter"]

client = ShopeeAffiliate(app_id=APP_ID, app_secret=APP_SECRET)
resp = client.shortlink(url, sub_ids)
```

It will return response class from `httpx` http client

## License
[MIT](https://choosealicense.com/licenses/mit/)
