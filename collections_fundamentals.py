# use dictionaries
def dictionaries_test():
    urls = {'Google': 'http://google.com',
            'Pluralsight': 'http://pluralsight.com',
            'Microsoft': 'http://microsoft.com'}
    print(urls)
    print(urls['Google'])

    for url in urls:
        print(url)
        print(urls[url])

    for key, value in urls.items():
        print("key: {key}, value: {value}".format(key=key, value=value))


# use set
def set_test():
    # remove duplicated items from a list with set help
    items = [1, 2, 3, 4, 5, 5, 5, 5]
    unique_items = set(items)
    print(unique_items)
    for item in unique_items:
        print(item)


# use of range and tuples
def range_test():
    items = range(14, 30, 2)
    for counter, value in enumerate(items):
        print("counter: {}, value: {}".format(counter, value))


# use of lists, tuples, str and str methods
def tuple_test():
    tuple1 = (1, 2, 3)
    print(tuple1)
    items = [1, 2, 3, 4, 5]
    min_number, max_number = min_and_max(items)
    print('for the list ' + ','.join(str(x) for x in items) + ' min number is ' + str(
        min_number) + ' and max number is ' + str(max_number))


# -------helpers------
def min_and_max(items):
    return min(items), max(items)


# TupleTest()
# RangeTest()
# DictionariesTest()
set_test()
