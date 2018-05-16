def str_analysis(value):
    if(value.isdigit()):
        if(int(value) < 90):
            print(value, " is a smaller number than expected")
        else:
            if(int(value)>90):
               print(value, " is pretty big number")
    else:
        if(value.isalpha()):
            print(value,"is all alphabetical characters!")
        else:
             print(value,"is neither all alpha nor all digit")
    
        
       
       
                
            
           
message = "" 
while(message  == "" ):
    message = input("Enter the value here: ")
    if(message != ""):
        str_analysis(message)
