from typing import Any, Text, List, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from utils.DBTools import retrieve_datum
from utils.DBTools import create_connection
from utils.PreprocessingData import PreprocessingData
import locale
import datetime
locale.setlocale(locale.LC_ALL, 'vi_VN')

PATH_CONFIRMED_GLOBAL_TS = r'~/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
PATH_DEATH_GLOBAL_TS = r'~/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
PATH_RECOVERED_GLOBAL_TS = r'~/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
TABLE_CONFIRMED_GLOBAL_TS = 'Confirmed_Global'
TABLE_DEATH_GLOBAL_TS = 'Death_Global'
TABLE_RECOVERED_GLOBAL_TS = 'Recovered_Global'
PATH_TO_DB = 'database.db'


def getCurrentDate(option):
	"""
			option:
					- death
					- confirmed
					- recovered
	"""
	pre_date = ""
	if (option == 'death'):
		pre_data = PreprocessingData(
			PATH_TO_DB, PATH_DEATH_GLOBAL_TS, TABLE_DEATH_GLOBAL_TS)
	elif (option == 'confirmed'):
		pre_data = PreprocessingData(
			PATH_TO_DB, PATH_CONFIRMED_GLOBAL_TS, TABLE_CONFIRMED_GLOBAL_TS)
	elif (option == 'recovered'):
		pre_data = PreprocessingData(
			PATH_TO_DB, PATH_RECOVERED_GLOBAL_TS, TABLE_RECOVERED_GLOBAL_TS)

	conn = create_connection(PATH_TO_DB)
	current_year = str(datetime.datetime.utcnow().year)
	current_date = str(pre_data.get_lastest_date())
	pieces = current_date.split('/')

	# Day/Month/Year
	format_date = str(pieces[1]) + '/' + \
		str(pieces[0]) + '/' + current_year
	# date_obj = datetime.datetime.strptime(format_date, "%d/%m/%Y").date()

	return format_date


def getDeath(option):
	"""
			option:
					- global
					- vietnam
			return as str
	"""
	pre_data = PreprocessingData(
		PATH_TO_DB, PATH_DEATH_GLOBAL_TS, TABLE_DEATH_GLOBAL_TS)
	conn = create_connection(PATH_TO_DB)

	# Get the lastest date from csv
	query_current_date = str("dg.'" + pre_data.get_lastest_date() + "'")

	# Build the query
	query_vietnamese_cases_death = str(
		r"SELECT " + query_current_date + " FROM Death_Global dg WHERE dg.'Country/Region' = 'Vietnam'")
	query_global_cases_death = str(
		r"SELECT SUM(" + query_current_date + ") FROM Death_Global dg")

	# Query database
	vietnamese_cases_death = retrieve_datum(conn, query_vietnamese_cases_death)
	global_cases_death = retrieve_datum(conn, query_global_cases_death)

	# Retrieve proper data defined by option (as param)
	number = ""
	if (option == 'global'):
		number = str(locale.format_string(
			"%d", global_cases_death[0], grouping=True))
	elif (option == 'vietnam'):
		number = str(locale.format_string(
			"%d", vietnamese_cases_death[0], grouping=True))

	# Close connection
	conn.close()

	return number


def getConfirmed(option):
	"""
			option:
					- global
					- vietnam
			return as str
	"""
	pre_data = PreprocessingData(
		PATH_TO_DB, PATH_DEATH_GLOBAL_TS, TABLE_DEATH_GLOBAL_TS)
	conn = create_connection(PATH_TO_DB)

	# Get the lastest date from csv
	query_current_date = str("cg.'" + pre_data.get_lastest_date() + "'")

	# Build the query
	query_vietnamese_cases_confirmed = str(
		r"SELECT " + query_current_date + " FROM Confirmed_Global cg WHERE cg.'Country/Region' = 'Vietnam'")
	query_global_cases_confirmed = str(
		r"SELECT SUM(" + query_current_date + ") FROM Confirmed_Global cg")

	# Query database
	vietnamese_cases_confirmed = retrieve_datum(
		conn, query_vietnamese_cases_confirmed)
	global_cases_confirmed = retrieve_datum(conn, query_global_cases_confirmed)

	# Retrieve proper data defined by option (as param)
	number = ""
	if (option == 'global'):
		number = str(locale.format_string(
			"%d", global_cases_confirmed[0], grouping=True))
	elif (option == 'vietnam'):
		number = str(locale.format_string(
			"%d", vietnamese_cases_confirmed[0], grouping=True))

	# Close connection
	conn.close()

	return number


def getRecovered(option):
	"""
			option:
					- global
					- vietnam
			return as str
	"""
	pre_data = PreprocessingData(
		PATH_TO_DB, PATH_RECOVERED_GLOBAL_TS, TABLE_RECOVERED_GLOBAL_TS)
	conn = create_connection(PATH_TO_DB)

	# Get the lastest date from csv
	query_current_date = str("rg.'" + pre_data.get_lastest_date() + "'")

	# Build the query
	query_vietnamese_cases_recovered = str(
		r"SELECT " + query_current_date + " FROM Recovered_Global rg WHERE rg.'Country/Region' = 'Vietnam'")
	query_global_cases_recovered = str(
		r"SELECT SUM(" + query_current_date + ") FROM Recovered_Global rg")

	# Query database
	vietnamese_cases_recovered = retrieve_datum(
		conn, query_vietnamese_cases_recovered)
	global_cases_recovered = retrieve_datum(conn, query_global_cases_recovered)

	# Retrieve proper data defined by option (as param)
	number = ""
	if (option == 'global'):
		number = str(locale.format_string(
			"%d", global_cases_recovered[0], grouping=True))
	elif (option == 'vietnam'):
		number = str(locale.format_string(
			"%d", vietnamese_cases_recovered[0], grouping=True))

	# Close connection
	conn.close()

	return number


################### CUSTOM ACTION ###################
class ActionAskDeath(Action):

	def name(self) -> Text:
		return "action_ask_death_cases_globally"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "😷 Cập nhật thông tin đến ngày " + getCurrentDate('death') + "\n🇻🇳 Tại Việt Nam có tổng số " + getDeath(
			'vietnam') + " trường hợp tử vong vì virus Corona 🦠\n" + "🌐 Con số này trên toàn thế giới là " + getDeath('global') + " người."

		dispatcher.utter_message(text=message)

		return []


class ActionAskConfirmed(Action):

	def name(self) -> Text:
		return "action_ask_confirmed_cases_globally"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "🧼👏 Đến ngày " + getCurrentDate('confirmed') + "\nTrên toàn thế giới đã có " + getConfirmed(
			'global') + " người dương tính với Covid-19\nTrong đó, 🇻🇳 Việt Nam có " + getConfirmed('vietnam') + " bệnh nhân."

		# conn.close()
		dispatcher.utter_message(text=message)

		return []

class ActionAskRecovered(Action):

	def name(self) -> Text:
		return "action_ask_recovered_cases_globally"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "📜 💪 Theo báo cáo đến ngày " + getCurrentDate('recovered') + "\n🌐 Trên toàn thế giới có " + getRecovered('global') + " người đã khỏi bệnh" + "\n🇻🇳 Trong đó Việt Nam có " + getRecovered('vietnam') + " người."

		# conn.close()
		dispatcher.utter_message(text=message)

		return []

############## Extend for global
class ActionAskDeathConfirmed(Action):
	def name(self) -> Text:
		return "action_ask_death_confirmed_cases_globally"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "🧼👏 Tính đến ngày " + getCurrentDate('death') + ", trên toàn thế giới 🌐 ghi nhận:\n Đã có tổng cộng " + getConfirmed('global') + " ca nhiễm\nvà " + getDeath('global') + " người tử vong vì Covid-19"

		dispatcher.utter_message(text=message)

		return []


class ActionAskDeathRecovered(Action):
	def name(self) -> Text:
		return "action_ask_death_recovered_cases_globally"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "Đến ngày " + getCurrentDate('death') + ", thống kê dịch Covid-19 trên toàn thế giới 🌐\n " + getDeath('global') + " trường hợp tử vong\n " + getRecovered('global') + " ca bình phục"

		dispatcher.utter_message(text=message)

		return []


class ActionAskConfirmedRecovered(Action):
	def name(self) -> Text:
		return "action_ask_confirmed_recovered_cases_globally"

	def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "Tính đến ngày " + getCurrentDate('confirmed') + ", trên toàn thế giới 🌐\n Có tất cả " + getConfirmed('global') + " ca nhiễm đã được ghi nhận\n " + getRecovered('global') + " ca khỏi bệnh"

		dispatcher.utter_message(text=message)

		return []

######################################
class ActionAskAll(Action):

	def name(self) -> Text:
		return "action_ask_all"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "📃⚕️ Cập nhật tình hình dịch bệnh Covid-19 đến ngày " + getCurrentDate('death') + "\nTrên toàn thế giới 🌐:\n- Số ca nhiễm: " + getConfirmed('global') + "\n- Số ca tử vong: " + getDeath('global') + "\n- Số ca khỏi: " + getRecovered('global') + "\nTại Việt Nam 🇻🇳:\n- Số ca nhiễm: " + getConfirmed('vietnam') + "\n- Số ca tử vong: " + getDeath('vietnam') + "\n- Số ca khỏi: " + getRecovered('vietnam')

		dispatcher.utter_message(text=message)

		return []


########################## VIETNAM ##########################
class ActionAskDeathVietnam(Action):

	def name(self) -> Text:
		return "action_ask_death_cases_vietnam"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "Cập nhật ngày " + getCurrentDate('death') + ", Việt Nam có " + getDeath(
			'vietnam') + " người tử vong do Covid-19 😢"

		dispatcher.utter_message(text=message)

		return []


class ActionAskConfirmedVietnam(Action):

	def name(self) -> Text:
		return "action_ask_confirmed_cases_vietnam"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "Tính đến ngày " + getCurrentDate('confirmed') + ", Việt Nam ghi nhận " + getConfirmed(
			'vietnam') + " trường hợp dương tính Covid-19"

		dispatcher.utter_message(text=message)

		return []


class ActionAskRecoveredVietnam(Action):

	def name(self) -> Text:
		return "action_ask_recovered_cases_vietnam"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "Tính đến ngày " + getCurrentDate('recovered') + ", đã có " + getRecovered(
			'vietnam') + " trên tổng số " + getConfirmed('vietnam') + " bệnh nhân tại Việt Nam đã được chữa khỏi Covid-19\n"

		dispatcher.utter_message(text=message)

		return []

################### Extend for Vietnam
class ActionAskDeathConfirmedVietnam(Action):

	def name(self) -> Text:
		return "action_ask_death_confirmed_cases_vietnam"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "🇻🇳 Tình hình dịch Covid-19 tại Việt Nam, ghi nhận tính đến ngày " + getCurrentDate('death') + "\n  " + getConfirmed('vietnam') + " trường hợp mắc mới\n  " + getDeath('vietnam') + " ca tử vong"  

		dispatcher.utter_message(text=message)

		return []


class ActionAskDeathRecoveredVietnam(Action):

	def name(self) -> Text:
		return "action_ask_death_recovered_cases_vietnam"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "🇻🇳 Cập nhật đến " + getCurrentDate('death') + ", tình hình dịch Covid tại Việt Nam:\n  " + getRecovered('vietnam') + " bệnh nhân khỏi bệnh\n  " + getDeath('vietnam') + " ca tử vong"  

		dispatcher.utter_message(text=message)

		return []


class ActionAskConfirmedRecoveredVietnam(Action):

	def name(self) -> Text:
		return "action_ask_confirmed_recovered_cases_vietnam"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "🇻🇳 Cập nhật tình hình dịch Covid-19 tại Việt Nam (ngày " + getCurrentDate('confirmed') + ")\n  " + getConfirmed('vietnam') + " người dương tính với virus Corona\n  " + getRecovered('vietnam') + " bệnh nhân khỏi bệnh"

		dispatcher.utter_message(text=message)

		return []

######################################

class ActionAskAllVietnam(Action):

	def name(self) -> Text:
		return "action_ask_all_cases_vietnam"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "🇻🇳 Tại Việt Nam (tính đến ngày " + getCurrentDate('confirmed') + "):\n- Số ca nhiễm: " + getConfirmed('vietnam') + "\n- Số ca tử vong: " + getDeath('vietnam') + "\n- Số ca khỏi: " + getRecovered('vietnam')

		dispatcher.utter_message(text=message)

		return []

###################### MISC
class ActionShowAdvices(Action):

	def name(self) -> Text:
		return "action_show_advices"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		message = "😷 Đeo khẩu trang khi ra khỏi nhà\n🤧 Duy trì khoảng cách giao tiếp từ 1-2 mét giữa bạn và người khác, đặc biệt là những người đang ho, hắt hơi và bị sốt.\n🙅‍♀️ Hạn chế sờ vào mắt, mũi và miệng.\n👏 Rửa tay thường xuyên bằng dung dịch rửa tay có cồn hoặc với xà phòng và nước.\n🤒 Nếu bạn bị sốt, ho và khó thở, hãy đi khám sớm và kể cho nhân viên y tế biết chi tiết trước đó bạn đã đi những đâu.\nNguồn: Bộ Y Tế"

		dispatcher.utter_message(text=message)

		return []