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

product_count.plot(kind="bar")

""" Top 10 companies by compaints """
company_complaints = company_complaints.groupby("Company").size()
company_complaints = company_complaints.sort_values(ascending=False)
company_complaints.head(10)

company_complaints[:10].plot(kind="bar")

""" Number of complaints by company response """
company_response_complaints = consumer_complaints[['Company response', 'ID']].copy()
company_response_complaints = company_response_complaints.groupby("Company response").size()
company_response_complaints = company_response_complaints.sort_values(ascending=False)
company_response_complaints.head(10)

company_response_complaints.plot(kind='barh')

""" Mean number of complaints per weekday """
""" First get the number of times each weekday occured in the month """
mcbd = consumer_complaints[['Date', 'ID']].copy()

date_set = set(mcbd.Date)
date_set = sorted(list(date_set))
date_set = pd.to_datetime(date_set, format='%m/%d/%Y')
date_set = date_set.to_series().map(lambda d: d.weekday())

""" Find the total number of compaints for each weekday """

complaints_by_product = complaints[['Date received','Complaint ID']].copy()
cbp = complaints_by_product.rename(columns={'Complaint ID': 'ID'}).copy()
cbp.index = pd.to_datetime(cbp["Date received"], format='%m/%d/%Y')
cbp['days_of_week'] = cbp.index.to_series().map(lambda d: d.weekday())
total = cbp.groupby('days_of_week').size()
total = total.sort_values(ascending=False)
total

""" Divide total by number of days """
mean = total/number_of_days

""" Create a new Frame from the means """
mean_by_day = pd.DataFrame({'Mean': mean})

mean_by_day.plot(kind='barh', alpha=0.75, color='r')
