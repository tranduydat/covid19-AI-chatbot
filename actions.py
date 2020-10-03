from typing import Any, Text, List, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from utils.DBTools import retrieve_datum
from utils.DBTools import create_connection
from utils.PreprocessingData import PreprocessingData

PATH_CONFIRMED_GLOBAL_TS = r'/home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
PATH_DEATH_GLOBAL_TS = r'/home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
PATH_RECOVERED_GLOBAL_TS = r'/home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
TABLE_CONFIRMED_GLOBAL_TS = 'Confirmed_Global'
TABLE_DEATH_GLOBAL_TS = 'Death_Global'
TABLE_RECOVERED_GLOBAL_TS = 'Recovered_Global'
PATH_TO_DB = 'database.db'


class ActionAskDeath(Action):

    def name(self) -> Text:
        return "action_ask_death_cases_globally"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pre_data = PreprocessingData(
            PATH_TO_DB, PATH_DEATH_GLOBAL_TS, TABLE_DEATH_GLOBAL_TS)
        conn = create_connection(PATH_TO_DB)

        # Get the lastest date from csv
        current_date = pre_data.get_lastest_date()
        query_current_date = str("dg.'" + current_date + "'")
        # Query
        query_vietnamese_cases_death = str(
            r"SELECT " + query_current_date + " FROM Death_Global dg WHERE dg.'Country/Region' = 'Vietnam'")
        query_global_cases_death = str(
            r"SELECT SUM(" + query_current_date + ") FROM Death_Global dg")
        vietnamese_cases_death = retrieve_datum(
            conn, query_vietnamese_cases_death)
        global_cases_death = retrieve_datum(conn, query_global_cases_death)

        message = str("Cập nhật thông tin vào ngày " + str(current_date) + "\n" + "🇻🇳 Tại Việt Nam có tổng số " + str(
            vietnamese_cases_death[0]) + " ca tử vong vì Covid-19" + "\n🌐 Trên toàn thế giới là " + str(global_cases_death[0]) + " trường hợp tử vong vì virus Corona")

        conn.close()
        dispatcher.utter_message(text=message)

        return []


class ActionAskConfirmed(Action):

    def name(self) -> Text:
        return "action_ask_confirmed_cases_globally"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pre_data = PreprocessingData(
            PATH_TO_DB, PATH_CONFIRMED_GLOBAL_TS, TABLE_CONFIRMED_GLOBAL_TS)
        conn = create_connection(PATH_TO_DB)

        # Get the lastest date from csv
        current_date = pre_data.get_lastest_date()
        query_current_date = str("cg.'" + current_date + "'")

        # Query
        query_vietnamese_cases_confirmed = str(
            r"SELECT " + query_current_date + " FROM Confirmed_Global cg WHERE cg.'Country/Region' = 'Vietnam'")
        query_global_cases_confirmed = str(
            r"SELECT SUM(" + query_current_date + ") FROM Confirmed_Global cg")

        # Query the result from database
        vietnamese_cases_confirmed = retrieve_datum(
            conn, query_vietnamese_cases_confirmed)
        global_cases_confirmed = retrieve_datum(conn,
                                                query_global_cases_confirmed)

        message = str("Cập nhật thông tin vào ngày " + str(current_date) + "\n" + "🇻🇳 Tại Việt Nam có tổng số " + str(
            vietnamese_cases_confirmed[0]) + " người được xác nhận nhiễm virus Corona" + "\n🌐 Trên toàn thế giới là " + str(global_cases_confirmed[0]) + " trường hợp nhiễm.")

        conn.close()
        dispatcher.utter_message(text=message)

        return []


class ActionAskRecovered(Action):

    def name(self) -> Text:
        return "action_ask_recovered_cases_globally"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pre_data = PreprocessingData(
            PATH_TO_DB, PATH_RECOVERED_GLOBAL_TS, TABLE_RECOVERED_GLOBAL_TS)
        conn = create_connection(PATH_TO_DB)

        # Get the lastest date from csv
        current_date = pre_data.get_lastest_date()
        query_current_date = str("rg.'" + current_date + "'")

        # Query
        query_vietnamese_cases_recovered = str(
            r"SELECT " + query_current_date + " FROM Recovered_Global rg WHERE rg.'Country/Region' = 'Vietnam'")
        query_global_cases_recovered = str(
            r"SELECT SUM(" + query_current_date + ") FROM Recovered_Global rg")

        # Query the result from database
        vietnamese_cases_recovered = retrieve_datum(
            conn, query_vietnamese_cases_recovered)
        global_cases_recovered = retrieve_datum(conn,
                                                query_global_cases_recovered)

        message = str("Cập nhật thông tin vào ngày " + str(current_date) + "\n" + "🇻🇳 Tại Việt Nam có tổng số " + str(
            vietnamese_cases_recovered[0]) + " ca đã khỏi bệnh Covid-19 🦠" + "\n Con số ngày trên toàn cầu là  " + str(global_cases_recovered[0]) + " người 🎉")

        conn.close()
        dispatcher.utter_message(text=message)

        return []
