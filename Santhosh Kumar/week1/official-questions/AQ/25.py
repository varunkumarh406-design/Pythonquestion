# Accept a positive integer as input and print True if it is a perfect 
# square and False otherwise. For example, if the input is 25 ,
# then you must print True . If the input is 15 , then you must print False


n=int(input()) #81
root=int(n**0.5) #81*0.5*0.5 = 9
print(root*root==n) #81==81

#4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900,961


#solution
#4 True
#9 True
#16 True
#25 True
#36 True
#49 True
#64 True
#81 True
#100 True
#121 True
#144 True
#169 True 
#196 True
#225 True
#256 True   
#289 True
#324 True
#364 True
#400 True
#441 True
#484 True
#529 True
#576 True
#625 True
#676 True
#729 True
#784True