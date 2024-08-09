import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file):
    return pd.read_csv(file)

def main():
    st.title("Interactive CSV Data Visualization")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Load data
        df = load_data(uploaded_file)
        
        # Display raw data
        st.subheader("Raw Data")
        st.write(df)

        # Select columns for visualization
        st.subheader("Data Visualization")
        columns = df.columns.tolist()
        x_axis = st.selectbox("Select X-axis", options=columns)
        y_axis = st.selectbox("Select Y-axis", options=columns)

        # Create plot
        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)

        # Filtering
        st.subheader("Data Filtering")
        filter_column = st.selectbox("Select column to filter", options=columns)
        unique_values = df[filter_column].unique().tolist()
        selected_values = st.multiselect("Select values", options=unique_values)

        if selected_values:
            filtered_df = df[df[filter_column].isin(selected_values)]
            st.write(filtered_df)

            # Create filtered plot
            fig, ax = plt.subplots()
            ax.scatter(filtered_df[x_axis], filtered_df[y_axis])
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            st.pyplot(fig)

if __name__ == "__main__":
    main()
