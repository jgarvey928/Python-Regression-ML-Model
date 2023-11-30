import csv
import numpy as np

__author__ = "John Garvey"
__date__ = "10/20/2023"
__assignment = "Project MS05"

# Ratio for Training
RATIO_TRAINING = 80

le_gdp_training = []
le_gdp_testing = []

le_uwc_training = []
le_uwc_testing = []

le_gdp_uwc_data = []
le_gdp_uwc_training = []
le_gdp_uwc_testing = []


def create_models():

    load_processed_data()
    temp = create_linear_reg_model(le_gdp_training, "LE Mean", "GDP Mean")
    global model01
    model01 = temp
    temp = create_linear_reg_model(le_uwc_training, "LE Mean", "UWC Mean")
    global model02
    model02 = temp
    temp = create_multi_linear_reg_model(le_gdp_uwc_data, le_gdp_training, le_uwc_training, "LE Mean", "GDP Mean", "UWC Mean")
    global model03
    model03 = temp

    write_models()

    write_multi_feature_data()

    return model01, model02, model03

    pass


def write_models():

    models_file = open("models/linear_regression_models.csv", "w")
    string = "==============================================\n"
    string = string + "Nations Mean Life Expectancy Linear Regression Models: \n"
    string = string + "==============================================\n"
    string = string + "Model01: Mean Life Expectancy = " + str(round(model01[0][0], 8)) + "(Mean GDP) + " + str(round(model01[1][0],8))+"\n"
    string = string + "Model02: Mean Life Expectancy = " + str(round(model02[0][0],8)) + "(Mean Underweight Children %) + " + str(round(model02[1][0],8))+"\n"
    string = string + "Model03: Mean Life Expectancy = " + str(round(model03[0][0],8)) + "(Mean GDP) + " + str(round(model03[1][0],8)) + "(Mean Underweight Children %) + " + str(round(model03[2][0],8)) + "\n"
    string = string + "==============================================\n"
    models_file.write(string)

    pass


def create_multi_linear_reg_model(data_list, training_list01, training_list02, target, feature01, feature02):

    combine_data(data_list, training_list01, training_list02, target, feature01, feature02)
    split_data()
    temp = []
    for country_info in le_gdp_uwc_training:
        target_data = float(country_info[target])
        feature01_data = float(country_info[feature01])
        feature02_data = float(country_info[feature02])
        temp.append([feature01_data, feature02_data, target_data])
    np_array = np.array(temp)

    A1 = np_array[:, 0]
    A1 = A1.reshape(-1, 1)

    A2 = np_array[:, 1]
    A2 = A2.reshape(-1, 1)

    b = np_array[:, 2]
    b = b.reshape(-1, 1)

    ones = np.ones(len(b))
    ones = ones.reshape(-1, 1)

    A = np.concatenate((A1, A2), axis=1)
    A = np.concatenate((A, ones), axis=1)
    AT = np.transpose(A)
    ATA = np.dot(AT, A)
    ATA_INV = np.linalg.inv(ATA)
    ATA_INV_AT = np.dot(ATA_INV, AT)
    w = np.dot(ATA_INV_AT, b)
    return w

    pass


def combine_data(data_list, training_list01, training_list02, target, feature01, feature02):

    for country_info01 in training_list01:
        for country_info02 in training_list02:
            if country_info01['Country Name'] == country_info02['Country Name']:
                data_list.append({'Country Name': country_info01['Country Name'],
                                        target :  country_info01[target],
                                        feature01 : country_info01[feature01],
                                        feature02 : country_info02[feature02]})

    pass


def split_data():

    perc = RATIO_TRAINING / 100
    sample_size = len(le_gdp_uwc_data)
    ratio = round(sample_size * perc)
    i = 1
    for country_info in le_gdp_uwc_data:
        if i <= ratio:
            le_gdp_uwc_training.append(country_info)
        else:
            le_gdp_uwc_testing.append(country_info)
        i += 1

    pass


def create_linear_reg_model(training_list, target, feature):

    temp = []
    for country_info in training_list:
        target_data = float(country_info[target])
        feature_data = float(country_info[feature])
        temp.append([feature_data, target_data])
    np_array = np.array(temp)

    A = np_array[:, 0]
    A = A.reshape(-1, 1)
    b = np_array[:, 1]
    b = b.reshape(-1, 1)
    ones = np.ones(len(b))
    ones = ones.reshape(-1, 1)
    A = np.concatenate((A, ones), axis=1)
    AT = np.transpose(A)
    ATA = np.dot(AT, A)
    ATA_INV = np.linalg.inv(ATA)
    ATA_INV_AT = np.dot(ATA_INV, AT)
    w = np.dot(ATA_INV_AT, b)
    return w

    pass


def write_multi_feature_data():

    training_file = open("data_processed/le_gdp_uwc_training.csv", "w")
    new_fieldnames = "Country Name,LE Mean,GDP Mean,UWC Mean\n"
    training_file.write(new_fieldnames)
    for country_info in le_gdp_uwc_training:
        training_file.write("\""+country_info['Country Name'] + "\"," + str(country_info["LE Mean"]) + "," + str(country_info["GDP Mean"])  + "," + str(country_info["UWC Mean"]) + "\n")

    testing_file = open("data_processed/le_gdp_uwc_testing.csv", "w")
    testing_file.write(new_fieldnames)
    for country_info in le_gdp_uwc_testing:
        testing_file.write("\""+country_info['Country Name'] + "\"," + str(country_info["LE Mean"]) + "," + str(country_info["GDP Mean"])  + "," + str(country_info["UWC Mean"]) + "\n")

    pass


def load_processed_data():

    read_processed("le_gdp_training.csv", le_gdp_training, "LE Mean", "GDP Mean")
    read_processed("le_gdp_testing.csv", le_gdp_testing, "LE Mean", "GDP Mean")

    read_processed("le_uwc_training.csv", le_uwc_training, "LE Mean", "UWC Mean")
    read_processed("le_uwc_testing.csv", le_uwc_testing, "LE Mean", "UWC Mean")

    pass


def read_processed(file_name, append_list, target, feature):

    # read from processed data file and add data to a list
    with open(f"./data_processed/{file_name}") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            add_dict = dict()
            add_dict['Country Name'] = row['Country Name']
            add_dict[target] = row[target]
            add_dict[feature] = row[feature]
            append_list.append(add_dict)
    pass


def display_list(pass_list):

    i = 0
    for row in pass_list:
        print(i, row)
        i += 1

    pass

