import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page1_summary import page1_summary_body
from app_pages.page2_sale_price_study import page2_sale_price_study_body
from app_pages.page3_predict import page3_predict_body
from app_pages.page4_hypothesis_and_validation import page4_hypothesis_and_validation_body
from app_pages.page5_ml_predict import page5_ml_predict_body

app = MultiPage(app_name= "PP5 - Sale Price Predictor") # Create an instance of the app 

# Add your app pages here using .add_page()
app.app_page("Project Summary", page1_summary_body)
app.app_page("House Sale Price Study", page2_sale_price_study_body)
app.app_page("Predict House Value", page3_predict_body)
app.app_page("Project Hypothesis and Validation", page4_hypothesis_and_validation_body)
app.app_page("ML: Predict House Value", page5_ml_predict_body)

app.run() # Run the  app

# code copied from Code Institute's Churnornmeter Project with some adjustments