import json 
import pandas as pd 

REQUIRED_FEATURES = [
    "Age","Gender","Ethnicity","ParentalEducation",
    "StudyTimeWeekly","Absences","Tutoring","ParentalSupport",
    "Extracurricular","Sports","Music","Volunteering"
]
        
def ensure_features(df: pd.DataFrame) -> pd.DataFrame:
    for col in REQUIRED_FEATURES:
        if not col in df.columns:   
            df[col] = None
    return df