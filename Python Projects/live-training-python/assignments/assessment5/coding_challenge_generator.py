# 13. Generator banao jo `1` se `N` tak even numbers generate kare.

def even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i
            
even_gen = even_numbers(10)
print("Even numbers from 1 to 10:")
for even in even_gen:
    print(even) 
    
    