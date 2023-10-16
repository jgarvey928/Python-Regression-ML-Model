# import matplotlib.pylab as plt
# import numpy as np
import csv

__author__ = "John Garvey"
__date__ = "10/14/2023"
__assignment = "Project MS03"

# life expectancy data and quantitative data lists
le_total = []
le_total_quant = []
# GDP per Capita data and quantitative data lists
gdp_pcap = []
gdp_pcap_quant = []
# technology export percentage data and quantitative data lists
tech_expo = []
tech_expo_quant = []
# percent of underweight children data and quantitative data lists
udwe_child = []
udwe_child_quant = []
# poverty percentage for population data and quantitative data lists
pov_ratio = []
pov_ratio_quant = []


def visualize_data():

    # TODO
    load_processed_data()
    get_quant_data()
    write_quant_data_table()
    print("Number of Countries is", len(le_total))
    print("Life Expectancy in", le_total[206]['Country Name'], le_total[206]['Country Code'], "in 2015 is", int(float(le_total[206]['2015'])), "years old")
    print("GDP per Capita in", gdp_pcap[41]['Country Name'], gdp_pcap[41]['Country Code'], f"in 2015 is ${float(gdp_pcap[41]['2015']):.2f} US dollars")
    print("High-technology exports in", tech_expo[103]['Country Name'], tech_expo[103]['Country Code'], f"in 2015 is {float(tech_expo[103]['2015']):.1f} (% of manufactured exports)")
    print("Prevalence of underweight, weight for age", udwe_child[211]['Country Name'], udwe_child[211]['Country Code'], f"in 2015 is {udwe_child[211]['2015']} (% of children under 5)")
    print("Poverty headcount ratio at national poverty lines", pov_ratio[210]['Country Name'], pov_ratio[210]['Country Code'], f"in 2015 is {pov_ratio[210]['2015']} (% of population)")
    display_list(le_total_quant)
    display_list(gdp_pcap_quant)
    display_list(tech_expo_quant)
    display_list(udwe_child_quant)
    display_list(pov_ratio_quant)

    pass


def write_quant_data_table():

    

    pass


def get_quant_data():
    # Life Expectancy at Birth
    load_quant_data_list(le_total, le_total_quant, 0)
    # GDP per Capita (current US$)
    load_quant_data_list(gdp_pcap, gdp_pcap_quant, 1)
    # High-technology exports (% of manufactured exports)
    load_quant_data_list(tech_expo, tech_expo_quant, 2)
    # Prevalence of underweight, weight for age (% of children under 5)
    load_quant_data_list(udwe_child, udwe_child_quant, 3)
    # Poverty headcount ratio at national poverty lines (% of population)
    load_quant_data_list(pov_ratio, pov_ratio_quant, 4)

    pass


def load_quant_data_list(proc_data_list, quant_data_list, indic):

    match indic:
        case 0:
            setup_quant_data_list(proc_data_list, quant_data_list, 'Life Expectancy from Birth')
        case 1:
            setup_quant_data_list(proc_data_list, quant_data_list, 'GDP per Capita (current US$)')
        case 2:
            setup_quant_data_list(proc_data_list, quant_data_list, 'High-technology exports (% of manufactured exports)')
        case 3:
            setup_quant_data_list(proc_data_list, quant_data_list, 'Prevalence of underweight, weight for age (% of children under 5)')
        case 4:
            setup_quant_data_list(proc_data_list, quant_data_list, 'Poverty headcount ratio at national poverty lines (% of population)')

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
        for i in range(16):
            if i < 10:
                if country_info[f"200{i}"] != "..":
                    temp = float(country_info[f"200{i}"])
                    country_value_list.append(temp)
                    all_value_list.append(temp)
            else:
                if country_info[f"20{i}"] != "..":
                    temp = float(country_info[f"20{i}"])
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
        for i in range(16):
            if i < 10:
                if country_info[f"200{i}"] != "..":
                    temp = float(country_info[f"200{i}"])
                    if temp < min_country:
                        min_country = temp
            else:
                if country_info[f"20{i}"] != "..":
                    temp = float(country_info[f"20{i}"])
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
        for i in range(16):
            if i < 10:
                if country_info[f"200{i}"] != "..":
                    temp = float(country_info[f"200{i}"])
                    if temp > max_country:
                        max_country = temp
            else:
                if country_info[f"20{i}"] != "..":
                    temp = float(country_info[f"20{i}"])
                    if temp > max_country:
                        max_country = temp
        quant_data_list[x]['Max'] = max_country
        if max_country > max_total:
            max_total = max_country
        x += 1
    quant_data_list[1]['Max'] = max_total
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
    with open(f"./data_processing/{file_name}") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            add_dict = dict()
            add_dict['Country Name'] = row['Country Name']
            add_dict['Country Code'] = row['Country Code']
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
            append_list.append(add_dict)
    pass


def display_list(pass_list):

    i = 0
    for row in pass_list:
        print(i, row)
        i += 1

    pass
