import streamlit as st
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

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
user = st.session_state.user

st.title("GENQAI")
st.write("Welcome:", user["email"])

st.subheader("Question Paper Configuration")

class_selected = st.selectbox("Select Class", ["Class 7", "Class 8"])
subject_selected = st.selectbox("Select Subject", ["Maths", "Hindi", "English"])
type_selected = st.selectbox("Select Exam Type", ["PT-1", "PT-2", "Half Yearly", "Final"])
units = st.multiselect("Select Units", ["Unit 1", "Unit 2", "Unit 3"])


# ---------------- PDF FUNCTION ----------------
def generate_pdf(class_selected, subject_selected, type_selected, units, selected_questions, total_marks):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    y = height - 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "GENQAI QUESTION PAPER")

    y -= 30
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, f"Class: {class_selected}")
    y -= 20
    pdf.drawString(50, y, f"Subject: {subject_selected}")
    y -= 20
    pdf.drawString(50, y, f"Exam Type: {type_selected}")
    y -= 20
    pdf.drawString(50, y, f"Units: {', '.join(units)}")
    y -= 20
    pdf.drawString(50, y, f"Total Marks: {total_marks}")

    y -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Questions:")

    y -= 30
    pdf.setFont("Helvetica", 11)

    for i, q in enumerate(selected_questions, start=1):
        text = f"Q{i}. {q['question']} ({q['marks']} Marks)"
        pdf.drawString(50, y, text[:90])  # prevent overflow
        y -= 20

        if y < 50:
            pdf.showPage()
            y = height - 50

    pdf.save()
    buffer.seek(0)
    return buffer


# ---------------- GENERATE PAPER ----------------
if st.button("Generate Question Paper"):

    if not units:
        st.error("Please select at least one unit")

    else:
        try:
            with open("data/question_bank.json", "r", encoding="utf-8") as f:
                question_bank = json.load(f)

            # SAFE DATA LOADING
            selected_questions = []

            for unit in units:
                selected_questions.extend(
                    question_bank.get(class_selected, {})
                                 .get(subject_selected, {})
                                 .get(unit, [])
                )

            if not selected_questions:
                st.warning("No questions found for selected options")
                st.stop()

            total_marks = sum(q["marks"] for q in selected_questions)

            st.success("Question Paper Generated")

            st.markdown("---")
            st.subheader(f"{class_selected} - {subject_selected}")
            st.write(f"Exam: {type_selected}")
            st.write(f"Units: {', '.join(units)}")
            st.write(f"Total Marks: {total_marks}")
            st.markdown("---")

            st.write("### Questions")

            for i, q in enumerate(selected_questions, start=1):
                st.write(f"Q{i}. {q['question']} ({q['marks']} Marks)")

            # ---------------- PDF GENERATION ----------------
            pdf_buffer = generate_pdf(
                class_selected,
                subject_selected,
                type_selected,
                units,
                selected_questions,
                total_marks
            )

            st.download_button(
                label="📄 Download Question Paper PDF",
                data=pdf_buffer,
                file_name="GenQAI_Question_Paper.pdf",
                mime="application/pdf"
            )

        except FileNotFoundError:
            st.error("question_bank.json not found in /data folder")

        except json.JSONDecodeError:
            st.error("Invalid JSON format in question_bank.json")

        except Exception as e:
            st.error(f"Unexpected error: {e}")


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.write("Logged in as:")

    if st.session_state.user:
        st.write(user["email"])

    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()