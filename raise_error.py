def rsp(mine, yours):
    allowed = ['가위', '바위', '보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError

# 오류가 있을 가능성이 있는 것을 try 에 넣어주고 except 구문을 사용하여 value error가 나는지 조회해보는 구문
try:
    rsp('가위', '바')
except ValueError:
    print("잘못된 값을 넣은 것 같습니다.")
    
    
    
    
# school - dictionary

 # 각 반에서 키가 190cm가 넘는 학생이 있으면 멈춘다. 
 # dictionary에서 items() 메소드는 key 값과 value 값을 모두 가져오게 만든다.
 
#  items()
# lala = {'포유류': ['돼지', '개', '고양이'],
#         '설치류': ['햄스터']}
 
#  for i, j in lala.items():
#      print("{} 종에는 {}가 있다.".format(i, j))
 
    
school = {'1반': [172, 185, 198, 172, 165, 199],
          '2반': [165, 177, 167, 180, 191]}

for class_number, students in school.items():
    # 위에서 key(반 이름) 와 students(학생들의 키)를 각각에 넣어준다.
    for student in students:
        if 190 < student:
            print(class_number, '반에 190을 넘는 학생이 있습니다. 그 학생의 키는 {}입니다.'.format(student))
            break
            # 이 break 는 바로 위의 if절인, '190보다 큰 학생' 에 대한 break이기 때문에 한 번만 훑고, 반복되지 않는다.
        
for class_number, students in school.items():
    for student in students:
        if 190 < student:
            print(class_number, '반에 190을 넘는 학생이 있습니다. 그 학생의 키는 {}입니다.'.format(student))
            
          
for class_number, students in school.items():
    for student in students:
        if 190 < student:
            print(class_number, '반에 190을 넘는 학생이 있습니다. 그 학생의 키는 {}입니다.'.format(student))
            raise StopIteration
            # 예외가 try 문에 있는 것이 아니기 때문에, 코드가 예외를 만나자마자 코드가 종료되었다. 
            
            # try 문으로 둘러싸보자.
            
# try ~ except 구문을 사용하여 중간에 끊어주는 구문.           
try:
    for class_number, students in school.items():
        for student in students:
            if 190 < student:
                print(class_number, '반에 190을 넘는 학생이 있습니다. 그 학생의 키는 {}입니다.'.format(student))
                raise StopIteration
            
except StopIteration:
    print("정상종료")
                
            