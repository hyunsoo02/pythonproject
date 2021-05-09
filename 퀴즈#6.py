def std_weight(height,gender):
    if gender=="여자":
        c=height**2*21
        return c
    else :
        c=height**2*22
        return c
weight=round(std_weight(175/100,"남자"),2)
print("키 175cm 남자의 표준 체중은 ",weight,"kg 입니다.",sep='')
