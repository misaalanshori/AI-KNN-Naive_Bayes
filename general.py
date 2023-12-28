import csv

def loadCSV(file_path):
    data_array = []
    
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            data_array.append(row)

    return data_array

def intDict(dict):
    for key in dict:
        try:
            dict[key] = float(dict[key])
        except Exception:
            dict[key] = dict[key]
    return dict

def dictListToInt(dict_list):
    dicsts = []
    for dict in dict_list:
        dicsts.append(intDict(dict))
    return dicsts