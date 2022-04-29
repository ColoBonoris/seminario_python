path_files = "files"
archivo_net = "netflix_titles.csv"

def inform_all_countries(path_arch):
    with open(path_arch,"r") as file_net:
        csv_net = csv.reader(file_net)
        header, data = next(csv_net), list(csv_net)
        country_index = header.index("Country")
        all_countries = set(map(lambda x: x[country_index],list))
    print("All countries: ")
    for i in all_countries:
        print(f"    {i}")

import os
import csv

path_arch = os.path.join(os.path.dirname(__file__),path_files,archivo_net)

with open(path_arch,"r") as file_net:
    csv_net = csv.reader(file_net)
    header, data = next(csv_net), list(csv_net)

inform_all_countries(path_arch)