import requests
import time

class RPILocatorPrice:
    def __init__(self, sort, currency, display):
        self.sort = sort
        self.currency = currency
        self.display = display

class RPILocatorLastStock:
    def __init__(self, display, sort):
        self.display = display
        self.sort = sort

class RPILocatorItem:
    def __init__(self, vendor, sku, avail, link, last_stock, description, price):
        self.vendor = vendor
        self.sku = sku
        self.avail = avail
        self.link = link
        self.last_stock = last_stock
        self.description = description
        self.price = price
    
    def __str__(self):
        return "Vendor: %s\nSKU: %s\nAvail: %s\nLink: %s\nLast Stock: %s\nDescription: %s\nPrice: %s\n" % (self.vendor, self.sku, self.avail, self.link, self.last_stock, self.description, self.price)
    
class RPILocator:
    def __init__(self, token):
        self.token = token

    def GetRPIList(self): 
        url = "https://rpilocator.com/data.cfm?method=getProductTable&token=" + self.token + "&=&_=" + str(int(time.time() * 1000))
        req_cookies = {
            "CFTOKEN": "0",
            "RPILOCATOR": "0",
            "CFID": "9cadbbf2-4ec8-4b42-a589-53ced3b6da22",
            "cfid": "9cadbbf2-4ec8-4b42-a589-53ced3b6da22",
            "_ga_JWVD0LRP64": "GS1.1.1660878449.1.1.1660880099.0.0.0",
            "_ga": "GA1.1.2070877416.1660878450"
        }
        req_headers = {
            "Host": "rpilocator.com",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://rpilocator.com/",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
            "X-Requested-With": "XMLHttpRequest",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }
        r = requests.get(url, headers=req_headers, cookies=req_cookies)
        return_list = []
        for item in r.json()["data"]:            
            price = RPILocatorPrice(item["price"]["sort"], item["price"]["currency"], item["price"]["display"])
            last_stock = RPILocatorLastStock(item["last_stock"]["display"], item["last_stock"]["sort"])
            return_list.append(RPILocatorItem(item["vendor"], item["sku"], item["avail"], item["link"], last_stock, item["description"], price))
        return (return_list, r.text)


