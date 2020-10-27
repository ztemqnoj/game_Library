'''
This program allows users to ipnut their games into a library
that tracks Name, Platform, Completed status, Rating (1-10)
'''
import csv

def getTitle():
# Title of the game
    title = str(input("What is the title of the game? "))

    return(title)

def getPlatform():
# PS, Xbox, Switch
    platform = str(input("What platform are you playing on? "))

    return(platform)

def getProgress():
# Backlog, Started, Finished
    while True:
        try:
            progress = str(input("How far have you gotten into the game? "))
            if progress.isalpha():
                break
            else:
                print("Progress must be a string. ")
        except TypeError:
            print("Progress must be a string. ")

    return(progress)

def getRating():
# Numerical value 1-10
    while True:
        try:
            rating = int(input("What would you rate this game? (1-10) "))
            if 1 <= rating <= 10:
                break
            else:
                print("The rating must be a numerical value up to 10: ")
        except ValueError:
            print("The rating must be a numerical value up to 10: ")
        
    return(rating)

def addGame():
# Use existing functions to add a new game to your library.
    
    #Open csv
    outfile = open('gameList.csv', 'a', newline='')
    w = csv.writer(outfile)

    while True:
        title = getTitle()
        platform = getPlatform()
        progress = getProgress()
        rating = getRating()

        print(title, platform, progress, rating)

        addAnother = input("Add this game to the Game List? Y/N: ")
        while True:
            if addAnother.lower() == "y":
                w.writerow([title, platform, progress, rating])
                print("Game list has been updated.")
                break
            elif addAnother.lower() == "n":
                break
                outfile.close()
                exit()
            else:
                print("Invalid entry. Try again.")
                break
        break

    return()

                      
addGame()
