def hanoi(N, frompole, subpole, topole):
    if N == 1:
        print(frompole, topole)
        return
    hanoi(N-1, frompole, topole, subpole)
    print(frompole, topole)
    hanoi(N-1, subpole, frompole, topole)
    
N = int(input())
print(2**N-1)
hanoi(N, 1, 2, 3)