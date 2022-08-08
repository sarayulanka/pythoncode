def recursive_fibo(num):
    if num <= 1:
        return num
    else:
        return recursive_fibo(num-1) + recursive_fibo(num-2)



