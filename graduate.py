# Project 4 – Graduate Rate (2017-2018)
# Name: Francisco Guzman
# Instructor: Dr. S. Einakian
# Section: 05
# main program
import sys

from graduate_funcs import *


def main():
    fname = sys.argv[1] #input('File name:')
    lines = read_file(fname)
    divisions = create_division(lines)
    innerlist = create_graduate(lines)
    create_files(divisions, innerlist)
if __name__ == "__main__":
    main()

# try:
# malesb = int(words[2])
# except ValueError:
# malesb = 0
# try:
# femalesb = int(words[3])
# except ValueError:
# femalesb = 0
# try:
# malesm = int(words[4])
# except ValueError:
# malesm = 0
# try:
# femalesm = int(words[5])
# except ValueError:
# femalesm = 0
# try:
# malesd = int(words[6])
# except ValueError:
# malesd = 0
# try:
# femalesd = int(words[7])
# except ValueError:
# femalesd = 0
# bachelors = (malesb, femalesb)
# masters = (malesm, femalesm)
# doctors = (malesd, femalesd)
