import databases

class Weapon:

    class Sharpness:
        
        def __init__(self) -> None:
            self.sharpness = databases.sharpness_data()

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

        class modifiers:

            def critical_boost():

                pass

            def crit_element():
                #35% SNS/DB/Bow
                #30% LBG/HBG
                #20% GS
                #25% other
                pass
            
                        
            



            pass
        
        def __init__(self) -> None:
            self.crit_multiplyer = 0.25
            self.affinity_is_set = False

        def set(self,affinity):
            self.affinity = int(affinity)
            if self.affinity > 0:
                self.crit_bonus = self.crit_multiplyer + 1
            elif self.affinity < 0:
                self.crit_bonus = 1 - self.crit_multiplyer
            else:
                self.crit_bonus = None
            self.affinity_is_set = True            

        def get(self):
            if self.affinity_is_set:
                return {
                        "affinity" : self.affinity,
                        "critical_bonus" : self.crit_bonus
                        }

    class Element:

        class modify:

            def element_plus():
                #+1 1.05x + 40 (inflated)
                #+2 1.10x + 60
                #+3 1.15x + 90
                pass
            
            def elemental_attack_up():
                #1.1x but the total cap of multiplications is 1.20
                pass
        
        def __init__(self) -> None:
            self.element_is_set = False
            self.second_element_is_set = False

        def set(self,element,amount,sharpness, double = False):
            self.first_element = element[0]
            first_amount = int(amount[0])/10
            self.first_amount = int(first_amount * sharpness)
            self.element_is_set = True

            if double:
                self.second_element = element[-1]
                secound_amount = int(int(amount[-1])/10)
                self.second_amount = secound_amount * sharpness
                self.second_element_is_set = True


        def get(self):
            values = {
                      "element" : self.first_element,
                      "amount" : self.first_amount,
                      }
            if self.second_element_is_set:
                values["second_element"] = self.second_element
                values["second_amount"] = self.second_amount

            return values

    class Type:

        def __init__(self) -> None:
            self.Types = databases.weapon_data()
            self.type_is_set = False
            
        def set(self,type):
            for weapon_data in self.Types:
                if type == weapon_data["name"]:
                    self.name = weapon_data["name"]
                    self.multiplyer = weapon_data["Special_multiplyer"]
                    self.weapon_class = weapon_data["Class"] 
                    self.type_is_set = True

        def get(self):
            if self.type_is_set:    
                return {
                        "name" : self.name, 
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
        
        def __init__(self) -> None:
            self.attack_is_set = False

        def set(self,weapon_nominal_attack,weapon_special_multiplyer):
            self.nominal_attack = int(weapon_nominal_attack)
            self.special_multiplyer = float(weapon_special_multiplyer)
            self.real_attack = int(self.nominal_attack/self.special_multiplyer)
            self.attack_is_set = True

        def modify(self,value):
            if self.attack_is_set:
                self.real_attack += int(value)
                self.nominal_attack = int(self.real_attack * self.special_multiplyer)

        def get(self):
            if self.attack_is_set:
                return self.real_attack


    def __init__(self) -> None:
        self.type_is_set = False
        self.attack_is_set = False
        self.have_sharpness = False

    def set_type(self,type):
        self.type = self.Type()
        self.type_multiplyer = self.type.set(type)
        self.type_is_set = True

    def set_sharpness(self,sharpness):
        if self.type_is_set and self.type.get()["Class"] == "Blademaster":
            self.sharpness = self.Sharpness()
            self.sharpness.set(sharpness)

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

    def set_elmental(self,element,amount,double = False):
        self.element = self.Element()
        self.element.set(element,amount,self.sharpness.get()["element"],double)

    def set_affinity(self,affinity : int):
        self.affinity = self.Affinity()
        self.affinity.set(affinity)


if __name__ == "__main__":

    #test area
    w1 = Weapon()
    w1.set_type("Great Sword")
    w1.set_sharpness("Green")
    w1.set_attack(1000)
    w1.set_affinity(50)
    w1.set_elmental(("Fire","Ice"),(500,400),True)
    print(w1.type.Types)

  









