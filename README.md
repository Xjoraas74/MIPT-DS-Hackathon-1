# Hackathon

## Оглавление
[1. Участники проекта](https://github.com/Xjoraas74/MPTI-DS-Hackathon-1/edit/master/README.md#Участники-проекта)

[2. Цель проекта](https://github.com/Xjoraas74/MPTI-DS-Hackathon-1/edit/master/README.md#Цель-проекта)

[3. Описание проекта](https://github.com/Xjoraas74/MPTI-DS-Hackathon-1/edit/master/README.md#Описание-проекта)

[4. Технологии](https://github.com/Xjoraas74/MPTI-DS-Hackathon-1/edit/master/README.md#Описание-проекта)

[5. Модели ML](https://github.com/Xjoraas74/MPTI-DS-Hackathon-1/edit/master/README.md#Модели-ML)

[6. Решение](https://github.com/BogdanTanchuk/DataCleaningProject/edit/master/README.md#Решение)

[7. Результаты](https://github.com/BogdanTanchuk/DataCleaningProject/edit/master/README.md#Результаты)

### Участники проекта
  - Самойлов Юрий
  - Танчук Богдан
  - Тухватуллин Динар

### Цель проекта
Создание модели для предсказания класса воды

### Описание проекта
Нужно подготовить данные для последующего прогнозирования стоимости жилья посредством машинного обучения
В рамках проекта необходимо загрузить обработать данные о качестве воды, представленные на [сайте NYC OpenData](https://data.cityofnewyork.us/Environment/Drinking-Water-Quality-Distribution-Monitoring-Dat/bkwf-xfky)

### Технологии
  - Python
    * numpy
    * pandas
    * sklearn
    * xgboost
    * catboost
    * hyperopt
    * seaborn
    * matplotlib

### Модели ML
  - XGBoost
  - Catboost
  - BaggingClassifier
  - LogisticRegression

### Решение
[Ноутбук с визуализацией](https://github.com/Xjoraas74/MPTI-DS-Hackathon-1/blob/master/Hackathon.ipynb)

### Результаты
**Наилучший результат показала модель XGBoost**
  - ***XGBoost - 0.75***
  - CatBoost - 0.74
  - BaggingClassifier - 0.73
  - LogisticRegression - 0.71