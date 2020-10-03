#!/bin/bash

# Global confirmed
wget -N --quiet https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv -P /home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/timeseries/

# Global deaths
wget -N --quiet https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv -P /home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/timeseries/

# Global recovered
wget -N --quiet https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv -P /home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/timeseries/
