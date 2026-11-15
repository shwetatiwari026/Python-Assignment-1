class Teacher:
    def teach(self):
        print("The person teaches students.")


class Researcher:
    def research(self):
        print("The person carries out research.")


class Professor(Teacher, Researcher):
    def introduce(self):
        print("I am a professor, a teacher and a researcher.")


person = Professor()
person.introduce()
person.teach()
person.research()
