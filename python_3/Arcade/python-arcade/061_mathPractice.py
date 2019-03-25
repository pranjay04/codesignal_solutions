def mathPractice(numbers):
    return functools.reduce(lambda i, x : (i+x[0]) if x[1]%2 !=0 else (i*x[0]), zip(numbers[1:], range(1,len(numbers))), numbers[0])
