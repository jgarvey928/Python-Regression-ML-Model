# import matplotlib.pylab as plt
# import numpy as np
import csv

__author__ = "John Garvey"
__date__ = "10/14/2023"
__assignment = "Project MS03"

le_total = []
gdp_pcap = []
pov_ppop = []


def visualize_data():

    load_processed_data()

    # TODO
    print(pov_ppop[216]['Country Name'], pov_ppop[216]['2001'])


    pass


def load_processed_data():

    with open("./data_processing/gdp_per_capita.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Poverty headcount ratio at national poverty lines (% of population)
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
            gdp_pcap.append(add_dict)

    with open("./data_processing/life_expectancy.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Poverty headcount ratio at national poverty lines (% of population)
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
            le_total.append(add_dict)

    with open("./data_processing/poverty_line.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Poverty headcount ratio at national poverty lines (% of population)
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
            pov_ppop.append(add_dict)

    for entry in le_total:
        print(entry)
    for entry in gdp_pcap:
        print(entry)
    for entry in pov_ppop:
        print(entry)

    pass
