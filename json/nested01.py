areas = [
    ('tokio','jp',36.933,(35.68564,139.69564)),
    ('dehli','in',21.935,(28.61234,77.20654))
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude:":>9}')
    for name,_,_,(laenge,breite) in areas:
        print(f'{name:15} | {laenge:9.4f} | {breite:9.4f}')
main()