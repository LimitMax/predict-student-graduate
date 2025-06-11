import streamlit as st
import pandas as pd
import joblib
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Student Academic Dashboard", layout="wide")

with st.sidebar:
    menu = option_menu(
        menu_title="📁 Main Menu",
        options=["Dashboard", "Prediction"],
        icons=["house", "graph-up"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "10px",
                "background": "linear-gradient(135deg, #1e3c72, #2a5298)",  # deep blue gradient
                "border-radius": "12px",
                "box-shadow": "0 4px 12px rgba(0,0,0,0.2)"
            },
            "icon": {
                "color": "#00ffff",  # aqua
                "font-size": "22px"
            },
            "nav-link": {
                "font-size": "16px",
                "color": "#ecf0f1",
                "padding": "10px 15px",
                "margin": "5px 0",
                "border-radius": "8px",
                "transition": "all 0.3s ease"
            },
            "nav-link:hover": {
                "background-color": "#3a6073",  # smooth hover effect
                "color": "#ffffff"
            },
            "nav-link-selected": {
                "background": "linear-gradient(90deg, #00c9ff, #92fe9d)",  # aqua to light green
                "color": "#1e1e2f",
                "font-weight": "bold",
                "box-shadow": "0 0 8px rgba(0, 201, 255, 0.6)"
            }
        }
    )

# Halaman Dashboard
if menu == "Dashboard":
    st.markdown("<h1 style='text-align: center;'>📊 Student Academic Dashboard</h1>", unsafe_allow_html=True)

    tableau_code = """
    <div class="tableauPlaceholder" id="viz1749645475354" style="position: relative">
        <noscript>
            <a href="#">
            <img alt="Dashboard 1" src="https://public.tableau.com/static/images/St/StudentAcademicDashboard/Dashboard1/1_rss.png" style="border: none" />
            </a>
        </noscript>
        <object class="tableauViz" style="display:none;">
            <param name="host_url" value="https%3A%2F%2Fpublic.tableau.com%2F" />
            <param name="embed_code_version" value="3" />
            <param name="site_root" value="" />
            <param name="name" value="StudentAcademicDashboard/Dashboard1" />
            <param name="tabs" value="no" />
            <param name="toolbar" value="yes" />
            <param name="static_image" value="https://public.tableau.com/static/images/St/StudentAcademicDashboard/Dashboard1/1.png" />
            <param name="animate_transition" value="yes" />
            <param name="display_static_image" value="yes" />
            <param name="display_spinner" value="yes" />
            <param name="display_overlay" value="yes" />
            <param name="display_count" value="yes" />
            <param name="language" value="en-US" />
        </object>
    </div>

    <script type="text/javascript">
        var divElement = document.getElementById('viz1749645475354');
        var vizElement = divElement.getElementsByTagName('object')[0];

        if (divElement.offsetWidth > 800) {
            vizElement.style.minWidth = '1200px';
            vizElement.style.maxWidth = '100%';
            vizElement.style.minHeight = '827px';
            vizElement.style.maxHeight = (divElement.offsetWidth * 0.75) + 'px';
        } else if (divElement.offsetWidth > 500) {
            vizElement.style.minWidth = '1200px';
            vizElement.style.maxWidth = '100%';
            vizElement.style.minHeight = '827px';
            vizElement.style.maxHeight = (divElement.offsetWidth * 0.75) + 'px';
        } else {
            vizElement.style.width = '100%';
            vizElement.style.height = '4027px';
        }

        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>

    """

    # Render full-width Tableau dashboard with height proportional to screen
    st.components.v1.html(tableau_code, height=900, scrolling=True)


# Halaman Prediction
elif menu == "Prediction":
    # Load model
    model = joblib.load("model/model_rf.pkl")

    st.title("🎓 Prediction of Student Status")
    st.markdown("Fill in the student data to predict academic status based on historical data.")

    with st.form("student_form"):
        st.subheader("📄 Personal & Academic information")
        col1, col2, col3 = st.columns(3)

        with col1:
            marital_status = st.selectbox("Marital Status", ["Select", 'Single', 'Married', 'Widower', 'Divorced','Facto Union','Legally Separated', 'Other'])
            marital_status_placeholder = st.empty()
            marital_status_other = marital_status_placeholder.text_input("↳ Other Marital Status") if marital_status == 'Other' else None

            application_mode = st.selectbox("Application Mode", ["Select", '1st phase - general contingent', 'Ordinance No. 612/93','1st phase - special contingent (Azores Island)','Holders of other higher courses','Ordinance No. 854-B/99','International student (bachelor)','1st phase - special contingent (Madeira Island)','2nd phase - general contingent','3rd phase - general contingent','Ordinance No. 533-A/99, item b2) (Different Plan)','Ordinance No. 533-A/99, item b3 (Other Institution)','Over 23 years old','Transfer','Change of course','Technological specialization diploma holders','Change of institution/course','Short cycle diploma holders','Change of institution/course (International)', 'Other'])
            course = st.selectbox("Study Program", ["Select", 'Biofuel Production Technologies','Animation and Multimedia Design','Social Service (evening attendance)','Agronomy','Communication Design','Veterinary Nursing','Informatics Engineering','Equinculture','Management','Social Service','Tourism','Nursing','Oral Hygiene','Advertising and Marketing Management','Journalism and Communication','Basic Education','Management (evening attendance)', 'Other'])
            attendance = st.selectbox("Attendance Time", ["Select", 'Daytime', 'Evening', 'Other'])

        with col2:
            prev_qualification = st.selectbox("Prev Qualification", ["Select", "Secondary education","Higher education - bachelor's degree","Higher education - degree","Higher education - master's","Higher education - doctorate","Frequency of higher education","12th year of schooling - not completed", "11th year of schooling - not completed","Other - 11th year of schooling","10th year of schooling","10th year of schooling - not completed","Basic education 3rd cycle (9th/10th/11th year) or equiv.","Basic education 2nd cycle (6th/7th/8th year) or equiv.","Technological specialization course","Higher education - degree (1st cycle)","Professional higher technical course","Higher education - master (2nd cycle)", "Other"])
            prev_qual_grade = st.number_input("Prev Qualification Grade", min_value=0.0, max_value=200.0, value=0.0)
            admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=200.0, value=0.0)
            age = st.number_input("Age", min_value=0, max_value=80, value=0)

        with col3:
            mothers_occupation = st.selectbox("Mother's Occupation", ["Select", 'Unemployed', "Student", "Legislative/Executive/Directors", "Intellectual/Scientific","Technicians", "Administrative staff", "Services/Security/Sellers","Farmers/Fishers", "Industry/Construction", "Machine Operators","Unskilled Workers", "Armed Forces", "Other", "(blank)","Health professionals", "Teachers", "ICT specialists", "Intermediate science/engineering technicians", "Intermediate health professionals","Legal/social/cultural technicians", "Secretaries/data processing","Accounting/financial/registry operators", "Other admin support","Personal service workers","Sellers", "Personal care workers","Construction workers", "Jewelers/artisans/etc.", "Food/clothing/woodworking","Cleaning workers", "Unskilled agri/fish/forestry", "Unskilled extractive/construction/etc.", "Meal prep assistants", "Other"])
            fathers_occupation = st.selectbox("Father's Occupation", ["Select", 'Unemployed', "Student", "Legislative/Executive/Directors", "Intellectual/Scientific","Technicians","Administrative staff", "Services/Security/Sellers", "Farmers/Fishers","Industry/Construction", "Machine Operators", "Unskilled Workers","Armed Forces", "Other", "(blank)","Armed Forces Officers","Armed Forces Sergeants", "Other Armed Forces personnel","Admin/Commercial Directors", "Hotel/Catering Directors", "Science/Engineering Specialists","Health professionals", "Teachers", "Finance/Admin Specialists","Intermediate science/engineering technicians", "Intermediate health professionals","Legal/social/cultural technicians", "ICT technicians","Secretaries/data processing","Accounting/financial/registry operators", "Other admin support","Personal service workers", "Sellers", "Personal care workers","Protection/security personnel", "Skilled agricultural producers","Subsistence farmers/fishers", "Skilled construction workers","Metalworkers", "Electricians","Food/clothing/woodworking","Fixed plant operators", "Assembly workers", "Drivers and mobile equipment operators","Unskilled agri/fish/forestry", "Unskilled extractive/construction/etc.","Meal prep assistants", "Street vendors","Other"])
            gender = st.selectbox("Gender", ["Select", 'Male', 'Female'])
            international = st.selectbox("International Student", ["Select", "Yes", "No"])

        st.markdown("## ⚙️ Social & Financial Conditions")
        col4, col5, col6 = st.columns(3)
        with col4:
            displaced = st.selectbox("Displaced", ["Select", "Yes", "No"])
        with col5:
            special_needs = st.selectbox("Special Needs", ["Select", "Yes", "No"])
        with col6:
            debtor = st.selectbox("Debtor", ["Select", "Yes", "No"])

        col7, col8 = st.columns(2)
        with col7:
            tuition_paid = st.selectbox("Tuition Paid", ["Select", "Yes", "No"])
        with col8:
            scholarship = st.selectbox("Scholarship Recipient", ["Select", "Yes", "No"])

        st.markdown("## 📘 Semester 1")
        col9, col10, col11 = st.columns(3)
        with col9:
            cu1_credited = st.number_input("Credits Earned (S1)", min_value=0, max_value=50, value=0)
            cu1_approved = st.number_input("Approved (S1)", min_value=0, max_value=50, value=0)
        with col10:
            cu1_enrolled = st.number_input("Courses Enrolled (S1)", min_value=0, max_value=50, value=0)
            cu1_grade = st.number_input("Average Grade (S1)", min_value=0.0, max_value=100.0, value=0.0)
        with col11:
            cu1_eval = st.number_input("Evaluation (S1)", min_value=0, max_value=20, value=0)
            cu1_no_eval = st.number_input("Without Evaluation (S1)", min_value=0, max_value=20, value=0)

        st.markdown("## 📙 Semester 2")
        col12, col13, col14 = st.columns(3)
        with col12:
            cu2_credited = st.number_input("Credits Earned (S2)", min_value=0, max_value=50, value=0)
            cu2_approved = st.number_input("Approved (S2)", min_value=0, max_value=50, value=0)
        with col13:
            cu2_enrolled = st.number_input("Courses Enrolled (S2)", min_value=0, max_value=50, value=0)
            cu2_grade = st.number_input("Average Grade (S2)", min_value=0.0, max_value=100.0, value=0.0)
        with col14:
            cu2_eval = st.number_input("Evaluation (S2)", min_value=0, max_value=20, value=0)
            cu2_no_eval = st.number_input("Without Evaluation (S2)", min_value=0, max_value=20, value=0)

        st.markdown("---")
        submitted = st.form_submit_button("🔍 Prediction")

    if submitted:
        if "Select" in [marital_status,application_mode,course,attendance,prev_qualification, mothers_occupation,fathers_occupation,gender,international,displaced,special_needs,debtor,tuition_paid,scholarship]:
            st.warning("⚠️ Please complete all data first.")
            st.snow()
        else:
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
            st.success(f"📌 Predicted Student Status: **{prediction}**")

            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba(input_data)[0]
                st.markdown("### 🔢 Probabilities:")
                for cls, prob in zip(model.classes_, probabilities):
                    st.markdown(f"- **{cls}**: `{prob:.2%}`")

                st.balloons()
                st.success("🎉 Prediction complete!")
            else:
                st.info("Model does not support probabilities.")
                st.snow()