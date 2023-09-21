fruit_basket=[]
unique_fruit=[]
repeat_fruit=[]
for i in range(5):
  fruits=input('Enter your fruits:')
  fruit_basket.append(fruits)
for fruits in fruit_basket:
    if fruits not in unique_fruit:
      unique_fruit.append(fruits)
    else:
         if fruits not in repeat_fruit:
             repeat_fruit.append(fruits) 
print('Unique fruit:',unique_fruit)
print('Repeat fruit:',repeat_fruit)