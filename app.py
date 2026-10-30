
import streamlit as st

st.set_page_config(
    page_title="DocuMatch AI",
    page_icon="📄"
)

st.title("📄 DocuMatch AI")
st.subheader("Smart Business Document Reconciliation")

st.write(
    "Upload and compare business documents "
    "to identify mismatches and missing information."
)

st.info("Welcome to DocuMatch AI!")

st.header("Planned Features")
st.write("- Purchase order and invoice comparison")
st.write("- Delivery quantity validation")
st.write("- Missing document detection")
st.write("- AI-powered supplier email drafting")
