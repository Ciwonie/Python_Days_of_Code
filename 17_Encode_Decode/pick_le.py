import pickle
# iso 639-3

class example_class:
    a_number = 35
    a_string = "hey"
    a_list = [1,2,3]
    a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
    a_tuple = (22, 33)


my_object = example_class()

my_pickled_object = pickle.dumps(my_object)
print(f"This is my pickled object:\n{my_pickled_object}\n")

my_object.a_dict = None

my_unpickled_object = pickle.loads(my_pickled_object)
print(f"a_dict of unpickled object:\n{my_unpickled_object.a_dict}\n")

# with open("ot_bytes.txt", "r", encoding="ISO-3166") as f:
#     for line in f:
#         pick = pickle.dumps(line)
#         print(pickle.loads(pick))
