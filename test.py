from multiprocessing.resource_sharer import stop
from this import d
import streamlit as st


def calc_quantity(inputs):
    try:
        return inputs[2] / (inputs[0] - inputs[1])
    except:
        st.write("Calculation error!")
        return -1



def num_field(label, columns=None, **input_params):
    c1, c2,c3, c4, c5 = st.columns(columns or [1, 1, 1, 1, 1])

    # Display field name with some alignment
    c1.markdown("#")
    c1.markdown(label)

    # Sets a default key parameter to avoid duplicate key errors
    input_params.setdefault("key", label)

    # Forward text input parameters
    return c2.number_input(label=label, **input_params, label_visibility='hidden')

def app():
    st.write("""# Risk Calculator""")

    # Take Inputs 
    col1,col2 = st.columns([1,1])

    # with col1:
    stop_loss = num_field('Stop Loss:',columns=None, step=1)
    # stop_loss = st.number_input('Stop Loss')
    # st.write('SL', stop_loss)


    entry = num_field('Entry:',columns=None, step=1)
    # entry = st.number_input('Entry')
    # st.write('Entry ', entry)

    risk = num_field('Risk:',columns=None,step=1)
    # risk = st.number_input('Risk')
    # st.write('Risk', risk)

    inputs = [stop_loss, entry, risk]


    quantity = calc_quantity(inputs)

    c1, c2 = st.columns([1, 4])

    calculate = c1.button(label='Calculate')
    clear = c2.button(label='Clear')
        
    if calculate:
            st.metric(label="Quantity:", value=quantity)
    
    if clear:
            st.metric(label="Quantity:", value=0)
            # stop_loss.


    # with st.form("my_form"):
    #     stop_loss = num_field('Stop Loss:',columns=None, step=1)
    #     entry = num_field('Entry:',columns=None, step=1)
    #     risk = num_field('Risk:',columns=None,step=1)

    #     st.write("Inside the form")

    #     # Every form must have a submit button.
    #     quantity = calc_quantity(inputs)

    #     submitted = st.form_submit_button("Submit")
    #     if submitted:
    #         st.metric(label="Quantity:", value=quantity)
    #         # st.write("slider", slider_val, "checkbox", checkbox_val)




    


# def app():
#     init()


def main():
    app()


main()


# risk / (sl-entry)