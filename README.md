[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
![Maintainer](https://img.shields.io/badge/maintainer-psZachary-blue)

 
# RPI Locator Python 
A Python implementation of the undocumented / unknown API found at `https://rpilocator.com`. When done right, this can allow you to get the drop on Rasberry PI restocks and (hopefully) bypass pesky scalpers. 
## Requirements
```
Python 3.0+ w/ pip
requests>=2.28.1
```

## Backend
This implementation of the API provided by `https://rpilocator.com` was created by hand without documentation. I did this by reverse engineering the endpoint `https://rpilocator.com/data.cfm` and viewing data requests sent at runtime via the browser to fill data on the frontend portion. 

## Example
```python
import rpi_locator

pi_locator = rpi_locator.RPILocator("TOKEN")

item_list, raw_data = pi_locator.GetRPIList()

for item in item_list:
    if item.avail == "Yes":
        print("Item: %s is available at %s %s", item.description, item.sort, item.currency)
```
## Getting Token
1. Go to https://rpilocator.com
2. Press `CTRL+SHIFT+I` or open inspect
3. Click the `Network` tab at the top
4. Follow the image below
<br></br>
![This is an image](https://i.ibb.co/Fgg2djG/token.png)


