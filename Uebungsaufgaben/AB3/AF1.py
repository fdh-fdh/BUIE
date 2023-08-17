class Student:
    def __init__(self, vorname, nachname, matrikelnummer):
        self.vorname = vorname
        self.nachname = nachname
        self._mktNr = matrikelnummer
        self.exams = []
        print('Welcome on board, ' + self.vorname)

    def get_mkt(self):
        print("I am finding your mkt, "+self.vorname + "!  " + str(self._mktNr) + " I've found it,ohuu ")
        return self._mktNr

    def set_mkt(self, mktnr):
        if len(mktnr) != 7:
            print('not valid number')
            #return self._mktNr
        else:
            self._mktNr = mktnr
            print('mkt has been changed')
            #return self._mktNr

    mktNr = property(get_mkt, set_mkt)


class Examiner:
    def __init__(self, vorname, nachname, mitarbeiter_id):
        self.vorname = vorname
        self.nachname = nachname
        self.mitarbeiter_id = mitarbeiter_id
        print("Welcome Mr./Mrs." + self.nachname)


class Exam:
    def __init__(self, name: str, date: int, place: int, examiner_id):
        self._name = name
        self._place = place
        self._date = date
        self._examiner_id = examiner_id
        self.student_list = []
        print("New Exam '" + self._name + "'is now available")

    def append_student_list(self, neu_student:Student):
        self.student_list.append(neu_student)
        print('student with name ' + neu_student.nachname + " " + neu_student.vorname + ' is added into exam ' + self._name)
        neu_student.exams.append(self._name)
        print("congrats " + neu_student.vorname, "you are in the exam " + self._name)
        return self.student_list


# list of Students' names
student_vorname = ("John", 'Maria', 'Anna', 'Paul', 'Sophia', 'Handsome', 'Pretty')
student_nachname = 'Schmidt'
Dozent_nachname = ("Streng","Lieb","Happy","Sad")
Dozent_Vorname = "mama"
mkt = 1000000
num = 0
student = {}
examiner = {}

# 7 students and 4 teachers will be set
for vorname in student_vorname:
    mkt = mkt + 1
    student[vorname] = Student(vorname, student_nachname, mkt)


mkt = 1000000
for vorname in Dozent_Vorname:
    for nachname in Dozent_nachname:
        mkt = mkt + 11
        examiner[nachname] = Examiner(vorname, nachname, mkt)


# print(student[student_vorname[0]].mktNr)
# print(examiner[Dozent_nachname[0]].mitarbeiter_id)

# initialising an exam
Intro_of_Quantum_Computing = Exam("Intro of Quantum Computing", 20351005, 1200, examiner[Dozent_nachname[0]].mitarbeiter_id)
Art_of_Sushi = Exam("Art of Sushi", 20221005, 3100, examiner[Dozent_nachname[1]].mitarbeiter_id)
fight_with_each_other = Exam("fight with each other: relaxing and become hard", 20360905, 1002,
                             examiner[Dozent_nachname[1]].mitarbeiter_id)
Eating_and_Joga = Exam("eating and joga", 20241005, 5300, examiner[Dozent_nachname[2]].mitarbeiter_id)
PE =Exam("PE", 20221125, 1205, examiner[Dozent_nachname[3]].mitarbeiter_id)

#set students into the exam

Intro_of_Quantum_Computing.append_student_list(student[student_vorname[0]])
Intro_of_Quantum_Computing.append_student_list(student[student_vorname[1]])
Intro_of_Quantum_Computing.append_student_list(student[student_vorname[2]])
Intro_of_Quantum_Computing.append_student_list(student[student_vorname[3]])

PE.append_student_list(student[student_vorname[0]])
PE.append_student_list(student[student_vorname[1]])
PE.append_student_list(student[student_vorname[2]])
PE.append_student_list(student[student_vorname[3]])

Art_of_Sushi.append_student_list(student[student_vorname[0]])
Art_of_Sushi.append_student_list(student[student_vorname[1]])
Art_of_Sushi.append_student_list(student[student_vorname[2]])
Art_of_Sushi.append_student_list(student[student_vorname[3]])

Eating_and_Joga.append_student_list(student[student_vorname[0]])
Eating_and_Joga.append_student_list(student[student_vorname[1]])
Eating_and_Joga.append_student_list(student[student_vorname[2]])
Eating_and_Joga.append_student_list(student[student_vorname[3]])

print("\n")
# Erstellen Sie eine Ausgabe mit allen Teilnehmern einer Prüfung
print("Eating_and_Joga have following participants:")
for i in range(1,len(Eating_and_Joga.student_list)):
    print(Eating_and_Joga.student_list[i].vorname,Eating_and_Joga.student_list[i].nachname)
print("\n")
print("PE have following participants:")
for i in range(1,len(PE.student_list)):
    print(PE.student_list[i].vorname, PE.student_list[i].nachname)
print("\n")
print("Art of Sushi have following participants:")
for i in range(1,len(Art_of_Sushi.student_list)):
    print(Art_of_Sushi.student_list[i].vorname,Art_of_Sushi.student_list[i].nachname)

# Erstellen Sie eine Ausgabe mit allen Prüfung eines Studenten
print("\n")
print("Student " + student_vorname[0] + " has following exams")
print(student[student_vorname[0]].exams)

print("\n")
print("Student " + student_vorname[1] + " has following exams")
print(student[student_vorname[1]].exams)

print("\n")
print("Student " + student_vorname[2] + " has following exams")
print(student[student_vorname[2]].exams)

