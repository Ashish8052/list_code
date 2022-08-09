
question_list = ["1.How many continents are there?","2.What is the capital of India?","3.NG mei kaun se course padhaya jaata hai?"]
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
ans=[3,4,1]
_5050=[["1.Four","2.seven"],["1.bhopal","2.Delhi"],["1.Software Engineering","2.Counsiing"]]
_ans=[2,2,1]
a=0
Rs=0
count=1
while a<len(question_list):
    print(question_list[a])
    c=0
    while c<len(options_list[a]):
        print(options_list[a][c])
        c=c+1
    if count<=1:
        life_line=input("are you needed life line")
        if "yes"==life_line or "YES"==life_line or "Yes"==life_line:
            d=0
            while d<len(_5050[a]):
                print(_5050[a][d])
                d=d+1
            _ans1=int(input("enter the answer"))
            if _ans[a]==_ans1:
                Rs=Rs+2000
                count=count+1
                print("answer is correct")
                print("your wining amount is",Rs)


            else:
                print("answer is not correct") 
                break
        else:
            print("now,i don't needed any life line")
            ans1=int(input("enter the answer"))
            if ans[a] == ans1:
                Rs=Rs+2000
                print("answer is correct")
                print("your wining amount is",Rs)
            else:
                print("ans is incorrect")
                break
    else:
        ans1=int(input("enter the answer"))
        if ans[a] == ans1:
            Rs=Rs+2000
            print("answer is correct")
            print("your wining amount is",Rs)            
        else:
            print("ans is incorrect")
            break
    a=a+1
print("your total wining amount is",Rs)
