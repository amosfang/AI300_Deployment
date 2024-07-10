## HEICODERS AI300 Capstone Project ##

## Folder Structure.

```
├── data
│   └── filename.csv
│   └── SampleDataForPrediction.csv
├── model
│   └── best_clf.pkl
├── notebooks
│   └── WorkingNotebook.ipynb
├── src
│   └── static
│      └── style.css
│   └── templates
│      └── index.html
│   └── app.py
│   └── input_processing.py
│   └── model.py
├── .gitignore
├── Readme.md
├── requirements.txt

```

## Website URL of deployed Flask web application 

[Dockerhub URL](https://hub.docker.com/r/mhidayatz/capstone-team4-flask-app) - Pull the latest tag, 1.3

[Deployed Web App URL](http://ec2-18-139-0-23.ap-southeast-1.compute.amazonaws.com/) - This app is optimized for both mobile devices and web browsers experience.

## Details on chosen final model and model parameters

```
CatBoostClassifier

{'learning_rate': 0.1,
 'l2_leaf_reg': 0.01,
 'iterations': 400,
 'depth': 9,
 'border_count': 64}

```

## Offline AUC metric of chosen final model

```
 CatBoostClassifier
 AUC: 0.9058097286413764
 Accuracy: 0.8971783835485414

```

## About This Repo

- Package dependencies can be found in `requirements.txt` file.
- Command to start Flask app: `python src/app.py`


## Sample Data
- The sample data for churn prediction can be located in the file named data-SampleDataForPrediction.csv, under the "Example Sheet" tab.
