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
easygui.msgbox("Welcome to the Monster Card Index!")
while Restart == 1:
    menu = easygui.buttonbox("What would you like to do today?", title=["Monster Card Index"], choices=["View Cards", "Edit/Delete Cards", "Add New Card", "Exit"])
    if menu == "Exit":
        easygui.msgbox("Very Well.")
        sys.exit()
        
    elif menu == "View Cards":
        while True == 1:
            monster_names = list(Monsters.keys())
            chosenmonster = easygui.choicebox("Choose what monster you'd like to view:", title=["Monster Selection"], choices=monster_names)
            if chosenmonster == None:
                break
            id_value = Monsters[chosenmonster]
            message = f"{chosenmonster}\n" + "-" * len(chosenmonster) + "\n"
            for stat, value in id_value.items():
                message += f"{stat}: {value}\n"
            viewchoice = easygui.buttonbox(message + "----------", choices=["Return", "Menu"])
            if viewchoice == ("Menu"):
                    break
                    
    elif menu == "Edit/Delete Cards":
        while True:
            monster_names = list(Monsters.keys())
            chosenmonster = easygui.choicebox("What Monster would you like to edit?", title=["Monster Editing"], choices=monster_names)
            if chosenmonster == None:
                break
            id_value = Monsters[chosenmonster]
            choice2 = easygui.buttonbox("Would you like to edit or delete " + chosenmonster + "?", choices=["Edit", "Delete"])
            if choice2 == "Delete":
                removed_monster = Monsters.pop(chosenmonster)
                easygui.msgbox("The card " + chosenmonster + " has been deleted.")
                break
            if choice2 == "Edit":
                id_value = Monsters[chosenmonster]
                message = f"{chosenmonster}\n" + "-" * len(chosenmonster) + "\n"
                for stat, value in id_value.items():
                    message += f"{stat}: {value}\n"
                editchoice = easygui.buttonbox(message + "----------\nWhat value would you like to change?", choices=["Strength", "Speed", "Stealth", "Cunning", "Cancel"])
                if editchoice == "Cancel":
                    break
                
                Newvalue = easygui.enterbox("Please enter what value you would like to change for " + editchoice + ":\nValues 1 - 25")
                if Newvalue == None:
                    break
                Monsters[chosenmonster][editchoice] = Newvalue
                easygui.msgbox(f"{editchoice} has been updated to {Newvalue} for {chosenmonster}.")

    elif menu == "Add New Card":
        while True:
                 
    













