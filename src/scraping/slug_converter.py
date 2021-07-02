

slug_dictinary = {
    'а': 'a', 'б': 'b',  'в':'v',  'г':'g',  'д':'d',  'е':'e',  'ё':'e',  'ж':'g',  'з':'z',
    'и': 'i',  'к':'k',  'л':'l',  'м':'m',  'н':'n',  'о':'o',  'п':'p',  'р':'r',  'с':'s',
    'т': 't',  'у':'u',  'ф':'f',  'х':'kh',  'ц':'c',  'ч':'ch',  'ш':'sh',  'щ':'sch',  'ъ':'',
    'ы': 'y',  'ь':'',  'э':'e',  'ю':'yu',  'я':'ya',

}

def from_cyr_to_en(test):
    text = test.replace(' ', '_').lower()
    tmp = ''
    for ch in text:
        tmp += slug_dictinary.get(ch, ch)
    return tmp