from sklearn import tree 
 
# x is a 2D list with 11 sublists (individuals) each containing 3 elements (height, weight, shoe size)
# Here we have a list of data points, each representing an individual.
# Each data point is a list of 3 values: height, weight, and shoe size.


def main():
    x = [
        # Male
        [175, 70, 42],  # Height: 175, Weight: 70, Shoe Size: 42
        # Female
        [160, 55, 38],  # Height: 160, Weight: 55, Shoe Size: 38
        # Male
        [180, 85, 44],  # Height: 180, Weight: 85, Shoe Size: 44
        # Female
        [165, 62, 39],  # Height: 165, Weight: 62, Shoe Size: 39
        # Male
        [178, 75, 43],  # Height: 178, Weight: 75, Shoe Size: 43
        # Female
        [158, 50, 37],  # Height: 158, Weight: 50, Shoe Size: 37
        # Male
        [183, 90, 45],  # Height: 183, Weight: 90, Shoe Size: 45
        # Female
        [162, 58, 38],  # Height: 162, Weight: 58, Shoe Size: 38
        # Male
        [177, 78, 42],  # Height: 177, Weight: 78, Shoe Size: 42
        # Female
        [155, 52, 36],  # Height: 155, Weight: 52, Shoe Size: 36
        # Male
        [185, 95, 46],  # Height: 185, Weight: 95, Shoe Size: 46
    ]

    # Here we have a list of labels for each data point.
    # Each label corresponds to the gender of the individual.
    y = [
        "Male",   # Male
        "Female", # Female
        "Male",   # Male
        "Female", # Female
        "Male",   # Male
        "Female", # Female
        "Male",   # Male
        "Female", # Female
        "Male",   # Male
        "Female", # Female
        "Male"    # Male
    ]

    # Here we create a decision tree classifier object.
    # This object will be used to train the classifier.
    CLF = tree.DecisionTreeClassifier()

    # Here we train the classifier using the training data.
    # The training data is the list of data points and the list of labels.
    CLF = CLF.fit(x,y)

    # Here we use the trained classifier to make a prediction.
    # We pass in a list of values for an individual to predict their gender.
    prediction = CLF.predict([[160, 55, 38]])

    # Here we print the predicted gender.
    x = [
        [175, 70, 42],  # Male
        [160, 55, 38],  # Female
        [180, 85, 44],  # Male
        [165, 62, 39],  # Female
        [178, 75, 43],  # Male
        [158, 50, 37],  # Female
        [183, 90, 45],  # Male
        [162, 58, 38],  # Female
        [177, 78, 42],  # Male
        [155, 52, 36],  # Female
        [185, 95, 46],  # Male
    ]

    # y is a 1D list with 11 elements corresponding to each individual's gender ("Male" or "Female")
    y = ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male"]

    CLF = tree.DecisionTreeClassifier()

    CLF = CLF.fit(x,y)

    prediction = CLF.predict([[160, 55, 38]])

    print(prediction)

if __name__ == "__main__":
    main()
