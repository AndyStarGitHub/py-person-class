from __future__ import annotations


class Person:

    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_in: list) -> list:
    result = []
    for human in people_in:
        result.append(Person(human["name"], human["age"]))

    # print(f"Person.people = {Person.people}")

    for human in people_in:
        current_person = Person.people.get(human["name"])
        current_wife = human.get("wife")
        if current_wife:
            current_person.wife = Person.people[current_wife]
        current_husband = human.get("husband")
        if current_husband:
            current_person.husband = Person.people[current_husband]
    return result

# res = hasattr(Person, "people")
# print(res)
# res = len(Person.people) == 0
# print(res)


# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
#
#
#
# person_list = create_person_list(people)
# print(person_list)
#
# res = hasattr(list[0], "wife")
# print(res)
# res = person_list[0].wife.husband == person_list[0]
# print(res)
#

# def path_to_main():
#     base_path = os.path.join("app", "main.py")
#     return (
#         base_path if os.path.exists(base_path)
#         else os.path.join(os.pardir, base_path)
#     )


# def test_person_instance_attribute_wife_and_husband_doesnt_exists():
#     with open(path_to_main()) as file:
#         tree = ast.parse(file.read())
#
#     assert (
#         len(
#             tree.__dict__["body"][0]
#             .__dict__["body"][1]
#             .__dict__["args"]
#             .__dict__["args"]
#         )
#         == 3
#     ), "'__init__' should takes only two arguments 'name' and 'age'!"


# res = test_person_instance_attribute_wife_and_husband_doesnt_exists()
# print(res)


# def test_double_quotes_instead_of_single():
#     ppp = path_to_main()
#     with open(path_to_main(), "r") as file:
#         main_content = file.read()
#
#         assert (
#             "'" not in main_content
#         ), "You have to use a double quotes \"\" instead of single ''"


# res = test_double_quotes_instead_of_single()
# print(res)
# def test_create_person_list_has_wife_and_wife_have_husband(
#        people_data, created_person_list):
#     assert (
#         hasattr(created_person_list[0], "wife")
#         and created_person_list[0].wife.husband == created_person_list[0]
#     ), (
#         f"Person with 'name' {created_person_list[0].name} should have "
#         f"attribute 'wife' with name {created_person_list[0].wife.name} and "
#         f"Person.wife.husband should links to that Person"
#     )
#
#
# res = test_create_person_list_has_wife_and_wife_have_husband(
#     people, person_list)
# print(res)


# def test_person_class_attribute_people_exists():
#     assert hasattr(
#         Person, "people"
#     ), "Class Person should have class attribute 'people'"
#     assert (
#         len(Person.people) == 0
#     ), "Initial length of 'Person.people' should equal to 0"
