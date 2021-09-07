def get_data_from_file(filepath):
    '''
    Extracts grades and lessons from text file
    input: filepath of the text file
    output: dictionary of lessons and grades
    '''
    
    # Read file contents
    with open(filepath, 'r') as f:
        student_grades = f.readlines()

    # Create dictionary of grades
    grades_dict = {}
    for i in range(len(student_grades)):
        _tmp = student_grades[i].strip()
        _tmp = _tmp.split(', ')
        grades_dict[_tmp[0]] = float(_tmp[1])
    
    return grades_dict