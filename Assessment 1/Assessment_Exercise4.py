import sys

question_1=input("1. What is the capital of France? ").lower() 
if question_1!="paris": 
    print("\nIncorrect, the capital of France is Paris.\n") 
else:   
    print ("\nCorrect! Next Question.\n") 

question_2=input("2. What is the capital of Germany? ").lower()
if question_2!="berlin":
    print("\nIncorrect, the capital of Germany is Berlin.\n")
else:
    print ("\nCorrect! Next Question.\n")

question_3=input("3. What is the capital of Croatia? ").lower()
if question_3!="zagreb":
    print("\nIncorrect, the capital of Croatia is Zagreb.\n")
else:
    print ("\nCorrect! Next Question.\n")

question_4=input("4. What is the capital of Spain? ").lower()
if question_4!="madrid":
    print("\nIncorrect, the capital of Spain is Madrid.!\n")
else:
    print ("\nCorrect! Next Question.\n")

question_5=input("5. What is the capital of Hungary? ").lower()
if question_5!="budapest":
    print("\nIncorrect, the capital of Hungary is Budapest.\n")
else:
    print ("\nCorrect! Next Question.\n")

question_6=input("6. What is the capital of Belgium? ").lower()
if question_6!="brussels":
    print("\nIncorrect, the capital of Belgium is Brussels.\n")
else:
    print ("\nCorrect! Next Question.\n")

question_7=input("7. What is the capital of Ireland? ").lower()
if question_7!="dublin":
    print("\nIncorrect, the capital of Ireland is Dublin.\n")
else:
    print ("\nCorrect! Next Question.\n")

question_8=input("8. What is the capital of Austira? ").lower()
if question_8!="vienna":
    print("\nIncorrect, the capital of Austira is Vienna.\n")
else:
    print ("\nCorrect! Next Question.\n")

question_9=input("9. What is the capital of Latvia? ").lower()
if question_9!="riga":
    print("\nIncorrect, the capital of Latvia is Riga.\n")
else:
    print ("\nCorrect! Next Question.\n")

question_10=input("10. What is the capital of Switzerland? ").lower()
if question_10!="bern":
    print("\nIncorrect, the capital of Switzerland is Bern. That ends the quiz, Thank you.\n")
else:
    print ("\nThank you for complething the quiz!\n")
    sys.exit()