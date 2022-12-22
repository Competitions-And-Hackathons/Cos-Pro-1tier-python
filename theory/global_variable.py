a = 10

def func():
    global a  #global 선언이 없으면 버그 뜬다.
    a = a+1
    print(a)

if __name__ == "__main__":
    func()


# 지역변수가 전역변수보다 우선시 된다.
# 실제 시험에서는 고려할 경우가 적기는 하다.