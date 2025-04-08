# 텍스트 파일을 불러옵니다.
# 문자간 공백을 지우는 함수 => strip
filename = 'corpus.txt'

def import_as_tuple(filename):
    tuples = []
    with open(filename) as file:
        for line in file:
            # 아래 코드를 작성하세요.
            line = line.strip()
            text, number = line.split(',')
            tuples.append((text,number))
    
    return tuples


# 아래 주석을 해제하고 결과를 확인해보세요.  
print(import_as_tuple(filename))
