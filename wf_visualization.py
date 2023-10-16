# import matplotlib.pylab as plt
# import numpy as np
import csv

__author__ = "John Garvey"
__date__ = "10/14/2023"
__assignment = "Project MS03"

le_total = []
gdp_pcap = []
tech_expo = []
udwe_child = []

def visualize_data():

    load_processed_data()

    # TODO
    i = 0
    for entry in le_total:
        print(i, entry)
        i += 1
    i = 0
    for entry in gdp_pcap:
        print(i, entry)
        i += 1
    i = 0
    for entry in tech_expo:
        print(i, entry)
        i += 1
    i = 0
    for entry in udwe_child:
        print(i, entry)
        i += 1

    print("Number of Countries is", len(le_total))
    print("Number of Countries is", len(gdp_pcap))
    print("Number of Countries is", len(tech_expo))
    print("Number of Countries is", len(udwe_child))
    print("Life Expectancy in", le_total[206]['Country Name'], "in 2015 is", int(float(le_total[206]['2015'])), "years old")
    print("GDP per Capita in", gdp_pcap[206]['Country Name'], f"in 2015 is ${float(gdp_pcap[206]['2015']):.2f} US dollars")
    print("High-technology exports in", tech_expo[206]['Country Name'], f"in 2015 is {float(tech_expo[206]['2015']):.1f} (% of manufactured exports)")
    print("Prevalence of underweight, weight for age", udwe_child[206]['Country Name'], f"in 2015 is {udwe_child[206]['2015']} (% of children under 5)")


    pass


def load_processed_data():

    with open("./data_processing/life_expectancy.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Life expectancy at birth
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

    with open("./data_processing/gdp_per_capita.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # GDP per capita (current US$)
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

    with open("./data_processing/tech_exports.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # High-technology exports (% of manufactured exports)
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
            tech_expo.append(add_dict)

    with open("./data_processing/underweight_children.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Prevalence of underweight, weight for age (% of children under 5)
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
            udwe_child.append(add_dict)

    pass
