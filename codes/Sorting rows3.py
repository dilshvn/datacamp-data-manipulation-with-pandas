# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending = [True, False])

# Print the top few rows
print(homelessness_reg_fam.head())