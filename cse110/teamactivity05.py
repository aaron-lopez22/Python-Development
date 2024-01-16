grade = float(input("What is you grade percentage? "))


if grade >= 90:
   letter = "A"
elif grade >= 80:
   letter = "B"
elif grade >= 70:
   letter = "C"
elif grade >= 60:
   letter = "D"
else:
    letter = "F"
sign = ""
grade2 = grade % 10
if grade2 >= 7:
  sign = "+"
elif grade2 < 3:
    sign = "-"
else:
    sign = ""
    
print(f"Your letter grade is: {sign} {letter}")

if grade >= 70:
    print("Congratulations you passed the class!")
else:
    print("Sorry you did not pass. We know you will be able to pass next time.")


   