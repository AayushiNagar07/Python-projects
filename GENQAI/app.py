import streamlit as st
import json

# ---------------- SESSION INIT ----------------
if "user" not in st.session_state:
    st.session_state.user = None


# ---------------- LOGIN ----------------
def login_screen():
    st.header("Login to GENQAI")

    if st.button("Log in with Google"):
        st.session_state.user = {
            "email": "aayushinagar385@gmail.com",
            "name": "Aayushi Nagar"
        }
        st.success("Logged in successfully!")
        st.rerun()

    st.info("Please login to continue.")


# ---------------- ROUTING ----------------
if st.session_state.user is None:
    login_screen()
    st.stop()


# ---------------- DASHBOARD ----------------
st.title("GENQAI")
st.write("Welcome:", st.session_state.user["email"])

st.subheader("Question Paper Configuration")

class_selected = st.selectbox(
    "Select Class",
    ["Class 7", "Class 8"]
)

subject_selected = st.selectbox(
    "Select Subject",
    ["Maths", "Hindi", "English"]
)

type_selected = st.selectbox(
    "Select Exam Type",
    ["PT-1", "PT-2", "Half Yearly", "Final"]
)

units = st.multiselect(
    "Select Units",
    ["Unit 1", "Unit 2", "Unit 3"]
)


# ---------------- GENERATE PAPER ----------------
if st.button("Generate Question Paper"):

    if not units:
        st.error("Please select at least one unit")

    else:
        try:
            with open("data/question_bank.json", "r", encoding="utf-8") as f:
                question_bank = json.load(f)

            selected_questions = []

            for unit in units:
                if (
                    class_selected in question_bank
                    and subject_selected in question_bank[class_selected]
                    and unit in question_bank[class_selected][subject_selected]
                ):
                    selected_questions.extend(
                        question_bank[class_selected][subject_selected][unit]
                    )

            st.success("Question Paper Generated")

            st.write("### Configuration")
            st.write("Class:", class_selected)
            st.write("Subject:", subject_selected)
            st.write("Exam Type:", type_selected)
            st.write("Units:", ", ".join(units))

            st.write("### Questions")

            if selected_questions:
                for i, question in enumerate(selected_questions, start=1):
                    st.write(f"{i}. {question}")
            else:
                st.warning("No questions found for the selected criteria.")

        except FileNotFoundError:
            st.error(
                "question_bank.json not found. Please create data/question_bank.json"
            )

        except json.JSONDecodeError:
            st.error("Invalid JSON format in question_bank.json")

        except Exception as e:
            st.error(f"Unexpected error: {e}")


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.write("Logged in as:")
    st.write(st.session_state.user["email"])

    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()