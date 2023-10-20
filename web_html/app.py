

from flask import Flask, request, send_file ,render_template ,redirect
from flask import jsonify
import os
import  jpype     
import  asposecells     
jpype.startJVM() 
from asposecells.api import Workbook
 
app = Flask(__name__ ,  template_folder='templates')

# Directorul în care sunt stocate fișierele
UPLOAD_FOLDER = '/home/bercovasile/Desktop/Programarea/Semestrul_3/proiect_de an/web_html'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route('/')
def index():
    return send_file('templates/index.html')

@app.route('/student', methods=['GET'])
def student():
    print("Student")  # Afișați "student" în consolă
    return send_file('templates/student.html')
    #return jsonify(message="Student selected")  # Trimiteți un răspuns JSON către client

@app.route('/teacher', methods=['GET'])
def thacher():
    print("Teacher")  # Afișați "student" în consolă
    return send_file('templates/teacher.html')
    #return jsonify(message="Student selected")  # Trimiteți un răspuns JSON către client

@app.route('/get_options_teacher', methods=['GET'])
def get_options_techer():
    # Aici puteți genera sau obține opțiunile din backend
    options_teacher = ["dsfsdfsd", "sdrser"] 
    return jsonify(options=options_teacher)

@app.route('/handle_selected_option', methods=['POST'])
def handle_selected_option():
    data = request.get_json()  # Obțineți datele JSON trimise de la client
    selected_option = data.get("selectedOption")
    print(f"Selected Option: {selected_option}")  # Afișați opțiunea aleasă în consolă
    return jsonify(message=f"Selected Option: {selected_option}")



@app.route('/get_options_grups', methods=['POST'])
def get_options_grups():
    data = request.get_json()
    selected_option = data.get("selectedOption")
    options_grups=[]
    if selected_option == "Anul 1" :
        with open('templates/timetable/student/Anul 1/grupe.txt') as f:
            for line in f:
                options_grups.append(line.strip())
        return jsonify(options=options_grups)        
    elif selected_option == "Anul 2" :
        with open('templates/timetable/student/Anul 2/grupe.txt') as f1:
            for line in f1:
                options_grups.append(line.strip())
        return jsonify(options=options_grups)   
    elif selected_option == "Anul 3" :
        with open('templates/timetable/student/Anul 3/grupe.txt') as f2:
            for line in f2:
                options_grups.append(line.strip())
        return jsonify(options=options_grups) 
    elif selected_option == "Anul 4" :
        with open('templates/timetable/student/Anul 4/grupe.txt') as f3:
            for line in f3:
                options_grups.append(line.strip())
        return jsonify(options=options_grups)

@app.route('/handle_selected_option_grups', methods=['POST'])
def handle_selected_option_grups():
    data = request.get_json()  # Obțineți datele JSON trimise de la client
    selected_option_grups = data.get("selectedOptionGrups")
    print(f"Selected Option: {selected_option_grups}")  # Afișați opțiunea aleasă în consolă
    # Puteți face orice altă prelucrare aici
    excel_file_path = '/home/bercovasile/Desktop/Programarea/Semestrul_3/proiect_de an/web_html/templates/timetable/student/Anul 1/TI-231.xlsx'
    # Returnați fișierul Excel către client
    return send_file(excel_file_path)
    #workbook = Workbook("/home/bercovasile/Desktop/Programarea/Semestrul_3/proiect_de an/web_html/templates/timetable/student/Anul 1/orar_grup.xlsx")
    
    #jpype.shutdownJVM()
    #return jsonify(workbook)







def find_file(search_query):
    for root, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for file in files:
            if search_query in file:
                return os.path.join(root, file)
    return None






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)







