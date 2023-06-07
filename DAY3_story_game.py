#give a final touch , and insert ascii art.
#TREASURE HUNT PROJECT

print (r"""
                    _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")

import time

print("\n")

print ("WELCOME TO TREASURE HUNT !")

time.sleep(1)
print("\n")
starting_txt = "Your ship wrecked and now u wake up in a room which is has 2 doors. You remember that only the lucky ones , the destined ones wake up to a room with 2 doors . You realise that you're the chosen one. "
for i in starting_txt.split():
    print(i, end=" ", flush=True)
    time.sleep(0.1)

time.sleep(3)
print()

print("There are 2 doors in front of you. One is red and another is green. Which one would you like to enter ?")
time.sleep(3)

#condition 1 : red or green door ?
door = input("type red or green : ")
if door == "red":
    time.sleep(1)

    red_door = "you enter the red door and...."
    for i in red_door.split():              #red_door text
        print(i,end=" ",flush=True)
        time.sleep(0.1)    
    
    print()
    time.sleep(2)
    
    ah = "a a a a a  a a a a a a  a a a a a a a  a a a a a a a a  a a a a a a  a a a a a a a  a a ahh h h h h  h h h h h h h h h h h h h "
    for i in ah.split():                    #aaahh text
        print(i,end="",flush=True)
        time.sleep(0.05)

    print()
    time.sleep(2)

    print ("u fell into a hole and DIED!!!\n")

    time.sleep(1)

    print ("GAME OVER !")
    print("\n")

#if user choses green then following ...
if door == "green":

    time.sleep(1)
    print("\n")
    
    water_text="You enter and now fall into a water body."
    for i in water_text.split():
        print(i,end=" ",flush = True)
        time.sleep(0.1)
    
    print()
    time.sleep(2)
    
    see_land_text="U see land far ashore. But between u and land, there are dangerous beings that may/may not hurt u , what would u like to do ? wait or swim accross"
    for i in see_land_text.split():
        print(i,end=" ",flush=True)
        time.sleep(0.1)
    print()

    water = input("type 'wait' or 'swim' ")
    
    #condition 2 : wait or swim
    if water =="wait":
        time.sleep(6)
        for _ in range (100):
            still_wait_text = "still wanna wait ? (y or n)"
            for i in still_wait_text.split():
                print(i,end=" ",flush=True)
                time.sleep(0.1)

            still_wait = input()
            #condition 3 : still wanna wait ?
            if still_wait == "y":
                time.sleep(3)
                print("ughhh...")
                time.sleep(6)
                print("uugowwurrrrr ....") 
                time.sleep(4)
                print("(silence....)")
                time.sleep(6)

                drowned_text = "u drowned. GAME OVER!!"
                for i in drowned_text.split():
                    print(i,end=" ",flush = True)
                    time.sleep(0.1)
                
                break

            else : 
                if still_wait == "n":

                    no_wait = "so u dont wanna wait? Good choice ! u swim and swim and swim ....."
                    for i in no_wait.split():
                        print(i,end=" ",flush=True)
                        time.sleep(0.1)

                    print()
                    time.sleep(1)

                    too_late = "but its too late, those beings are onto u . GO. FAST. SWIM, otherwise .... "
                    for i in too_late.split():
                        print(i,end=" ",flush=True)
                        time.sleep(0.1)

                    print()
                    time.sleep(3)
                    print("They Got You. ur ded. (lmao) .\nGAME OVER !!!")
                    break
    elif water == "swim":
        ofc_swim_txt = "of course u'd swim. what else would one choose ? u swim. no dangerous beings harm u . u reach land safely ."
        for i in ofc_swim_txt.split():
            print(i,end=" ",flush=True)
            time.sleep(0.1)

        print()
        
        lady_txt = "what do u see ? 3 beautiful ladies standing in front of 3 doors. One is tall and hot, a typical choice. another is short and hot (hmmm, hotness at every inch), last one is short and cute (really cute !) "
        for i in lady_txt.split():
            print(i,end=" ",flush=True)
            time.sleep(0.1)
        
        print()
        time.sleep(5)
        
        print("choose any one of the following \n1)tall and hot\n2)short and hot\n3)short and cute\n")
        lady_choose = input ("""type 1,2 or 3""")

        print()

        if lady_choose == "1":
            choice1 ="what a typical choice.\nSHE STABBED U, ur lmao ded. \nGAMEOVER!"
            for i in choice1.split():
                print (i,end=" ",flush=True)
                time.sleep(0.1)

        elif lady_choose == "2":
            choice2 ="what a typical choice.\nSHE STABBED U, ur lmao ded. \nGAMEOVER!"
            for i in choice2.split():
                print (i,end=" ",flush=True)
                time.sleep(0.1)

        elif lady_choose == "3":
            choice3 ="what a typical choice.\nIs she gonna kill u ?"
            for i in choice3.split():
                print(i,end=" ",flush=True)
                time.sleep(0.1)
            
            time.sleep(3)

            whoa ="whoa ? what just happened ? she gave u the treasure ? you've won !\nGAME OVER!!!"
            for i in whoa.split():
                print (i, end=" ",flush=True)