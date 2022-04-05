import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレグロスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')
else:
    right_column.write('k')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1への回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2への回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3への回答')

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option,'です。'

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は、', text,'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 25)
# 'あなたの調子は、', condition,'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='sample image', use_column_width=True)
