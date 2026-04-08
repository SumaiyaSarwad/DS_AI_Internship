# TASK 3 — THE COMPLEXITY CREATOR (POLYNOMIAL FEATURES)
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data = {
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [30000, 35000, 42000, 52000, 65000,
               81000, 100000, 122000, 147000, 175000]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

linear_preds = linear_model.predict(X_test)
linear_r2 = r2_score(y_test, linear_preds)

print("\nR² Score (Original Feature):", linear_r2)

poly = PolynomialFeatures(degree=2, include_bias=False)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

poly_preds = poly_model.predict(X_test_poly)
poly_r2 = r2_score(y_test, poly_preds)

print("R² Score (Polynomial Degree 2):", poly_r2)

print("\n===== PERFORMANCE COMPARISON =====")
print("Original Linear Model R² :", linear_r2)
print("Polynomial Model R²      :", poly_r2)

if poly_r2 > linear_r2:
    print("\nPolynomial features improved the model performance.")
else:
    print("\nPolynomial features did not improve performance.")

print("\nPolynomial Feature Engineering Completed Successfully!")

'''
Output:
    R² Score (Original Feature): 0.98143674574653
    R² Score (Polynomial Degree 2): 0.9999552277149941

    ===== PERFORMANCE COMPARISON =====
    Original Linear Model R² : 0.98143674574653
    Polynomial Model R²      : 0.9999552277149941

    Polynomial features improved the model performance.

    Polynomial Feature Engineering Completed Successfully!
'''

