# Zomato Restaurant Rating Predictor

A Streamlit app for exploring restaurant reviews and predicting a restaurant rating from a customer review, restaurant, cuisine, and average cost. The project includes an interactive dashboard, a trained scikit-learn model, source datasets, and notebooks documenting the data and modeling workflow.

## Features

- Predicts a rating out of 5 from review text and restaurant details.
- Summarizes the dataset with restaurant, review, average-rating, and average-cost metrics.
- Visualizes rating distributions and the most-reviewed restaurants and cuisines.
- Lets you preview sample records from the processed dataset.

## Run locally

Use Python 3.10 or newer. From the repository root, install the app's dependencies and start Streamlit:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS or Linux
source .venv/bin/activate
```

Install dependencies and run the app:

```bash
python -m pip install streamlit pandas plotly joblib scikit-learn
streamlit run app/app.py
```

The app loads the processed dataset from `data/processed/zomato_processed.csv` and the trained model from `models/zomato_rating_model.pkl`. Keep both files in those locations when running the app.

## Project structure

```text
app/          Streamlit app and visualization components
data/
  raw/        Source restaurant and review CSV files
  processed/  Processed dataset used by the app
models/       Trained rating prediction model
notebooks/    Data loading, engineering, analysis, and model training
src/          Supporting preprocessing and model scripts
```

## Model and data

The training notebook prepares review text with TF-IDF, encodes restaurant and cuisine fields, and evaluates regression models for rating prediction. The deployed model is serialized with joblib. Loading serialized scikit-learn models can depend on the scikit-learn version used to train them; if loading fails, use the matching environment or retrain the model with `notebooks/05_Model_Training.ipynb`.

The repository includes raw and processed CSV data for reproducibility. Check the original dataset's terms and attribution requirements before redistributing or reusing the data.