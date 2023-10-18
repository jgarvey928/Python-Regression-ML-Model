# INSTALLED matplotlib
import matplotlib.pylab as plt

import csv

__author__ = "John Garvey"
__date__ = "10/14/2023"
__assignment = "Project MS03"

# NUMBER OF COUNTRIES IN DATASET
NUMB_COUNTRIES = 217
# NUMBER OF DATA CATEGORIES
NUMB_CATEGORIES = 5
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
# all correlations data list
all_correlations = []


def visualize_data():

    # Main Visualization Process
    load_processed_data()

    #############################################################################
    """                PANAMA OUTLIER DATA REMOVED FOR TECH EXPO              """
    remove_data_from_list("Country Name", "Panama", tech_expo)
    #############################################################################

    get_quant_data()
    get_qual_data()
    write_summary_data_table()
    get_correlations()
    write_correlations_data_table()
    create_scatter_plots()

    # TODO Create a histogram for qualitative data
    create_histogram()

    """ PRIMITIVE TESTS """
    # print("Number of Countries is", len(le_total))
    # print("Life Expectancy in", le_total[206]['Country Name'], le_total[206]['Country Code'], "in 2015 is", int(float(le_total[206]['2015'])), "years old")
    # print("GDP per Capita in", gdp_pcap[41]['Country Name'], gdp_pcap[41]['Country Code'], f"in 2015 is ${float(gdp_pcap[41]['2015']):.2f} US dollars")
    # print("High-technology exports in", tech_expo[103]['Country Name'], tech_expo[103]['Country Code'], f"in 2015 is {float(tech_expo[103]['2015']):.1f} (% of manufactured exports)")
    # print("Prevalence of underweight, weight for age", udwe_child[211]['Country Name'], udwe_child[211]['Country Code'], f"in 2015 is {udwe_child[211]['2015']} (% of children under 5)")
    # print("Poverty headcount ratio at national poverty lines", pov_ratio[210]['Country Name'], pov_ratio[210]['Country Code'], f"in 2015 is {pov_ratio[210]['2015']} (% of population)")

    # display_list(le_total)
    # display_list(gdp_pcap)
    # display_list(tech_expo)
    # display_list(udwe_child)

    # display_list(le_total_summ)
    # display_list(gdp_pcap_summ)
    # display_list(tech_expo_summ)
    # display_list(udwe_child_summ)
    # display_list(pov_ratio_summ)

    # display_list(all_correlations)

    pass


def create_histogram():

    # le_total_summ = LEB
    # gdp_pcap_summ = GDP
    # tech_expo_summ = HTE
    # udwe_child_summ = UWC
    # pov_ratio_summ = NPR

    numbers_collected = [
        le_total_summ[0]["Number Collected From"],
        gdp_pcap_summ[0]["Number Collected From"],
        tech_expo_summ[0]["Number Collected From"],
        udwe_child_summ[0]["Number Collected From"],
        pov_ratio_summ[0]["Number Collected From"],
    ]

    category_types = ["LEB", "GDP", "HTE", "UWC", "NPR"]

    fig, ax = plt.subplots()
    ax.set(title=r'Data Category Sample Sizes ', ylabel='Number of Countries Collectd From', xlabel="Data Categories")
    bars = ax.bar(category_types, numbers_collected)
    bars[0].set_color('green')
    bars[0].set_label("LEB = "+le_total_summ[0]["Data Type"])
    bars[1].set_color('red')
    bars[1].set_label("GDP = "+gdp_pcap_summ[0]["Data Type"])
    bars[2].set_color('purple')
    bars[2].set_label("HTE = "+tech_expo_summ[0]["Data Type"])
    bars[3].set_color('orange')
    bars[3].set_label("UWC = "+udwe_child_summ[0]["Data Type"])
    bars[4].set_color('blue')
    bars[4].set_label("NPR = "+pov_ratio_summ[0]["Data Type"])
    ax.bar_label(bars, fmt='%.2f')
    ax.legend(loc='lower right')
    fig.savefig("visuals/categories_sample_size.png")

    pass


def create_scatter_plots():

    # : Create scatter plots for all pairs of quantitative features that you selected.
    #  For example, if you have quantitative features A, B, and C, you will construct AB, AC, and BC.
    #  output should be saved to visuals\*.png where * represents different filenames of your choice.
    #  plot the MEANS for all pair categories of data i.e. LEB, GDP, HTE, UWC, NPR

    # LEB_GDP = le_total_summ, gdp_pcap_summ
    create_pair_plot(le_total_summ, gdp_pcap_summ, "LEB_GDP")

    # LEB_HTE = le_total_summ, tech_expo_summ
    create_pair_plot(le_total_summ, tech_expo_summ, "LEB_HTE")

    # LEB_UWC = le_total_summ, udwe_child_summ
    create_pair_plot(le_total_summ, udwe_child_summ, "LEB_UWC")

    # LEB_NPR = le_total_summ, pov_ratio_summ
    """ 
    There is noticeable difference between the plot and the correlation
    The correlation is -0.324 but the plot seems to suggest a much stronger
    negative correlation. This is because the plot is using all every countries
    mean life expectancy and mean poverty ratio which shows a stronger correlation.
    Each countries correlation is calculated from the matching data in each year for both 
    life expectancy and  poverty ratio, if there is no data in each matching year then it not
    add to the correlation calculation. Which means the calc correlation will use much fewer values
    for its calculations. Each country may only have a couple entries for NPR so the only compare those
    two entries with the corresponding years value for the LEB. Which means much different representations of the LEB
    than the mean LEB of that country.
    """
    create_pair_plot(le_total_summ, pov_ratio_summ, "LEB_NPR")

    # GDP_HTE = gdp_pcap_summ, tech_expo_summ
    create_pair_plot(gdp_pcap_summ, tech_expo_summ, "GDP_HTE")

    # GDP_UWC = gdp_pcap_summ, udwe_child_summ
    create_pair_plot(gdp_pcap_summ, udwe_child_summ, "GDP_UWC")

    # GDP_NPR = gdp_pcap_summ, pov_ratio_summ
    create_pair_plot(gdp_pcap_summ, pov_ratio_summ, "GDP_NPR")

    # HTE_UWC = tech_expo_summ, udwe_child_summ
    create_pair_plot(tech_expo_summ, udwe_child_summ, "HTE_UWC")

    # HTE_NPR = tech_expo_summ, pov_ratio_summ
    create_pair_plot(tech_expo_summ, pov_ratio_summ, "HTE_NPR")

    # UWC_NPR = udwe_child_summ, pov_ratio_summ
    create_pair_plot(udwe_child_summ, pov_ratio_summ, "UWC_NPR")

    pass


def create_pair_plot(summ_data_y, summ_data_x, indic):

    data_means_x = []
    data_means_y = []

    for i in range(2, NUMB_COUNTRIES):
        data_means_x.append(summ_data_x[i]['Mean'])
        data_means_y.append(summ_data_y[i]['Mean'])

    # display_list(data_means_x)
    # display_list(data_means_y)

    fig, ax = plt.subplots()
    match indic:
        case "LEB_GDP":
            title = "Life Expectancy VS GDP"
            ax.scatter(data_means_x, data_means_y, color="red")
            ax.set(title=title, ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}.png")
            ax.set(xlim=[0, 40000], title=title+" Focused", ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}_focused.png")
        case "LEB_HTE":
            title = "Life Expectancy VS Technology Export Perc."
            ax.scatter(data_means_x, data_means_y, color="green")
            ax.set(title=title, ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}.png")
        case "LEB_UWC":
            title = "Life Expectancy VS Underweight Children"
            ax.scatter(data_means_x, data_means_y, color="purple")
            ax.set(title=title, ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}.png")
        case "LEB_NPR":
            title = "Life Expectancy VS National Poverty Ratio"
            ax.scatter(data_means_x, data_means_y, color="hotpink")
            ax.set(title=title, ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}.png")
        case "GDP_HTE":
            title = "GDP VS Technology Export Perc."
            ax.scatter(data_means_x, data_means_y, color="black")
            ax.set(title=title, ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}.png")
        case "GDP_UWC":
            title = "GDP VS Underweight Children"
            ax.scatter(data_means_x, data_means_y, color="magenta")
            ax.set(title=title, ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}.png")
            ax.set(ylim=[0, 20000], title=title+" Focused", ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}_focused.png")
        case "GDP_NPR":
            title = "GDP VS National Poverty Ratio"
            ax.scatter(data_means_x, data_means_y, color="blue")
            ax.set(title=title, ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}.png")
            ax.set(ylim=[0, 20000], title=title+" Focused", ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}_focused.png")
        case "HTE_UWC":
            title = "Technology Export Perc. VS Underweight Children"
            ax.scatter(data_means_x, data_means_y, color="orange")
            ax.set(title=title, ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}.png")
        case "HTE_NPR":
            title = "Technology Export Perc. VS National Poverty Ratio"
            ax.scatter(data_means_x, data_means_y, color="darkblue")
            ax.set(title=title, ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}.png")
        case "UWC_NPR":
            title = "Underweight Children VS National Poverty Ratio"
            ax.scatter(data_means_x, data_means_y, color="brown")
            ax.set(title=title, ylabel=summ_data_y[0]["Data Type"], xlabel=summ_data_x[0]["Data Type"])
            fig.savefig(f"visuals/{title.lower().replace(' ', '_')}.png")

    pass


def write_correlations_data_table():

    # : Outputs the global mean pairwise correlations into a table in data_processed/correlations.txt
    correlations_file = open("data_processed/correlations.txt", "w")
    correlations_file.write('=======================================================================|\n')
    correlations_file.write("                  Global Correlation Data For 2000-2015                |\n")
    correlations_file.write('=======================================================================|\n')
    correlations_file.write(" Acronyms:                                                             |\n"
                            "  LEB = Life Expectancy from Birth                                     |\n"
                            "  GDP = Gross Domestic Product                                         |\n"
                            "  HTE = High-Technology Exports                                        |\n"
                            "  UWC = Underweight Children                                           |\n"
                            "  NPR = National Poverty Ratio                                         |\n")
    correlations_file.write('=======================================================================|\n')
    correlations_file.write('           |    LEB    |    GDP    |    HTE    |    UWC    |    NPR    |\n')
    correlations_file.write('-----------------------------------------------------------------------|\n')
    correlations_file.write('    LEB    |   1.000   |           |           |           |           |\n')
    correlations_file.write('-----------------------------------------------------------------------|\n')
    correlations_file.write(f'    GDP    |   {all_correlations[0]["LEB_GDP"]:.3f}   |   1.000   |           |           |           |\n')
    correlations_file.write('-----------------------------------------------------------------------|\n')
    correlations_file.write(f'    HTE    |   {all_correlations[0]["LEB_HTE"]:.3f}   |  {all_correlations[0]["GDP_HTE"]:.3f}   |   1.000   |           |           |\n')
    correlations_file.write('-----------------------------------------------------------------------|\n')
    correlations_file.write(f'    UWC    |  {all_correlations[0]["LEB_UWC"]:.3f}   |  {all_correlations[0]["GDP_UWC"]:.3f}   |  {all_correlations[0]["HTE_UWC"]:.3f}   |   1.000   |           |\n')
    correlations_file.write('-----------------------------------------------------------------------|\n')
    correlations_file.write(f'    NPR    |  {all_correlations[0]["LEB_NPR"]:.3f}   |  {all_correlations[0]["GDP_NPR"]:.3f}   |   {all_correlations[0]["HTE_NPR"]:.3f}   |   {all_correlations[0]["UWC_NPR"]:.3f}   |   1.000   |\n')
    correlations_file.write('-----------------------------------------------------------------------|\n')
    correlations_file.close()

    pass


def get_correlations():

    # : Get the pairwise correlations for all countries for each of the categories
    # : Then get the global means for the pairwise correlations for each of the categories
    # : First find pairwise correlations for the Life Expectancy (LE) and GDP for each country
    # : Then save these correlations in a dictionary for each country in the all_correlations list
    # : Then repeat this process find and store all the pairwise correlations for each category in order below
    """
        Acronyms :
            Life Expectancy from Birth = LEB
            Gross Domestic Product = GDP
            High-Technology Exports = HTE
            Underweight Children = UWC
            National Poverty Ratio = NPR

        Steps:
            1.   LEB_GDP
            2.   LEB_HTE
            3.   LEB_UWC
            4.   LEB_NPR
            5.   GDP_HTE
            6.   GDP_UWC
            7.   GDP_NPR
            8.   HTE_UWC
            9.   HTE_NPR
            10.  UWC_NPR

        Data Lists :
             all_correlations - stores all pairwise correlations for each country
             le_total - contains the variables for correlations
             le_total_summ - contains the means for the variables
             gdp_pcap
             gdp_pcap_summ
             tech_expo
             tech_expo_summ
             udwe_child
             udwe_child_summ
             pov_ratio
             pov_ratio_summ

        Dictionary Fields (e.x. index=0):
            {'Country Name': 'All Countries',
             'LEB_GDP': Global Mean,
             'LEB_HTE': Global Mean,
             'LEB_UWC': Global Mean,
             'LEB_NPR': Global Mean,
             'GDP_HTE': Global Mean,
             'GDP_UWC': Global Mean,
             'GDP_NPR': Global Mean,
             'HTE_UWC': Global Mean,
             'HTE_NPR': Global Mean,
             'UWC_NPR': Global Mean,
            }
    """
    # : Setup correlation data list
    setup_correlations_data_list()
    # Load correlation data
    find_correlations_for(le_total, le_total_summ, gdp_pcap, gdp_pcap_summ, "LEB_GDP")
    find_correlations_for(le_total, le_total_summ, tech_expo, tech_expo_summ, "LEB_HTE")
    find_correlations_for(le_total, le_total_summ, udwe_child, udwe_child_summ, "LEB_UWC")
    find_correlations_for(le_total, le_total_summ, pov_ratio, pov_ratio_summ, "LEB_NPR")
    find_correlations_for(gdp_pcap, gdp_pcap_summ, tech_expo, tech_expo_summ, "GDP_HTE")
    find_correlations_for(gdp_pcap, gdp_pcap_summ, udwe_child, udwe_child_summ, "GDP_UWC")
    find_correlations_for(gdp_pcap, gdp_pcap_summ, pov_ratio, pov_ratio_summ, "GDP_NPR")
    find_correlations_for(tech_expo, tech_expo_summ, udwe_child, udwe_child_summ, "HTE_UWC")
    find_correlations_for(tech_expo, tech_expo_summ, pov_ratio, pov_ratio_summ, "HTE_NPR")
    find_correlations_for(udwe_child, udwe_child_summ, pov_ratio, pov_ratio_summ, "UWC_NPR")
    # Get the mean from all countries correlations and save as global correlations
    get_global_correlations()
    pass


def get_global_correlations():

    # : Find and add the global means for each of the pairwise correlations from all the countries
    # print(all_correlations[0])
    add_global_corr_means('LEB_GDP')
    add_global_corr_means('LEB_HTE')
    add_global_corr_means('LEB_UWC')
    add_global_corr_means('LEB_NPR')
    add_global_corr_means('GDP_HTE')
    add_global_corr_means('GDP_UWC')
    add_global_corr_means('GDP_NPR')
    add_global_corr_means('HTE_UWC')
    add_global_corr_means('HTE_NPR')
    add_global_corr_means('UWC_NPR')
    # print(all_correlations[0])

    pass


def add_global_corr_means(key_name):

    sum_values = []
    n = 0
    for i in range(len(all_correlations)):
        if all_correlations[i][key_name] is not None:
            # SHOWS CORRELATIONS
            # print(key_name, ": ", all_correlations[i][key_name])
            sum_values.append(all_correlations[i][key_name])
            n += 1

    sum_of_values = sum(sum_values)
    if n != 0:
        mean = sum_of_values / n

    all_correlations[0][key_name] = mean

    pass


def setup_correlations_data_list():

    all_correlations.append({'Country Name': 'All Countries',
                             'LEB_GDP': None,
                             'LEB_HTE': None,
                             'LEB_UWC': None,
                             'LEB_NPR': None,
                             'GDP_HTE': None,
                             'GDP_UWC': None,
                             'GDP_NPR': None,
                             'HTE_UWC': None,
                             'HTE_NPR': None,
                             'UWC_NPR': None})

    for i in range(NUMB_COUNTRIES):
        all_correlations.append({'Country Name': le_total[i]['Country Name'],
                                 'LEB_GDP': None,
                                 'LEB_HTE': None,
                                 'LEB_UWC': None,
                                 'LEB_NPR': None,
                                 'GDP_HTE': None,
                                 'GDP_UWC': None,
                                 'GDP_NPR': None,
                                 'HTE_UWC': None,
                                 'HTE_NPR': None,
                                 'UWC_NPR': None})

    pass


def find_correlations_for(proc_data_list_x, has_means_x, proc_data_list_y, has_means_y, indic):

    for i in range(NUMB_COUNTRIES):
        # print(i)
        correlation = get_correlation(proc_data_list_x[i], has_means_x[i+2]['Mean'], proc_data_list_y[i], has_means_y[i+2]['Mean'])
        # : Store country's correlation in correlation data list in appropriate field
        all_correlations[i + 1][indic] = correlation

    pass


def get_correlation(country_dict_x, country_mean_x, country_dict_y, country_mean_y):

    # If one of means for the data lists for the country is None that means they have 0 values in that data list so skip
    if country_mean_x is not None and country_mean_y is not None:
        diff_mean_values_x = []
        diff_mean_values_y = []

        # for year 2000 to 2015 only use values in years which are not blank for both data lists
        for i in range(16):
            if i < 10:
                if country_dict_x[f"200{i}"] != ".." and country_dict_y[f"200{i}"] != "..":
                    diff_mean_values_x.append(float(country_dict_x[f"200{i}"]) - country_mean_x)
                    diff_mean_values_y.append(float(country_dict_y[f"200{i}"]) - country_mean_y)
            else:
                if country_dict_x[f"20{i}"] != ".." and country_dict_y[f"20{i}"] != "..":
                    diff_mean_values_x.append(float(country_dict_x[f"20{i}"]) - country_mean_x)
                    diff_mean_values_y.append(float(country_dict_y[f"20{i}"]) - country_mean_y)

        if len(diff_mean_values_x) > 1 and len(diff_mean_values_y) > 1:
            sigma_x = get_sigma(diff_mean_values_x)
            sigma_y = get_sigma(diff_mean_values_y)
            covariance = get_covariance(diff_mean_values_x, diff_mean_values_y)
            pearson_correlation = covariance / (sigma_x * sigma_y)

            """ PRIMITIVE TESTS """
            # print(country_dict_x)
            # print("Mean: ", country_mean_x)
            # print(diff_mean_values_x)
            # print("Sigma: ", sigma_x)
            #
            # print(country_dict_y)
            # print("Mean: ", country_mean_y)
            # print(diff_mean_values_y)
            # print("Sigma: ", sigma_y)
            #
            # print("Covariance: ", covariance)
            # print("Pearson Correlation: ", pearson_correlation, "\n")

            return pearson_correlation
        else:
            return None
    else:
        return None

    pass


def get_covariance(diff_mean_values_x, diff_mean_values_y):

    values_to_sum = []
    for i in range(len(diff_mean_values_x)):
        values_to_sum.append(diff_mean_values_x[i] * diff_mean_values_y[i])
    covariance = sum(values_to_sum)
    return covariance


def get_sigma(diff_mean_values):

    squared_values = [n**2 for n in diff_mean_values]
    sum_of_squares = sum(squared_values)
    sigma = sum_of_squares ** (1/2)
    return sigma


def write_summary_data_table():

    summary_file = open("data_processed/summary.txt", "w")
    summary_file.write('=========================================================================================================================\n')
    summary_file.write(' Summary Datasets Information For 2000-2015    |      Min  |         Max  |    Median  |       Mean  |  Collected From  |\n')
    summary_file.write('=========================================================================================================================\n')
    summary_file.write(" "+le_total_summ[0]['Data Type']+"            | ")
    summary_file.write(f"{le_total_summ[1]['Min']:8.2f}"+"  |    ")
    summary_file.write(f"{le_total_summ[1]['Max']:8.2f}"+"  |  ")
    summary_file.write(f"{le_total_summ[1]['Median']:8.2f}"+"  |   ")
    summary_file.write(f"{le_total_summ[1]['Mean']:8.2f}"+"  |        ")
    summary_file.write(f"{le_total_summ[0]['Number Collected From']:8.2f}" + "  |\n")
    summary_file.write('-----------------------------------------------|-----------|--------------|------------|-------------|------------------|\n')
    summary_file.write(" "+gdp_pcap_summ[0]['Data Type']+"   |   ")
    summary_file.write(f"{gdp_pcap_summ[1]['Min']:.2f}"+"  |  ")
    summary_file.write(f"{gdp_pcap_summ[1]['Max']:,.2f}"+"  |  ")
    summary_file.write(f"{gdp_pcap_summ[1]['Median']:,.2f}"+"  |  ")
    summary_file.write(f"{gdp_pcap_summ[1]['Mean']:,.2f}"+"  |        ")
    summary_file.write(f"{gdp_pcap_summ[0]['Number Collected From']:8.2f}" + "  |\n")
    summary_file.write('-----------------------------------------------|-----------|--------------|------------|-------------|------------------|\n')
    summary_file.write(" "+tech_expo_summ[0]['Data Type']+"   | ")
    summary_file.write(f"{tech_expo_summ[1]['Min']:8.2f}"+"  |    ")
    summary_file.write(f"{tech_expo_summ[1]['Max']:8.2f}"+"  |  ")
    summary_file.write(f"{tech_expo_summ[1]['Median']:8.2f}"+"  |   ")
    summary_file.write(f"{tech_expo_summ[1]['Mean']:8.2f}"+"  |        ")
    summary_file.write(f"{tech_expo_summ[0]['Number Collected From']:8.2f}" + "  |\n")
    summary_file.write('-----------------------------------------------|-----------|--------------|------------|-------------|------------------|\n')
    summary_file.write(" "+udwe_child_summ[0]['Data Type']+"  | ")
    summary_file.write(f"{udwe_child_summ[1]['Min']:8.2f}"+"  |    ")
    summary_file.write(f"{udwe_child_summ[1]['Max']:8.2f}"+"  |  ")
    summary_file.write(f"{udwe_child_summ[1]['Median']:8.2f}"+"  |   ")
    summary_file.write(f"{udwe_child_summ[1]['Mean']:8.2f}"+"  |        ")
    summary_file.write(f"{udwe_child_summ[0]['Number Collected From']:8.2f}" + "  |\n")
    summary_file.write('-----------------------------------------------|-----------|--------------|------------|-------------|------------------|\n')
    summary_file.write(" "+pov_ratio_summ[0]['Data Type']+"      | ")
    summary_file.write(f"{pov_ratio_summ[1]['Min']:8.2f}"+"  |    ")
    summary_file.write(f"{pov_ratio_summ[1]['Max']:8.2f}"+"  |  ")
    summary_file.write(f"{pov_ratio_summ[1]['Median']:8.2f}"+"  |   ")
    summary_file.write(f"{pov_ratio_summ[1]['Mean']:8.2f}"+"  |        ")
    summary_file.write(f"{pov_ratio_summ[0]['Number Collected From']:8.2f}" + "  |\n")
    summary_file.write('-------------------------------------------------------------------------------------------------------------------------')
    summary_file.close()

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
        for i in range(16):
            if i < 10:
                if country_info[f"200{i}"] != "..":
                    some_data = True
            else:
                if country_info[f"20{i}"] != "..":
                    some_data = True
        if some_data:
            countries_collected += 1

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
    with open(f"./data_processed/{file_name}") as csvfile:
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


def remove_data_from_list(key_name, remove_id, remove_list):

    for country_info in remove_list:
        if country_info[key_name] == remove_id:
            # print(country_info)
            for i in range(16):
                if i < 10:
                    country_info[f"200{i}"] = ".."
                else:
                    country_info[f"20{i}"] = ".."
            # print(country_info)
            return
    pass
