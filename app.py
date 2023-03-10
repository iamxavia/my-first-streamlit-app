!pip install streamlit
!pip install protobuf==3.20.0
%%writefile app.py
import streamlit as st

st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if a==0:
  if b==0:
    kq="Phương trình có vô số nghiệm"
  else:
    kq="Phương trình vô nghiệm"
else:
  kq="Phương trình có 1 nghiệm " + str(-b/a)

if st.button("Giải"):
  st.write(kq)
!streamlit run app.py & npx localtunnel --port 8501