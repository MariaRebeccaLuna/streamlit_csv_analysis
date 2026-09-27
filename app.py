import streamlit as st
import pandas as pd

st.title("Min dataanalys")

st.write("Ladda upp en CSV-fil för att analysera datan.")

uploaded_file = st.file_uploader(
    "Välj en CSV-fil",
    type="csv"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Filtrera data")

    products = ["Alla produkter"] + sorted(df["Product"].unique().tolist())

    selected_product = st.selectbox(
        "Välj produkt",
        products
    )

    if selected_product == "Alla produkter":
        filtered_df = df
    else:
        filtered_df = df[df["Product"] == selected_product]

    st.write("### Sammanfattning")

    number_of_rows = df.shape[0]
    number_of_columns = df.shape[1]
    total_sales = df["Sales"].sum()

    col1, col2, col3 = st.columns(3)

    col1.metric("Antal rader:", number_of_rows)
    col2.metric("Anntal kolumner:", number_of_columns)
    col3.metric("Total försäljning:", f"{total_sales:,} kr")

    st.write("### Försäljning per produkt")
    
    sales_by_product = filtered_df.groupby("Product")["Sales"].sum()
        
    st.bar_chart(sales_by_product)

    st.write("### Datan")
    st.dataframe(filtered_df)
    