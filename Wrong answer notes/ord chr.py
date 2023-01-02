## ord는 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
result1 = ord('a')
result2 = ord('ㄱ')
result3 = hex(ord('b'))
print(f"ord('a') : {result1}")
print(f"ord('ㄱ') : {result2}")
print(f"hex(ord('b')) : {result3}\n")

#----------------------------------------------------------------------------#

## chr는 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환합니다.
result4 = chr(97)
result5 = chr(12593)
result6 = chr(0x62)
print(f"chr(97) : {result4}")
print(f"chr(12593) : {result5}")
print(f"chr(0x62) : {result6}")