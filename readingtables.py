from bs4 import BeautifulSoup
import requests
import pandas as pd
largest_cities = pd.read_html(
    'https://3083218.youcanlearnit.net/geographytables.html')[2]
# print(largest_cities)
base_link = 'https://hplussport.net/#people'
page_read = requests.get(base_link)
soup = BeautifulSoup(page_read.content)
board_names = soup.select('.card-name')
board_roles = soup.select('.card-title')
results = []
for i in range(len(board_roles)):
    person_name = board_names[i].text
    person_role = board_roles[i].text
    result_df = pd.DataFrame(
        data=[[person_role, person_name]],
        columns=['Role', 'Name']
    )
    results.append(result_df)
results = pd.concat(results)
print(results)
