import streamlit as st

# Page Setup
st.set_page_config(page_title="Shankar Garments Billing", layout="wide")
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>SHANKAR GARMENTS</h1>", unsafe_allow_phtml=True)
st.markdown("---")

# Header Labels
h_cols = st.columns([1, 3, 3, 3, 2, 2])
h_cols[0].write("**S.No**")
h_cols[1].write("**Customer/Item Name**")
h_cols[2].write("**Rate 60 Math**")
h_cols[3].write("**Rate 64 Math**")
h_cols[4].write("**Total Pieces**")
h_cols[5].write("**Total Amount**")

grand_pieces = 0
grand_amount = 0

# 10 Rows for 10 Members
for i in range(1, 11):
    r = st.columns([1, 3, 3, 3, 2, 2])
    
    # S.No
    r[0].write(f"**{i}**")
    
    # Name
    name = r[1].text_input(f"Name", key=f"n{i}", label_visibility="collapsed")
    
    # Rate 60 Column (Math view)
    p60 = r[2].number_input(f"P60_{i}", min_value=0, step=1, key=f"p60_{i}", label_visibility="collapsed")
    amt60 = p60 * 60
    if p60 > 0:
        r[2].caption(f"Calculation: {p60} × 60 = ₹{amt60}")

    # Rate 64 Column (Math view)
    p64 = r[3].number_input(f"P64_{i}", min_value=0, step=1, key=f"p64_{i}", label_visibility="collapsed")
    amt64 = p64 * 64
    if p64 > 0:
        r[3].caption(f"Calculation: {p64} × 64 = ₹{amt64}")

    # Total Pieces (60 pieces + 64 pieces)
    row_pieces = p60 + p64
    r[4].info(f"{row_pieces}")

    # Total Amount (60 total + 64 total)
    row_amt = amt60 + amt64
    r[5].success(f"₹{row_amt}")

    # Totals for the bottom
    grand_pieces += row_pieces
    grand_amount += row_amt

st.markdown("---")

# Grand Totals at the bottom
f_cols = st.columns([1, 3, 3, 3, 2, 2])
f_cols[3].markdown("### GRAND TOTAL:")
f_cols[4].markdown(f"### {grand_pieces}")
f_cols[5].markdown(f"### ₹{grand_amount}")

if st.button("Clear All Data"):
    st.cache_data.clear()
    st.rerun()
