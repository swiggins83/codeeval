import sys

def main():
    mult()

def mult():
    """Print out multiplication tables in a grid-like fashion."""

    nums = [1,2,3,4,5,6,7,8,9,10,11,12]

    for i in range(1,13):        
        for num in nums:
            whitespace = ' '
            whitespace *= (4-len(str(num*i)))

                    
            sys.stdout.write(str(num*i) + whitespace)
        print
    

if __name__ == "__main__":
    main()
