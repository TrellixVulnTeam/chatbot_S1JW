import pickle

common_dict = {
    'name' : 'Balaji', 
    'age' : '23',
    'data' : '27/5/2018'
}

# common_dict['another_data'] = 'fine'
readed_dict = open('sample_user.pickle', 'rb')
dick = pickle.load(readed_dict)
readed_dict.close()

dick['sample_dict2'] = 'hello world'

pick_file = open('sample_user.pickle', 'wb')
pickle.dump(dick, pick_file)
pick_file.close()

read_dict = open('sample_user.pickle', 'rb')
print_dict = pickle.load(read_dict)
print(print_dict)
read_dict.close()