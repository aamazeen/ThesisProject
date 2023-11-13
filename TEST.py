test_dict = {'key1': 'value1', 'key2': 'value2'}
test_dict2 = {}
for item in test_dict:
    print(item)
    test_dict2[item] = test_dict[item]
print(test_dict2)