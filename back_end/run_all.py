import subprocess
import os

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


os.makedirs('group_schedules', exist_ok=True)
yearNames=['anul_I', 'anul_II','anul_III', 'anul_IV']
for year in yearNames:
    os.makedirs(yearNames, exist_ok=True)


print(f'{colors.BOLD}{colors.UNDERLINE}{colors.OKBLUE}####Creating groups schedules.{colors.ENDC }')
subprocess.run(['python', 'student_schedule.py'])
print(f'{colors.BOLD}{colors.UNDERLINE}{colors.OKBLUE}####Done.\n\n{colors.ENDC }')

print(f'{colors.BOLD}{colors.UNDERLINE}{colors.OKBLUE}####Extracting prof names.{colors.ENDC }')
subprocess.run(['python','extract_prof_names.py'])
print(f'{colors.BOLD}{colors.UNDERLINE}{colors.OKBLUE}####Done.\n\n{colors.ENDC }')

print(f'{colors.BOLD}{colors.UNDERLINE}{colors.OKBLUE}####Creating prof schedules.{colors.ENDC }')
subprocess.run(['python', 'prof_schedule.py'])
print(f'{colors.BOLD}{colors.UNDERLINE}{colors.OKBLUE}####Done.\n\n{colors.ENDC }')
