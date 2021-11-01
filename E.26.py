def search_in_tuple(tup,search):
    if search in tup:
        return f'element found at index: {tup.count(search)}'    #count num
    else:
        return "element not found in tuple" 
print(search_in_tuple((10,20,30,30,40,30,50),30))

def search_in_tuple(tup,search):
    if search in tup:
        # return f'element found at index: {tup.index(search)}'
        pass
    else:
        return "element not found in tuple" 
print(search_in_tuple((10,20,30,30,40,30,50),70))     #find index