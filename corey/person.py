class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    # def __str__(self):
    #     return f'[Name: {self.name}, Job: {self.job}, Pay : {self.pay})]'

    def __repr__(self):
        return f"[Person({self.name}, {self.job}, {self.pay})]"

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percentage):
        self.pay = int(self.pay * (1 + percentage))


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, "MGR", pay)

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)

# class Manager:
#     def __init__(self, name, pay):
#         self.person = Person(name, "MGR", pay)
#
#     def give_raise(self, percent, bonus=.10):
#         self.person.give_raise(percent + bonus)
#
#     def __getattr__(self, attr):
#         return getattr(self.person, attr)
#
#     def __repr__(self):
#         return repr(self.person)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raise(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='Dev', pay=1000000)
    # print(bob.name, bob.pay)
    # print(sue.name, sue.pay)
    # print(bob.last_name(), sue.last_name())
    # sue.give_raise(.10)
    # print(sue)
    tom = Manager('Tom Jones', 50000)
    # tom.give_raise(.10)
    # print(tom.last_name())
    # print(tom)

    # print("______________________________________All Three ______________________________")
    # for obj in (bob, sue, tom):
    #     obj.give_raise(.10)
    #     print(obj)

    development = Department(bob, sue)
    development.add_member(tom)
    development.give_raise(.10)
    development.show_all()
