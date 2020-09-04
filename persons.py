from decorators import decor_quiz_result
import random

class Testing:
    def __init__(self):
        self.tests_results = {}
        self.success_rate = {}
        
    def chemistry_check(self, student, questions_qty):
        print('=========================================================================')
        print('Starting quiz for student {1} , Id:{0}'.format(student.id, student.name))
        print("List any {0} of the first 20 elements in the Period table:".format(questions_qty))
        responses = {}
        count = questions_qty
        while count > 0:
            answer = student.get_answer()
            if answer.isalpha():
                if answer in responses.values():
                    print("{0} was already entered          <--no duplicates allowed".format(answer))
                else:
                    responses[questions_qty-count+1] = answer
                    count -= 1
            else:
                print("Not alphabetic. Try again.")
        self.tests_results["chemistry"] = responses
        return "Chemistry check DONE"
    
    def algebra_check(self, student, questions_qty, questions):
        print('=========================================================================')
        print('Starting quiz for student {1} , Id:{0}'.format(student.id, student.name))
        responses = {}
        count = questions_qty
        while count > 0:
            question_number = random.randint(0, len(questions)-1)
            question = list(questions.keys())[question_number]
            while question in responses.keys():
                question_number = random.randint(0, len(questions)-1)
                question = list(questions.keys())[question_number]
            print('Question №{0} : {1}'.format(question_number, question))
            answer = student.get_answer()
            if answer.isdecimal():
                responses[question] = answer
                count -= 1
            else:
                print("Not a number. Try again.")
        self.tests_results["algebra"] = responses
        return "Algebra check DONE"
    
    @decor_quiz_result #just for testing decorator
    def responses_check(self, subject, responses, quiz_data):
        if type(quiz_data) is type(dict()):
            print("Answers  : ", [key +': '+ quiz_data[key] for key in responses[subject].keys()])
            print("Responses: ", [key +': '+ responses[subject][key] for key in responses[subject].keys()])
            correct_responses = {key : value for key, value in responses[subject].items() if quiz_data[key]==responses[subject][key]}
            wrong_responses = {key : value for key, value in responses[subject].items() - correct_responses.items()}
            self.success_rate = {subject : len(correct_responses)/len(responses[subject].values())}
        else:
            correct_responses = [response for response in responses[subject].values() if (response in quiz_data)]
            wrong_responses = [response for response in responses[subject].values() if (response not in correct_responses)]
            self.success_rate = {subject : len(correct_responses)/len(responses[subject].values())}
        return correct_responses, wrong_responses, self.success_rate

#------------------------------------------------------------------------------
class Human:
    def __init__(self, name):
        self.name = name

class Teacher(Human): #Teacher IS A Human
    def __init__(self, id, name):
        super().__init__(name)
        self.id = id
       
    def get_quiz_data(self, filepath):
        with open(filepath, 'r') as el_file:
            if len(el_file.readline().split(','))>1:
                el_file.seek(0)
                quiz_data = {el.strip().lower().split(',')[0]:','.join(el.strip().lower().split(',')[1:]) for el in el_file.read().splitlines()}
            else:
                el_file.seek(0)
                quiz_data = {el.strip().lower() for el in el_file.read().splitlines()}
        return quiz_data
    
    def get_questions_qty(self):
        self.questions_qty = input('How many questions ask: ')
        while not self.questions_qty.isdigit():
            print("Not a number. Try again.")
            self.questions_qty = input('How many questions ask: ')
        self.questions_qty = int(self.questions_qty)
        return self.questions_qty
    
class Student(Human): #Student IS A Human
    def __init__(self, id, name, tests):
        super().__init__(name)
        self.id = id
        self.tests = tests #Student HAS tests (class Testing)
        
    def get_answer(self):
        return input("My answer: ").lower().strip()

#------------------------------------------------------------------------------
class LearnGroup:
    def __init__(self, group_id):
        self.group_id = group_id
        self.students = None #LearnGroup HAS students
        self.teacher = None #LearnGroup HAS teacher
        self.questions_qty = None