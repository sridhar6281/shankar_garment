import streamlit as st
import pandas as pd

# Set Page Title
st.set_page_config(page_title="Shankar Garments Billing", layout="wide")

# App Heading
st.markdown("<h1 style='text-align: center;'>SHANKAR GARMENTS</h1>", unsafe_allow_html=True)
st.markdown("---")

# Initialize totals
grand_total_pieces = 0
grand_total_amount = 0

# Create Header Row for the Table
cols = st.columns([1, 3, 2, 2, 2, 2])
cols[0].write("**S.No**")
cols[1].write("**Name**")
cols[2].write("**Pieces (Rate: 60)**")
cols[3].write("**Pieces (Rate: 64)**")
cols[4].write("**Total Pieces**")
cols[5].write("**Total Amount**")

# Create 10 rows for 10 members
for i in range(1, 11):
    row_cols = st.columns([1, 3, 2, 2, 2, 2])
    
    # S.No
    row_cols[0].write(f"{i}")
    
    # Name Input
    name = row_cols[1].text_input(f"Name {i}", label_visibility="collapsed", key=f"name_{i}")
    
    # Pieces @ 60 Input
    p60 = row_cols[2].number_input(f"60_{i}", min_value=0, step=1, label_visibility="collapsed", key=f"p60_{i}")
    
    # Pieces @ 64 Input
    p64 = row_cols[3].number_input(f"64_{i}", min_value=0, step=1, label_visibility="collapsed", key=f"p64_{i}")
    
    # Row Calculations
    row_total_pieces = p60 + p64
    row_total_amount = (p60 * 60) + (p64 * 64)
    
    # Display Row Totals
    row_cols[4].info(f"{row_total_pieces}")
    row_cols[5].success(f"₹{row_total_amount}")
    
    # Add to Grand Totals
    grand_total_pieces += row_total_pieces
    grand_total_amount += row_total_amount

st.markdown("---")

# Grand Total Section
final_cols = st.columns([1, 3, 2, 2, 2, 2])
final_cols[3].markdown("### GRAND TOTAL:")
final_cols[4].markdown(f"### {grand_total_pieces}")
final_cols[5].markdown(f"### ₹{grand_total_amount}")

# Simple Print Button (Browser Default)
if st.button("Ready to Print?"):
    st.write("Press Ctrl+P (or Cmd+P on Mac) to save this as a PDF receipt.")