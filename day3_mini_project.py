english = int(input("enter a number:"))
hindi = int(input("enter a number:"))
math = int(input("enter a number:"))
science = int(input("enter a number:"))
social = int(input("enter a number:"))

total = (english + hindi + math + science + social)
print("total marks:", total)
percentage = (total)/5
print("percentage:", percentage)
if percentage >= 35:
    print("pass")
else:
    print("fail")
    

