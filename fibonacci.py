def main():
    num = eval(input("Program to find the fibonacci number we want. \n What number you need"))
    total = round (num/2)
    x,y = 1,1
    fi = list ([1,1])
    for i in range(total):
        x = x + y
        fi. append(x)
        print(fi[num-1])
main()