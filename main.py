import persons as pers

def take_test(subject, group, decorated=True):
    group.questions_qty = group.teacher.get_questions_qty()
    quiz_data = group.teacher.get_quiz_data(subject.lower()+'.txt')
    for student in group.students.values():
        if subject == 'algebra':
            student.tests.algebra_check(student, group.questions_qty, quiz_data)
        elif subject == 'chemistry':
            student.tests.chemistry_check(student, group.questions_qty)
    
    #print('\nQuiz data:')
    #print(quiz_data)
    
    for student in some_group.students.values():
        #print('=========================================================================')
        print('\n{0} results for student {1} , Id:{2}'.format(subject, student.name, student.id))
        if decorated:
            student.tests.responses_check(subject, student.tests.tests_results, quiz_data)
        else:
            #student.tests.responses_check.origin(student, subject.lower(), student.tests.tests_results, quiz_data) #orgin responses_check (w/o decorator)
            cr, wr, sr = student.tests.responses_check.origin(student, subject.lower(), student.tests.tests_results, quiz_data) #orgin responses_check (w/o decorator)
            print( "{0:.0%} is correct".format(sr[subject]) )
            if type(quiz_data) is type(dict()):
                print( "Found: {0}".format('; '.join(ans for ans in [el[0]+'='+el[1] for el in list(cr.items())]) ) )
                print( "Not Found: {0}".format('; '.join(ans for ans in [el[0]+'='+el[1] for el in list(wr.items())]) ) )
            else:
                print( "Found: {0}".format(' '.join(cr).title()) )
                print( "Not Found: {0}".format(' '.join(wr).title()) )
            
students = {}
students[pers.Student(1, 'John Smith',pers.Testing()).id] = pers.Student(1, 'John Smith',pers.Testing())
students[pers.Student(2, 'Jane Doe',pers.Testing()).id] = pers.Student(2, 'Jane Doe',pers.Testing())

some_group = pers.LearnGroup(0)
some_group.students = students
some_group.teacher = pers.Teacher(0, 'Rajesh Kutrapali')

#possible tests: algebra, chemistry
#decorated=False provides responses_check w/o decorator
take_test('chemistry', some_group, decorated=False)
