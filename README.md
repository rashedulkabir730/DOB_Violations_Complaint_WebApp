# DOB Violations and Complaints Web App

View the Dashboard here: [dobviolationscomplaints.streamlit.app](dobviolationscomplaints.streamlit.app)

This dashboard displays the violations and complaints of buildings in the NYC area issued by the Department of Buildings.

## Overview:

A user can input an address or select an address from the side panel. This action populates a stacked bar chart showing the number of active and closed violations, with the different sections representing the type of device to which the violation pertains. Next to the bar chart are the different violation descriptions provided. Below these two sections is the complaints section. There is a stacked bar chart that displays the number of complaints over time, differentiated by the priority given to the complaint. Priority A is the most pertinent, while Priority D is the least. Next to this chart are descriptions of the complaints made.

### Drawbacks:
This data was downloaded and cleaned by me. I did not use the API, as I didn't think it would have allowed me to pull as much data as I needed, though I may be wrong. As a result, the data cannot be up-to-date. Additionally, I had to figure out a way to upload the two large datasets to be able to use them in Streamlit Cloud. I opted to upload them to the release section of this repository. There is probably a better way to do that.

## Links & References:

- [Violations Dataset](https://data.cityofnewyork.us/Housing-Development/DOB-Violations-Active-/cepu-5g8r/about_data)
- [Complaints Dataset](https://data.cityofnewyork.us/Housing-Development/DOB-Complaints-Received/eabe-havv/about_data)
- I used this information to append a Priority Description Column: [Audit Report on the Department of Buildings' Response and Follow-Up to Complaints](https://comptroller.nyc.gov/reports/audit-report-on-the-department-of-buildings-response-and-follow-up-to-complaints/)
- This project was inspired by: [NYC Restaurant Violations App](https://eigenfoo-nyc-restaurant-violations-app-oc3mad.streamlit.app)
