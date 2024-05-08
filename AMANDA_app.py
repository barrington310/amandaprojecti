!pip install streamlit
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
# Load the saved model
loaded_model = joblib.load('random_forest_model.joblib')
# Load the pre-trained model
clf = joblib.load('random_forest_model.joblib')

# Load the ColumnTransformer for encoding
column_trans = ColumnTransformer(
    [('onehot', OneHotEncoder(), ['Activity', 'Department', 'cloud'])],
    remainder='passthrough'
)
def main():
    st.title("Security Level Checker")
    st.write("Upload a CSV file to check the security levels.")

    # File Upload
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the uploaded file
        data = pd.read_csv(uploaded_file)

        # Preprocess the data
        X_encoded = column_trans.transform(data)

        # Make predictions
        predictions = clf.predict(X_encoded)

        # Display the predictions
        st.write("Predictions:")
        for prediction in predictions:
            if prediction == 3:
                st.write("Normal (Security Level 3)")
            elif prediction == 2:
                st.write("Intrusion Detected (Security Level 2)")
            else:
                st.write("Unknown Security Level")
if __name__ == "__main__":
    main()
