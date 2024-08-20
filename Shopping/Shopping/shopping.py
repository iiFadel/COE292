
import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")

def load_data(filename):
    evidence= []
    labels= []
    monthsDict= dict([("Jan", 1), ("Feb", 2), ("Mar", 3), ("Apr", 4),
                      ("May", 5), ("June", 6), ("Jul", 7), ("Aug",8 ),
                      ("Sep", 9), ("Oct", 10), ("Nov", 11), ("Dec", 12)])
    with open(filename, "r") as file:
        reader= csv.DictReader(file)
        for row in reader:
            nList= []
            nList.append(int(row["Administrative"]))
            nList.append(float(row["Administrative_Duration"]))
            nList.append(int(row["Informational"]))
            nList.append(float(row["Informational_Duration"]))
            nList.append(int(row["ProductRelated"]))
            nList.append(float(row["ProductRelated_Duration"]))
            nList.append(float(row["BounceRates"]))
            nList.append(float(row["ExitRates"]))
            nList.append(float(row["PageValues"]))
            nList.append(float(row["SpecialDay"]))
            nList.append(monthsDict[row["Month"]])
            nList.append(int(row["OperatingSystems"]))
            nList.append(int(row["Browser"]))
            nList.append(int(row["Region"]))
            nList.append(int(row["TrafficType"]))
            nList.append(0 if row["VisitorType"]== "New_Visitor" else 1)
            nList.append(0 if row["Weekend"]== "FALSE" else 1)
            labels.append(0 if row["Revenue"]== "FALSE" else 1)
            evidence.append(nList)

    return (evidence, labels)


def train_model(evidence, labels):
    trainModel= KNeighborsClassifier(n_neighbors= 1)
    trainModel.fit(evidence, labels)
    return trainModel


def evaluate(labels, predictions):
    positive= 0
    negative= 0
    sensitivity= 0
    specificity= 0

    for element in range(len(labels)):
        if labels[element]== 1:
            positive+= 1
            if labels[element]== predictions[element]:
                sensitivity+= 1

        if labels[element]== 0:
            negative+= 1
            if labels[element]== predictions[element]:
                specificity+= 1

    sensitivity= sensitivity/positive
    specificity= specificity/negative

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
