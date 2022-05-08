# Invoice-OCR
OCR project that can fetch bill amount from a PDF invoice

## Dependencies:

```bash
pip install streamlit, pytesseract, pdf2image, opencv-python
```

Other than these, you also required some pytesseract files and poppler files:


### For Pytesseract
Install it from here: https://github.com/UB-Mannheim/tesseract/wiki

Then replace the pyts_path variable with the path of "pytesseract.exe"

For example, it was this for me:
```python
pyts_path = "C:\Program Files\Tesseract-OCR\Tesseract.exe"
```


### For Poppler
Download it from here: https://blog.alivate.com.au/poppler-windows/
and extract it.

Then replace the poppler_path variable with the path of poppler's bin folder

For example, it was this for me:
```python
poppler_path = r"C:\Program Files\poppler-0.68.0\bin"
```

## Demonstration:
Open powershell window in the same folder where the source-code is present.

Run the following streamlit app using the following command:

```bash
streamlit run .\OCR_streamlit.py
```

Following window will open up:

![image](https://user-images.githubusercontent.com/92942861/167298480-5a674664-eb0d-480f-aa5a-3a59ce076926.png)

Now, simply upload an invoice PDF and it will return the bill amount

![image](https://user-images.githubusercontent.com/92942861/167298732-f5cfefab-3a95-410f-bf8d-90da5f143834.png)

