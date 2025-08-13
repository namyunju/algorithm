pattern = 'ababbab'
# table [0,0,0,0,0,0,0]
table = [0 for _ in range(len(pattern))]
# i, j 는 pattern 의 인덱스
# pattern 문자열 내 반복되는 부분
# i 두고 j 1씩 키우며 문자열의 첫 문자와 같아지는 인덱스 찾음
# 찾으면 i 1 키워서 다음 인덱스도 같은지 비교
# table의 j(처음 같아진 지점)인덱스에 i(같은 부분의 인덱스)를 할당
i = 0
for j in range(1, len(pattern)):
    while i > 0 and pattern[i] != pattern[j]:
        i = table[i-1]

    if pattern[i] == pattern[j]:
        i += 1
        table[j] = i
# i = 0, j = 1 이면 i = 0
# i = 0, j = 2 이면 같다. >> i = 1, table[2] = 1
# [0,0,1,0,0,0,0]: 2번 인덱스에서 첫 번째 문자와 같음
# i = 1, j = 3 . while 문 해당 안됨 i = 2, table[3] = 2
# [0,0,1,2,0,0,0]: 3번 인덱스에서 두 번째 문자와 같음
# i = 2, j = 4 while 때문에 i= table[i-1]로 i = 0이 됨.


print(table)
