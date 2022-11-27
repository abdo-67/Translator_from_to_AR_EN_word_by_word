import time    # you can don't use this, just i like it
print("Weclome in your translator")

print("Important Alert: this translator is very rudimentary\nword by word")

print("thank you")

print("\n")

transAr = {
    "اليوم":"today",
    "المدرسة" :"school",
    "بعد الظهر" :"afternoon",
    "الفصل":"class",
    "اتوبيس":"bus",
    "النادى":"club"

}



transEn = {
    "today":"اليوم",
     "school":"المدرسة",
     "afternoon":"بعد الظهر",
     "class":"الفصل",
     "bus":"اتوبيس",
     "club":"النادى"
}



doExit ="##"
while True:


    choice = input("ar to en press 1 \n en to ar press 2 \n").strip()


    if choice != "1" and choice!= "2":
        print("Error\nPlease Enter 1 , 2 ""\n")

    elif choice == "1":
        while True:

             wordsAr = input("ادخل الكلمة ").strip()
             if wordsAr == "##":
                 break
             else:
                 try:
                     print(f"{wordsAr}:{transAr.__getitem__(str(wordsAr))}")
                 except:
                     print("هذه الكلمة غير متوفرة")
             print("\n")
             print("اذ اردت الرجوع ادخل ##")
             print("\n")


    else:
        while True:
            wordsEn = input("Enter the word ").strip().lower()
            if wordsEn == "##":
                break
            else:

                try:
                    print(f"{wordsEn}:{transEn.__getitem__(str(wordsEn))}")
                except:
                    print("this word is not valid")
            print("\n")
            print("if you want back press ##")
            print("\n")
