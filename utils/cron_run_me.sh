# Pull lastest data from CSSEGI repo
cd /home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData
git pull origin master
cd -

# Remove database
rm -rf /home/trdat/Workspaces/covid19-rasa-chatbot/database.db

# Create empty database
touch /home/trdat/Workspaces/covid19-rasa-chatbot/database.db

# Pull data and export these into sqlite3 database.db
python /home/trdat/Workspaces/covid19-rasa-chatbot/utils/PullData.py