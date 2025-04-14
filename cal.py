import streamlit as st
import math

# --- Session State Initialization ---
if 'display' not in st.session_state:
    st.session_state.display = '0'

# --- Expression Evaluation Function ---
def evaluate_expression(expr):
    try:
        expr = expr.replace('^', '**').replace('√', 'math.sqrt')
        result = eval(expr, {"__builtins__": None, "math": math})
        return str(result)
    except:
        return "Error"

# --- Button Click Handler ---
def button_click(value):
    if value == 'C':
        st.session_state.display = '0'
    elif value == '=':
        st.session_state.display = evaluate_expression(st.session_state.display)
    elif value == '±':
        if st.session_state.display.startswith('-'):
            st.session_state.display = st.session_state.display[1:]
        elif st.session_state.display != '0':
            st.session_state.display = '-' + st.session_state.display
    elif value == '√':
        st.session_state.display = f"√{st.session_state.display}"
    elif value == '^':
        st.session_state.display += '^'
    else:
        if st.session_state.display in ['0', 'Error']:
            st.session_state.display = value
        else:
            st.session_state.display += value

# --- Page Layout Config ---
st.set_page_config(page_title="Advanced Calculator", layout="centered")
st.markdown("## 🧮 **Advanced Calculator**")
st.markdown("Type directly using your keyboard (e.g. `5+5`, `√16`, `2^3`) and press **Enter**")

# --- Keyboard Input with Live Evaluation ---
kb_input = st.text_input(
    label="Type your expression and press Enter:",
    value='',
    key="keyboard_input",
    label_visibility="collapsed",
    placeholder="e.g. 5+5 or √16 or 2^3",
)

if kb_input:
    result = evaluate_expression(kb_input)
    st.session_state.display = result

# --- Display the Result ---
st.markdown("### ➤ Result:")
st.text_input("", value=st.session_state.display, key="calc_display", disabled=True, label_visibility="collapsed")

# --- Calculator Buttons Grid ---
col1, col2, col3, col4, col5 = st.columns(5)

# Row 1
with col1: st.button("7", on_click=button_click, args=('7',), use_container_width=True)
with col2: st.button("8", on_click=button_click, args=('8',), use_container_width=True)
with col3: st.button("9", on_click=button_click, args=('9',), use_container_width=True)
with col4: st.button("/", on_click=button_click, args=('/',), use_container_width=True)
with col5: st.button("√", on_click=button_click, args=('√',), use_container_width=True)

# Row 2
with col1: st.button("4", on_click=button_click, args=('4',), use_container_width=True)
with col2: st.button("5", on_click=button_click, args=('5',), use_container_width=True)
with col3: st.button("6", on_click=button_click, args=('6',), use_container_width=True)
with col4: st.button(".*", on_click=button_click, args=('*',), use_container_width=True)
with col5: st.button("^", on_click=button_click, args=('^',), use_container_width=True)

# Row 3
with col1: st.button("1", on_click=button_click, args=('1',), use_container_width=True)
with col2: st.button("2", on_click=button_click, args=('2',), use_container_width=True)
with col3: st.button("3", on_click=button_click, args=('3',), use_container_width=True)
with col4: st.button((".-"), on_click=button_click, args=('-',), use_container_width=True)
with col5: st.button("±", on_click=button_click, args=('±',), use_container_width=True)

# Row 4
with col1: st.button("0", on_click=button_click, args=('0',), use_container_width=True)
with col2: st.button(".", on_click=button_click, args=('.',), use_container_width=True)
with col3: st.button((".+"), on_click=button_click, args=('+',), use_container_width=True)
with col4: st.button("=", on_click=button_click, args=('=',), use_container_width=True)
with col5: st.button("C", on_click=button_click, args=('C',), use_container_width=True)
