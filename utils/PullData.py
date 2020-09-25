from PreprocessingData import PreprocessingData

PATH_CONFIRMED_GLOBAL_TS = r'/home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
PATH_DEATH_GLOBAL_TS = r'/home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
PATH_RECOVERED_GLOBAL_TS = r'/home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
TABLE_CONFIRMED_GLOBAL_TS = 'Confirmed_Global'
TABLE_DEATH_GLOBAL_TS = 'Death_Global'
TABLE_RECOVERED_GLOBAL_TS = 'Recovered_Global'
PATH_TO_DB = '../database.db'

# Save csv to sql
process_confirmed_data = PreprocessingData(PATH_TO_DB, PATH_CONFIRMED_GLOBAL_TS, TABLE_CONFIRMED_GLOBAL_TS)
process_confirmed_data.save_to_sql()

process_death_data = PreprocessingData(PATH_TO_DB, PATH_DEATH_GLOBAL_TS, TABLE_DEATH_GLOBAL_TS)
process_death_data.save_to_sql()

process_recoverd_data = PreprocessingData(PATH_TO_DB, PATH_RECOVERED_GLOBAL_TS, TABLE_RECOVERED_GLOBAL_TS)
process_recoverd_data.save_to_sql()