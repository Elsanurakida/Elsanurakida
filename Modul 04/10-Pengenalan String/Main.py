# string adalah kumpulan dari karakter 

data = "ini adalah string"
print(data)
print("panjang karakter : ", len (data))
print("tipe data : ", type (data))

# 1. cara membuat string 

"""
    1. denganmenggunakan single qoute '---'
    2.dengan menggunakan double qoute "---"
"""

data = 'data menggunakan single quote'
print (data)

data = "menggunakan double qoute"
print (data)

print ("ini adalah hari jum'at")
print ("nama saya ma'ruf ")

# 2. kekuatan tanda \

# memuat ' menjadi string
print ('mari sholat jum\'at')
print ('saya ma\'ruf')

# double backslash
print ('c : \\ user \\ adam ')

# tab (\t)
print ("MU\t\tjuara")

# backspace (\b)
print ("MU\bjuara")

# newline (enter)
print ("baris satu .\nbaris dua.") # LF -> line feed # macOS
print ("baris satu . \n\r bsris dua. ") # CRLF -> windows

# raw string 
print (r'c:\user\adam')
