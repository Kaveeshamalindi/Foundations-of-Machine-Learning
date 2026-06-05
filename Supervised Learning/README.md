# Regression

Regression is a type of supervised learning where the goal is to predict a number that can vary along a continuous scale, like guessing someone's house price or the temperature tomorrow. This involves identifying relationships between input features and a continuous output value.

## Regression.py

**Output Description**: This code would produce five numerical predictions representing the disease progression values for the first five samples in the dataset. These values are continuous numbers that reflect the predicted severity of diabetes based on the patient's features.

---

# Classification

Classification tasks are about predicting categorical outcomes. For instance, a healthcare provider might use patient data to classify individuals as either having a certain condition or not—here, outcomes are discrete categories, such as "diabetic" or "non-diabetic."

## Classification.py

**Output Description**: This code would output an array of predicted class labels (numbers 0, 1, or 2) for the first five iris flowers in the dataset. Each number represents a specific flower species: 0 for setosa, 1 for versicolor, and 2 for virginica.

### Features (X)

**Each flower includes:** sepal length, sepal width, petal length, petal width
- X contains numerical measurements.

### Target (y)

**y contains flower categories:** Setosa, Versicolor, Virginica

---

## Overall Workflow 

```Load Data → Train Model → Make Predictions```
