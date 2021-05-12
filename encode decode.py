import base64
str =  input("Enter a string to encode and decode: ")
str_enc = str.encode(encoding='utf8')
print("The encoded string in utf8 format is : ",str_enc)
bs64str_enc = base64.b64encode(str_enc)
print("The encoded string in base 64 format is ",bs64str_enc)
print("The decoded string is : ",str_enc.decode('utf8','strict'))
