print("Enter your marks of below subjects : " )
c=int(input("C : " )) 
java=int(input("Java : " )) 
dbms=int(input("DBMS : " )) 
html=int(input("HTML : " )) 
react=int(input("React : " )) 

marks = c+java+dbms+html+react
percentage=marks/5.0 
if(c<35 or java<35 or dbms<35 or html<35 or react<35 ):
    print("Fail" )
else:
    if(percentage>90 and percentage<=100 ):
        print("Grade A" ) 
        print("Topper 🏆!!!")

    elif(percentage>70 and percentage<=90 ):
        print("Grade B" )

    elif(percentage>55 and percentage<=70 ):
        print("Grade C" ) 

    elif(percentage>=35 and percentage<=55 ):
        print("Grade D" ) 
        

