def cel_fer():
    celsius=int(input("Enter the temperature in celsius that you have to convert into Fahernhiet:\n"))
    fher=(celsius*(9/5))+32
    print(f"The temperature {celsius} degree celsius in Fahernhiet is {fher}.")
def cm_inch(): 
    cm=int(input("Enter the centimeter you have to conert into inches:\n"))
    inch=cm/2.54
    print(f"The centimeter {cm}cm in inches is {inch}")
def kg_pound():
    kg=int(input("Enter the kg you have to convert into pounds:\n"))
    pound=kg*2.2046
    print(f"The kg {kg} in pounds is {pound}. ")
def main():
    while True:
         print("======WELCOME TO THE MEASUREMENT CONVERTER======\n")
         print("Please enter the suitable option;\n")
         print("1.celsius to Fhernhiet")
         print("2.centimeter to inches")
         print("3.KG to pounds")
         print("4.Exit")
         choice=input("ENTER THE VALID OPTION:")
         if choice=="1":
             cel_fer()
         elif choice=="2":
             cm_inch()
         elif choice=="3":
             kg_pound()
             
         elif choice=="4":
             print("Exiting the program.........")
             break
         else:
             print("-------THE OPTION IS INCORRECT (PLEASE ENTER THE VALID OPTION)------")
             
if __name__=="__main__":
    main()


