# CSV, JSON 모듈을 임포트합니다.
import csv
import json
# from elice_utils import EliceUtils

# elice_utils = EliceUtils()

def books_to_json(src_file, dst_file):
    # 아래 함수를 완성하세요.
    books = []
    with open(src_file) as src:
        reader = csv.reader(src)
        
        # 각 줄 별로 대응되는 book 딕셔너리를 만듭니다.
        for row in reader:
            # 책 정보를 저장하는 딕셔너리를 생성합니다.
            book = {
                "title" : row[0],
                "author" : row[1],
                "genre" : row[2],
                "pages" : int(row[3]),
                "publisher" : row[4]
            }
            books.append(book)
    
    with open(dst_file, 'w') as dst:
        # 딕셔너리 -> 문자열 (json)
        book_str = json.dumps(books)
        # JSON 형식으로 dst_file에 저장합니다.
        dst.write(book_str)


# 아래 주석을 해제하고 결과를 확인해보세요.  
src_file = 'prac_0401/books.csv'
dst_file = 'prac_0401/books.json'
books_to_json(src_file, dst_file)
# elice_utils.send_file(dst_file)

# dumps하고 write대신에 한번에
# json.dump(books, dst)로 해도 될까요?