# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales', index='type', aggfunc=(np.mean, np.median))

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)