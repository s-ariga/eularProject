def name_score(name: str, n: int):
    '''
    名前nameの文字それぞれをアルファベットの順番に変更した総和とnの積を計算する

    parameters
    -----------------------
    name : string
        アルファベット大文字の名前
    n : int
        名前の順番
    '''
    order = lambda char: ord(char) - ord('A') + 1
    # アルファベットのアルファベット順の番号を返す

    score = sum(order(char) for char in name)
    return score*n

if __name__ == '__main__':
    with open("names.txt", "r") as name_file:
        # names.txtは1行
        names = sorted(name_file.read().replace('"','').replace('\n','').split(','))
    
    assert name_score('ABC', 3) == 18, 'name_number Error'
    answer = sum(name_score(name, n+1) for n, name in enumerate(names))
    print(answer)
