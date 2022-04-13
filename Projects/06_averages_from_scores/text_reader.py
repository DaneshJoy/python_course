
def get_data_from_text_file(my_data):
    scores_dict = {}
    for line in my_data:
        # print(line.strip())
        lesson = line.split(',')
        scores_dict[lesson[0]] = float(lesson[1].strip())
        # print(scores_dict)
        
    return scores_dict
