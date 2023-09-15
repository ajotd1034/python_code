def convert_score(score_list: list):
    
    re_score_list = []
    
    for score in score_list:
        score = str(score)
        re_score = f'{score[1]}{score[0]}'
        re_score_list.append(int(re_score))
        
    print(re_score_list)


if __name__ == '__main__':
    score_list = [35, 46, 57, 91, 29]
    convert_score(score_list)
    