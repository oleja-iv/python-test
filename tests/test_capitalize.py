from capitalize import capitalize

if capitalize('hello!') != 'Hello!':
    raise Exeption("Doesn't work!")

if capitalize('') != '':
    raise Exception("Not work with empty string!")

print('All works correctly!')