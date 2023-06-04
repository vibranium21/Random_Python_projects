#Import the math module
import math

# Tell the computer how to pythogorean thereom
def hypotenuse(legA, legB):
  hypotenuse_squared = legA**2+legB**2
  return(math.sqrt(hypotenuse_squared))
def leg(legB, hypotenuse):
  leg_squared = hypotenuse**2 - legB**2
  return(math.sqrt(leg_squared))

#Ask for the details of the equation
side = input("Would you like to calculate the length of the hypotenuse, or a leg? Reply With 'leg' or 'hypotenuse')
if side.lower == leg: 
  try:            
    length_other_leg = float(input('What is the length of the other leg?')
    hypotenuse_length = float(input('What is the length of the hypotenuse?')
  except ValueError:
    print("Please answer with a number")
  print(hypotenuse(length_other_leg , hypotenuse_length))
            
                           
if side.lower == hypotenuse:
  try:            
    length_other_leg = float(input('What is the length of the first leg?')
    length_leg = float(input('What is the length of the other leg?')
  except ValueError:
    print("Please answer with a number")
  print(leg(length_leg , length_leg))
