import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import sklearn

# ── Load data ────────────────────────────────────────────────────────────────
print("Loading data...")
df = pd.read_csv('data.csv', sep=';')
print(f"Dataset asli: {df.shape[0]} baris")
print(f"Distribusi:\n{df['Status'].value_counts().to_string()}\n")

# ── Filter: hanya Dropout dan Graduate ───────────────────────────────────────
# Data Enrolled TIDAK digunakan untuk training karena belum memiliki label akhir.
# Data Enrolled dapat digunakan untuk inferensi/prediksi saja.
df_model = df[df['Status'].isin(['Dropout', 'Graduate'])].copy()
print(f"Setelah filter (Dropout + Graduate): {df_model.shape[0]} baris")
print(f"  - Dropout  : {(df_model['Status']=='Dropout').sum()}")
print(f"  - Graduate : {(df_model['Status']=='Graduate').sum()}")
print(f"  - Enrolled (excluded dari training): {(df['Status']=='Enrolled').sum()}\n")

# ── Encode target (binary) ────────────────────────────────────────────────────
le = LabelEncoder()
df_model['Status_encoded'] = le.fit_transform(df_model['Status'])
print(f"Label encoding: {dict(zip(le.classes_, le.transform(le.classes_)))}")
print(f"  0 = Dropout | 1 = Graduate\n")

# ── Pisahkan fitur dan target ─────────────────────────────────────────────────
X = df_model.drop(['Status', 'Status_encoded'], axis=1)
y = df_model['Status_encoded']

numerical_features   = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

print(f"Numerical features  : {len(numerical_features)}")
print(f"Categorical features: {len(categorical_features)}")

# ── Train-test split ──────────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\nTrain size: {X_train.shape[0]} | Test size: {X_test.shape[0]}")

# ── Pipeline preprocessing ────────────────────────────────────────────────────
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler',  StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot',  OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer,     numerical_features),
    ('cat', categorical_transformer, categorical_features)
])

# ── Model ─────────────────────────────────────────────────────────────────────
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight='balanced'
)

clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model',        model)
])

# ── Training ──────────────────────────────────────────────────────────────────
print("\nTraining model (Binary: Dropout vs Graduate)...")
clf.fit(X_train, y_train)

# ── Evaluasi cepat ────────────────────────────────────────────────────────────
from sklearn.metrics import accuracy_score, classification_report
y_pred = clf.predict(X_test)
print(f"\nAccuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"\nClassification Report:\n{classification_report(y_test, y_pred, target_names=le.classes_)}")

# ── Simpan model ──────────────────────────────────────────────────────────────
joblib.dump(clf, 'model_student.pkl')
joblib.dump(le,  'label_encoder.pkl')

print("\n✅ Model berhasil disimpan!")
print(f"   scikit-learn version : {sklearn.__version__}")
print(f"   Classes              : {le.classes_}  (Binary)")
print(f"   File                 : model_student.pkl, label_encoder.pkl")
print("\nSekarang jalankan: streamlit run app.py")
