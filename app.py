import streamlit as st
import pandas as pd
import pickle



# Cache the model so it loads only once
@st.cache_resource
def load_model():
   with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)
   return model

def main():
    # Set page configuration
    st.set_page_config(page_title="Startup Profit Predictor", layout="centered")
    
    # App Title and Description
    st.title("Startup Profit Predictor")
    st.markdown("""
    This app predicts the profit for a startup based on its spending in R&D, Administration, and Marketing, 
    as well as the state where it operates. Adjust the inputs using the sidebar and click **Predict Profit** 
    to see the forecast.
    """)

    # Sidebar for User Inputs
    st.sidebar.header("Input Parameters")
    
    rd_spend = st.sidebar.number_input("R&D Spend", min_value=0.0, value=150000.0, step=1000.0, format="%.2f")
    admin = st.sidebar.number_input("Administration", min_value=0.0, value=120000.0, step=1000.0, format="%.2f")
    marketing = st.sidebar.number_input("Marketing Spend", min_value=0.0, value=300000.0, step=1000.0, format="%.2f")
    state = st.sidebar.selectbox("State", options=["New York", "California", "Florida"])
    
    # Load the saved model
    model = load_model()

    # Prediction Trigger
    if st.sidebar.button("Predict Profit"):
        # Create a DataFrame from user inputs
        input_data = pd.DataFrame({
            'R&D Spend': [rd_spend],
            'Administration': [admin],
            'Marketing Spend': [marketing],
            'State': [state]
        })
        
        try:
            # Generate prediction using the loaded model
            prediction = model.predict(input_data)
            st.success(f"Predicted Profit: ${prediction[0]:,.2f}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

if __name__ == '__main__':
    main()







