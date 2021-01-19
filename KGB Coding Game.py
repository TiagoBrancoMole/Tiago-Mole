def  kgbcodinggame():
        
        lives = 3
        import time
        print("Aldrich: Welcome Agent 11")
        time.sleep(3.5)
        import time
        print("Aldrich: You have been assigned a mission to find and collect valuable Soviet papers in a KGB building in East Berlin")
        time.sleep(3.5)
        import time
        print("Aldrich: Operation Recall is especially important as the big guys in the CIA believe the papers contain Russian nuclear codes")
        time.sleep(3.5)
        import time
        print("Aldrich: You only have three chances at this, before the Mission is cancelled. If the KGB finds you with the papers the mission is done, no matter how many lives you have left")
        time.sleep(8.5)
        import time
        acceptchallenge = str(input("Aldrich: If you want to accept this mission, just say Yes. If not, just say No and we will find another Agent to complete the mission"))
        if acceptchallenge == "No":
                import time
                print("Aldrich: Well, thats too bad. I thought you were up to the challenge. Goodbye and good luck Agent 11")
                time.sleep(3.5)
                exit()
        if acceptchallenge == "Yes":
                import time
                print("Aldrich: Welcome to East Berlin Agent. Pretty ugly, right? Walk towards that black building on the corner of the street.")
                time.sleep(4.5)
                movement1 = str(input("Aldrich: This is your last chance to turn back. If you decide to advance just say Advance, if not say Turn Back"))
                if movement1 == "Turn Back":
                        import time
                        print("Aldrich: Well, thats too bad. I thought you were up to the challenge. Goodbye, and good luck Agent 11")
                        time.sleep(4.0)
                        exit()
                if movement1 == "Advance":
                        print("Aldrich: Listen up, when you approach the multiple security checkpoints in the building the keypad on the side of the door will ask you a question in Russian. Tom here at the CIA will translate the message to you and you will need to answer it.")
        time.sleep(6.5)
        import time
        print("Aldrich: If you get a question wrong it will send an alert to a KGB soldier who will check the door and find you")
        time.sleep(6.5)
        import time
def room1():
        import time
        print("Aldrich: You are approaching the Building. Keep your head low and the guards will go investigate a suspicous person.")
        time.sleep(4.0)
        import time
        print("Aldrich: Go now")
        time.sleep(7.0)
        import time
        print("KGB Security Code: Кем был Брежнев?")
        time.sleep(5.0)
        answer1 = str(input("Tom: Who was Brezhnev?"))
        correctanswer = "Prime Minister of Soviet Union"
        if answer1 != correctanswer:
            newlives = lives - 1
            import time
            print("Aldrich: No! Thats wrong! A Soviet Guard is now coming for you!")
            time.sleep(4.5)
            print("KGB Soldier: Стоп! Нарушитель! Ты идешь со мной!") 
        if answer1 == correctanswer:
            import time    
            print("Aldrich: Nice job. Now move to the hallway to the left of you. Do you see that door to the right of you? That is a KGB drying room. Break into that room so you can pass as a soldier in the halls")
            time.sleep(8.5)
        if newlives < 1:

                print("Aldrich: Its over, mission has been cancelled. I thought you were better than this Agent")
                exit()
        if newlives >= 1:
                print("You still can complete the mission")
                room1()
def room2():
        import time
        print("Aldrich: However, there is a door to the left of you that has not been identified by intel")
        time.sleep(7.0)
        movement = str(input("Aldrich: This is your call Agent, which door do you want to go through? The Left Door or the Right Door"))
        if movement == "Left Door":
                import time
                print("Aldrich: Alright Tom here will translate this question. Be careful, we have not identified what could be behind that door")
                time.sleep(4.5)
                import time
                print("KGB Security Code: Кто был первым лидером славного Советского Союза?")
                time.sleep(5.0)
                import time
                answer2 = str(input("Tom: Who was the first leader of the Soviet Union"))
        if answer2 != "Vladimir Lenin":
                import time
                print("Aldrich: No! thats wrong! c'mon Agent! I thought you could do thi...")
                time.sleep(2.5)
                import time
                print("KGB Soldier: Стоп! руки за спину! Американский злоумышленник!")
                time.sleep(2.0)
                newlives3 = newlives2 - 1

        if answer2 == "Vladimir Lenin":
                newlives3 = newlives2 - 1
                import time
                print("Aldrich: Nice job! Alright breach the door, watch out, there may be soldiers on the other si....")
                time.sleep(2.4)
                import time
                print("KGB Officers: Стоп! руки вверх! одна земля!")
                time.sleep(3.7)

        if newlives2 < 1:
                print("Aldrich: Its too late, the mission has been cancelled. I thought more of you Agent")
                exit()
        if newlives2 >= 1:
                print("Aldrich: You still have a chance to complete the mission Agent!")
                room2()
                        
                           
def room3():
            import time
            print("Aldrich: Stop! Guard coming up behind you")
            time.sleep(8.0)
            import time
            print("KGB Soldier: хорошего дня")
            time.sleep(5.5)
            import time
            print("Aldrich: Wow, that was a close one")
            time.sleep(6.5)
            import time
            print("Aldrich: Ok now head to the keypad, the hallway is clear. Be quick as there are an increased amount of KGB soldiers patrolling today")
            time.sleep(3.0)
            print("Когда была революция славы?")
            import time
            correctanswer2 = str(input("Tom: When was the Communist revolution?"))
            time.sleep(3.0)
            if correctanswer2 != "1917":
                    newlives4 = newlives3 - 1
                    import time
                    print("Aldrich: No! thats wrong! C'mon Agent......")
                    time.sleep(4.0)
                    import time
                    print("KGB Soldier: Вы думали, что сможете ворваться! высокомерные американцы")
                    time.sleep(4.0)
            if correctanswer2 == "1917":
                    import time
                    print("Aldrich: Nice job Agent. Alright, grab a KGB uniform and change quickly")
                    time.sleep(4.0)
            if newlives4 < 1:
                    import time
                    print("Aldrich: Its over, the mission has been cancelled. I thought you were better than this Agent")
                    time.sleep(3.0)
                    exit()
            if newlives4 >= 1:
                    import time
                    print("Aldrich: You still can complete the mission")
                    room3()
                    time.sleep(3.0)
def room4():
        import time
        uniformchoice = str(input("Aldrich: Which uniform do you want to wear Agent? KGB Officer or KGB Soldier?"))
        time.sleep(4.0)
        if uniformchoice == "KGB Officer":
                newlives5 = newlives4 + 0
                import time
                print("Aldrich: Alright, get changed quickly. With the KGB Officer uniform we believe that you will be less suspicous. KGB Soldiers are always scared of their boss, and a Officer uniform can get us into important rooms")
                time.sleep(4.0)
        if uniformchoice == "KGB Soldier":
                newlives5 = newlives4 - 1
                import time
                print("Aldrich: Alright, as a Soldier you can move through the hallways pretending to be on patrol. Watch out for officers, they  like to pick on new soldiers and if they find you, your done")
                time.sleep(4.5)
                import time
                print("Aldrich: Exit the room, and be careful, intel says in the next few minutes Soldiers will pick up their clothes, so you have to move now")
                time.sleep(5.0)
                import time
                print("KGB Soldier: Эй, где твой значок Наша нация? Под чьим офицером ты?")
                time.sleep(5.5)
                import time
                response = str(input("Tom: Quick! answer Belkezov!"))
                time.sleep(3.0)
                if response != "Belkezov":
                        import time
                        print("KGB Soldier: Ты не в моем отряде! Самозванец! Самозванец!")
                        time.sleep(3.0)
                        import time
                        print("Aldrich: No! thats not what we told you to say! the mission has been compromised!")
                        newlives6 = newlives5 - 1
                        time.sleep(2.5)
                if response == "Belkezov":
                        import time
                        print("KGB Soldier: Забавно, ведь подразделения Белкезова сейчас нет на объекте, им на родине дано особое задание. охранники поймают его!")
                        time.sleep(2.0)
                        import time
                        print("Aldrich: Damn it, they gave us wrong intel! The mission has been cancelled! Im sorry Agent")
                        time.sleep(3.5)
                if newlives6 < 1:
                        print("Aldrich: Its over, the mission has been cancelled. I thought you could do this Agent")
                        exit()
                if newlives6 >= 1:
                        print("Aldrich: You still have a chance to complete the mission!")
                        room5()
        import time
        print("Aldrich: Now that you are dressed as a KGB Officer, very few soldiers will look you in the face")
        time.sleep(4.0)
def room5():
        import time
        print("Aldrich: Now head down the corrider and turn left at the end of the hall")
        time.sleep(6.5)
        import time
        print("KGB Guard: Простите, сэр, но этот коридор конфиденциальный. Только квалифицированный персонал может проходить через")
        time.sleep(3.5)
        import time
        print("Tom: Sorry sir, but this hallway is confidential. Only qualified personnel can go through")
        time.sleep(3.7)
        import time
        print("Aldrich: Ok, intel has told us that there are two code words that may work to get yourself through that hallway")
        print("Tom: The two words are Капиталистический осел. This is pronounced Kapitalisticheskiy osel. The other word is Советский жеребец, pronounced Sovetskiy zherebets") 
        CodeWord = str(input("Aldrich: Agent you can choose which code word you want to use?"))
        if CodeWord == "Kapitalisticheskiy osel":
                newlives7 = newlives6 - 1
                import time
                print("KGB Guard: Sorry sir, this hallway is confidential. Please leave the area")
                time.sleep(3.5)
                import time
                print("Aldrich: Dang it the codeword was wrong. You have to find a different way in")
                time.sleep(3.7)
                import time
                print("Aldrich: alright there is a different path you can take to get there. Go through that door to the left of the hallwy you just left")
                time.sleep(4.0)
                import time
                print("Aldrich: Alright now head to the keypad...")
                time.sleep
                import time
                print("KGB Soldier: Вы думаете, мы вас не найдем! Ха! Американское высокомерие")
                time.sleep(2.5)
                import time
        if CodeWord == "Sovetskiy zherebets":
            import time
            print("KGB Guard: Go on ahead sir. If you are here for the Beleztsky Report its the Second door on the Right, and if you are here for the Slovetsky Report, third door to to the Left")
            time.sleep(2.5)
            import time
            print("Aldrich: Woah, Intel has not told us that Solevetsky was here")
            time.sleep(3.0)
        if newlives7 < 1:
                print("Aldrich: The mission has ben cancelled, I thought you could do this Agent")
                exit()
        if newlives7 >= 1:
                print("Aldrich: You can still do this Agent")
                room6()
def room6():
        import time
        print("Aldrich: Alright ")
   
kgbcodinggame()