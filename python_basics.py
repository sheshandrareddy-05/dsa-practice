#variables
name="sheshandra"
age=20
cgpa=7.5
is_student=True

#list
skills=["python","dsa","machine learning"]
print(skills[0]) #prints python

#for loop
for skill in skills:
    print("learning:",skill)

    #while loop
    count=1
    while count<=5:
      print("day",count) 
      count+=1

      # if else
      if cgpa>=7.5:
        print("good cgpa!")
    else:
        print("need to improve")
      
      #string formatting 
        print(f"mt name is {name} and i am {age} years old")

      #basic math
        x=10
        y=3
        print(x+y) #addition
        print(x*y) #multiply
        print(x/y) #division
        print(x%y) #remainder