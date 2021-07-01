
def main():
    
    try:
        num = int(input("Enter your Line Number : "))
    except ValueError:
        print("Please enter only number")
        main()

    init = 1
    time = init

    try:
        for i in range(1,num+1):
            tmp = init
            for j in range(i):
                print(tmp,end='     ')
                tmp += 2

            print()
            time += 2
            init += time
    except UnboundLocalError:
        print("Re-enter")
        main()

main()