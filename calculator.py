import matlab.engine
import streamlit as st

eng = matlab.engine.start_matlab()

st.set_page_config(
    page_title="Calculator",
    initial_sidebar_state="expanded",
)

st.title('Calculator')
st.markdown("---")

inp1 = st.number_input(label="Enter Number 1")
option = st.selectbox('Select Operator', ('+', '-', 'x', '/'))
inp2 = st.number_input(label="Enter Number 2")

ans = 0

if option == '+':
    ans = eng.add(inp1, inp2, nargout=1)
elif option == '-':
    ans = eng.sub(inp1, inp2, nargout=1)
elif option == 'x':
    ans = eng.mul(inp1, inp2, nargout=1)
elif option == '/':
    if inp2 != 0:
        ans = eng.div(inp1, inp2, nargout=1)
    else:
        ans = "Cannot Divide By Zero"

st.markdown("### Answer = " + str(ans))
# st.text(str(ans))
