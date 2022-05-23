def greet(lang):
    if lang == 'es':
        return('hola')
    elif lang == 'fr':
        return('bonjour')
    else:
        return('hello')
print(greet('es'),'Caro')
print(greet('fr'),'Louise')
print(greet('en'),'Nick')
        
