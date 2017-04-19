print('''------ bytes<->string ------''')

web = "www.baidu.com"
print(type(web),"\n")

print('''------byte(utf8/gb2312)------''')
web_bytes_utf8 = web.encode(encoding="utf-8")
print(type(web_bytes_utf8))
print(web_bytes_utf8)

web_bytes_gb2312 = web.encode(encoding="utf-8")
print(type(web_bytes_gb2312))
print(web_bytes_gb2312)


print('''------string------''')
web_string = web_bytes_utf8.decode()
print(type(web_string))
print(web_string)

web_string_gb2312 = web_bytes_gb2312.decode("gb2312")
print(type(web_string_gb2312))
print(web_string_gb2312)