import winapps

for item in winapps.list_installed():
    g = item.name
    #print(item.name.split(","))
    print(g.split(","))
