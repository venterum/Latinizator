def latinizator(text):
    basic_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 
        'е': 'e', 'ё': 'о', 'ж': 'ž', 'з': 'z', 'и': 'i', 
        'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 
        'ш': 'š', 'щ': 'šch', 'ы': 'y', 'э': 'é', 
        'ю': 'u', 'я': 'a',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 
        'Е': 'Je', 'Ё': 'Jo', 'Ж': 'Ž', 'З': 'Z', 'И': 'I', 
        'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 
        'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č', 
        'Ш': 'Š', 'Щ': 'Šch', 'Ы': 'Y', 'Э': 'É', 
        'Ю': 'Ju', 'Я': 'Ja'
    }
    soft_map = {
        'л': 'ĺ', 'т': 't́', 'д': 'd́', 'н': 'ń', 'п': 'ṕ', 'б': 'b́',
        'с': 'ś', 'р': 'ŕ', 'з': 'ź', 'м': 'ḿ', 'в': 'v́', 'Б': 'B́',
        'Л': 'Ĺ', 'Т': 'T́', 'Д': 'D́', 'Н': 'Ń', 'П': 'Ṕ',
        'С': 'Ś', 'Р': 'Ŕ', 'З': 'Ź', 'М': 'Ḿ', 'В': 'V́'
    }
    vowels = {'а', 'о', 'у', 'э', 'ы', 'я', 'е', 'ё', 'ю', 'и',
              'А', 'О', 'У', 'Э', 'Ы', 'Я', 'Е', 'Ё', 'Ю', 'И'}
    result = []
    
    for i, char in enumerate(text):
        if char in {'ь', 'ъ'}:
            continue
        
        prev_char = text[i - 1] if i > 0 else ''
        next_char = text[i + 1] if i + 1 < len(text) else ''
        
        if char in {'и', 'И'} and (i == 0 or prev_char == ' '):
            result.append(basic_map[char.lower()] if char.isupper() else basic_map[char])
        elif char in {'е', 'ё', 'ю', 'я', 'Е', 'Ё', 'Ю', 'Я', 'и', 'И'} and (i == 0 or prev_char in {'ь', 'ъ', ' '} or prev_char in vowels):
            result.append('J' + basic_map[char.lower()] if char.isupper() else 'j' + basic_map[char])
        
        elif char in {'е', 'ё', 'ю', 'я', 'Е', 'Ё', 'Ю', 'Я', 'И', 'и'}:
            if i == 0 or next_char.lower() in {'ь', 'ъ'}:
                result.append('J' + basic_map[char.lower()] if char.isupper() else 'j' + basic_map[char])
            else:
                result.append(basic_map[char])
        
        elif char in soft_map and next_char.lower() in {'ь', 'Ь', 'ё', 'ю', 'я', 'Ё', 'Ю', 'Я'}:
            result.append(soft_map[char])
        
        else:
            result.append(basic_map.get(char, char))
    
    return ''.join(result)