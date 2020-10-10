#!/usr/bin/env bash

source ~/.virtualenv/rasa/bin/activate; cronitor ping LM9GRq --run; cd /home/trdat/Workspaces/covid19-rasa-chatbot/realtime_data/COVID_19_CSSEGISandData; git pull origin master; cd -; rm -rf /home/trdat/Workspaces/covid19-rasa-chatbot/database.db; touch /home/trdat/Workspaces/covid19-rasa-chatbot/database.db; python /home/trdat/Workspaces/covid19-rasa-chatbot/utils/PullData.py; cronitor ping LM9GRq --complete
