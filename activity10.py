#comments
#jeepney fare
#if user is a student, then user discount must be applied
#getting a 20% discount if student, if not, no discount

name = input("Input your name ---> ")
aStudent = input("Are you a student? (Yes / No) ")
fare = eval(input("your pay --> "))

if aStudent.lower() == "yes":
       discount = fare * .2
       new_fare = fare - discount
       print("Hi", name, "your student discount is ", discount, " Discounted fare is ", new_fare)
else: 
       print("Sorry ", name, "you are not eligible for student discount") 