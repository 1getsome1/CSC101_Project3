# Project 4 – Graduate Rate (2017-2018)
# Name: Francisco Guzman
# Instructor: Dr. S. Einakian
# Section: 05
# classes and functionalities will be provided here

# class Division
class Division:
    def __init__(self, id, division_name):
        self.id = id
        self.division_name = division_name


# class Graduate
class Graduate:
    def __init__(self, id: str, major: str, bachelor: tuple[int, int], master: tuple[int, int],
                 doctor: tuple[int, int]):
        self.id = id
        self.major = major
        self.bachelor = bachelor
        self.master = master
        self.doctor = doctor

    def __eq__(self, other):
        if type(other) == Graduate:
            return other.bachelor == self.bachelor and other.master == self.master and other.doctor == self.doctor
        return False

    def __repr__(self):
        return f"Graduate({self.bachelor}, {self.master}, {self.doctor})"


# Design Recipe
# 1) read file and return list of strings
# 2) read_file(file_name: str):
# 3) template of function
#     - open the file
#     - read first 3 lines
#     - make a list with each line of the file
#     - split up each string from the list
# 4) test case:
# 5)

def read_file(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        lines = file.readlines()[3:]
    return [line.strip() for line in lines]


# Design Recipe
# 1) create list of Division objects
# 2) create_division (list_str: list[str]):
# 3) template of function
#     - make an empty list
#     - make an empty variable
#     - use split for each line in the list of strings
#     - get the id of the current line
#     - get the division name of the current line
#     - if the id ends with '00' then it signals a new division class
#     - make the current id and division name into an actual Division object
# 4) test case:
# 5)

def create_division(list_str: list[str]) -> list[Division]:
    divisions = []
    for x in list_str:
        line = x.split(',')
        division = Division(line[0], line[1])
        if division.id.endswith('00'):
            divisions.append(division)
    return divisions


# Design Recipe
# 1) create list of Graduate objects
# 2) create_graduate (list_str: list[str]):
# 3) template of function
#     - make an empty list
#     - make an empty variable
#     - go through each line in the list of strings
#     - split each line into words
#     - get all necessary components to create graduate object
#     - make variables for id, major, bachelor, master, doctor
#     - each time that there is a division a new list is created
# 4) test case:
# 5)

def create_graduate(list_str: list[str]) -> list[Graduate]:
    inner_list = []
    for x in list_str:
        inner_list = []
        words = x.split(',')
        id = words[0]
        major = words[1]
        while not id.endswith('00'):
            bachelors = (int(words[2]), int(words[3]))
            masters = (int(words[4]), int(words[5]))
            doctors = (int(words[6]), int(words[7]))
            grad_major = Graduate(id, major, bachelors, masters, doctors)
            inner_list.append(grad_major)
        else:
            continue
    return inner_list


# Design Recipe
# 1) create files for each division
# 2) create_files (lst_div_obj: list[Division], lst_grad_obj: list[Graduate]):
# 3) template of function
#   1. cycle through lst_div_obj
#   1-1. make the name of the file the first word of the division name
#   1-2. open the file to write and give it the ID, Major, Bachelor, Master, Doctor header
#   2. cycle through the list of graduates and make three variables equal to 0
#   3. for each different degree in graduates add there numbers for females and males
#   4. write in the file the necessary requirements
# 4) test case:
# 5)

def create_files(lst_div_obj: list[Division], lst_grad_obj: list[Graduate]) -> None:
    for d in lst_div_obj:
        d_name = r'C:\Users\franh\PycharmProjects' + d.division_name.split()[0] + ".csv"
        with open(d_name, 'a') as file:
            file.write("ID\tMajor\tBachelor\tMaster\tDoctor\n")
            for grad in lst_grad_obj:
                bachelors_total = masters_total = doctors_total = 0
                while d.id != grad.id:
                    bachelors_total = grad.bachelor[0] + grad.bachelor[1]
                    masters_total = grad.master[0] + grad.bachelor[1]
                    doctors_total = grad.doctor[0] + grad.bachelor[1]
                file.write(f"{d.id}\t{grad.major}\t{bachelors_total}\t{masters_total}\t{doctors_total}\n")
    file.close()


# Design Recipe
# 1) find total and average graduate for all divisions
# 2) find_total_avg_all_divisions(lst_div_obj: list[Division], lst_grad_obj: list[Graduate])->list[tuple]:
# 3) template of function
#   - make an empty list
#   - cycle through the objects in division
#   - make some variables equal to zero for later use
#   - cycle throughout the graduates in the list of grad
#   - while the id of the grad does not match the division id get the total of all the people with degrees and get the
#   average
#   - append to the list
# 4) test case:
# 5)
def find_total_avg_all_divisions(lst_div_obj: list[Division], lst_grad_obj: list[Graduate]) -> list[tuple]:
    t_avg = []
    things = ()
    for d in lst_div_obj:
        total_b = total_m = total_d = 0
        overall_t = 0
        total_disciplines = avg = 0
        for grad in lst_grad_obj:
            while d.id != grad.id:
                total_b += (grad.bachelor[0] + grad.bachelor[1])
                total_m += (grad.master[0] + grad.bachelor[1])
                total_d += (grad.doctor[0] + grad.bachelor[1])
                overall_t += total_b + total_m + total_d
                total_disciplines += 1
                avg += overall_t // total_disciplines
                things = (total_disciplines, avg)
            t_avg.append(things)
    return t_avg


# Design Recipe
# 1) find (female, male) graduate rate for given major
# 2) find_graduate_rate_major(lst_grad_obj: list[Graduate], major_name: str):
# 3) template of function
#   - cycle through the list of graduates
#   - make variables t_male, t_female, tot all equal to 0
#   - make an if statement to check if the current graduate major is equal to the major_name
#   - if it is true total all the males and females from all the degrees of that major
# 4) test case:
# 5)
def find_graduate_rate_major(lst_grad_obj: list[Graduate], major_name: str):
    for grad in lst_grad_obj:
        t_male = t_female = tot = 0
        if grad.major == major_name:
            t_male += grad.bachelor[0] + grad.master[0] + grad.doctor[0]
            t_female += grad.bachelor[1] + grad.master[1] + grad.doctor[1]
            tot += (t_male, t_female)
        return tot

#print(f"Total Of Processed number of graduates in Computer and information sciences and support service (all levels females and males) : {tot} ")
