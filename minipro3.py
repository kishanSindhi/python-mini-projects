print('''You are standing in a dark room.
You can't see any thing as it is so dark.
But suddently you see a ittle ray of light at a distant
You walk in that direction you find 2 doors there..
There can b any thing behind that door....
It is might be bettr to stay where you are. 
There can b something dangerous wating for you behind the door.
There might be something interesting thing behind the door.
So its your choice to go through the door
If you want to go get out of the dark you can but at a risk
So which door you will select RIGHT one or LEFTone''')
s1 = input("'r' for RIGHT door || 'l' for LEFT door")
if s1 == 'r':
    print('''There if a BIG MONSTER sleeping right in front of another door
             If you want to show some bravery then you can kill the monter.
             There is shotgun next to you.
             If you want to kill the monster by shooting him at his head
             Or you can trace pass silently while he is sleeping.
             Its your choice... ''')
    s2 = input("'k' for killng the monster || 't' for trace passing silently")
    if s2 == 'k':
        print('''The monster was too strong.
                 Your shotgun didn't even scrach him.
                 How can you so dumb.
                 Now monster will kill you''')
        exit()
    elif s2 == 't':
        print('''You succesfully entered the door without even disturbing the monster's sleep.
                 You entered the room full of dimonds.
                 And there is an another door in front of you.
                 If you want you can take some dimonds with you in that door.
                 That might be exit
                 You can leave your life with easily after taking some hand full of dimonds in your pocket
                 You can enjoy your lif after that..''')
        s3 = input(
            "'t' for taking dimonds with you || 'n' for not taking diamonds with you")
        if s3 == 't':
            print('''The diamonds wer cursed....
                     The one who touch the diamonds dies in few days
                     So enjoy your last days with your loved ones...:(''')
            exit()
        elif s3 == 'n':
            print('''You are an honest man.
                     You win the game of life
                     You seems to be a wise guy.
                     You did not take un necessary risk.''')
            exit()
        else:
            print("Enter the corre ct value")
    else:
        print("You might have entered incorrect value")

elif s1 == 'l':
    print('''There is a bear in the room, there is a door behind the bear.
             The bear is eating honey.
             if you want you can easily trace pass by walking silently.
             Or you can take the honey from bear and run to the next door.''')
    s2 = input(
        "'s' for tracepassing silently || 't' for taking honey from the bear")
    if s2 == 't':
        print('''You trie taking honey from bear
                 The bear was too strong for you...
                 You thought you can defeat bear barehanded
                 Are you sreious...
                 
                 GAME OVER''')
        exit()
    elif s2 == 't':
        print('''You succesfully entered the door without even disturbing the monster's sleep.
                 You entered the room full of dimonds.
                 And there is an another door in front of you.
                 If you want you can take some dimonds with you in that door.
                 That might be exit
                 You can leave your life with easily after taking some hand full of dimonds in your pocket
                 You can enjoy your lif after that..''')
        s3 = input(
            "'t' for taking dimonds with you || 'n' for not taking diamonds with you")
        if s3 == 't':
            print('''The diamonds wer cursed....
                     The one who touch the diamonds dies in few days
                     So enjoy your last days with your loved ones...:(''')
            exit()
        elif s3 == 'n':
            print('''You are an honest man.
                     You win the game of life
                     You seems to be a wise guy.
                     You did not take un necessary risk.''')
            exit()
        else:
            print("You might have entered incorrect value")
    else:
        print("you might have entered incorrect value")
else:
    print("You might have entered incorrect value")
