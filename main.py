class Weapon:


    class Sharpness:
        
        def __init__(self) -> None:
            self.sharpness = [
                {"name" : "Red", "attack" : 0.5 ,"element" : 0.25 },
                {"name" : "Orange", "attack" : 0.75 ,"element" : 0.50 },
                {"name" : "Yellow", "attack" : 1 ,"element" : 0.75 },
                {"name" : "Green", "attack" : 1.05 ,"element" : 1 },
                {"name" : "Blue", "attack" : 1.2 ,"element" : 1.06 },
                {"name" : "White", "attack" : 1.32 ,"element" : 1.12 },
                {"name" : "Purple", "attack" : 1.44 ,"element" : 1.20 },
            ]

        def set(self,sharpness):
            for sharpness_data in self.sharpness:
                if sharpness_data["name"] == sharpness:
                    self.name = sharpness_data["name"]
                    self.attack = sharpness_data["attack"]
                    self.element = sharpness_data["element"]

        def get(self):
            return  {
                    "name" : self.name,
                    "attack" :self.attack,
                    "element" : self.element
                    }
        
    class Affinity:

        pass

    class Type:

        def __init__(self) -> None:
            self.Types = [
                {"Name" : "Great Sword", "Special_multiplyer" : 5.4, "Class" : "Blademaster"},
                {"Name" : "Long Sword", "Special_multiplyer" : 3.3, "Class" : "Blademaster"},
                {"Name" : "Sword and Shield", "Special_multiplyer" : 1.4, "Class" : "Blademaster"},
                {"Name" : "Dual Blades", "Special_multiplyer" : 1.4, "Class" : "Blademaster"},
                {"Name" : "Lance", "Special_multiplyer" : 2.3, "Class" : "Blademaster"},
                {"Name" : "Gunlance", "Special_multiplyer" : 2.3, "Class" : "Blademaster"},
                {"Name" : "Hammer", "Special_multiplyer" : 5.2, "Class" : "Blademaster"},
                {"Name" : "Hunting Horn", "Special_multiplyer" : 5.2, "Class" : "Blademaster"},
                {"Name" : "Insect Glaive", "Special_multiplyer" : 3.1, "Class" : "Blademaster"},
                {"Name" : "Charge Blade", "Special_multiplyer" : 3.6, "Class" : "Blademaster"},
                {"Name" : "Heavy Bowgun", "Special_multiplyer" : 1.5, "Class" : "Gunner"},
                {"Name" : "Light Bowgun", "Special_multiplyer" : 1.3, "Class" : "Gunner"},
                {"Name" : "Bow", "Special_multiplyer" : 1.2, "Class" : "Gunner"}
            ]
            
        def set(self,type):
            for weapon_data in self.Types:
                if type == weapon_data["Name"]:
                    self.name = weapon_data["Name"]
                    self.multiplyer = weapon_data["Special_multiplyer"]
                    self.weapon_class = weapon_data["Class"] 

        def get(self):
            return {
                    "Name" : self.name, 
                    "Class" : self.weapon_class , 
                    "Special_Multiplyer" : self.multiplyer
                    }

    class Attack:

        class Modifiers:

            def __init__(self,real_attack,) -> None:
                pass
            
            def Group_A():
                #Power Charm +6 base
                pass

            def Group_B():
                #Power Talon +9
                pass

            def Group_C():
                #Demon Drug +5 
                #Mega Demon Drug +7
                #Attack up S (felyne) +3
                #Attack up M (felyne) +5 
                #Attack up L (felyne) +7
                pass

            def Group_D():
                #Might Seed +10
                #Migth Pill +25
                #Demon Horn +10
                #Demon Shot +10
                #Cool Cat (felyne) +15 if use gesture "kick back"
                pass

            def Group_E():
                #Felyne Booster +3
                pass

            def Group_F():
                #Attack Up S +10
                #Attack Up M +15
                #Attack Up L +20
                #Attack Up XL +25
                #Horned Blade +20 sharpness +1
                pass
            
            def Group_G():
                #Adrenaline+2 Attack + 30% (40% HP)
                #Felyne Heroics Attack + 35% (10% HP)
                pass

            def Group_H():
                #Attack Up (S) Song Attack + 10% (again for 15%)
                #Attack Up (M) Song Attack + 15% (again for 20%)
                pass

            def Group_I():
                #Fortitude (1 cart) attack + 10% 
                #Fortitude (2 cart) attack + 20% 
                pass

            def Group_J():
                #Challenger > Peak Performance/Prudence > Latent Power 
                #only the bigest keep

                #Challenger +1 +10, affinity + 10%
                #Challenger +2 +25, affinity + 20%
                #Peak Performance +20 
                #Latent Power +1 +30% affinity
                #Latent Power +2 +50% affinity
                pass


        def set(self,weapon_nominal_attack,weapon_special_multiplyer):
            self.nominal_attack = int(weapon_nominal_attack)
            self.special_multiplyer = float(weapon_special_multiplyer)
            self.real_attack = int(self.nominal_attack/self.special_multiplyer)

        def modify(self,value):
            self.real_attack += int(value)
            self.nominal_attack = int(self.real_attack * self.special_multiplyer)

        def get(self):
            return self.real_attack


    def __init__(self) -> None:
        self.type_is_set = False
        self.attack_is_set = False
        self.have_sharpness = False

    def set_type(self,type):
        self.type = self.Type()
        self.type_multiplyer = self.type.set(type)
        self.type_is_set = True

    def set_attack(self,attack):
        attack = int(attack)
        if self.type_is_set:
            self.attack = self.Attack()
            special_multiplyer = self.type.get()["Special_Multiplyer"]
            if self.type.get()["Class"] == "Blademaster":
                attack *= self.sharpness.get()["attack"]
            self.attack.set(attack,special_multiplyer)
            self.attack_is_set = True
        else:
            print("Error: Type is not set")

    def set_sharpness(self,sharpness):
        if self.type_is_set and self.type.get()["Class"] == "Blademaster":
            self.sharpness = self.Sharpness()
            self.sharpness.set(sharpness)

    def set_affinity(self,affinity):
        pass

if __name__ == "__main__":

    #test area
    w1 = Weapon()
    w1.set_type("Great Sword")
    w1.set_sharpness("Purple")
    w1.set_attack(1000)
















