from random import*
count=0
for num1 in range(1,51): 
    num2=randrange(5,51)
    if 5<=num2<=15:
        print('[0] '+str(num1)+'번째 손님 (소요시간: '+str(num2)+'분)')
        count+=1
    else:
        print('[ ] '+str(num1)+'번째 손님 (소요시간: '+str(num2)+'분)')
print('총 탑승 승객 : '+str(count)+'분')
