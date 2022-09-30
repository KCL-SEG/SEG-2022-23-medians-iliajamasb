"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def findMedian(numberList):
    numberList.sort()
    length = len(numberList)
    
    if length%2!=0:
        ++length
        length/=2
        --length
        return(numberList[int(length)])
    
    else:
        length/=2
        return((numberList[int(length-1)]+numberList[int(length)])/2)
        
        
    
    


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        print(findMedian(numbers))
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
