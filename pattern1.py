'''for row in range(7):
    for col in range(5):
        if((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
            print("* ",end=' ')
        else:
            print(end='')
    print()'''

for row in range(7):
    for col in range(5):
        if((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end='')
        else:
            print(end=' ')
    print()

# num = int(input("enter the number of row: "))
# for i in range(1,num+1):
#     for j in range(1,num-i+1):
#         print(end=' ')
#     for j in range(i,0,-1):
#         print(j,end='')
#     for j in range(2,i+1):
#         print(j,end='')
#     print()

# string = input("enter the string : ")
# length = len(string)
# for row in range(length):
#      for col in range(row+1):
#          print(string[col],end='')
#      print()

'''from html.parser import HTMLParser
a=HTMLParser().parse_comment("hudioyuthg")

print(a)'''