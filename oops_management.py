
class StudentsNotFoundError(Exception):
    pass
class LoadData(Exception):
    pass
class MarksError(Exception):
    pass
class SubjectMissing(Exception):
    pass
class Person:
    def __init__(self , name):
        self.name = name
    def display_info(self):
        print("NAME -->" , self.name)
class Student(Person):
    def __init__(self , name , rollno , marks):
        super().__init__(name)
        self.rollno = rollno
        self.marks = marks
        self.load_data = []
        self.total_subject = 0
        self.total_markss = 0

        if self.marks > 100:
            raise MarksError("MARKS ALWAYS LESS THAN OR EQUAL TO 100 !")
        
    def load_datas(self , filename):
        try:
            with open(filename , "r") as file:
                data = file.readlines()
                for i in data:
                    if i not in self.load_data:
                        self.load_data.append(eval(i.strip()))
        except FileNotFoundError:
            print('FILE NOT EXISTS')
    def save_data(self):
        with open( 'updated_student_list.txt', "w") as file:         
            for i in self.load_data:
                if type(i).__name__ == 'dict':
                    file.write(str(i) + "\n")
                else:
                    pass
    def add_subject(self , subject):
        if len(self.load_data) > 0:
            for i in self.load_data:
                if i["ROLL_NO"] == self.rollno:
                    for key in i["MARKS"]:
                        if key.capitalize() == subject.capitalize():
                            print("SUBJECT IS ALREADY PRESENT !")
                            break
                    else:
                        i["MARKS"][subject] = self.marks

                    break
            else:
                raise StudentsNotFoundError("THIS STUDENT NOT IN YOUR DATA")
        else:
            raise LoadData("FIRST LOAD DATA")
        self.save_data()
    def update_marks(self , subject):
        if len(self.load_data) > 0:
            for i in self.load_data:
                if i["ROLL_NO"] == self.rollno:
                    for key in i["MARKS"]:
                        if key == subject:
                            i["MARKS"][subject] = self.marks
                            break
                    else:
                        print("SUBJECT NOT FOUND")
                    break
            else:
                raise StudentsNotFoundError("THIS STUDENT NOT IN YOUR DATA")
        else:
            raise LoadData("FIRST LOAD DATA")

        self.save_data()
    def  calculate_total(self):
        total_marks = 0
        if len(self.load_data) > 0:
            for i in self.load_data:
                if i["ROLL_NO"] == self.rollno:
                    self.total_subject = len(i["MARKS"])
                    for key in i["MARKS"]:
                        total_marks += i["MARKS"][key]
                    self.total_markss = total_marks
                    return total_marks
                    
            else:
                raise StudentsNotFoundError("THIS STUDENT NOT IN YOUR DATA")
        else:
            raise LoadData("FIRST LOAD DATA")
    def calculate_percentage(self):
        a = self.calculate_total()
        if self.total_subject == 0:
            raise ZeroDivisionError("No subjects found for this student") 
        else:
            return a / self.total_subject
        
    def calculate_grade(self):
        a = self.calculate_percentage()
        if a >= 80:
            return "GRADE A"
        elif a >= 60:
            return "GRADE B"
        elif a >= 50:
            return "GRADE C"
        elif a >= 33:
            return "GRADE D"
        else:
            return "FAIL" 
    def display_info(self):
        for i in self.load_data:
            if i["ROLL_NO"] == self.rollno:
                print(i)
        print("TOTAL MARKS-->" , self.total_markss , "\nPERCENTAGE -->" , 
            self.calculate_percentage() , "\nGRADE-->" , self.calculate_grade() , "\nTOTAL SUBJECT-->" , self.total_subject)
class Teacher(Person):
    def __init__(self , name , subject):
        super().__init__(name)
        self.subject = subject
    def display_info(self):
        print("NAME -->" , self.name , "\nSUBJECT-->" , self.subject)

class SchoolManger:
    @staticmethod
    def add_student(students_list , add_student):
        students_list.append(add_student)
    @staticmethod
    def search_student_by_rollno(student_list , search_student_):
        if len(student_list) > 0:
            for i in student_list:
                if i["ROLL_NO"] == search_student_:
                    print(i)
                    break
            else:
                print("STUDENT NOT FOUND!") 
        else:
            print("YOUR DATA IS EMPTY !")
    @staticmethod
    def delete_student_by_rollno(student_list , delete_stu):
        if len(student_list) > 0:
            for i in student_list:
                if i["ROLL_NO"] == delete_stu:
                    student_list.remove(i)
                    break                             
            else:
                print("STUDENT NOT FOUND!") 
        else:
            print("YOUR DATA IS EMPTY !")
    @staticmethod
    def update_student(student_list , rollno):
        if len(student_list) > 0:
            for i in student_list:
                if i["ROLL_NO"] == rollno:
                    print("1.NAME || 2.SUBJECT || 3.MARKS")
                    option = int(input("ENTER YOUR OPTION :"))
                    if option == 1:
                        name = input("ENTER YOUR NAME:")
                        i["NAME"] = name
                    elif option == 2:
                        old_subject = input("ENTER YOUR OLD SUBJECT :").capitalize()
                        new_subject = input("ENTER YOUR NEW SUBJECT :").capitalize()
                        for key in i["MARKS"]:
                            if key == old_subject:
                                i["MARKS"][new_subject] = i["MARKS"].pop(old_subject)
                                break
                            
                        else:
                            print("SUBJECT NOT FOUND")
                    elif option == 3:
                        subject_name = input("ENTER YOUR SUBJECT NAME :")
                        marks = int(input("ENTER YOUR MARKS ! OUT OF 100 :"))
                        for key in i["MARKS"]:
                            if key == subject_name:
                                i["MARKS"][subject_name] = marks
                                break
                        else:
                            print("SUBJECT NOT FOUND")
                    else:
                        print("INVALID OPTION")
                
            else:
                print("STUDENT NOT FOUND!")           # {"ROLL_NO": 1, "NAME": "Ali", "MARKS": {"Math": 95, "Science": 80}}
        else:
            print("YOUR DATA IS EMPTY !")
    @staticmethod
    def save_data(student_list , filename):
        import csv
        with open(filename , "w" , newline= '') as file:
            writer = csv.writer(file)
            writer.writerow(["ROLL_NO" , "NAME" , "MARKS"])
            for i in student_list:
                writer.writerow([i["ROLL_NO"] , i["NAME"] , i["MARKS"]])
    @staticmethod
    def load_data(student_list , file_name):
        import csv
        with open(file_name , "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            for i in reader:
                student_list.append({"ROLL_NO":int(i[0]) , "NAME":i[1] , "MARKS":eval(i[2])})
    @staticmethod
    def analyze_data(student_list):
        total_student = 0
        total_markss = 0
        highest_marks = 0
        lowest_marks = 1000000000
        subject_coverage = { }
        student_analyzes = []
        class_ = {}
        for i in student_list:
            student_analyze = { }
            total_student += 1
            student_analyze["ROLL_NO"] = i["ROLL_NO"]
            total_marks = 0
            total_sub = 0
            for key in i["MARKS"]:
                total_marks  += i["MARKS"][key]
                total_markss += i["MARKS"][key]
                total_sub += 1
                if key not in subject_coverage:
                    subject_coverage[key] = 1
                else:
                    subject_coverage[key] += 1
            if total_marks > highest_marks:
                highest_marks = total_marks
            if lowest_marks > total_marks:
                lowest_marks = total_marks
            student_analyze["TOTAL MARKS"] = total_marks
            if total_sub > 0:
                per = (total_marks / (total_sub * 100)) * 100
            else:
                raise ZeroDivisionError(" YOUR SUBJECT IS ZERO SO PERCENTAGE IS NOT CALCULATE")
            student_analyze["PERCENTAGE"] = per
            if per > 80:
                student_analyze["GRADE"] = 'A'
            elif per > 60:
                student_analyze["GRADE"] = 'B'
            elif per > 33:
                student_analyze["GRADE"] = 'C'
            else:
                student_analyze["GRADE"] = 'FAIL'
            student_analyzes.append(student_analyze)
        class_["AVG MARKS FOR ALL CLASS"] = total_markss / total_student
        class_["HIGHEST MARKS FOR ALL CLASS IS"] = highest_marks
        class_["LOWEST MARKS FOR ALL CLASS IS "] = lowest_marks
        return total_student , subject_coverage , student_analyzes , class_



student_lists = [
    {"ROLL_NO": 1, "NAME": "Ali", "MARKS": {"Math": 95, "Science": 80}},
    {"ROLL_NO": 2, "NAME": "Sara", "MARKS": {"Math": 70, "English": 85}},
    {"ROLL_NO": 3, "NAME": "John", "MARKS": {"Science": 60, "History": 75}},
    {"ROLL_NO": 4, "NAME": "Aman", "MARKS": {"Math": 40, "Science": 30, "English": 50 , "PYTHON": 45}}
]
try:
    s1 = SchoolManger()
    s1.save_data(student_lists , "student.csv")
    loaded_data = [ ]
    s1.load_data(loaded_data , "student.csv")
    print(loaded_data)
    total_student , subject_coverage , student_analyzes , class_ = s1.analyze_data(loaded_data)
    print("===" * 20)
    print("TOTAL STUDENT IS -->" , total_student , "\nSUBJECT COVERAGE -->" ,
           subject_coverage , "\nSTUDENT ANALYZES DATA -->" , student_analyzes ,
             "\nCLASS DATA -->" , class_)

except Exception as e:
    print(e)