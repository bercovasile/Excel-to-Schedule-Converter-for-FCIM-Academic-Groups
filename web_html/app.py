

from flask import Flask, request, send_file ,render_template ,redirect
from flask import jsonify
import os
import jpype     
import asposecells     
import logging
jpype.startJVM() 
from asposecells.api import Workbook

 
app = Flask(__name__ ,  template_folder='/templates')




UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


#-----------------------------------------------------------




#-----------------------------------------------------------

@app.route('/')
def index():
    return send_file('templates/index.html')

@app.route('/student', methods=['GET'])
def student():
    print("Student")  
    return send_file('templates/student.html')

@app.route('/teacher', methods=['GET'])
def thacher():
    print("Teacher") 
    return send_file('templates/teacher.html')

#-----------------------------------------------------------




#-----------------------------------------------------------

def options_teacher():
    options_teacher=[]
    with open('./timetable/teacher/teacher.txt') as f:
        for line in f:
            options_teacher.append(line.strip())
    return options_teacher

def search_names(șir, lista_de_nume):
    rezultat = [nume for nume in lista_de_nume if șir in nume]
    return rezultat

@app.route('/get_options_teacher', methods=['GET'])
def get_options_teacher():
    options_teachers=options_teacher()
    return jsonify(options=options_teachers)  



@app.route('/handle_selected_option_teacher', methods=['POST'])
def handle_selected_option_teacher():
    data = request.get_json()
    selected_option_grups = data.get("selectedOptionTeacher")

    print(f"Selected Option: {selected_option_grups}") 

    rezultat_cautare = search_names(selected_option_grups, options_teacher())
    print(rezultat_cautare)

    excel_file_path = find_file_teacher(selected_option_grups)
    print(f"Fint paht is {excel_file_path}")
    return send_file(excel_file_path)


@app.route('/get_options_teacher_from_text_input', methods=['POST'])
def get_options_teacher_from_text_input():
    data = request.get_json()
    selected_option_grups = data.get("selectedOptionTeacher")
    options_teachers=search_names(selected_option_grups, options_teacher())
    return jsonify(options=options_teachers)  



def find_file_teacher(search_query):
    excel_extensions = ['.xlsx', '.xls', '.xlsm', '.xlsb', '.xltx', '.xltm']  # Lista cu extensiile Excel

    for root, dirs, files in os.walk("./timetable/teacher/"):
        for file in files:
            for ext in excel_extensions:
                if file.endswith(ext) and search_query in file:
                    return os.path.join(root, file)
    return None

#-----------------------------------------------------------




#-----------------------------------------------------------

@app.route('/get_options_grups', methods=['POST'])
def get_options_grups():
    data = request.get_json()
    selected_option = data.get("selectedOption")
    options_grups=[]
    if selected_option == "Anul 1" :
        with open('./timetable/student/Anul 1/grupe.txt') as f:
            for line in f:
                options_grups.append(line.strip())
        return jsonify(options=options_grups)        
    elif selected_option == "Anul 2" :
        with open('./timetable/student/Anul 2/grupe.txt') as f1:
            for line in f1:
                options_grups.append(line.strip())
        return jsonify(options=options_grups)   
    elif selected_option == "Anul 3" :
        with open('./timetable/student/Anul 3/grupe.txt') as f2:
            for line in f2:
                options_grups.append(line.strip())
        return jsonify(options=options_grups) 
    elif selected_option == "Anul 4" :
        with open('./timetable/student/Anul 4/grupe.txt') as f3:
            for line in f3:
                options_grups.append(line.strip())
        return jsonify(options=options_grups)

@app.route('/handle_selected_option_grups', methods=['POST'])
def handle_selected_option_grups():
    data = request.get_json()  # Obțineți datele JSON trimise de la client
    selected_option_grups = data.get("selectedOptionGrups")
    print(f"Selected Option: {selected_option_grups}")  # Afișați opțiunea aleasă în consolă
    # Puteți face orice altă prelucrare aici
    excel_file_path = find_file_student(selected_option_grups)
    print(f"Fint paht is {excel_file_path}")
    # Returnați fișierul Excel către client
    return send_file(excel_file_path)


def find_file_student(search_query):
    excel_extensions = ['.xlsx', '.xls', '.xlsm', '.xlsb', '.xltx', '.xltm']  # Lista cu extensiile Excel

    for root, dirs, files in os.walk("./timetable/student/"):
        for file in files:
            for ext in excel_extensions:
                if file.endswith(ext) and search_query in file:
                    return os.path.join(root, file)
    return None

#-----------------------------------------------------------




#-----------------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)







