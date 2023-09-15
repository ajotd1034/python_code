def count(person_number: int):
    person_list = list(range(1, person_number + 1))
    last_idx = 0

    while len(person_list) > 2:
        temp_list = person_list[:]

        for idx, person in enumerate(temp_list):
            if (idx + 1) % 3 == 0:
                person_list.remove(temp_list[idx])
                if idx < len(temp_list):
                    last_idx = idx + 1
        
        for i in range(len(temp_list) - 1, last_idx - 1, -1):
            person_list.remove(temp_list[i])
            person_list.insert(0, temp_list[i])
        
    print(f'No. {person_list[-1]} pick.')


if __name__ == '__main__':
    person_number = int(input('How many people are here? (0-100) '))
    if person_number == 0:
        print('---No one is here, please input again.---')
    else:
        count(person_number)
