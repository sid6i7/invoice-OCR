# OCR using pytessaract and OpenCV

import re
import cv2
from pdf2image import convert_from_path

import streamlit as st
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = 'add path to Tesseract.exe'

# st.image("bill.png",width=250)
st.title("WHAT'S THE BILL AMOUNT?")


def save_uploadedfile(uploadedfile):
    with open(os.path.join("tempDir", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())


uploaded_pdf = st.file_uploader("Upload Files", type=['pdf'])
if uploaded_pdf is not None:
   file_details = {"FileName": uploaded_pdf.name, "FileType": uploaded_pdf.type}
   save_uploadedfile(uploaded_pdf)
   st.write("file upload successful")

if uploaded_pdf is not None:
    pages = convert_from_path("tempDir\{}".format(uploaded_pdf.name), 500, poppler_path="add path to poppler\bin")

    i = 1
    for page in pages:
        image_name = "invoice_" + str(i) + ".jpg"
        page.save(image_name, "JPEG")
        i = i+1

    img = cv2.imread('invoice_1.jpg', cv2.IMREAD_GRAYSCALE)
    #_, img = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    st.image(img)
    #cv2.imshow('Result', img)
    #cv2.waitKey(0)
    text = pytesseract.image_to_string(img)
    text = text.replace(",", "")
    text = text.replace("$", "")
    print(text)
    x = re.findall("\d+\.\d+", text)
    print(x)
    x = [float(i) for i in x]
    total = max(x)
    print(total)

    st.success("Bill Amount: {}".format(total))
