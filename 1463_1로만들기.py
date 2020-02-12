input("소수를 구할 수를 입력하세요 : ")

def isPrime():
    num = input("소수를 구할 수를 입력하세요 : ")

    for i in num:
        if num/i == 0:
            isPrime() = False
            print(str(num) + "은 소수입니다.")
            break
        else:
            print(str(num) + "은 소수가 아닙니다.")
            return 0