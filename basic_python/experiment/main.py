def sum_then_print(*numbers):
    print(numbers)
    
    total = 0
    for n in numbers:
        print("This is total: ", total)
        print("This is number: ", n)
        total = total + n
        print("Current total: ", total)
    return(total)


print(sum_then_print(2, 3, 4, 5, 4))
# output ➜ 18