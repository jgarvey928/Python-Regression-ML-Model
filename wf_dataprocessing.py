import csv

__author__ = "John Garvey"
__date__ = "10/14/2023"
__assignment = "Project MS03"

# Data Format:
"""  NEEDS UPDATING!!!
['Series Name', 'Series Code', 'Country Name', 'Country Code', '2000 [YR2000]', '2001 [YR2001]', '2002 [YR2002]',
'2003 [YR2003]', '2004 [YR2004]', '2005 [YR2005]', '2006 [YR2006]', '2007 [YR2007]', '2008 [YR2008]', '2009 [YR2009]',
'2010 [YR2010]', '2011 [YR2011]', '2012 [YR2012]', '2013 [YR2013]', '2014 [YR2014]', '2015 [YR2015]'] 
"""


def process_data(input_filename):
    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        new_fieldnames = ("Country Name,Country Code,"
                          +"1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,"
                          +"1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,"
                          +"1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,"
                          +"1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,"
                          +"2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,"
                          +"2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,"
                          +"2020,2021,2022\n")
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
                life_expectancy_file.write(f"{row['Country Code']},{row['1960 [YR1960]']},"
                              f"{row['1961 [YR1961]']},{row['1962 [YR1962]']},{row['1963 [YR1963]']},{row['1964 [YR1964]']},"                                             
                              f"{row['1965 [YR1965]']},{row['1966 [YR1966]']},{row['1967 [YR1967]']},{row['1968 [YR1968]']},"                                                 
                              f"{row['1969 [YR1969]']},{row['1970 [YR1970]']},{row['1971 [YR1971]']},{row['1972 [YR1972]']},"                                             
                              f"{row['1973 [YR1973]']},{row['1974 [YR1974]']},{row['1975 [YR1975]']},{row['1976 [YR1976]']},"                                               
                              f"{row['1977 [YR1977]']},{row['1978 [YR1978]']},{row['1979 [YR1979]']},{row['1980 [YR1980]']},"                                   
                              f"{row['1981 [YR1981]']},{row['1982 [YR1982]']},{row['1983 [YR1983]']},{row['1984 [YR1984]']},"                                            
                              f"{row['1985 [YR1985]']},{row['1986 [YR1986]']},{row['1987 [YR1987]']},{row['1988 [YR1988]']},"                                            
                              f"{row['1989 [YR1989]']},{row['1990 [YR1990]']},{row['1991 [YR1991]']},{row['1992 [YR1992]']},"                                              
                              f"{row['1993 [YR1993]']},{row['1994 [YR1994]']},{row['1995 [YR1995]']},{row['1996 [YR1996]']},"                                           
                              f"{row['1997 [YR1997]']},{row['1998 [YR1998]']},{row['1999 [YR1999]']},{row['2000 [YR2000]']},"                    
                              f"{row['2001 [YR2001]']},{row['2002 [YR2002]']},{row['2003 [YR2003]']},{row['2004 [YR2004]']},"
                              f"{row['2005 [YR2005]']},{row['2006 [YR2006]']},{row['2007 [YR2007]']},{row['2008 [YR2008]']},"
                              f"{row['2009 [YR2009]']},{row['2010 [YR2010]']},{row['2011 [YR2011]']},{row['2012 [YR2012]']},"
                              f"{row['2013 [YR2013]']},{row['2014 [YR2014]']},{row['2015 [YR2015]']},{row['2016 [YR2016]']},"     
                              f"{row['2017 [YR2017]']},{row['2018 [YR2018]']},{row['2019 [YR2019]']},{row['2020 [YR2020]']},"                                             
                              f"{row['2021 [YR2021]']},{row['2022 [YR2022]']}\n")
            # GDP per capita (current US$)
            if row['Series Code'] == "NY.GDP.PCAP.CD":
                gdp_per_capita_file.write("\"" + row['Country Name'] + "\",")
                gdp_per_capita_file.write(f"{row['Country Code']},{row['1960 [YR1960]']},"
                              f"{row['1961 [YR1961]']},{row['1962 [YR1962]']},{row['1963 [YR1963]']},{row['1964 [YR1964]']},"                                             
                              f"{row['1965 [YR1965]']},{row['1966 [YR1966]']},{row['1967 [YR1967]']},{row['1968 [YR1968]']},"                                                 
                              f"{row['1969 [YR1969]']},{row['1970 [YR1970]']},{row['1971 [YR1971]']},{row['1972 [YR1972]']},"                                             
                              f"{row['1973 [YR1973]']},{row['1974 [YR1974]']},{row['1975 [YR1975]']},{row['1976 [YR1976]']},"                                               
                              f"{row['1977 [YR1977]']},{row['1978 [YR1978]']},{row['1979 [YR1979]']},{row['1980 [YR1980]']},"                                   
                              f"{row['1981 [YR1981]']},{row['1982 [YR1982]']},{row['1983 [YR1983]']},{row['1984 [YR1984]']},"                                            
                              f"{row['1985 [YR1985]']},{row['1986 [YR1986]']},{row['1987 [YR1987]']},{row['1988 [YR1988]']},"                                            
                              f"{row['1989 [YR1989]']},{row['1990 [YR1990]']},{row['1991 [YR1991]']},{row['1992 [YR1992]']},"                                              
                              f"{row['1993 [YR1993]']},{row['1994 [YR1994]']},{row['1995 [YR1995]']},{row['1996 [YR1996]']},"                                           
                              f"{row['1997 [YR1997]']},{row['1998 [YR1998]']},{row['1999 [YR1999]']},{row['2000 [YR2000]']},"                    
                              f"{row['2001 [YR2001]']},{row['2002 [YR2002]']},{row['2003 [YR2003]']},{row['2004 [YR2004]']},"
                              f"{row['2005 [YR2005]']},{row['2006 [YR2006]']},{row['2007 [YR2007]']},{row['2008 [YR2008]']},"
                              f"{row['2009 [YR2009]']},{row['2010 [YR2010]']},{row['2011 [YR2011]']},{row['2012 [YR2012]']},"
                              f"{row['2013 [YR2013]']},{row['2014 [YR2014]']},{row['2015 [YR2015]']},{row['2016 [YR2016]']},"     
                              f"{row['2017 [YR2017]']},{row['2018 [YR2018]']},{row['2019 [YR2019]']},{row['2020 [YR2020]']},"                                             
                              f"{row['2021 [YR2021]']},{row['2022 [YR2022]']}\n")
            # High-technology exports (% of manufactured exports)
            if row['Series Code'] == "TX.VAL.TECH.MF.ZS":
                tech_exports_file.write("\"" + row['Country Name'] + "\",")
                tech_exports_file.write(f"{row['Country Code']},{row['1960 [YR1960]']},"
                              f"{row['1961 [YR1961]']},{row['1962 [YR1962]']},{row['1963 [YR1963]']},{row['1964 [YR1964]']},"                                             
                              f"{row['1965 [YR1965]']},{row['1966 [YR1966]']},{row['1967 [YR1967]']},{row['1968 [YR1968]']},"                                                 
                              f"{row['1969 [YR1969]']},{row['1970 [YR1970]']},{row['1971 [YR1971]']},{row['1972 [YR1972]']},"                                             
                              f"{row['1973 [YR1973]']},{row['1974 [YR1974]']},{row['1975 [YR1975]']},{row['1976 [YR1976]']},"                                               
                              f"{row['1977 [YR1977]']},{row['1978 [YR1978]']},{row['1979 [YR1979]']},{row['1980 [YR1980]']},"                                   
                              f"{row['1981 [YR1981]']},{row['1982 [YR1982]']},{row['1983 [YR1983]']},{row['1984 [YR1984]']},"                                            
                              f"{row['1985 [YR1985]']},{row['1986 [YR1986]']},{row['1987 [YR1987]']},{row['1988 [YR1988]']},"                                            
                              f"{row['1989 [YR1989]']},{row['1990 [YR1990]']},{row['1991 [YR1991]']},{row['1992 [YR1992]']},"                                              
                              f"{row['1993 [YR1993]']},{row['1994 [YR1994]']},{row['1995 [YR1995]']},{row['1996 [YR1996]']},"                                           
                              f"{row['1997 [YR1997]']},{row['1998 [YR1998]']},{row['1999 [YR1999]']},{row['2000 [YR2000]']},"                    
                              f"{row['2001 [YR2001]']},{row['2002 [YR2002]']},{row['2003 [YR2003]']},{row['2004 [YR2004]']},"
                              f"{row['2005 [YR2005]']},{row['2006 [YR2006]']},{row['2007 [YR2007]']},{row['2008 [YR2008]']},"
                              f"{row['2009 [YR2009]']},{row['2010 [YR2010]']},{row['2011 [YR2011]']},{row['2012 [YR2012]']},"
                              f"{row['2013 [YR2013]']},{row['2014 [YR2014]']},{row['2015 [YR2015]']},{row['2016 [YR2016]']},"     
                              f"{row['2017 [YR2017]']},{row['2018 [YR2018]']},{row['2019 [YR2019]']},{row['2020 [YR2020]']},"                                             
                              f"{row['2021 [YR2021]']},{row['2022 [YR2022]']}\n")
            # Prevalence of underweight, weight for age (% of children under 5)
            if row['Series Code'] == "SH.STA.MALN.ZS":
                underweight_children_file.write("\"" + row['Country Name'] + "\",")
                underweight_children_file.write(f"{row['Country Code']},{row['1960 [YR1960]']},"
                              f"{row['1961 [YR1961]']},{row['1962 [YR1962]']},{row['1963 [YR1963]']},{row['1964 [YR1964]']},"                                             
                              f"{row['1965 [YR1965]']},{row['1966 [YR1966]']},{row['1967 [YR1967]']},{row['1968 [YR1968]']},"                                                 
                              f"{row['1969 [YR1969]']},{row['1970 [YR1970]']},{row['1971 [YR1971]']},{row['1972 [YR1972]']},"                                             
                              f"{row['1973 [YR1973]']},{row['1974 [YR1974]']},{row['1975 [YR1975]']},{row['1976 [YR1976]']},"                                               
                              f"{row['1977 [YR1977]']},{row['1978 [YR1978]']},{row['1979 [YR1979]']},{row['1980 [YR1980]']},"                                   
                              f"{row['1981 [YR1981]']},{row['1982 [YR1982]']},{row['1983 [YR1983]']},{row['1984 [YR1984]']},"                                            
                              f"{row['1985 [YR1985]']},{row['1986 [YR1986]']},{row['1987 [YR1987]']},{row['1988 [YR1988]']},"                                            
                              f"{row['1989 [YR1989]']},{row['1990 [YR1990]']},{row['1991 [YR1991]']},{row['1992 [YR1992]']},"                                              
                              f"{row['1993 [YR1993]']},{row['1994 [YR1994]']},{row['1995 [YR1995]']},{row['1996 [YR1996]']},"                                           
                              f"{row['1997 [YR1997]']},{row['1998 [YR1998]']},{row['1999 [YR1999]']},{row['2000 [YR2000]']},"                    
                              f"{row['2001 [YR2001]']},{row['2002 [YR2002]']},{row['2003 [YR2003]']},{row['2004 [YR2004]']},"
                              f"{row['2005 [YR2005]']},{row['2006 [YR2006]']},{row['2007 [YR2007]']},{row['2008 [YR2008]']},"
                              f"{row['2009 [YR2009]']},{row['2010 [YR2010]']},{row['2011 [YR2011]']},{row['2012 [YR2012]']},"
                              f"{row['2013 [YR2013]']},{row['2014 [YR2014]']},{row['2015 [YR2015]']},{row['2016 [YR2016]']},"     
                              f"{row['2017 [YR2017]']},{row['2018 [YR2018]']},{row['2019 [YR2019]']},{row['2020 [YR2020]']},"                                             
                              f"{row['2021 [YR2021]']},{row['2022 [YR2022]']}\n")
            # Poverty headcount ratio at national poverty lines (% of population)
            if row['Series Code'] == "SI.POV.NAHC":
                poverty_ratio_file.write("\"" + row['Country Name'] + "\",")
                poverty_ratio_file.write(f"{row['Country Code']},{row['1960 [YR1960]']},"
                              f"{row['1961 [YR1961]']},{row['1962 [YR1962]']},{row['1963 [YR1963]']},{row['1964 [YR1964]']},"                                             
                              f"{row['1965 [YR1965]']},{row['1966 [YR1966]']},{row['1967 [YR1967]']},{row['1968 [YR1968]']},"                                                 
                              f"{row['1969 [YR1969]']},{row['1970 [YR1970]']},{row['1971 [YR1971]']},{row['1972 [YR1972]']},"                                             
                              f"{row['1973 [YR1973]']},{row['1974 [YR1974]']},{row['1975 [YR1975]']},{row['1976 [YR1976]']},"                                               
                              f"{row['1977 [YR1977]']},{row['1978 [YR1978]']},{row['1979 [YR1979]']},{row['1980 [YR1980]']},"                                   
                              f"{row['1981 [YR1981]']},{row['1982 [YR1982]']},{row['1983 [YR1983]']},{row['1984 [YR1984]']},"                                            
                              f"{row['1985 [YR1985]']},{row['1986 [YR1986]']},{row['1987 [YR1987]']},{row['1988 [YR1988]']},"                                            
                              f"{row['1989 [YR1989]']},{row['1990 [YR1990]']},{row['1991 [YR1991]']},{row['1992 [YR1992]']},"                                              
                              f"{row['1993 [YR1993]']},{row['1994 [YR1994]']},{row['1995 [YR1995]']},{row['1996 [YR1996]']},"                                           
                              f"{row['1997 [YR1997]']},{row['1998 [YR1998]']},{row['1999 [YR1999]']},{row['2000 [YR2000]']},"                    
                              f"{row['2001 [YR2001]']},{row['2002 [YR2002]']},{row['2003 [YR2003]']},{row['2004 [YR2004]']},"
                              f"{row['2005 [YR2005]']},{row['2006 [YR2006]']},{row['2007 [YR2007]']},{row['2008 [YR2008]']},"
                              f"{row['2009 [YR2009]']},{row['2010 [YR2010]']},{row['2011 [YR2011]']},{row['2012 [YR2012]']},"
                              f"{row['2013 [YR2013]']},{row['2014 [YR2014]']},{row['2015 [YR2015]']},{row['2016 [YR2016]']},"     
                              f"{row['2017 [YR2017]']},{row['2018 [YR2018]']},{row['2019 [YR2019]']},{row['2020 [YR2020]']},"                                             
                              f"{row['2021 [YR2021]']},{row['2022 [YR2022]']}\n")

        life_expectancy_file.close()
        gdp_per_capita_file.close()
        tech_exports_file.close()
        underweight_children_file.close()
        poverty_ratio_file.close()
    pass



