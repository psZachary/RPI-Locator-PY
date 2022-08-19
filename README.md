import rpi_locator

pi_locator = rpi_locator.RPILocator("t65l4ych1jtc7kyhe1bp6ohysjabh02m62dr5c28")

while True:    
    list, raw_data = pi_locator.GetRPIList()
    for item in list:
        if item.avail == "Yes":
            print("Item: %s is available at %s %s", item.description, item.sort, item.currency)
