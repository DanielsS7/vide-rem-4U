def weapon_data(key=None):    
    data = [
        {"name" : "Great Sword", "Special_multiplyer" : 5.4, "Class" : "Blademaster"},
        {"name" : "Long Sword", "Special_multiplyer" : 3.3, "Class" : "Blademaster"},
        {"name" : "Sword and Shield", "Special_multiplyer" : 1.4, "Class" : "Blademaster"},
        {"name" : "Dual Blades", "Special_multiplyer" : 1.4, "Class" : "Blademaster"},
        {"name" : "Lance", "Special_multiplyer" : 2.3, "Class" : "Blademaster"},
        {"name" : "Gunlance", "Special_multiplyer" : 2.3, "Class" : "Blademaster"},
        {"name" : "Hammer", "Special_multiplyer" : 5.2, "Class" : "Blademaster"},
        {"name" : "Hunting Horn", "Special_multiplyer" : 5.2, "Class" : "Blademaster"},
        {"name" : "Insect Glaive", "Special_multiplyer" : 3.1, "Class" : "Blademaster"},
        {"name" : "Switch Axe", "Special_multiplyer" : 5.4, "Class" : "Blademaster"},
        {"name" : "Charge Blade", "Special_multiplyer" : 3.6, "Class" : "Blademaster"},
        {"name" : "Heavy Bowgun", "Special_multiplyer" : 1.5, "Class" : "Gunner"},
        {"name" : "Light Bowgun", "Special_multiplyer" : 1.3, "Class" : "Gunner"},
        {"name" : "Bow", "Special_multiplyer" : 1.2, "Class" : "Gunner"}
    ]
    if key == "name":
        names = []
        for x in data:
            names.append(x["name"])
        return names
    elif key == "special_multiplyer":
        multiplyers = []
        for x in data:
            multiplyers.append(x["Special_multiplyer"])
        return multiplyers
    elif key == "class":
        classes = []
        for x in data:
            classes.append(x["Class"])
    else:
        return data

def sharpness_data(key=None):
    data = [
        {"name" : "Red", "attack" : 0.5 ,"element" : 0.25 },
        {"name" : "Orange", "attack" : 0.75 ,"element" : 0.50 },
        {"name" : "Yellow", "attack" : 1 ,"element" : 0.75 },
        {"name" : "Green", "attack" : 1.05 ,"element" : 1 },
        {"name" : "Blue", "attack" : 1.2 ,"element" : 1.06 },
        {"name" : "White", "attack" : 1.32 ,"element" : 1.12 },
        {"name" : "Purple", "attack" : 1.44 ,"element" : 1.20 },
    ]
    if key == "name":
        names = []
        for x in data:
            names.append(x["name"])
        return names
    elif key == "attack":
        names = []
        for x in data:
            names.append(x["attack"])
        return names
    elif key == "element":
        names = []
        for x in data:
            names.append(x["element"])
        return names
    else:
        return data





