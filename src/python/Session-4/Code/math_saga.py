def factorial(num: int):
    '''
    calculate n! using recursion

    parameters
    ----------
    num : int

    returns
    -------
    int    
    '''
    if num < 0:
        raise ValueError("factorial is undefined for negative numbers")
    if num ==0 or num == 1:
        return 1
    return num *factorial(num -1)



def is_prime(num : int) -> bool:
    '''
    Check wether a number is prime

    parameters
    ----------
    num : int
    number to test 

    returns
    -------
    bool 
    True if Prime , otherwise False.
    
    
    '''
    if num < 2:
        return False
    for i in range(2,num):
        if num % i ==0:
            return False
    return True        


def common_divisors(num_1:int, num_2: int ) ->  list[int]:
    limit = min(num_1,num_2)
    divisors = []

    for divisor in range (1, limit+1):
        if num_1 % divisor == 0 and num_2 % divisor == 0 :
             divisors.append(divisor)
    return divisors            