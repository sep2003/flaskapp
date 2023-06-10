list1=["redcolour","orange#","green","orange@","white"]
char_list=["colour","#","@"]
output_list=[]
for ele in list1:
    for char in char_list:
        if char in ele:
            flag=True
            output_list.append(ele.replace(char,""))
            flag=False
            output_list.append(ele)
            print(output_list)

            
    
    
    ###
    
# question2:

r=int(input("enter a value of radius :"))   
print("area of circle is :",3.14*r*r)

##

#question3:
     
            
for math import floor

num_1=int(input("enter a value number :"))
num_2=int(input("enter a value of next number :"))
qotient=floor(num_1/num_2)
remainder=num_1%num_2
print("qotient:",str(qotient))
print("remainder:",str(remainder))


##
#question4:
n=int(input("enter a value n :"))
sum=(n((n+1)/2))
print("sum of first positive integer,sum")
###
#question5:
temp_1=int(input("enter a temprature*c :"))
temperature=temp_1*9/5+32
print("temperature in fahrenheit :"+str(temperature)+"F")

##
#question6:

dic1={1:10,
      2:20
      }
dic2={3:30,
      4:40
      }
dic3={5:50,
      6:60
      }
dic4={}
for k,v in dic1.item():
    dic4[k]=v
for k,v in dic2.item():
    dic4[k]=v   
for k,v in dic3.item():
    dic4[k]=v         








