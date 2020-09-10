# Author: Christian Jones cpj5199@psu.edu
# Collaborator: Ivy Qi ijq5005@psu.edu
# Collaborator: Dongsheng Zhang dkz5086@psu.edu
# Section: 5
# Breakout: 14

def getLetterGrade(grade):
  if grade >= 93.0:
    print("Your letter grade for CMPSC 131 is A.")
  elif  grade >= 90.0:
    print("Your letter grade for CMPSC 131 is A-.")
  elif grade >= 87.0:
    print("Your letter grade for CMPSC 131 is B+.")
  elif grade >= 83.0:
    print("Your letter grade for CMPSC 131 is B.")
  elif grade >= 80.0:
    print("Your letter grade for CMPSC 131 is B-.")
  elif grade >= 77.0:
    print("Your letter grade for CMPSC 131 is C+.")
  elif grade >= 73.0:
    print("Your letter grade for CMPSC 131 is C.")
  elif grade >= 70.0:
    print("Your letter grade for CMPSC 131 is C-.")
  elif grade >= 60.0:
    print("Your letter grade for CMPSC 131 is D.")
  elif grade < 60.0:
    print("Your letter grade for CMPSC 131 is F.")

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  getLetterGrade(grade)

if __name__ == "__main__":
  run()
