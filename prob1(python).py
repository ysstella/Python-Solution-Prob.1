def f(n):
    import matplotlib.pyplot as plt
    import numpy as np
    
    f = np.copy(n)
    f[f < 10] = f[f < 10]**2 - 7
    for x in range(10, n.size):
        f[x] = f[x - 10]
       
    plt.figure(figsize=(10,7))    
    plt.suptitle('Function f(n)')
    plt.xlabel('n from 0 to 99')
    plt.ylabel('f(n)')
    plt.stem(n,f, linefmt='--', markerfmt='C0o', basefmt= 'C2-')
    plt.show
    print(f)
    return

