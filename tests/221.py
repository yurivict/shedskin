# str/bytes/bytearray

# str

# 'capitalize', 'casefold', 'center', 'count', 'expandtabs', 'find', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isspace', 'istitle', 'isupper', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

print('bla'.endswith('la'))
print('-'.join(['a', 'b', 'c']))
#print('bla'.isprintable(), chr(200).isprintable())

# bytes

# {'fromhex', 'hex'}

print(b'bla'.endswith(b'la'))
print(b'-'.join([b'a', b'b', b'c']))
#print(b'bla'.hex())

# bytes ^ bytearray: {'__delitem__', 'pop', 'reverse', '__imul__', 'remove', '__iadd__', 'copy', 'insert', 'extend'}

ba = bytearray(b'bla')
ba.clear()
print(ba)

ba = bytearray(b'bla')
ba[1] = 80
print(ba)

#ba = bytearray(b'bla')
#ba.append(81)
#print(ba)
