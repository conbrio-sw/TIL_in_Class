def fx_a():
    print("나는 fx_a함수입니다. 숫자 100을 반환해요")
    return 100
def sum(a, b):
    print("숫자 2개를 더해줘요")
    return a + b
print(fx_a())
print(sum(100, fx_a()))