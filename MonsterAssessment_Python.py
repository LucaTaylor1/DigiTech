import sys

Restart = 1
while Restart == 1:
    Monsters = {"Stoneling" :
                { "Strength" : "7" ,
                  "Speed" : "1" ,
                  "Stealth" : "25" ,
                  "Cunning" : "15"},
                "Vexscream" :
                { "Strength" : "1" ,
                  "Speed" : "6" ,
                  "Stealth" : "21" ,
                  "Cunning" : "19"},
                "Dawnmirage" :
                { "Strength" : "5" ,
                  "Speed" : "15" ,
                  "Stealth" : "18" ,
                  "Cunning" : "22"},
                "Blazegolem" :
                { "Strength" : "15" ,
                  "Speed" : "20" ,
                  "Stealth" : "23" ,
                  "Cunning" : "6"},
                "Websnake" :
                { "Strength" : "7" ,
                  "Speed" : "15" ,
                  "Stealth" : "10" ,
                  "Cunning" : "5"},
                "Moldvine" :
                { "Strength" : "21" ,
                  "Speed" : "18" ,
                  "Stealth" : "14" ,
                  "Cunning" : "5"},
                "Vortexwing" :
                { "Strength" : "19" ,
                  "Speed" : "13" ,
                  "Stealth" : "19" ,
                  "Cunning" : "2"},
                "Rotthing" :
                { "Strength" : "16" ,
                  "Speed" : "7" ,
                  "Stealth" : "4" ,
                  "Cunning" : "12"},
                "Froststep" :
                { "Strength" : "14" ,
                  "Speed" : "14" ,
                  "Stealth" : "17" ,
                  "Cunning" : "4"},
                "Wispghoul" :
                { "Strength" : "17" ,
                  "Speed" : "19" ,
                  "Stealth" : "3" ,
                  "Cunning" : "2"},
                }

    print("----------------------------\n\nHere are the monster cards you hold:")
    for Monsters_id, Monsters_info in Monsters.items():
                print (f"----------\n{Monsters_id}")
                for key, value in Monsters_info.items():
                    print(f"{key}: {value}")

    Monster_swap = input("----------\n\nWould you like to swap a monster card for your own? Y/N: ").lower()
    if Monster_swap == ("Y").lower():
        Monster_name = input("What monster card would you like to replace? ")
        id_value = Monsters[Monster_name]
        print (f"----------\n{Monster_name}")
        for key, value in id_value.items():
                    print(f"{key}: {value}")
    else:
        print("Ok")
        sys.exit()

    token = 1

    New_card = input("----------\nWhat name would you like for your new monster? ")
    print("\nThe following values can only be between 1 and 25!")
    while token == 1:
        New_strength = input("\nHow strong do you want your card to be? ")
        New_speed = input("How fast do you want your card to be? ")
        New_stealth = input("How stealthy do you want your card to be? ")
        New_cunning = input("How cunning do you want your card to be? ")

        stats = [int(New_strength), int(New_speed), int(New_stealth), int(New_cunning)]

        if any(stat < 1 or stat > 25 for stat in stats):
            print("\nPlease redo, one of your stats are invalid:\n")
        else:
            print("\nHere is your new card!")
            token + 100
            break

    Monsters[New_card] = Monsters[Monster_name]
    del Monsters[Monster_name]
    Monsters[New_card]["Strength"] = New_strength
    Monsters[New_card]["Speed"] = New_speed
    Monsters[New_card]["Stealth"] = New_stealth
    Monsters[New_card]["Cunning"] = New_cunning

    print(f"\n----------\n{New_card}")
    for key, value in Monsters[New_card].items():
        print(f"{key}: {value}")

    validation = input("----------\n\nAny changes to your card? Y/N: ")

    if validation == ("N").lower():
        print("\n\n\nHere is your Updated list of monster cards:")
        for monster_id, monster_info in Monsters.items():
            print(f"----------\n{monster_id}")
            for key, value in monster_info.items():
                print(f"{key}: {value}")
                print("----------)")
                sys.exit()
    else:
        Strengthchange = input("\nWould you like to change it's strength? ")
        if Strengthchange == ("Y").lower():
            New_strength2 = input("What is your new strength?" )
            Monsters[New_card]["Strength"] = New_strength2
            
        Speedchange = input("\nWould you like to change it's speed? ")
        if Speedchange == ("Y").lower():
            New_speed2 = input("What is your new speed?" )
            Monsters[New_card]["Speed"] = New_speed2
            
        Stealthchange = input("\nWould you like to change it's stealth? ")
        if Stealthchange == ("Y").lower():
            New_stealth2 = input("What is your new stealth?" )
            Monsters[New_card]["Stealth"] = New_stealth2
            
        Cunningchange = input("\nWould you like to change it's cunning? ")
        if Cunningchange == ("Y").lower():
            New_cunning2 = input("What is your new cunning?")
            Monsters[New_card]["Cunning"] = New_cunning2
            
    print(f"\n----------\n{New_card}")
    for key, value in Monsters[New_card].items():
        print(f"{key}: {value}")
    print("----------")

    Restart1 = input("Would you like to redo? ")
    if Restart1 == ("Y").lower():
        Restart = 1
    elif Restart1 == ("N").lower():
        Restart = 0

                 
    












