def byKey(e):
    return e['passing_grade']

how_many_created = list()
count = input('Kaç tane öğrencinin kaydı girilecek: ')
try:
    count = int(count)
    for a in range(count):
        student = {}
        first_name = input('Adı: ')
        last_name = input('Soyadı: ')
        midterm_grade = input('Ara Notu: ')
        try:
            midterm_grade = int(midterm_grade)
        except:
            midterm_grade = 0
        project_grade = input('Proje Notu: ')
        try:
            project_grade = int(project_grade)
        except:
            project_grade = 0           
        final_grade = input('Final Notu: ')
        try:
            final_grade = int(final_grade)
        except:
            final_grade = 0
        passing_grade = int(midterm_grade * 0.3 + project_grade * 0.3 + final_grade * 0.4)
        student = {'first_name':first_name,'last_name':last_name,'midterm_grade':midterm_grade,'project_grade':project_grade,'final_grade':final_grade,'passing_grade':round(float(passing_grade))}
        how_many_created.append(student)
    how_many_created.sort(reverse=True,key=byKey)
    print(how_many_created)
except:
    print('İşleme Devam Edilemiyor.')
    
