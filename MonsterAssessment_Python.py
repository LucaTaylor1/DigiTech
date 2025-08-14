import sys, easygui

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

Restart = 1
easygui.msgbox("Welcome to the Monster Card Index!", title=["Monster Card Index"])
while Restart == 1:
    menu = easygui.buttonbox("What would you like to do today?", title=["Monster Card Index"], choices=["View Cards", "Edit/Delete Cards", "Add New Card", "Exit"])
    if menu == "Exit":
        easygui.msgbox("Very Well. Goodbye.", title=["Farewell"])
        sys.exit()
        
    elif menu == "View Cards":
        while True:
            monster_names = list(Monsters.keys())
            chosenmonster = easygui.choicebox("Choose what monster you'd like to view:", title=["Monster Selection"], choices=monster_names)
            if chosenmonster == None:
                break
            id_value = Monsters[chosenmonster]
            message = f"{chosenmonster}\n" + "-" * len(chosenmonster) + "\n"
            for stat, value in id_value.items():
                message += f"{stat}: {value}\n"
            viewchoice = easygui.buttonbox(message + "----------", title=[chosenmonster], choices=["Return", "Menu"])
            if viewchoice == ("Menu"):
                    break
                    
    elif menu == "Edit/Delete Cards":
        while True:
            monster_names = list(Monsters.keys())
            chosenmonster = easygui.choicebox("What Monster would you like to edit?", title=["Monster Editing"], choices=monster_names)
            if chosenmonster == None:
                break
            id_value = Monsters[chosenmonster]
            choice2 = easygui.buttonbox("Would you like to edit or delete " + chosenmonster + "?", title=["Edit or Delete " + chosenmonster], choices=["Edit", "Delete", "Cancel"])
            if choice2 == "Delete":
                confirmation = easygui.buttonbox("Are you certain you want to delete " + chosenmonster + "?", title=["Confirmation"], choices=["Yes", "No"])
                if confirmation == "No":
                    break
                else:
                    removed_monster = Monsters.pop(chosenmonster)
                    easygui.msgbox("The card " + chosenmonster + " has been deleted.", title=[chosenmonster + "'s deletion"])
                    break
            if choice2 == "Edit":
                id_value = Monsters[chosenmonster]
                message = f"{chosenmonster}\n" + "-" * len(chosenmonster) + "\n"
                for stat, value in id_value.items():
                    message += f"{stat}: {value}\n"
                editchoice = easygui.buttonbox(message + "----------\nWhat value would you like to change?", title=["Value Editing"], choices=["Strength", "Speed", "Stealth", "Cunning", "Cancel"])
                if editchoice == "Cancel":
                    break
                
                Newvalue = easygui.enterbox("Please enter what value you would like to change for " + editchoice + ":\nValues 1 - 25", title=[editchoice + " Editing"])
                if Newvalue == None:
                    break
                Monsters[chosenmonster][editchoice] = Newvalue
                easygui.msgbox(f"{editchoice} has been updated to {Newvalue} for {chosenmonster}.", title=["Edit confirmed"])
            if choice2 == "Cancel":
                break

    elif menu == "Add New Card":
        while True:
            card_name = easygui.enterbox("What would you like to name your new card?", title=["New card name"])

            if card_name == None:
                break
            elif card_name.strip() == "":
                easygui.msgbox("Name cannot be blank", title=["Error"])
            elif card_name in Monsters:
                easygui.msgbox("The monster " + card_name + " already exists!", title=["Error"])
                continue
            else:
                msg = "What stats would you like for " + card_name + "?"
                title = card_name + "s' Stats"
                Stats = ["Strength", "Speed", "Stealth", "Cunning"]
                statstest = easygui.multenterbox(msg, title, Stats)
                if statstest == None:
                    break

                strength = statstest[0] if len(statstest) > 0 else ""
                speed = statstest[1] if len(statstest) > 1 else ""
                stealth = statstest[2] if len(statstest) > 2 else ""
                cunning = statstest[3] if len(statstest) > 3 else ""

                if strength == "" or speed == "" or stealth == "" or cunning == "":
                    easygui.msgbox("All four stat boxes must be filled in.", title=["Error"])
                    continue

                str = int(strength)
                spe = int(speed)
                ste = int(stealth)
                cun = int(cunning)

                if str <= 0 or str >= 26:
                    easygui.msgbox("Keep Strength between 1 and 25!", title=["Error"])
                    continue

                if spe <= 0 or spe >= 26:
                    easygui.msgbox("Keep Speed between 1 and 25!", title=["Error"])
                    continue

                if ste <= 0 or ste >= 26:
                    easygui.msgbox("Keep Stealth between 1 and 25!", title=["Error"])
                    continue

                if cun <= 0 or cun >= 26:
                    easygui.msgbox("Keep Cunning between 1 and 25!", title=["Error"])
                    continue

                Monsters[card_name] = {"Strength" : statstest[0], "Speed" : statstest[1],
                                       "Stealth" : statstest[2], "Cunning" : statstest[3]}
                
                easygui.msgbox("The card " + card_name + " has been successfully added!", title=[card_name + " created"])
                break
