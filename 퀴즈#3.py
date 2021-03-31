#사이트 비밀번호 만들기
address=input("사이트 주소를 적어주십시오 : ")
num=address.index(".")
core=address[7:num]
password=core[:3]+str(len(core))+str(core.count('e'))+"!"
print(f"이 사이트의 비밀번호는 {password}입니다.")