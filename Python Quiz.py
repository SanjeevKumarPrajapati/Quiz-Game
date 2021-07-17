import playsound
from gtts import gTTS
import pyfiglet
pp=0
def speak(text):
    tts=gTTS(text=text,lang="en")
    filename="ff.mp3"
    tts.save(filename)
    playsound.playsound(filename)
def question1():
    print("\n\t\tQ.1) What Relationship Is Appropriate For Fruit And Papaya? ")
    print("\n\t\t\tA. association")
    print("\t\t\tB. composition")
    print("\t\t\tC. inheritance")
    print("\t\t\tD. All of the above")
    def answer():
        global pp
        a=input("\n\t\t\tEnter Your Choice : ").lower()
        if(a=='a' or a=='association'):
            pp-=1
        elif(a=='b' or a=="composition"):
            pp-=1
        elif(a=="c" or a=="inheritance"):
            pp+=1
        elif(a=="d" or a=="All of the above"):
            pp-=1
        else:
            print("Please Enter valid option......")
            answer()
    answer()
def question2():
    print("\n\t\tQ.2)  Which of the following function gets a space-padded string with the original string\n\t\t           left-justified to a total of width columns? ")
    print("\n\t\t\tA.  isupper()")
    print("\t\t\tB.  join(seq)")
    print("\t\t\tC.  len(string)")
    print("\t\t\tD. ljust(width[, fillchar])")
    def answer():
        global pp
        a=input("\n\t\t\tEnter Your Choice : ").lower()
        if(a=='a' or a=='isupper()'):
            pp-=1
        elif(a=='b' or a=="join(seq)"):
            pp-=1
        elif(a=="c" or a=="len(string)"):
            pp-=1
        elif(a=="d" or a=="ljust(width[, fillchar])"):
            pp+=1
        else:
            print("Please Enter valid option......")
            answer()
    answer()
def question3():
    print("\n\t\tQ.3)  Which of the following data types is not supported in python?")
    print("\n\t\t\tA. Numbers")
    print("\t\t\tB. String")
    print("\t\t\tC. List")
    print("\t\t\tD. Slice")
    def answer():
        global pp
        a=input("\n\t\t\tEnter Your Choice : ").lower()
        if(a=='a' or a=='Numbers'):
            pp-=1
            print(pp)
        elif(a=='b' or a=="String"):
            pp-=1
        elif(a=="c" or a=="List"):
            pp-=1
        elif(a=="d" or a=="Slice"):
            pp+=1
        else:
            print("Please Enter valid option......")
            answer()
    answer()
def question4():
    print("\n\t\tQ.4)  Which Of The Following Keywords Mark The Beginning Of The Class Definition?")
    print("\n\t\t\tA. def")
    print("\t\t\tB. return")
    print("\t\t\tC. class")
    print("\t\t\tD. All of the above")
    def answer():
        global pp
        a=input("\n\t\t\tEnter Your Choice : ").lower()
        if(a=='a' or a=='def'):
            pp-=1
            print(pp)
        elif(a=='b' or a=="return"):
            pp-=1
        elif(a=="c" or a=="class"):
            pp+=1
        elif(a=="d" or a=="All of the above"):
            pp-=1
        else:
            print("Please Enter valid option......")
            answer()
    answer()
def question5():
    print("\n\t\tQ.5)  Which of the following function convert an object to a string in python?")
    print("\n\t\t\tA. int(x [,base])")
    print("\t\t\tB. str(x)")
    print("\t\t\tC. long(x [,base] )")
    print("\t\t\tD. float(x)")
    def answer():
        global pp
        a=input("\n\t\t\tEnter Your Choice : ").lower()
        if(a=='a' or a=='int(x [,base])'):
            pp-=1
            print(pp)
        elif(a=='b' or a=="str(x)"):
            pp+=1
        elif(a=="c" or a=="long(x [,base] )"):
            pp-=1
        elif(a=="d" or a=="float(x)"):
            pp-=1
        else:
            print("Please Enter valid option......")
            answer()
    answer()
def question():
    question1()
    sure1=input("\t\t\tAre You Sure to Continue this Quiz (Y/N) : ").lower()
    if(sure1=="y" or sure1=="yes"):
        question2()
        sure2=input("\t\t\tAre You Sure to Continue this Quiz (Y/N) : ").lower()
        if(sure2=="y" or sure2=="yes"):
            question3()
            sure3=input("\t\t\tAre You Sure to Continue this Quiz (Y/N) : ").lower()
            if(sure3=="y" or sure3=="yes"):
                question4()
                sure4=input("\t\t\tAre You Sure to Continue this Quiz (Y/N) : ").lower()
                if(sure4=="y" or sure4=="yes"):
                    question5()
                    print("\t\t\tYour Score is ",pp)
                    print("\n\t\t\tCorrect Answer is : - \n")
                    print("\t\t\tAnswer 1 :- C.) inheritance")
                    print("\t\t\tAnswer 2 :- D.) ljust(width[, fillchar])")
                    print("\t\t\tAnswer 3 :- D.) Slice")
                    print("\t\t\tAnswer 4 :- C.) class")
                    print("\t\t\tAnswer 5 :- B.) str(x)")
                    sure5=input("\t\t\tGo to main Menu (Y/N) : ").lower()
                    if(sure5=="y" or sure5=="yes"):
                        main()
                    else:
                        exit
                elif(sure4=="n" or sure4=="no"):
                    print("\t\t\tYour Score is ",pp)
                    print("\n\t\t\tCorrect Answer is : - \n")
                    print("\t\t\tAnswer 1 :- C.) inheritance")
                    print("\t\t\tAnswer 2 :- D.) ljust(width[, fillchar])")
                    print("\t\t\tAnswer 3 :- D.) Slice")
                    print("\t\t\tAnswer 4 :- C.) class")
                    main()
            elif(sure3=="n" or sure3=="no"):
                print("\t\t\tYour Score is ",pp)
                print("\n\t\t\tCorrect Answer is : - \n")
                print("\t\t\tAnswer 1 :- C.) inheritance")
                print("\t\t\tAnswer 2 :- D.) ljust(width[, fillchar])")
                print("\t\t\tAnswer 3 :- D.) Slice")
                main()
        elif(sure2=="n" or sure2=="no"):
            print("\t\t\tYour Score is ",pp)
            print("\n\t\t\tCorrect Answer is : - \n")
            print("\t\t\tAnswer 1 :- C.) inheritance")
            print("\t\t\tAnswer 2 :- D.) ljust(width[, fillchar])")
            main() 
    elif(sure1=="n" or sure1=="no"):
        print("\t\t\tYour Score is ",pp)
        print("\n\t\t\tCorrect Answer is : - \n")
        print("\t\t\tAnswer 1 :- C.) inheritance")
        main()
def start_quiz():
    a=input("\n\t\t\tAre You Sure to start this quiz (Y/N): ").lower()
    if(a=='y' or a=='yes'):
        question()
    else:
        main()
print("\n=====================================================================\n")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: WELCOME:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::  WELCOME ::::::::::::::::::::::::  WELCOME ::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: WELCOME:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
def main():
    print("\n=====================================================================\n")
    print("\t\t\t\t1.) Start Quiz")
    print("\t\t\t\t2.) Exit")
    print("\n=====================================================================\n")
    b=int(input("\n\t\t\t\tEnter Your Choice : " ))
    if(b==1):
        start_quiz()
    elif(b==2):
        exit
    else:
        exit
    print("\n=====================================================================\n")
main()
