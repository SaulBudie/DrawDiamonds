num = eval(input("Number pls?: \n"))
#expand first
for seggs in range(num):
    print(" " * (num - seggs), "*" * (2*seggs + 1))
#reduce in the bottom
for seggs in range(num - 2, -1, -1):
    print(" " * (num - seggs), "*" * (2*seggs + 1))