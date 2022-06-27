
def count_characters(s):
    pass
if __name__=="__main__":
    s=input()
    L=count_characters(s)
    print("Lower|Upper|Digits|SpecialCharacters")
    print(' '.join(map(str,L)))
