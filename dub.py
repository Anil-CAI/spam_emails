from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI() 

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load dataset and train the model
raw_mail_data = pd.read_csv('mail_data.csv')
mail_data = raw_mail_data.where(pd.notnull(raw_mail_data), '')

# Label encoding: spam -> 0, ham -> 1
mail_data.loc[mail_data['Category'] == 'spam', 'Category'] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category'] = 1

x = mail_data['Message']
y = mail_data['Category'].astype(int)

# Feature extraction
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
x_features = feature_extraction.fit_transform(x)

# Train model
model = LogisticRegression()
model.fit(x_features, y)

# Request Model
class MailRequest(BaseModel):
    message: str

@app.post("/predict")
def predict(request: MailRequest):
    input_data_feature = feature_extraction.transform([request.message])
    prediction = model.predict(input_data_feature)
    return {"prediction": "ham" if prediction[0] == 1 else "spam"}
