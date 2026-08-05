def add (x:  float , y: float ):
   '''sum function
        args:
        param_1= user must input the first num
        type_param1=float 
        param_2= user must input the Second num
        type_param2=float 
        return: this function return the sum of two num
        type_return = float
   
   '''

   return x+y 


def sub (x:  float , y: float ):
   '''sub function
        args:
        param_1= user must input the first num
        type_param1=float 
        param_2= user must input the Second num
        type_param2=float 
        return: this function return the sub of two num
        type_return = float
   
   '''

   return x-y 


def div (x:  float , y: float ):
   '''div function
        args:
        param_1= user must input the first num
        type_param1=float 
        param_2= user must input the Second num
        type_param2=float 
        return: this function return the div of two num
        type_return = float
   
   '''

   return x/y 


def multiply (x:  float , y: float ):
   '''multiply function
        args:
        param_1= user must input the first num
        type_param1=float 
        param_2= user must input the Second num
        type_param2=float 
        return: this function return the multiply of two num
        type_return = float
   
   '''

   return x*y


def main():
   print("calc app")
   print("==================")

   print("1 add")
   print("2 sub")
   print("3 div")
   print("4 multi")
   choice = input("enter choice 1 - 2 - 3 - 4 ")
   num_1= float (input("enter first num"))
   num_2= float (input("enter second num"))

   if choice =='1':
      print (f"first num {num_1} , second num {num_2} " , add(num_1 ,num_2))
   elif choice=='2'  :
      print (f"first num {num_1} , second num {num_2} " , sub(num_1 ,num_2)) 
   elif choice =='3' :
      print( f"first num {num_1} , second num {num_2} " , div (num_1 ,num_2)  )
   elif choice=='4' :
      print( f"first num {num_1} , second num {num_2} " , multiply (num_1 ,num_2)  )