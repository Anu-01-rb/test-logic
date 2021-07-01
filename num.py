
def main():
    try:
        num = int(input("Enter your Line Number : "))
        init = 1
        time = init

        for i in range(1,num+1):
            tmp = init
            for j in range(i):
                print(tmp,end=' ')
                tmp += 2

            print()
            time += 2
            init += time
    except ValueError:
        print('ERROR: You not input number!')

    

main()