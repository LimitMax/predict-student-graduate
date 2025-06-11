import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model/model_rf.pkl")

st.set_page_config(page_title="Prediksi Status Mahasiswa", layout="wide")
st.title("🎓 Prediksi Status Mahasiswa")
st.markdown("Isi data mahasiswa untuk memprediksi status akademik berdasarkan data historis.")

with st.form("student_form"):
    st.subheader("📄 Informasi Pribadi & Akademik")
    col1, col2, col3 = st.columns(3)

    with col1:
        marital_status = st.selectbox("Status Pernikahan", ['Single', 'Married', 'Widower', 'Divorced','Facto Union','Legally Separated', 'Other'])
        application_mode = st.selectbox("Mode Aplikasi", ['1st phase - general contingent', 'Ordinance No. 612/93','1st phase - special contingent (Azores Island)','Holders of other higher courses','Ordinance No. 854-B/99','International student (bachelor)','1st phase - special contingent (Madeira Island)','2nd phase - general contingent','3rd phase - general contingent','Ordinance No. 533-A/99, item b2) (Different Plan)','Ordinance No. 533-A/99, item b3 (Other Institution)','Over 23 years old','Transfer','Change of course','Technological specialization diploma holders','Change of institution/course','Short cycle diploma holders','Change of institution/course (International)', 'Other'])
        course = st.selectbox("Program Studi", ['Biofuel Production Technologies','Animation and Multimedia Design','Social Service (evening attendance)','Agronomy','Communication Design','Veterinary Nursing','Informatics Engineering','Equinculture','Management','Social Service','Tourism','Nursing','Oral Hygiene','Advertising and Marketing Management','Journalism and Communication','Basic Education','Management (evening attendance)', 'Other'])
        attendance = st.selectbox("Waktu Kehadiran", ['Daytime', 'Evening', 'Other'])

    with col2:
        prev_qualification = st.selectbox("Kualifikasi Sebelumnya", ["Secondary education","Higher education - bachelor's degree","Higher education - degree","Higher education - master's","Higher education - doctorate","Frequency of higher education","12th year of schooling - not completed", "11th year of schooling - not completed","Other - 11th year of schooling","10th year of schooling","10th year of schooling - not completed","Basic education 3rd cycle (9th/10th/11th year) or equiv.","Basic education 2nd cycle (6th/7th/8th year) or equiv.","Technological specialization course","Higher education - degree (1st cycle)","Professional higher technical course","Higher education - master (2nd cycle)", "Other"])
        prev_qual_grade = st.number_input("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 100.0)
        admission_grade = st.number_input("Nilai Masuk (Admission Grade)", 0.0, 200.0, 120.0)
        age = st.number_input("Umur Saat Mendaftar", 15, 80, 20)

    with col3:
        mothers_occupation = st.selectbox("Pekerjaan Ibu", ['Unemployed', "Student", "Legislative/Executive/Directors", "Intellectual/Scientific","Technicians", "Administrative staff", "Services/Security/Sellers","Farmers/Fishers", "Industry/Construction", "Machine Operators","Unskilled Workers", "Armed Forces", "Other", "(blank)","Health professionals", "Teachers", "ICT specialists", "Intermediate science/engineering technicians", "Intermediate health professionals","Legal/social/cultural technicians", "Secretaries/data processing","Accounting/financial/registry operators", "Other admin support","Personal service workers","Sellers", "Personal care workers","Construction workers", "Jewelers/artisans/etc.", "Food/clothing/woodworking","Cleaning workers", "Unskilled agri/fish/forestry", "Unskilled extractive/construction/etc.", "Meal prep assistants", "Other"])
        fathers_occupation = st.selectbox("Pekerjaan Ayah", ['Unemployed', "Student", "Legislative/Executive/Directors", "Intellectual/Scientific","Technicians","Administrative staff", "Services/Security/Sellers", "Farmers/Fishers","Industry/Construction", "Machine Operators", "Unskilled Workers","Armed Forces", "Other", "(blank)","Armed Forces Officers","Armed Forces Sergeants", "Other Armed Forces personnel","Admin/Commercial Directors", "Hotel/Catering Directors", "Science/Engineering Specialists","Health professionals", "Teachers", "Finance/Admin Specialists","Intermediate science/engineering technicians", "Intermediate health professionals","Legal/social/cultural technicians", "ICT technicians","Secretaries/data processing","Accounting/financial/registry operators", "Other admin support","Personal service workers", "Sellers", "Personal care workers","Protection/security personnel", "Skilled agricultural producers","Subsistence farmers/fishers", "Skilled construction workers","Metalworkers", "Electricians","Food/clothing/woodworking","Fixed plant operators", "Assembly workers", "Drivers and mobile equipment operators","Unskilled agri/fish/forestry", "Unskilled extractive/construction/etc.","Meal prep assistants", "Street vendors","Other"])
        gender = st.selectbox("Jenis Kelamin", ['Male', 'Female'])
        international = st.selectbox("Mahasiswa Internasional", ["Yes", "No"])

    st.markdown("## ⚙️ Kondisi Sosial & Finansial")
    col4, col5, col6 = st.columns(3)
    with col4:
        displaced = st.selectbox("Displaced", ["Yes", "No"])
    with col5:
        special_needs = st.selectbox("Berkebutuhan Khusus", ["Yes", "No"])
    with col6:
        debtor = st.selectbox("Punya Tunggakan?", ["Yes", "No"])

    col7, col8 = st.columns(2)
    with col7:
        tuition_paid = st.selectbox("Pembayaran Lancar?", ["Yes", "No"])
    with col8:
        scholarship = st.selectbox("Penerima Beasiswa", ["Yes", "No"])

    st.markdown("## 📘 Semester 1")
    col9, col10, col11 = st.columns(3)
    with col9:
        cu1_credited = st.number_input("Kredit Diterima (S1)", 0, 50, 5)
        cu1_approved = st.number_input("Disetujui (S1)", 0, 50, 5)
    with col10:
        cu1_enrolled = st.number_input("Mata Kuliah Diambil (S1)", 0, 50, 6)
        cu1_grade = st.number_input("Nilai Rata-rata (S1)", 0.0, 20.0, 12.0)
    with col11:
        cu1_eval = st.number_input("Evaluasi (S1)", 0, 20, 3)
        cu1_no_eval = st.number_input("Tanpa Evaluasi (S1)", 0, 20, 1)

    st.markdown("## 📙 Semester 2")
    col12, col13, col14 = st.columns(3)
    with col12:
        cu2_credited = st.number_input("Kredit Diterima (S2)", 0, 50, 5)
        cu2_approved = st.number_input("Disetujui (S2)", 0, 50, 5)
    with col13:
        cu2_enrolled = st.number_input("Mata Kuliah Diambil (S2)", 0, 50, 6)
        cu2_grade = st.number_input("Nilai Rata-rata (S2)", 0.0, 20.0, 13.0)
    with col14:
        cu2_eval = st.number_input("Evaluasi (S2)", 0, 20, 3)
        cu2_no_eval = st.number_input("Tanpa Evaluasi (S2)", 0, 20, 1)

    st.markdown("---")
    submitted = st.form_submit_button("🔍 Prediksi")

if submitted:
    # Mapping categorical to numeric
    yes_no_map = {"Yes": 1, "No": 0}
    gender_map = {'Male': 1, 'Female': 0}

    prev_qualification_map = {
        "Secondary education": 1,
        "Higher education - bachelor's degree": 2,
        "Higher education - degree": 3,
        "Higher education - master's": 4,
        "Higher education - doctorate": 5,
        "Frequency of higher education": 6,
        "12th year of schooling - not completed": 9,
        "11th year of schooling - not completed": 10,
        "Other - 11th year of schooling": 12,
        "10th year of schooling": 14,
        "10th year of schooling - not completed": 15,
        "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
        "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Professional higher technical course": 42,
        "Higher education - master (2nd cycle)": 43,
        "Other": 0
    }

    marital_map = {
        "Single": 1,
        "Married": 2,
        "Widower": 3,
        "Divorced": 4,
        "Facto Union": 5,
        "Legally Separated": 6,
        "Other": 7
    }

    attendance_map = {
        "Daytime": 1,
        "Evening": 0,
        "Other": 2
    }

    # Mother occupation
    occupation_map_mother = {
        "Student": 0,
        "Legislative/Executive/Directors": 1,
        "Intellectual/Scientific": 2,
        "Technicians": 3,
        "Administrative staff": 4,
        "Services/Security/Sellers": 5,
        "Farmers/Fishers": 6,
        "Industry/Construction": 7,
        "Machine Operators": 8,
        "Unskilled Workers": 9,
        "Armed Forces": 10,
        "Other": 90,
        "(blank)": 99,
        "Health professionals": 122,
        "Teachers": 123,
        "ICT specialists": 125,
        "Intermediate science/engineering technicians": 131,
        "Intermediate health professionals": 132,
        "Legal/social/cultural technicians": 134,
        "Secretaries/data processing": 141,
        "Accounting/financial/registry operators": 143,
        "Other admin support": 144,
        "Personal service workers": 151,
        "Sellers": 152,
        "Personal care workers": 153,
        "Construction workers": 171,
        "Jewelers/artisans/etc.": 173,
        "Food/clothing/woodworking": 175,
        "Cleaning workers": 191,
        "Unskilled agri/fish/forestry": 192,
        "Unskilled extractive/construction/etc.": 193,
        "Meal prep assistants": 194,
        "Unemployed": 196
    }

    # Father occupation
    occupation_map_father = {
        "Student": 0,
        "Legislative/Executive/Directors": 1,
        "Intellectual/Scientific": 2,
        "Technicians": 3,
        "Administrative staff": 4,
        "Services/Security/Sellers": 5,
        "Farmers/Fishers": 6,
        "Industry/Construction": 7,
        "Machine Operators": 8,
        "Unskilled Workers": 9,
        "Armed Forces": 10,
        "Other": 90,
        "(blank)": 99,
        "Armed Forces Officers": 101,
        "Armed Forces Sergeants": 102,
        "Other Armed Forces personnel": 103,
        "Admin/Commercial Directors": 112,
        "Hotel/Catering Directors": 114,
        "Science/Engineering Specialists": 121,
        "Health professionals": 122,
        "Teachers": 123,
        "Finance/Admin Specialists": 124,
        "Intermediate science/engineering technicians": 131,
        "Intermediate health professionals": 132,
        "Legal/social/cultural technicians": 134,
        "ICT technicians": 135,
        "Secretaries/data processing": 141,
        "Accounting/financial/registry operators": 143,
        "Other admin support": 144,
        "Personal service workers": 151,
        "Sellers": 152,
        "Personal care workers": 153,
        "Protection/security personnel": 154,
        "Skilled agricultural producers": 161,
        "Subsistence farmers/fishers": 163,
        "Skilled construction workers": 171,
        "Metalworkers": 172,
        "Electricians": 174,
        "Food/clothing/woodworking": 175,
        "Fixed plant operators": 181,
        "Assembly workers": 182,
        "Drivers and mobile equipment operators": 183,
        "Unskilled agri/fish/forestry": 192,
        "Unskilled extractive/construction/etc.": 193,
        "Meal prep assistants": 194,
        "Street vendors": 195,
        "Unemployed": 196
    }

    application_map = {
        "1st phase - general contingent": 1,
        "Ordinance No. 612/93": 2,
        "1st phase - special contingent (Azores Island)": 5,
        "Holders of other higher courses": 7,
        "Ordinance No. 854-B/99": 10,
        "International student (bachelor)": 15,
        "1st phase - special contingent (Madeira Island)": 16,
        "2nd phase - general contingent": 17,
        "3rd phase - general contingent": 18,
        "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
        "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
        "Over 23 years old": 39,
        "Transfer": 42,
        "Change of course": 43,
        "Technological specialization diploma holders": 44,
        "Change of institution/course": 51,
        "Short cycle diploma holders": 53,
        "Change of institution/course (International)": 57,
        "Other": 0
    }

    course_map = {
        "Biofuel Production Technologies": 33,
        "Animation and Multimedia Design": 171,
        "Social Service (evening attendance)": 8014,
        "Agronomy": 9003,
        "Communication Design": 9070,
        "Veterinary Nursing": 9085,
        "Informatics Engineering": 9119,
        "Equinculture": 9130,
        "Management": 9147,
        "Social Service": 9238,
        "Tourism": 9254,
        "Nursing": 9500,
        "Oral Hygiene": 9556,
        "Advertising and Marketing Management": 9670,
        "Journalism and Communication": 9773,
        "Basic Education": 9853,
        "Management (evening attendance)": 9991,
        "Other": 0
    }


    # Input DataFrame
    input_data = pd.DataFrame([{
        'Marital_status': marital_map[marital_status],
        'Application_mode': application_map[application_mode],
        'Course': course_map[course],
        'Daytime_evening_attendance': attendance_map[attendance],
        'Previous_qualification': prev_qualification_map[prev_qualification],
        'Previous_qualification_grade': prev_qual_grade,
        'Mothers_occupation': occupation_map_mother[mothers_occupation],
        'Fathers_occupation': occupation_map_father[fathers_occupation],
        'Admission_grade': admission_grade,
        'Displaced': yes_no_map[displaced],
        'Educational_special_needs': yes_no_map[special_needs],
        'Debtor': yes_no_map[debtor],
        'Tuition_fees_up_to_date': yes_no_map[tuition_paid],
        'Gender': gender_map[gender],
        'Scholarship_holder': yes_no_map[scholarship],
        'Age_at_enrollment': age,
        'International': yes_no_map[international],
        'Curricular_units_1st_sem_credited': cu1_credited,
        'Curricular_units_1st_sem_enrolled': cu1_enrolled,
        'Curricular_units_1st_sem_evaluations': cu1_eval,
        'Curricular_units_1st_sem_approved': cu1_approved,
        'Curricular_units_1st_sem_grade': cu1_grade,
        'Curricular_units_1st_sem_without_evaluations': cu1_no_eval,
        'Curricular_units_2nd_sem_credited': cu2_credited,
        'Curricular_units_2nd_sem_enrolled': cu2_enrolled,
        'Curricular_units_2nd_sem_evaluations': cu2_eval,
        'Curricular_units_2nd_sem_approved': cu2_approved,
        'Curricular_units_2nd_sem_grade': cu2_grade,
        'Curricular_units_2nd_sem_without_evaluations': cu2_no_eval
    }])

    # Predict
    prediction = model.predict(input_data)[0]
    st.success(f"📌 Status Mahasiswa yang Diprediksi: **{prediction}**")

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)[0]
        st.markdown("### 🔢 Probabilitas:")
        for cls, prob in zip(model.classes_, probabilities):
            st.markdown(f"- **{cls}**: `{prob:.2%}`")
    else:
        st.info("Model tidak mendukung probabilitas.")