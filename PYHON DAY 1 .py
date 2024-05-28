#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PYTHON DAY 1 PRACTISE


# In[1]:


#print number of characters for given string
user_name=input("")
print(len(user_name))


# In[3]:


#Instructions
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Write your code below this line 👇
two_digit_number = input()
num1=int(two_digit_number[0])
num2=int(two_digit_number[1])
print(num1+num2)


# In[4]:


#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
height = input()
weight = input()
weight1=float(weight)
height1=float(height)
multi=height1*height1
BMI=int(weight1/multi)
print(BMI)


# In[5]:


age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

years=90-int(age)
weeks=years*52
print(f"You have {weeks} weeks left.")


# In[6]:


# Even or odd
number = int(input())
if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# In[7]:


# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI=float(weight/height**2)
if BMI<18.5:
  print(f"Your BMI is {BMI} , you are underweight.")
elif BMI>=18.5 and BMI<25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI>25 and BMI<30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI>30 and BMI<35:
  print(f"Your BMI is {BMI}, you are obese.")
elif BMI>35:
  print(f"Your BMI is {BMI}, you are clinically obese.")
  
  
  


# In[9]:


#Leap Year
year = int(input())
if year%4==0:
  if year%100==0:
    if year%400==0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")


# In[ ]:




