from wf_dataprocessing import process_data
from wf_visualization import visualize_data

__author__ = "John Garvey"
__date__ = "10/14/2023"
__assignment = "Project MS03"


if __name__ == '__main__':
    filename = "data_original/TheWorldBank_DevelopmentIndicators.csv"
    process_data(filename)
    visualize_data()
