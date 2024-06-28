import csv
from matplotlib.pylab import shuffle
import numpy as np
from wf_ml_training import create_models
from wf_ml_prediction import create_predictions

__author__ = "John Garvey"
__date__ = "10/20/2023"
__assignment = "Project MS05"

# Years Start
YEAR_START = 1960
# Year End
YEAR_END = 2022
# NUMBER OF COUNTRIES IN DATASET
NUMB_COUNTRIES = 217
# NUMBER OF DATA CATEGORIES
NUMB_CATEGORIES = 5
# Ratio for Training
RATIO_TRAINING = 80
# life expectancy data and quantitative data lists
le_total = []
le_total_summ = []
# GDP per Capita data and quantitative data lists
gdp_pcap = []
gdp_pcap_summ = []
# technology export percentage data and quantitative data lists
tech_expo = []
tech_expo_summ = []
# percent of underweight children data and quantitative data lists
udwe_child = []
udwe_child_summ = []
# poverty percentage for population data and quantitative data lists
pov_ratio = []
pov_ratio_summ = []

all_means_data = []

le_gdp_data = []
le_gdp_training = []
le_gdp_testing = []

le_uwc_data = []
le_uwc_training = []
le_uwc_testing = []

le_gdp_uwc_testing = []

accuracy = []


def evaluate_data():

    load_processed_data()
    get_quant_data()
    get_qual_data()
    get_all_means()
    write_means_data()
    train_and_test_data()
    model01, model02, model03 = create_models()
    le_gdp_uwc_testing = create_predictions(model01, model02, model03)

    mse01 = find_mse01(model01[0][0], model01[1][0], le_gdp_testing, "LE Mean", "GDP Mean")
    acc01 = find_accuracy()
    mse02 = find_mse01(model02[0][0], model02[1][0], le_uwc_testing, "LE Mean", "UWC Mean")
    acc02 = find_accuracy()
    mse03 = find_mse02(model03[0][0], model03[1][0], model03[2][0], le_gdp_uwc_testing, "LE Mean", "GDP Mean", "UWC Mean")
    acc03 = find_accuracy()

    write_eval_summary(mse01, acc01, mse02, acc02, mse03, acc03)

    pass


def write_eval_summary(mse01, acc01, mse02, acc02, mse03, acc03):

    training_file = open("evaluation/summary.txt", "w")
    string = '================================================================\n'
    string = string + "Model #  |   MSE             | Mean Accuracy (Years) | \n"
    string = string + "================================================================\n"
    string = string + "Model 01 GDP  | " + str(mse01)+" | "+str(acc01) + "\n"
    string = string + "Model 02 UWC  | " + str(mse02)+" | "+str(acc02) + "\n"
    string = string + "Model 03 Both | " + str(mse03)+" | "+str(acc03) + "\n"
    string = string + "================================================================\n"
    training_file.write(string)

    pass


def find_accuracy():

    n = 0
    summ = 0
    for diff in accuracy:
        summ += diff
        n += 1
    return summ/n

    pass


def find_mse01(coef, inter, testing_data, target, feature):

    n = len(testing_data)
    summ = 0
    for country_info in testing_data:
        pred = coef * float(country_info[feature]) + inter
        sub = pred - float(country_info[target])
        accuracy.append(abs(sub))
        sqrd = sub * sub
        summ += sqrd
    return summ / n
    pass


def find_mse02(coef01, coef02, inter, testing_data, target, feature01, feature02):
    n = len(testing_data)
    summ = 0
    for country_info in testing_data:
        pred = coef01 * float(country_info[feature01]) + coef02 * float(country_info[feature02]) + inter
        sub = pred - float(country_info[target])
        accuracy.append(abs(sub))
        sqrd = sub * sub
        summ += sqrd
    return summ / n

    pass


def train_and_test_data():

    get_feature_target_mean('LE Mean', 'GDP Mean', le_gdp_data)
    split_data(le_gdp_data, le_gdp_training, le_gdp_testing)
    write_single_feature_data(le_gdp_training, le_gdp_testing, "le_gdp", 'LE Mean', 'GDP Mean')

    get_feature_target_mean('LE Mean', 'UWC Mean', le_uwc_data)
    split_data(le_uwc_data, le_uwc_training, le_uwc_testing)
    write_single_feature_data(le_uwc_training, le_uwc_testing, "le_uwc", 'LE Mean', 'UWC Mean')

    pass


def write_single_feature_data(training_list, testing_list, file_name, target, feature):

    training_file = open("data_processed/"+file_name+"_training.csv", "w")
    new_fieldnames = "Country Name,"+target+","+feature+"\n"
    training_file.write(new_fieldnames)
    for country_info in training_list:
        training_file.write("\""+country_info['Country Name'] + "\"," + str(country_info[target]) + "," + str(country_info[feature]) + "\n")

    testing_file = open("data_processed/"+file_name+"_testing.csv", "w")
    testing_file.write(new_fieldnames)
    for country_info in testing_list:
        testing_file.write("\""+country_info['Country Name'] + "\"," + str(country_info[target]) + "," + str(country_info[feature]) + "\n")


    pass


def split_data(data_list, training_list, testing_list):

    perc = RATIO_TRAINING / 100
    sample_size = len(data_list)
    ratio = round(sample_size * perc)
    temp = data_list
    shuffle(temp)
    shfData = temp
    i = 1
    for country_info in shfData:
        if i <= ratio:
            training_list.append(country_info)
        else:
            testing_list.append(country_info)
        i += 1

    pass


def get_feature_target_mean(target, feature, data_list):

    for country_info in all_means_data:
        if country_info[target] != -1 and country_info[feature] != -1:
            data_list.append({"Country Name": country_info["Country Name"],
                                target: country_info[target],
                                feature: country_info[feature]})

    pass


def write_means_data():

    all_means_data_file = open("data_processed/all_means_data.csv", "w")
    new_fieldnames = "Country Name,LE Mean,GDP Mean,TECH Mean,UWC Mean,POV Mean\n"
    all_means_data_file.write(new_fieldnames)
    for country_info in all_means_data:
        all_means_data_file.write("'Country Name':\"" + str(country_info["Country Name"]) +
                                    "\",'LE Mean':" + str(country_info["LE Mean"]) +
                                    ",'GDP Mean':" + str(country_info["GDP Mean"]) +
                                    ",'TECH Mean':" + str(country_info["TECH Mean"]) +
                                    ",'UWC Mean':" + str(country_info["UWC Mean"]) +
                                    ",'POV Mean':" + str(country_info["POV Mean"]) + "\n")

    pass


def get_all_means():

    i = 1
    for country_info in le_total:
        le_mean, gdp_mean,  tech_mean, uwc_mean, pov_mean = get_means(country_info["Country Name"])
        all_means_data.append({"Country Name": country_info["Country Name"],
                                "LE Mean": le_mean,
                                "GDP Mean": gdp_mean,
                                "TECH Mean": tech_mean,
                                "UWC Mean": uwc_mean,
                                "POV Mean": pov_mean})
        # print(i, le_mean, gdp_mean,  tech_mean, uwc_mean, pov_mean)
        i += 1

    pass


def get_means(country_name):

    le_mean = -1
    gdp_mean = -1
    tech_mean = -1
    uwc_mean = -1
    pov_mean = -1

    for country_info in le_total_summ[2:]:
        if country_info["Country Name"] == country_name:
            le_mean = country_info["Mean"]

    for country_info in gdp_pcap_summ[2:]:
        if country_info["Country Name"] == country_name:
            gdp_mean = country_info["Mean"]

    for country_info in tech_expo_summ[2:]:
        if country_info["Country Name"] == country_name:
            tech_mean = country_info["Mean"]

    for country_info in udwe_child_summ[2:]:
        if country_info["Country Name"] == country_name:
            uwc_mean = country_info["Mean"]

    for country_info in pov_ratio_summ[2:]:
        if country_info["Country Name"] == country_name:
            pov_mean = country_info["Mean"]

    return le_mean, gdp_mean, tech_mean, uwc_mean, pov_mean

    pass


def load_processed_data():

    # Life expectancy at birth
    read_processed("life_expectancy.csv", le_total)
    # GDP per capita (current US$)
    read_processed("gdp_per_capita.csv", gdp_pcap)
    # High-technology exports (% of manufactured exports)
    read_processed("tech_exports.csv", tech_expo)
    # Prevalence of underweight, weight for age (% of children under 5)
    read_processed("underweight_children.csv", udwe_child)
    # Poverty headcount ratio at national poverty lines (% of population)
    read_processed("poverty_ratio.csv", pov_ratio)

    pass


def read_processed(file_name, append_list):

    # read from processed data file and add data to a list
    with open(f"./data_processed/{file_name}") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            add_dict = dict()
            add_dict['Country Name'] = row['Country Name']
            add_dict['Country Code'] = row['Country Code']
            add_dict['1960'] = row['1960']
            add_dict['1961'] = row['1961']
            add_dict['1962'] = row['1962']
            add_dict['1963'] = row['1963']
            add_dict['1964'] = row['1964']
            add_dict['1965'] = row['1965']
            add_dict['1966'] = row['1966']
            add_dict['1967'] = row['1967']
            add_dict['1968'] = row['1968']
            add_dict['1969'] = row['1969']
            add_dict['1970'] = row['1970']
            add_dict['1971'] = row['1971']
            add_dict['1972'] = row['1972']
            add_dict['1973'] = row['1973']
            add_dict['1974'] = row['1974']
            add_dict['1975'] = row['1975']
            add_dict['1976'] = row['1976']
            add_dict['1977'] = row['1977']
            add_dict['1978'] = row['1978']
            add_dict['1979'] = row['1979']
            add_dict['1980'] = row['1980']
            add_dict['1981'] = row['1981']
            add_dict['1982'] = row['1982']
            add_dict['1983'] = row['1983']
            add_dict['1984'] = row['1984']
            add_dict['1985'] = row['1985']
            add_dict['1986'] = row['1986']
            add_dict['1987'] = row['1987']
            add_dict['1988'] = row['1988']
            add_dict['1989'] = row['1989']
            add_dict['1990'] = row['1990']
            add_dict['1991'] = row['1991']
            add_dict['1992'] = row['1992']
            add_dict['1993'] = row['1993']
            add_dict['1994'] = row['1994']
            add_dict['1995'] = row['1995']
            add_dict['1996'] = row['1996']
            add_dict['1997'] = row['1997']
            add_dict['1998'] = row['1998']
            add_dict['1999'] = row['1999']
            add_dict['2000'] = row['2000']
            add_dict['2001'] = row['2001']
            add_dict['2002'] = row['2002']
            add_dict['2003'] = row['2003']
            add_dict['2004'] = row['2004']
            add_dict['2005'] = row['2005']
            add_dict['2006'] = row['2006']
            add_dict['2007'] = row['2007']
            add_dict['2008'] = row['2008']
            add_dict['2009'] = row['2009']
            add_dict['2010'] = row['2010']
            add_dict['2011'] = row['2011']
            add_dict['2012'] = row['2012']
            add_dict['2013'] = row['2013']
            add_dict['2014'] = row['2014']
            add_dict['2015'] = row['2015']
            add_dict['2016'] = row['2016']
            add_dict['2017'] = row['2017']
            add_dict['2018'] = row['2018']
            add_dict['2019'] = row['2019']
            add_dict['2020'] = row['2020']
            add_dict['2021'] = row['2021']
            add_dict['2022'] = row['2022']
            append_list.append(add_dict)
    pass


def get_qual_data():
    # Life Expectancy at Birth
    load_qual_data_list(le_total, le_total_summ)
    # GDP per Capita (current US$)
    load_qual_data_list(gdp_pcap, gdp_pcap_summ)
    # High-technology exports (% of manufactured exports)
    load_qual_data_list(tech_expo, tech_expo_summ)
    # Prevalence of underweight, weight for age (% of children under 5)
    load_qual_data_list(udwe_child, udwe_child_summ)
    # Poverty headcount ratio at national poverty lines (% of population)
    load_qual_data_list(pov_ratio, pov_ratio_summ)

    pass


def load_qual_data_list(proc_data_list, quant_data_list):

    countries_collected = 0
    for country_info in proc_data_list:
        some_data = False
        for i in range(YEAR_START, YEAR_END):
            if country_info[f"{i}"] != "..":
                some_data = True
        if some_data:
            countries_collected += 1
        else:
            # print(country_info["Country Name"])
            remove_data_from_list("Country Name", country_info["Country Name"], quant_data_list)
            pass

    quant_data_list[0]['Number Collected From'] = countries_collected

    pass


def get_quant_data():
    # Life Expectancy at Birth
    load_quant_data_list(le_total, le_total_summ, 0)
    # GDP per Capita (current US$)
    load_quant_data_list(gdp_pcap, gdp_pcap_summ, 1)
    # High-technology exports (% of manufactured exports)
    load_quant_data_list(tech_expo, tech_expo_summ, 2)
    # Prevalence of underweight, weight for age (% of children under 5)
    load_quant_data_list(udwe_child, udwe_child_summ, 3)
    # Poverty headcount ratio at national poverty lines (% of population)
    load_quant_data_list(pov_ratio, pov_ratio_summ, 4)

    pass


def load_quant_data_list(proc_data_list, quant_data_list, indic):

    match indic:
        case 0:
            setup_quant_data_list(proc_data_list, quant_data_list, 'Life Expectancy from Birth (years)')
        case 1:
            setup_quant_data_list(proc_data_list, quant_data_list, 'Gross Domestic Product GDP per capita (US$)')
        case 2:
            setup_quant_data_list(proc_data_list, quant_data_list, 'High-Technology (% of manufactured exports)')
        case 3:
            setup_quant_data_list(proc_data_list, quant_data_list, 'Underweight Children (% of children under 5)')
        case 4:
            setup_quant_data_list(proc_data_list, quant_data_list, 'National Poverty Ratio (% of population)')

    get_min(proc_data_list, quant_data_list)
    get_max(proc_data_list, quant_data_list)
    get_median_and_mean(proc_data_list, quant_data_list)

    pass


def setup_quant_data_list(proc_data_list, quant_data_list, data_type):

    quant_data_list.append({'Data Type': data_type})
    quant_data_list.append({'Country Name': 'All Countries', 'Min': None, 'Max': None, 'Median': None, 'Mean': None})

    for country_info in proc_data_list:
        add_dict = dict()
        add_dict['Country Name'] = country_info['Country Name']
        add_dict['Min'] = None
        add_dict['Max'] = None
        add_dict['Median'] = None
        add_dict['Mean'] = None
        quant_data_list.append(add_dict)

    pass


def get_median_and_mean(proc_data_list, quant_data_list):

    all_value_list = []
    all_median = None
    all_mean = None
    x = 2
    for country_info in proc_data_list:
        country_value_list = []
        country_median = None
        country_mean = None
        for i in range(YEAR_START, YEAR_END):
            if country_info[f"{i}"] != "..":
                temp = float(country_info[f"{i}"])
                country_value_list.append(temp)
                all_value_list.append(temp)
            pass  # loop through each year

        # get mean for each country
        if len(country_value_list) != 0:
            country_mean = sum(country_value_list) / len(country_value_list)
        quant_data_list[x]['Mean'] = country_mean

        # get median for each country
        # remove and sort duplicates
        country_value_list = list(set(country_value_list))
        country_value_list.sort()
        mid = len(country_value_list) / 2  # right upper bound for even
        if len(country_value_list) != 0:
            country_median = country_value_list[int(mid)]
        quant_data_list[x]['Median'] = country_median
        x += 1
        pass  # loop through each country

    # get mean for total data
    if len(all_value_list) != 0:
        all_mean = sum(all_value_list) / len(all_value_list)
    quant_data_list[1]['Mean'] = all_mean

    # get median for total data
    # remove and sort duplicates
    all_value_list = list(set(all_value_list))
    all_value_list.sort()
    mid = len(all_value_list) / 2
    if len(all_value_list) != 0:
        all_median = all_value_list[int(mid)]
    quant_data_list[1]['Median'] = all_median

    pass


def get_min(proc_data_list, quant_data_list):

    min_total = 9999999999
    x = 2
    for country_info in proc_data_list:
        min_country = 9999999999
        for i in range(YEAR_START, YEAR_END):
            if country_info[f"{i}"] != "..":
                temp = float(country_info[f"{i}"])
                if temp < min_country:
                    min_country = temp
        quant_data_list[x]['Min'] = min_country
        if min_country < min_total:
            min_total = min_country
        x += 1
    quant_data_list[1]['Min'] = min_total
    pass


def get_max(proc_data_list, quant_data_list):

    max_total = -1
    x = 2
    for country_info in proc_data_list:
        max_country = -1
        for i in range(YEAR_START, YEAR_END):
            if country_info[f"{i}"] != "..":
                temp = float(country_info[f"{i}"])
                if temp > max_country:
                    max_country = temp
        quant_data_list[x]['Max'] = max_country
        if max_country > max_total:
            max_total = max_country
        x += 1
    quant_data_list[1]['Max'] = max_total
    pass


def display_list(pass_list):

    i = 0
    for row in pass_list:
        print(i, row)
        i += 1

    pass


def remove_data_from_list(key_name, remove_id, remove_list):

    for country_info in remove_list:
        # print(country_info)
        try:
            if country_info[key_name] == remove_id:
                # removed_names.append(country_info["Country Name"])
                remove_list.remove(country_info)
                return
        except:
            pass
    pass

if __name__ == '__main__':
    evaluate_data()
