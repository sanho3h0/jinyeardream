# 단어 모음을 선언합니다. 수정하지 마세요.
words = [
    'apple',
    'banana',
    'alpha',
    'bravo',
    'cherry',
    'charlie',
]

def filter_by_prefix(words, prefix):
    # 아래 코드를 작성하세요.
    # new_words=[]
    # for w in words:
    #     if w.startswith(prefix):
    #         new_words.append(w)
    # return new_words #1

    # new_words = [w for w in words if w.startswith(prefix)]
    # return new_words #2

    return [w for w in words if w.startswith(prefix)]#3



# 아래 주석을 해제하고 결과를 확인해보세요.  
a_words = filter_by_prefix(words, 'a')
print(a_words)
