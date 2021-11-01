# dict_value = {
#             120: ("Visal", "Borey", "Sovann"),
#             130: ("Hout","Mouyleng","Pidor"),
#             140: ("Nary", "Misora", "Masaaki"),
#             }
# for key, value in dict_value.items():      #for taking key and value
#     print(key , ":" , *value)              # use * for taking value one by one

def dict_value(dict):
    count = 1
    for key, value in dict.items():
        print(key , ":" , *value)
        if count != len(dict):
            print("*" * 10)
            count += 1
        # return dict 
(dict_value({
            120: ("Visal", "Borey", "Sovann"),
            130: ("Hout","Mouyleng","Pidor"),
            140: ("Nary", "Misora", "Masaaki"),     
            })) 