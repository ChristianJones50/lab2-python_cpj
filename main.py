# Author: Christian Jones cpj5199@psu.edu
# Collaborator: Ivy Qi ijq5005@psu.edu
# Collaborator: Dongsheng Zhang dkz5086@psu.edu
# Section: 5
# Breakout: 14

def getLetterGrade(grade):
  if grade >= 93.0:
    gradePoint = "A"
  elif  grade >= 90.0:
    gradePoint = "A-"
  elif grade >= 87.0:
    gradePoint = "B+"
  elif grade >= 83.0:
    gradePoint = "B"
  elif grade >= 80.0:
    gradePoint = "B-"
  elif grade >= 77.0:
    gradePoint = "C+"
  elif grade >= 70.0:
    gradePoint = "C"
  elif grade >= 60.0:
    gradePoint = "D"
  elif grade < 60.0:
    gradePoint = "F"
  return gradePoint

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(grade)}.")

if __name__ == "__main__":
  run()

