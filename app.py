
import streamlit as st
import pymupdf

st.set_page_config(
    page_title="DocuMatch AI",
    page_icon="📄"
)

st.title("📄 DocuMatch AI")
st.subheader("Smart Business Document Reconciliation")

st.write("Upload a PDF to extract its text.")

uploaded_file = st.file_uploader(
    "Choose a PDF document",
    type=["pdf"]
)

if uploaded_file is not None:
    try:
        pdf_bytes = uploaded_file.getvalue()

        with pymupdf.open(
    stream=pdf_bytes,
    filetype="pdf"
) as pdf:
            extracted_text = "\n".join(
                page.get_text()
                for page in pdf
            )

        if extracted_text.strip():
            st.success("Text extracted successfully!")
            st.text_area(
                "Extracted PDF Text",
                extracted_text,
                height=350
            )
        else:
            st.warning(
                "No selectable text found in this PDF."
            )

    except Exception:
        st.error(
            "Could not read this PDF. Try another PDF."
        )
