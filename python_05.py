text = 'Clarusway'
print(text[0])

print(text[ : 5] + 'k' + text[-3:])
yeni_string = text[ :5] + 'k' + text[-3:]

var_string = 'ClarusWay'
print(var_string.lower())
print(var_string)
var_string = 'ClarusWay' . lower()
print(var_string)

text = 'AaBbCc'
print(text.lower())
text = text. lower()

var_str = 'In God we Trust'
var_str.lower()
print(var_str)

e_mail = 'bulent@clarusway.com'
print ('@' in e_mail)

text = 'www. clarusway.com'
print(text.endswith(' .com'))
print(text.startswith('http:'))

text = 'www.clarusway. com'
print(text.endswith('om'))
print(text.startswith('w'))

email = "clarusway@clarusway.com is my e-mail address"
print(email.startswith("@", 9))
print(email.endswith("-", 10, 32))

text = 'a b cd'
len(text)

email = "clarusway@clarusway.com is my e-mail address"
print(email.startswith("@", 9))
print(email.endswith("-", 10, 32))

text = 'www.clarusway.com'
print(text.endswith('.co'))
print(text.startswith('w.'))

text = """
Data preprocessing is an important task in text classification.
This program counts words in a sentence. It starts with space separated words."""
print ("To count words in a sentence : ", text.count(" ") + 1)

text = 'abcdef'
text.startswith('b',-5)

text = 'abcabcabc'
text.find('ca')
text.find('klm')
text.rfind('a')
text.index('ca')

text = 'www. clarusway . com'
print (text. index ('com' ) )
print (text. find ('com' ))

sentence = "I live and work in Virginia"
print(sentence.upper())
print(sentence. lower())
print(sentence. swapcase())
print(sentence) # note that, source text is unchanged

text = 'ClaRusWay'
text.upper()
text.lower()
text.swapcase()
text.replace('w', '***')
text.replace('W',' *** ').lower()

sentence = "I live and work in Virginia"
title_sentence = sentence. title()
print(title_sentence)
changed_sentence = sentence.replace("i", "+")
print(changed_sentence)
print(sentence) # note that, again source text is unchanged

text = 'the better the family, the better the society'
text = text. title()
print(text)

sentence = "I live and work in Virginia"
swap_case = sentence. swapcase()
print(swap_case)
print(swap_case.capitalize()) # changes 'i' to uppercase and
# the rest to lowercase

text = "S0d0me and G0m0re"
text.replace('0', 'o')

space_string = "listen first"
print(space_string.strip()) # removes all spaces from both sides

source_string = "interoperability"
print(source_string.strip("yi"))
# removes trailing "y" or "i" or "yi" or "y" from both sides

print(None or 1)

a = " "
b = "False"
c = True
d = ""
print(a or b or c and not d)

print("None or True and 1")

A = True
B = False
logic = (A or B) and (not A)
print(logic)

space_string = "  listen first  "
print(space_string.strip()) # removes all spaces from both 

source_string = "interoperability"
print(source_string.strip("yi"))
# removes trailing "y" or "i" or "yi" or "iy" from both sides

source_string = "interoperability"
print(source_string. lstrip("in"))
# removes "i" or "n" or "in" or "ni" from the left side

source_string = "interoperability"
print(source_string.rstrip("yt"))
# removes "y" or "t" or "yt" or "ty" from the right side

text = 'tyou can learn almost everything in pre-classz'
text.strip('tz')

text = text.rstrip('z').lstrip('t').upper()
print(text)

text = 'In God we Trust'
print(text.replace("ee", "e"))
text1 = text[:9]
text2 = text [10: ]
print(text1 + text2)