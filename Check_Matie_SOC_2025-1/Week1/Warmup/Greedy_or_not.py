from collections import deque
n = int(input())
ll = list(map(int, input().split()))
s1 = sum(ll[::2])
s2 = sum(ll[1::2])
l = deque(ll)
score1 = 0
score2 = 0
chance = 1
if n%2 == 1:
    state = [[1,1],[0,0]]
else:
    state = [[1,0],[0,1]]
while n>0:
    e = False
    if n%2 == 0:
        if chance == 1:
            if s1+score1>s2+score2:
                e = True
                if state[0][0] == 1:
                    c = l.popleft()
                    s1-=c
                    state[0][0] = 0
                    state[1][0] = 1
                else:
                    c = l.pop()
                    s1-=c
                    state[0][1] = 0
                    state[1][1] = 1
                score1 += c
            elif s2+score1>s1+score2:
                e = True
                if state[1][0] == 1:
                    c = l.popleft()
                    s2-=c
                    state[1][0] = 0
                    state[0][0] = 1
                else:
                    c = l.pop()
                    s2-=c
                    state[1][1] = 0
                    state[0][1] = 1
                score1 += c
        else:
            if s1+score2>s2+score1:
                e = True
                if state[0][0] == 1:
                    c = l.popleft()
                    s1-=c
                    state[0][0] = 0
                    state[1][0] = 1
                else:
                    c = l.pop()
                    s1-=c
                    state[0][1] = 0
                    state[1][1] = 1
                score2 += c
            elif s2+score2>s1+score1:
                e = True
                if state[1][0] == 1:
                    c = l.popleft()
                    s2-=c
                    state[1][0] = 0
                    state[0][0] = 1
                else:
                    c = l.pop()
                    s2-=c
                    state[1][1] = 0
                    state[0][1] = 1
                score2 += c
    if not e:
        if l[0]>l[-1]:
            c=l.popleft()
            if state[0][0] == 1:
                s1-=c
                state[0][0] = 0
                state[1][0] = 1
            else:
                s2-=c
                state[0][0] = 1
                state[1][0] = 0
        else:
            c=l.pop()
            if state[0][1] == 1:
                s1-=c
                state[0][1] = 0
                state[1][1] = 1
            else:
                s2-=c
                state[0][1] = 1
                state[1][1] = 0
        if chance == 1:
            score1 += c
        else:
            score2 += c
    chance = 3-chance
    n-=1
if score1>score2:
    print("Player 1 wins")
elif score2>score1:
    print("Player 2 wins")
else:
    print("Its a draw")
