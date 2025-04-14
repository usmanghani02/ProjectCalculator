import streamlit as st
import math

# --- Session State Initialization ---
if 'input_expr' not in st.session_state:
    st.session_state.input_expr = '0'
if 'result' not in st.session_state:
    st.session_state.result = ''
if 'kb_input' not in st.session_state:
    st.session_state.kb_input = ''

# --- Expression Evaluation Function ---
def evaluate_expression(expr):
    try:
        expr = expr.replace('^', '**').replace('√', 'math.sqrt')
        expr = expr.replace('π', str(math.pi))
        expr = expr.replace('×', '*').replace('−', '-').replace('＋', '+')
        result = eval(expr, {"_builtins_": None, "math": math})
        return str(result)
    except:
        return "Error"

# --- Button Click Handler ---
def button_click(value):
    if value == 'C':
        st.session_state.input_expr = '0'
        st.session_state.result = ''
        st.session_state.kb_input = ''  # Clear keyboard input as well
    elif value == '=':
        st.session_state.result = evaluate_expression(st.session_state.input_expr)
    elif value == '±':
        if st.session_state.input_expr.startswith('-'):
            st.session_state.input_expr = st.session_state.input_expr[1:]
        elif st.session_state.input_expr != '0':
            st.session_state.input_expr = '-' + st.session_state.input_expr
    elif value == '√':
        st.session_state.input_expr = f"√({st.session_state.input_expr})"
    elif value == '^':
        st.session_state.input_expr += '^'
    else:
        if st.session_state.input_expr in ['0', 'Error']:
            st.session_state.input_expr = value
        else:
            st.session_state.input_expr += value

# --- Page Layout ---
st.set_page_config(page_title="🧮 Enhanced Calculator", layout="centered")
st.markdown("<h2 style='text-align: center;'>🧮 Enhanced Calculator</h2>", unsafe_allow_html=True)

# --- Display Input and Result ---
st.markdown("### ➤ Expression:")
st.text_input("", value=st.session_state.input_expr, key="expression_display", disabled=True, label_visibility="collapsed")

st.markdown("### ➤ Result:")
st.text_input("", value=st.session_state.result, key="result_display", disabled=True, label_visibility="collapsed")

# --- Keyboard Input (Fixed) ---
kb_input = st.text_input(
    label="Or type an expression and press Enter:",
    value=st.session_state.kb_input,
    key="keyboard_input",
    label_visibility="visible",
    placeholder="e.g. 5+5 or √16 or 2^3",
)

# Handle keyboard input
if kb_input and kb_input != st.session_state.kb_input:
    st.session_state.input_expr = kb_input
    st.session_state.result = evaluate_expression(kb_input)
    st.session_state.kb_input = kb_input  # Store the current input
    st.rerun()

# --- Calculator Buttons Layout ---
def create_row(buttons):
    cols = st.columns(len(buttons))
    for col, label in zip(cols, buttons):
        if label:
            col.button(label, on_click=button_click, args=(label,), use_container_width=True)
        else:
            col.markdown(" ")  # Empty placeholder

# Button Grid
create_row(["7", "8", "9", "/", "√"])
create_row(["4", "5", "6", "×", "^"])
create_row(["1", "2", "3", "−", "±"])
create_row(["0", ".", "＋", "=", "C"])

# --- Optional Styling ---
st.markdown("""
<style>
    .stButton>button {
        height: 3em;
        font-size: 1.3em;
        margin: 0.2em;
    }
    .stTextInput>div>input {
        font-size: 1.5em;
        text-align: right;
        background-color: #f3f3f3;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)
