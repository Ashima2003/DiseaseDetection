from tkinter import *
import numpy as np
import pandas as pd
from PIL import Image, ImageTk
import chardet
import csv

from tkinter import ttk
import tkinter as tk

l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
      'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
      'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
      'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
      'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
      'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
      'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
      'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
      'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
      'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
      'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
      'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
      'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
      'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria',
      'family_history', 'mucoid_sputum',
      'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
      'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
      'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
      'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
      'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
      'yellow_crust_ooze']

disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
           'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
           ' Migraine', 'Cervical spondylosis',
           'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
           'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
           'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
           'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
           'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
           'Impetigo']

l2 = []
for x in range(0, len(l1)):
    l2.append(0)


# TRAINING DATA df 
df = pd.read_csv("Training.csv")

df.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                          'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                          'Bronchial Asthma': 9, 'Hypertension ': 10,
                          'Migraine': 11, 'Cervical spondylosis': 12,
                          'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                          'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                          'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                          'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                          'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                          'Varicose veins': 30, 'Hypothyroidism': 31,
                          'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                          '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                          'Psoriasis': 39,
                          'Impetigo': 40}}, inplace=True)



disease_to_doctor = {
    'Drug Reaction': 'Allergist',
    'Allergy': 'Allergist',
    'Hypertension': 'Cardiologist',
    'Heart attack': 'Cardiologist',
    'Psoriasis': 'Dermatologist',
    'Chicken pox': 'Dermatologist',
    'Acne': 'Dermatologist',
    'Impetigo': 'Dermatologist',
    'Fungal infection': 'Dermatologist',
    'Hypothyroidism': 'Endocrinologist',
    'Diabetes': 'Endocrinologist',
    'Hypoglycemia': 'Endocrinologist',
    'Hyperthyroidism': 'Endocrinologist',
    'GERD': 'Gastroenterologist',
    'Peptic ulcer disease': 'Gastroenterologist',
    'Jaundice': 'Gastroenterologist',
    'Dimorphic hemmorhoids(piles)': 'Gastroenterologist',
    'Gastroenteritis': 'Gastroenterologist',
    'Urinary tract infection': 'Gynecologist',
    'Chronic cholestasis': 'Hepatologist',
    'Hepatitis A': 'Hepatologist',
    'Hepatitis B': 'Hepatologist',
    'Hepatitis C': 'Hepatologist',
    'Hepatitis E': 'Hepatologist',
    'Hepatitis D': 'Hepatologist',
    'Alcoholic hepatitis': 'Hepatologist',
    'Malaria': 'Internal Medicine',
    'Dengue': 'Internal Medicine',
    'Migraine': 'Neurologist',
    'Cervical spondylosis': 'Neurologist',
    'Paralysis (brain hemorrhage)': 'Neurologist',
    'AIDS': 'Osteopathic',
    '(vertigo) Paroxysmal Positional Vertigo': 'Otolaryngologist',
    'Common Cold': 'Otolaryngologist',
    'Typhoid': 'Pediatrician',
    'Varicose veins': 'Phlebologist',
    'Bronchial Asthma': 'Pulmonologist',
    'Pneumonia': 'Pulmonologist',
    'Osteoarthritis': 'Rheumatologist',
    'Arthritis': 'Rheumatologist',
    'Tuberculosis': 'Tuberculosis'
}

X = df[l1]

y = df[["prognosis"]]  
np.ravel(y)

# TESTING DATA = tr
tr = pd.read_csv("Testing.csv")
tr.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                          'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                          'Bronchial Asthma': 9, 'Hypertension ': 10,
                          'Migraine': 11, 'Cervical spondylosis': 12,
                          'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                          'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                          'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                          'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                          'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                          'Varicose veins': 30, 'Hypothyroidism': 31,
                          'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                          '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                          'Psoriasis': 39,
                          'Impetigo': 40}}, inplace=True)

X_test = tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

doctorRequired=""

def DecisionTree():
    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()  # empty model of the decision tree
    clf3 = clf3.fit(X, y)

    # calculating accuracy
    from sklearn.metrics import accuracy_score
    y_pred = clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(l1)):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted = predict[0]
    diseaseSuffering=disease[predicted]
    print(diseaseSuffering)


    def get_doctor_for_disease(disease):
      return disease_to_doctor.get(disease, "Doctor not found for this disease")
    
    doctorRequired=get_doctor_for_disease(diseaseSuffering)
    
    print(f"The doctor for {diseaseSuffering} is {doctorRequired}")
    run_query(doctorRequired)




    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")

def is_time_in_range(time_range, input_time):
    start_time, end_time = time_range.split('-')
    return start_time <= input_time <= end_time


def run_query(doctor_name):
    # Create a new pop-up window
    result_window = tk.Toplevel()
    result_window.title("Doctor Availability")

    # Create a Treeview widget to display the results in tabular format
    tree = ttk.Treeview(result_window)
    tree["columns"] = ("Name","Speciality", "Availability")
    tree.heading("#0", text="Doctor")
    tree.heading("#1", text="Name")
    tree.heading("#2", text="Speciality")
    tree.heading("#3", text="Availability")

    # Filter rows where the Doctor column matches the specified doctor
    with open('doctorrrr.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Doctor'] == doctor_name:
                name=row['Name']
                speciality = row['Speciality']
                availability = row['Availability']
                tree.insert("", "end", text=doctor_name, values=(name, speciality, availability))

    # Pack the Treeview widget
    tree.pack(expand=True, fill="both")




root = Tk()
root.title("DISEASE PREDICTOR SYSTEM")
root.geometry("1400x1400+0+0")
root.resizable(False, False)

# entry variables

Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Name = StringVar()

# Heading
title_lbl = Label(root, text="Disease Prediction System", font=("times and roman", 30, "bold"), bg="#08a29e", fg="white")
title_lbl.place(x=250, y=0, width=1000, height=100)

main_frame = Frame(root, bd=2, bg="lightgreen")
main_frame.place(x=250, y=100, width=1000, height=600)

img = Image.open("google2.png")
img = img.resize((1000, 600), Image.LANCZOS)
photoimg = ImageTk.PhotoImage(img)

f_lbl = Label(main_frame, image=photoimg)
f_lbl.place(x=0, y=0, width=1000, height=600)

# labels
name_lbl = Label(main_frame, text="Name of the Patient", font=("times and roman", 25, "bold"), fg="white", bg="#558e95")
name_lbl.place(x=50, y=0, width=350, height=50)

S1Lb = Label(main_frame, text="Symptom 1", font=("times and roman", 17, "bold"), fg="white", bg="#4c8086")
S1Lb.place(x=50, y=70, width=250, height=50)

S2Lb = Label(main_frame, text="Symptom 2", font=("times and roman", 17, "bold"), fg="white", bg="#4c8086")
S2Lb.place(x=50, y=130, width=250, height=50)

S3Lb = Label(main_frame, text="Symptom 3", font=("times and roman", 17, "bold"), fg="white", bg="#4c8086")
S3Lb.place(x=50, y=190, width=250, height=50)

S4Lb = Label(main_frame, text="Symptom 4", font=("times and roman", 17, "bold"), fg="white", bg="#4c8086")
S4Lb.place(x=50, y=250, width=250, height=50)

S5Lb = Label(main_frame, text="Symptom 5", font=("times and roman", 17, "bold"), fg="white", bg="#4c8086")
S5Lb.place(x=50, y=310, width=250, height=50)

lrLb = Label(main_frame, text="Result", font=("times and roman", 17, "bold"), fg="white", bg="#013b73")
lrLb.place(x=50, y=500, width=250, height=50)

# Label for appointment time
time_label = Label(main_frame, text="Appointment Time", font=("times and roman", 17, "bold"), fg="white", bg="#4c8086")
# time_label.grid(row=0, column=0, padx=10, pady=10)
time_label.place(x=50,y=370,width=250,height=50)


# entries
OPTIONS = sorted(l1)

NameEn = Entry(main_frame, textvariable=Name, font=("times and roman", 17, "bold"))
NameEn.place(x=450, y=0, width=450, height=50)

S1En = OptionMenu(main_frame, Symptom1, *OPTIONS)
S1En.place(x=450, y=70, width=300, height=50)

S2En = OptionMenu(main_frame, Symptom2, *OPTIONS)
S2En.place(x=450, y=130, width=300, height=50)

S3En = OptionMenu(main_frame, Symptom3, *OPTIONS)
S3En.place(x=450, y=190, width=300, height=50)

S4En = OptionMenu(main_frame, Symptom4, *OPTIONS)
S4En.place(x=450, y=250, width=300, height=50)

S5En = OptionMenu(main_frame, Symptom5, *OPTIONS)
S5En.place(x=450, y=310, width=300, height=50)


def validate_time():
    input_time = time_entry.get()
    # Check if input is in valid time format (HH:MM)
    if len(input_time) == 5 and input_time[2] == ':' and input_time[:2].isdigit() and input_time[3:].isdigit():
        # Store the input time in a variable or process it as needed
        appointment_time = input_time
        print("Appointment Time:", appointment_time)
    else:
        print("Please enter the time in HH:MM format.")


# Entry widget for inputting time
time_entry = Entry(main_frame, font=("times and roman", 17, "bold"))
# time_entry.grid(row=0, column=1, padx=10, pady=10)
time_entry.place(x=450,y=370,width=125,height=50)

# Button to trigger validation of input time
validate_button = Button(main_frame, text="Set Time", command=validate_time, font=("times and roman", 17, "bold"), fg="white", bg="#4c8086")
# validate_button.grid(row=0, column=2, padx=10, pady=10)
validate_button.place(x=600,y=370,width=125,height=50)


dst = Button(main_frame, text="Analyse", command=DecisionTree, font=("times and roman", 17, "bold"), bg="#013b73",
             fg="white")
dst.place(x=50, y=430, width=250, height=50)
exit_button = Button(main_frame, text="Exit", command=root.destroy,font=("times and roman", 17, "bold"), bg="#013b73",
             fg="white")
exit_button.place(x=450,y=430, width=300, height=50)

t1 = Text(main_frame, height=1, width=40, font=("times and roman", 15, "bold"), bg="#013b73", fg="white")
t1.place(x=450, y=500, width=300, height=50)


root.mainloop()