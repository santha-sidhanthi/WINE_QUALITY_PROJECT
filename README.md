
This wine quality prediction model.
The model is built using Linear Regression Algorithm

If the predicted wine quality is greater tha 5, it is good quality.
If the predicted wine quality is less tha 5, it is bad quality. 


The dataset has 12 columns:  [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,
                                  total_sulfur_dioxide,density,pH,sulphates,alcohol]



├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources, downloaded from Kaggle dataset
│ 
│
│
├── models             <- Trained and serialized models, "model.pkl" file [model trained and tested and saved on disk.]
│
├── notebooks          <- Jupyter notebooks. "EDA_WINEDATA.ipynb"
│
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├│   │
│   ├── data           <- Scripts to download or generate data
│   │   │   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── app.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └──
│
└── Templates         <- html files
│   │   ├── home.html
│   │   └── predict.html
│   │
│   │
│   └──
└──
