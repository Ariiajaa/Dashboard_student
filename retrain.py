import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv('data.csv', sep=';')

# Encode target
le = LabelEncoder()
df['Status_encoded'] = le.fit_transform(df['Status'])

# Pisahkan fitur dan target
X = df.drop(['Status', 'Status_encoded'], axis=1)
y = df['Status_encoded']

# Identifikasi kolom
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Pipeline preprocessing
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numerical_features),
    ('cat', categorical_transformer, categorical_features)
])

# Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight='balanced'
)

clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', model)
])

# Training
print("Training model...")
clf.fit(X_train, y_train)

# Simpan model
joblib.dump(clf, 'model_student.pkl')
joblib.dump(le, 'label_encoder.pkl')

print("✅ Model berhasil disimpan!")
print(f"   sklearn version: {__import__('sklearn').__version__}")
print(f"   Classes: {le.classes_}")