# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness['region'] == 'South Atlantic') | (homelessness['region'] == 'Mid-Atlantic')]

# See the result
print(south_mid_atlantic)