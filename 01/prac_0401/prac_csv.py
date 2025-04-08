# csv 모듈을 임포트합니다. 
import csv

def print_book_info(filename):
    with open(filename) as file:
        # ',' 기호로 분리된 CSV 파일을 처리하세요..
        reader = csv.reader(file)
        
        # 처리된 파일의 각 줄을 불러옵니다.
        for row in reader:
            
            # 함수를 완성하세요.
            title = row[0]
            author = row[1]
            pages = row[3]
            print("{} ({}): {}p".format(title, author, pages))


# 아래 주석을 해제하고 실행 결과를 확인해보세요.
filename = 'prac_0401/books.csv' 
# 파일 디렉토리의 경로를 설정해야함
print_book_info(filename)