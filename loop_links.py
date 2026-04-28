def locators_links():

    contador = 0 
    locator_link = "/html/body/div[2]/main/div[4]/div[7]/div[2]/div[1]/div/a"
    for i in range(30):
        contador +=1
        locator_links = locator_link.replace("/div[1]", f"/div[{contador}]")
        print(locator_links)
    return locator_links