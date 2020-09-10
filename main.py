# Author: Christian Jones cpj5199@psu.edu
# Collaborator: Ivy Qi ijq5005@psu.edu
# Collaborator: Dongsheng Zhang dkz5086@psu.edu
# Section: 5
# Breakout: 14

def getLetterGrade(grade):
  if grade >= 93:
    letter = "A"
    print("Your letter grade for CMPSC 131 is " + letter + ".")
  elif  grade >= 90:
    letter = "A-"
    print("Your letter grade for CMPSC 131 is " + letter + ".")
  elif grade >= 87:
    letter = "B+"
    print("Your letter grade for CMPSC 131 is " + letter + ".")
  elif grade >= 83:
    letter = "B"
    print("Your letter grade for CMPSC 131 is " + letter + ".")
  elif grade >= 80:
    letter = "B-"
    print("Your letter grade for CMPSC 131 is " + letter + ".")
  elif grade >= 77:
    letter = "C+"
    print("Your letter grade for CMPSC 131 is " + letter + ".")
  elif grade >= 73:
    letter = "C"
    print("Your letter grade for CMPSC 131 is " + letter + ".")
  elif grade >= 70:
    letter = "C-"
    print("Your letter grade for CMPSC 131 is " + letter + ".")
  elif grade >= 60:
    letter = "D"
    print("Your letter grade for CMPSC 131 is " + letter + ".")
  elif grade < 60:
    letter = "F"
    print("Your letter grade for CMPSC 131 is " + letter + ".")


def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  getLetterGrade(grade)

if __name__ == "__main__":
  run()
