# Fibonacci using a loop

totalNums = []
totalTerms = 10000

prev1 = 0
prev2 = 1

for fibonacci in range(totalTerms):
    newFibonacci = prev1 + prev2
    prev2 = prev1
    prev1 = newFibonacci
    totalNums.append(newFibonacci)
    

# Fibonacci using recursion

totalNums = []
termsUsed = 2
totalTerms = 16 # 15, 0 based indexing

def fibonacci(prev1, prev2):
    global totalTerms
    global termsUsed

    if totalTerms >= termsUsed:
        newFibonacci = prev1 + prev2
        prev2 = prev1
        prev1 = newFibonacci
        totalNums.append(newFibonacci)

        termsUsed += 1
        fibonacci(prev1, prev2)
    else:
        print(totalNums)
    

fibonacci(0, 1)

# Finding nth fibonacci based on the formula F(n) = F(n - 1) + F(n - 2) and recursion

def certainFibonacci(number):
    if number <= 1:
        return number   
    else:
        return certainFibonacci(number - 1) + certainFibonacci(number - 2)

print(certainFibonacci(15))