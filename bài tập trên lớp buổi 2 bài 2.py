def fibonacci(n):
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
 
print("dãy số fibonacci có giá trị nhỏ thua 1000: ");
sb = "";
for i in range(0, 17):
    sb = sb + str(fibonacci(i)) + ", ";
print(sb)      

