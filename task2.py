import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, ConfusionMatrixDisplay

def main():
    print("--- Project 2: Data Classification Using AI ---")
    
   
    print("\nLoading Iris dataset...")
    iris = load_iris()
    X = iris.data
    y = iris.target
    print(f"Dataset loaded. Samples: {X.shape[0]}, Features: {X.shape[1]}, Classes: {len(np.unique(y))}")
    
   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=True)
    print(f"Data split completed: {X_train.shape[0]} training samples, {X_test.shape[0]} testing samples.")

    
    print("\nApplying StandardScaler...")
    scaler = StandardScaler()
    # Fit only on training data, then transform both
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 4. Initialize and Train the KNN Algorithm
    # Using k=5 as shown in "THE WORKFLOW: SCIKIT-LEARN" slide
    k_value = 5
    print(f"\nInitializing KNeighborsClassifier with k={k_value}...")
    model = KNeighborsClassifier(n_neighbors=k_value)
    
    print("Fitting the model (Memorizing the map)...")
    model.fit(X_train_scaled, y_train)
    
  
    print("Making predictions on the test set...")
    predictions = model.predict(X_test_scaled)
    
   
    print("\n--- Output Validation ---")
    
   
    f1 = f1_score(y_test, predictions, average='weighted')
    print(f"F1 Score (Weighted): {f1:.4f}")
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, predictions)
    print("Confusion Matrix:")
    print(cm)
    
    # Visualize Confusion Matrix and save to file
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
    disp.plot(cmap=plt.cm.Blues)
    plt.title('Confusion Matrix - Iris KNN')
    
    output_filename = 'confusion_matrix.png'
    plt.savefig(output_filename)
    print(f"\nVisualized confusion matrix saved to '{output_filename}'.")
    
    # Optional: Plotting the Elbow Method to verify if k=5 is good
    print("\nEvaluating 'K' values using the Elbow Method...")
    error_rates = []
    k_range = range(1, 20)
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train_scaled, y_train)
        pred_i = knn.predict(X_test_scaled)
        # Error rate is 1 - accuracy (or we can just track average error)
        error_rates.append(np.mean(pred_i != y_test))
        
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, error_rates, color='blue', linestyle='dashed', marker='o',
             markerfacecolor='red', markersize=8)
    plt.title('Error Rate vs. K Value (The Elbow Method)')
    plt.xlabel('K Value')
    plt.ylabel('Error Rate')
    
    elbow_filename = 'elbow_method.png'
    plt.savefig(elbow_filename)
    print(f"Elbow method plot saved to '{elbow_filename}'.")

if __name__ == "__main__":
    main()
