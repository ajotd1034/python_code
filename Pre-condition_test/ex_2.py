def count_char(welcome_string: str):
    
    welcome_string = welcome_string.upper().replace(' ', '')
    keys = sorted(list(set(welcome_string)))

    for key in keys:
        print(f'{key} {welcome_string.count(key)}')
    

if __name__ == '__main__':
    welcome_string = 'Hello welcome to Cathay 60th year anniversary'
    count_char(welcome_string)
    