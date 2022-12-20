#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except BaseException as err:
        result = None
        sys.stderr.write("Exception: %s\n" % err)
    return result
