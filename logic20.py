def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    number0=0
    number1=0

    x1=n%10
    number0+=x1==0
    number1+=x1==1
    n//=10

    x2=n%10
    number0+=x2==0 and n !=0
    number1+=x2==1
    n//=10

    x3=n%10
    number0+=x3==0 and n !=0
    number1+=x3==1
    n//=10

    x4=n%10
    number0+=x4==0 and n !=0
    number1+=x4==1
    n//=10

    return number1>number0

print(main(1111))

