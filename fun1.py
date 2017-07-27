#c=0
#for num in range(1,101):
  #  print(num)
 #   c=c+num
#print(c)


start=int(input('what is the first number'))
end=int(input('what is the last number'))
def add_numbers(start,end):
    c=0
    for number in range (start,end):
         #print(number)
         c=c+number
    return c
answer=add_numbers(start,end)
print(answer)




