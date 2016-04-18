import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

consumer_complaints = pd.read_csv('complaints_dec_2014.csv')
consumer_complaints.head()

""" Indexes by date received """
date_series = consumer_complaints.pop('Date received')
consumer_complaints.index = pd.to_datetime(date_series, format='%m/%d/%Y')

""" Rename for ease of use """
consumer_complaints = consumer_complaints.rename(columns={"Complaint ID":"ID"}).copy()

""" Sorted list of Products by number of complaints """
product_count = consumer_complaints[['Product', 'ID']].copy()
product_count = product_count.groupby("Product").size()
product_count = product_count.sort_values(ascending=False)

""" Top 10 companies by compaints """
company_complaints = company_complaints.groupby("Company").size()
company_complaints = company_complaints.sort_values(ascending=False)
company_complaints.head(10)

""" Number of complaints by company response """
company_response_complaints = consumer_complaints[['Company response', 'ID']].copy()
company_response_complaints = company_response_complaints.groupby("Company response").size()
company_response_complaints = company_response_complaints.sort_values(ascending=False)
company_response_complaints.head(10)
