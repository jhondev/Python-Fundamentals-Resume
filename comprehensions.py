def print_collection(items):
    # Items joined with a comprehension
    items_joined = ','.join(str(x) for x in items)
    print('list ' + items_joined)


print_collection([1, 2, 3])
