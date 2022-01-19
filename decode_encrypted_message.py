import base64

MESSAGE = 'FkYBFhYQFRISQUpfTEsCBggABkRZU1cCDgoGAA0LEBFKQUhDUhYDFQQDBwAIS0lUSgQ'\
    'UBRoBBBJG RlBFSwULFx8EFgoXHxVGTUZNBA8EDBEbBB8GGwdXQVtGTRACAAoXBgQWRFlTVxM'\
    'ABAgMGB9CVFdB VRAUFRVGTUZNAwMDQlRXQVUUHB1RRhw='

KEY = 'marcuspaafjellet'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(eval(''.join(result)))
