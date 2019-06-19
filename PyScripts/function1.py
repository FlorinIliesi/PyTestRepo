# create functions in python that will take an argument and will return 1 for True or 0 for False for the following checks:
# - if the entry is numberic
# - if the entry is alphanumberic (chars and numbers)
# - if the entry is chars only
# - if entry is lowwercase
# - if entry is uppercase


def is_numberic(a):
    from pandas.core.dtypes.inference import is_number
    return 1 if is_number(a) else 0


def is_lowecase(a):
    return 1 if is_lowecase(a) else 0


def is_chars(a):
    return 1 if is_chars(a) else 0


def is_alfa(a):
    import re
    return 1 if bool(re.match('^[a-zA-Z0-9]+$', a)) else 0

