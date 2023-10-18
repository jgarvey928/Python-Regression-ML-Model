import csv

__author__ = "John Garvey"
__date__ = "10/14/2023"
__assignment = "Project MS03"

# Data Format:
""" 
['Series Name', 'Series Code', 'Country Name', 'Country Code', '2000 [YR2000]', '2001 [YR2001]', '2002 [YR2002]',
'2003 [YR2003]', '2004 [YR2004]', '2005 [YR2005]', '2006 [YR2006]', '2007 [YR2007]', '2008 [YR2008]', '2009 [YR2009]',
'2010 [YR2010]', '2011 [YR2011]', '2012 [YR2012]', '2013 [YR2013]', '2014 [YR2014]', '2015 [YR2015]'] 
"""


def process_data(input_filename):
    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        new_fieldnames = "Country Name,Country Code,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015\n"
        life_expectancy_file = open("data_processed/life_expectancy.csv", "w")
        life_expectancy_file.write(new_fieldnames)
        gdp_per_capita_file = open("data_processed/gdp_per_capita.csv", "w")
        gdp_per_capita_file.write(new_fieldnames)
        tech_exports_file = open("data_processed/tech_exports.csv", "w")
        tech_exports_file.write(new_fieldnames)
        underweight_children_file = open("data_processed/underweight_children.csv", "w")
        underweight_children_file.write(new_fieldnames)
        poverty_ratio_file = open("data_processed/poverty_ratio.csv", "w")
        poverty_ratio_file.write(new_fieldnames)
        for row in reader:
            # Life expectancy at birth
            if row['Series Code'] == "SP.DYN.LE00.IN":
                # !!! NEED TO PUT PARATHESIS "" AROUND THE COUNTRY NAME BECAUSE CAN CONTAIN A COMMA FOR CSV!!!
                life_expectancy_file.write("\""+row['Country Name']+"\",")
                life_expectancy_file.write(f"{row['Country Code']},{row['2000 [YR2000]']},"
                              f"{row['2001 [YR2001]']},{row['2002 [YR2002]']},{row['2003 [YR2003]']},{row['2004 [YR2004]']},"
                              f"{row['2005 [YR2005]']},{row['2006 [YR2006]']},{row['2007 [YR2007]']},{row['2008 [YR2008]']},"
                              f"{row['2009 [YR2009]']},{row['2010 [YR2010]']},{row['2011 [YR2011]']},{row['2012 [YR2012]']},"
                              f"{row['2013 [YR2013]']},{row['2014 [YR2014]']},{row['2015 [YR2015]']}\n")
            # GDP per capita (current US$)
            if row['Series Code'] == "NY.GDP.PCAP.CD":
                gdp_per_capita_file.write("\"" + row['Country Name'] + "\",")
                gdp_per_capita_file.write(f"{row['Country Code']},{row['2000 [YR2000]']},"
                              f"{row['2001 [YR2001]']},{row['2002 [YR2002]']},{row['2003 [YR2003]']},{row['2004 [YR2004]']},"
                              f"{row['2005 [YR2005]']},{row['2006 [YR2006]']},{row['2007 [YR2007]']},{row['2008 [YR2008]']},"
                              f"{row['2009 [YR2009]']},{row['2010 [YR2010]']},{row['2011 [YR2011]']},{row['2012 [YR2012]']},"
                              f"{row['2013 [YR2013]']},{row['2014 [YR2014]']},{row['2015 [YR2015]']}\n")
            # High-technology exports (% of manufactured exports)
            if row['Series Code'] == "TX.VAL.TECH.MF.ZS":
                tech_exports_file.write("\"" + row['Country Name'] + "\",")
                tech_exports_file.write(f"{row['Country Code']},{row['2000 [YR2000]']},"
                              f"{row['2001 [YR2001]']},{row['2002 [YR2002]']},{row['2003 [YR2003]']},{row['2004 [YR2004]']},"
                              f"{row['2005 [YR2005]']},{row['2006 [YR2006]']},{row['2007 [YR2007]']},{row['2008 [YR2008]']},"
                              f"{row['2009 [YR2009]']},{row['2010 [YR2010]']},{row['2011 [YR2011]']},{row['2012 [YR2012]']},"
                              f"{row['2013 [YR2013]']},{row['2014 [YR2014]']},{row['2015 [YR2015]']}\n")
            # Prevalence of underweight, weight for age (% of children under 5)
            if row['Series Code'] == "SH.STA.MALN.ZS":
                underweight_children_file.write("\"" + row['Country Name'] + "\",")
                underweight_children_file.write(f"{row['Country Code']},{row['2000 [YR2000]']},"
                                        f"{row['2001 [YR2001]']},{row['2002 [YR2002]']},{row['2003 [YR2003]']},{row['2004 [YR2004]']},"
                                        f"{row['2005 [YR2005]']},{row['2006 [YR2006]']},{row['2007 [YR2007]']},{row['2008 [YR2008]']},"
                                        f"{row['2009 [YR2009]']},{row['2010 [YR2010]']},{row['2011 [YR2011]']},{row['2012 [YR2012]']},"
                                        f"{row['2013 [YR2013]']},{row['2014 [YR2014]']},{row['2015 [YR2015]']}\n")
            # Poverty headcount ratio at national poverty lines (% of population)
            if row['Series Code'] == "SI.POV.NAHC":
                poverty_ratio_file.write("\"" + row['Country Name'] + "\",")
                poverty_ratio_file.write(f"{row['Country Code']},{row['2000 [YR2000]']},"
                                        f"{row['2001 [YR2001]']},{row['2002 [YR2002]']},{row['2003 [YR2003]']},{row['2004 [YR2004]']},"
                                        f"{row['2005 [YR2005]']},{row['2006 [YR2006]']},{row['2007 [YR2007]']},{row['2008 [YR2008]']},"
                                        f"{row['2009 [YR2009]']},{row['2010 [YR2010]']},{row['2011 [YR2011]']},{row['2012 [YR2012]']},"
                                        f"{row['2013 [YR2013]']},{row['2014 [YR2014]']},{row['2015 [YR2015]']}\n")

        life_expectancy_file.close()
        gdp_per_capita_file.close()
        tech_exports_file.close()
        underweight_children_file.close()
        poverty_ratio_file.close()
    pass



