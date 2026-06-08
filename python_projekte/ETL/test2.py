def umfang_flaeche(laenge, breite):
    return (2 * (laenge + breite), laenge * breite)

umfang_flaeche(3,6)
umfang, flaeche = umfang_flaeche(12, 45)
print(f'{umfang=}, {flaeche=}')