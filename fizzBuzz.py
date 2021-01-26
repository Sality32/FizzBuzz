def fizzBuzz( n: int):
    lst = []
    i=1
    for x in range (n):
        if i % 15 == 0:
            lst.append("FizzBuzz")
        elif i % 3 == 0 :
            lst.append("Fizz")
        elif i % 5 == 0:
            lst.append("Buzz")
        else :
            lst.append(str(i))
        i+=1
    
    return lst


rsl = fizzBuzz(15)
print(rsl)