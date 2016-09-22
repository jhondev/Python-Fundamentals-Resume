import sys
from math import log

def convert(s):
    #convert to an integer
    try:
        x = -1
        x = int(s)        
    # except ValueError:
    #     x = -1
    # except TypeError:
    #     x = -2
    #     print('typeerror')
    except (ValueError, TypeError) as e:
        # x = -1
        # print('error handling with tuple')
        ##pass
        print("error message: {}".format(str(e)))
        #print("derr: {}".format(sys.stderr))
        #sys.stderr
        #raise
    return x

def string_log(s):
    v = convert(s)
    return log(v)

#convert([1, 2])
string_log("33")