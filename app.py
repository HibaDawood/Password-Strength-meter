import streamlit as st
import string
import base64
import random
import re

#page Title
st.title("🔐 Password Strength Meter")
st.markdown("🔐 Test your password strength! Strengthen it with our tips if it is weak. 💪✨")

# Custom CSS to style the input field
st.markdown(
    """
    <style>
        
        input[type="text"], 
        input[type="number"], 
        input[type="password"], 
        textarea {
        background-color: #cce0ff !important; 
        color: #000000 !important;  
        border: 2px solid #007bff !important; 
        border-radius: 5px !important; 
        padding: 8px !important;
        }
        ::placeholder {
            color: gray !important;
        }
         h1, h2, h3, p, span {
            color: black !important;
        }
        div.stButton > button {
        background-color: #205781;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 20px;
    }
       div.stButton > button:hover {
        background-color: #205786; 
        color: white;
        cursor: pointer;
        border: 1px solid #000000
    }
    </style>
    """,
    unsafe_allow_html=True
)

def generate_password(length):
    characters = string.digits + string.ascii_letters + "@#$%^&*"
    return "".join(random.choice(characters) for i in range(length))

password_length = st.number_input("Enter the length of password", min_value=8, max_value=20, value=10)
if st.button("Generate Password"):
    password = generate_password(password_length)
    st.success(f"{password}")


def check_password_strength(password):
    score = 0
    common_password = ["12345678", "pakistan123", "china321", "password", "abc789"]
    if password in common_password:
        return "❌ This password is easily guessed. Try a stronger and more unique one.", "Weak" 
    
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🟣 Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and (r"[a-z]", password):
        score += 1
    else:
        feedback.append("🟣 Include both uppercase and lowercase letters.")

    if re.search(r"\d", password) and (r"[a-z]", password):
        score += 1
    else:
        feedback.append("🟣 Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🟣 Include at least one special character (!@#$%^&*).")

    if score == 4:
        return "💪🏻✅ Strong Password!", "Strong"
    elif score == 3:
        return "⚠ Moderate Password - Consider adding more security features.", "Moderate"
    else:
        return "\n".join(feedback), "Weak"

check_password = st.text_input("Enter your password", type="password")
if st.button("Check Strength"):
    if check_password:
       result, Strength =  check_password_strength(check_password)
       if Strength == "Strong":
           st.success(result)
           st.snow()
       elif Strength == "Moderate":
           st.warning(result)
       else:
           st.error("Weak Password - Improve it using these tips:")
           for tip in result.split("\n"):
               st.write(tip)
    else:
        st.warning("Please enter a password")

def set_bg_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()
    return encoded_image  

encoded_image = set_bg_image("images/image.png")


st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
