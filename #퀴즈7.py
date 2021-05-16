for num in range(1,51) :
    with open(str(num)+'주차.txt','w',encoding='utf8') as work_file:
        work_file.write('-',num,'주차 주간보고 -')
        work_file.write('부서 :')
        work_file.write('이름 :')
        work_file.write('업무 요약 :')
