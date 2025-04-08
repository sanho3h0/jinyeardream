# 텍스트 파일을 불러옵니다.
filename = 'corpus.txt'

def print_lines(filename):
    # 아래 코드를 작성하세요.
    with open(filename) as file:
        line_number = 1
        for l in file:
            # 1 This is Elice. 와 같이, "(줄번호) (내용)" 형식으로 출력합니다.
            print(f"{line_number} {l}")
            # print(str(line_number),l)
            # print(str(line_number)+' '+l) 와 같음
            line_number += 1
# 아래 주석을 해제하고 결과를 확인해보세요.  
print_lines(filename)