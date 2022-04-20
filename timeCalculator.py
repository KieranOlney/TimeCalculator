def getTask(): #Get the initial user input for what task the user wishes to perform
    print("Please Select from the Following Options what you would like to do:\n1 - Add two times (in seconds) together\n2 - Subtract two times (in seconds) from each other\n3 - Convert a time from Seconds to Days, Hours & Minutes\n4 - Convert a time from Days, Hours & Minutes to Seconds\n5 - Exit the Program")
    userInput = input("Please Enter the number corresponding to your desired option: ")
    return userInput

def addTimes(): #Simple addition function, Outputs in Seconds
    firstSecs = input("Please enter the first number of seconds: ")
    secondSecs = input("Please enter the number of seconds you wish to add to "+firstSecs+": ")
    result = int(firstSecs) + int(secondSecs)
    print(firstSecs," + ",secondSecs," = ",result,"\n\n\n")
    return

def subtractTimes(): #Simple Subtraction Function, Outputs in Seconds
    firstSecs = input("Please enter the first number of seconds: ")
    secondSecs = input("Please enter the number of seconds you wish to subtract from "+firstSecs+": ")
    result = int(firstSecs) - int(secondSecs)
    print(firstSecs," - ",secondSecs," = ",result,"\n\n\n")
    return

def convertFromSecs(): #Conversion from Seconds, returns Int values for Days, Hours, Mins and Seconds to prevent long float values
    seconds = int(input("Please enter the number of seconds that you wish to convert: "))
    minutes = int(seconds/60)
    remSecs = int(seconds%60)
    hours = int(minutes/60)
    remMins = int(minutes%60)
    days = int(hours/24)
    remHours = int(hours%24)
    print(seconds," Seconds is equal to ",days,"Days, ",remHours,"Hours, ",remMins,"Minutes & ",remSecs,"Seconds.\n\n\n")

def convertToSecs(): #Conversion to Seconds from a human readable time format to Seconds
    print("Please enter the times you wish to convert to seconds")
    days = int(input("Days: "))
    hours = int(input("Hours: "))
    mins = int(input("Minutes: "))
    secs = int(input("Seconds: "))
    calc = days*24 
    calc = calc+hours
    calc = calc*60
    calc = calc+mins
    calc = calc*60
    calc = calc+secs
    print(days,"Days, ",hours,"Hours, ",mins,"Minutes & ",secs,"Seconds is equal to ",calc," Seconds.\n\n\n")
    return

def main(): #Main function to allow for selection of tasks and continuous use without restarting program
    end = False 
    print("Hello, Welcome to Kieran O's Time Calculator & Converter.\n\n")
    while end==False:
        task = getTask()
        if task == "1":
            addTimes()
        elif task == "2":
            subtractTimes()
        elif task == "3":
            convertFromSecs()
        elif task == "4":
            convertToSecs()
        elif task == "5": 
            break
        else:
            print("Sorry i didn't understand that input, please input again. Your input should be a single number. For example '3'.\n\n")
    
    print("\nThank you for using Kieran O's Time Calculator & Converter :)")
    return

main()