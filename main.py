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

    class Affinity:
        pass

    class Type:

        def __init__(self) -> None:
            self.Types = [
                {"Name" : "Great Sword", "special_multiplyer" : 5.4},
                {"Name" : "Long Sword", "special_multiplyer" : 3.3},
                {"Name" : "Sword and Shield", "special_multiplyer" : 1.4},
                {"Name" : "Dual Blades", "special_multiplyer" : 1.4},
                {"Name" : "Lance", "special_multiplyer" : 2.3},
                {"Name" : "Gunlance", "special_multiplyer" : 2.3},
                {"Name" : "Hammer", "special_multiplyer" : 5.2},
                {"Name" : "Hunting Horn", "special_multiplyer" : 5.2},
                {"Name" : "Insect Glaive", "special_multiplyer" : 3.1},
                {"Name" : "Charge Blade", "special_multiplyer" : 3.6},
                {"Name" : "Heavy Bowgun", "special_multiplyer" : 1.5},
                {"Name" : "Light Bowgun", "special_multiplyer" : 1.3},
                {"Name" : "Bow", "special_multiplyer" : 1.2}
            ]
        
        def set(self,type):
            for weapon in self.Types:
                if type == weapon["Name"]:
                    self.name = weapon["Name"]
                    self.multiplyer = weapon["special_multiplyer"]
                    return self.multiplyer

    class Attack:

        class Buffs:
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

        def set_real(self,weapon_nominal_attack,weapon_special_multiplyer):
            self.nominal_attack = int(weapon_nominal_attack)
            self.special_multiplyer = float(weapon_special_multiplyer)
            self.real_attack = int(self.nominal_attack/self.special_multiplyer)
            return self.real_attack

        def change_real(self,value):
            self.real_attack += int(value)
            self.nominal_attack = int(self.real_attack * self.special_multiplyer)

        def get_real_attack(self):
            return self.real_attack

        def get_nominal_attack(self):
            return self.nominal_attack

    def __init__(self) -> None:
        self.type = self.Type()
        self.type_multiplyer = self.type.set("Hunting Horn")

        self.attack = self.Attack()
        self.real_attack = self.attack.set_real(624,self.type_multiplyer)
        

if __name__ == "__main__":

    w1 = Weapon()
    




