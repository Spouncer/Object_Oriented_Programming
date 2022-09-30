def fibonacci(n):
    
    if n > 3:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
    else:
        return 1
   
for a in range(1,11):
    print(fibonacci(a))