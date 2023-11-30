import csv

__author__ = "John Garvey"
__date__ = "10/20/2023"
__assignment = "Project MS05"

le_gdp_testing = []
le_uwc_testing = []
le_gdp_uwc_testing = []

accuracy = []


def create_predictions(model01, model02, model03):

    load_processed_data()

    actual01 = le_gdp_testing[0]["LE Mean"]
    pred01 = make_prediction01(model01, le_gdp_testing[0]["GDP Mean"])
    actual02 = le_uwc_testing[0]["LE Mean"]
    pred02 = make_prediction01(model02, le_uwc_testing[0]["UWC Mean"])
    actual03 = le_gdp_uwc_testing[0]["LE Mean"]
    pred03 = make_prediction02(model03, le_gdp_uwc_testing[0]["GDP Mean"], le_gdp_uwc_testing[0]["UWC Mean"])

    models_file = open("models/linear_regression_predictions.csv", "w")
    models_file.seek(0,1)
    string = "============================================================================================\n"
    string = string + "Country: " + le_gdp_testing[0]["Country Name"] + " | Actual Life Expectancy: " + le_gdp_testing[0]["LE Mean"] + " | Mean GDP per Capita: " + le_gdp_testing[0]["GDP Mean"] + "\n"
    string = string + "Model01: Mean Life Expectancy = " + str(round(model01[0][0], 8)) + "(Mean GDP) + " + str(round(model01[1][0],8))+"\n"
    string = string + "Model01 GDP Prediction:  "+str(pred01)+" = " + str(model01[0]) +"("+ le_gdp_testing[0]["GDP Mean"] + ") + " + str(model01[1]) + "\n"
    string = string + "Model01 GDP Difference: " + str(float(le_gdp_testing[0]["LE Mean"]) - pred01) + "\n"
    string = string + "============================================================================================\n"
    string = string + "Country: " + le_uwc_testing[0]["Country Name"] + " | Actual Life Expectancy: " + le_uwc_testing[0]["LE Mean"] + " | Mean Underweight Children %: " + le_uwc_testing[0]["UWC Mean"] + "\n"
    string = string + "Model02: Mean Life Expectancy = " + str(round(model02[0][0],8)) + "(Mean Underweight Children %) + " + str(round(model02[1][0],8))+"\n"
    string = string + "Model02 UWC Prediction:  "+str(pred02)+" = " + str(model02[0]) +"("+ le_uwc_testing[0]["UWC Mean"] + ") + " + str(model02[1]) + "\n"
    string = string + "Model02 UWC Difference: " + str(float(le_uwc_testing[0]["LE Mean"]) - pred02) + "\n"
    string = string + "============================================================================================\n"
    string = string + "Country: " + le_gdp_uwc_testing[0]["Country Name"] + " | Actual Life Expectancy: " + le_gdp_uwc_testing[0]["LE Mean"] + " | Mean GDP per Capita: " + le_gdp_uwc_testing[0]["GDP Mean"] + " Mean Underweight Children %: " + le_gdp_uwc_testing[0]["UWC Mean"] + "\n"
    string = string + "Model03: Mean Life Expectancy = " + str(round(model03[0][0], 8)) + "(Mean GDP) + " + str(round(model03[1][0], 8)) + "(Mean Underweight Children %) + " + str(round(model03[2][0], 8)) + "\n"
    string = string + "Model03 Both Prediction:  "+str(pred03)+" = " + str(model03[0]) +"("+ le_gdp_uwc_testing[0]["GDP Mean"] +") * "+ str(model03[1]) +"("+ le_gdp_uwc_testing[0]["UWC Mean"] + ") + " + str(model03[2]) + "\n"
    string = string + "Model03 Both Difference: " + str(float(le_gdp_uwc_testing[0]["LE Mean"]) - pred03) + "\n"
    string = string + "============================================================================================"
    models_file.write(string)

    return le_gdp_uwc_testing

    pass


def make_prediction01(model, feature):

    coef = float(model[0])
    inter = float(model[1])
    pred = coef * float(feature) + inter
    return pred

    pass


def make_prediction02(model, feature01, feature02):

    coef01 = float(model[0])
    coef02 = float(model[1])
    inter = float(model[2])
    pred = coef01 * float(feature01) + coef02 * float(feature02) + inter
    return pred

    pass


def load_processed_data():

    read_processed("le_gdp_testing.csv", le_gdp_testing, "LE Mean", "GDP Mean", "")
    read_processed("le_uwc_testing.csv", le_uwc_testing, "LE Mean", "UWC Mean", "")
    read_processed("le_gdp_uwc_testing.csv", le_gdp_uwc_testing, "LE Mean", "GDP Mean", "UWC Mean")

    pass


def read_processed(file_name, append_list, target, feature01, feature02):

    # read from processed data file and add data to a list
    with open(f"./data_processed/{file_name}") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            add_dict = dict()
            add_dict['Country Name'] = row['Country Name']
            add_dict[target] = row[target]
            add_dict[feature01] = row[feature01]
            if feature02 != "":
                add_dict[feature02] = row[feature02]
            append_list.append(add_dict)
    pass


def display_list(pass_list):

    i = 0
    for row in pass_list:
        print(i, row)
        i += 1

    pass
