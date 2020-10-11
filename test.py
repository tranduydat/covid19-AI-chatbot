import unidecode

list_provinces = []
list_intents = []
list_synonyms = []

with open('./vietnam_provinces.txt', 'r') as f:
    for line in f:
        list_provinces.append(line)

pname = list_provinces[0]
pname_nospace_lowercase_uni = unidecode.unidecode(pname.replace(' ', '').lower())
pname_lowercase = unidecode.unidecode(pname.replace(' ', '').lower())

# Add new item to list
list_synonyms.append(pname_nospace_lowercase_uni + "_s\n")
list_intents.append("ask_" + pname_nospace_lowercase_uni + "_vn")

# Format string
'## intent:ask_{}_vn\n- [{}]{"entity": "{}_synonym", "value": "{}_s"} có bao nhiêu [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [mắc]{"entity": "getvirus_synonym", "value": "getvirus"} rồi\n- [{}]{"entity": "{}_synonym", "value": "{}_s"} có bao nhiêu [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [chết]{"entity": "die_synonym", "value": "die"} rồi\n- [{}]{"entity": "{}_synonym", "value": "{}_s"} có bao nhiêu [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [khỏi]{"entity": "resolved_synonym", "value": "resolved"} bệnh rồi\n- số [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [chết]{"entity": "die_synonym", "value": "die"} do [Covid-19](covid_synonym) ở [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- [Covid-19](covid_synonym) tại [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- số [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [khỏi]{"entity": "resolved_synonym", "value": "resolved"} [Covid-19](covid_synonym) ở [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- số [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} mắc [Covid-19](covid_synonym) ở [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- [{}]{"entity": "{}_synonym", "value": "{}_s"} có số [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [chết]{"entity": "die_synonym", "value": "die"} do [Covid-19](covid_synonym)\n- [{}]{"entity": "{}_synonym", "value": "{}_s"} có bao nhiêu [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [khỏi]{"entity": "resolved_synonym", "value": "resolved"} [Covid-19](covid_synonym)\n- [{}]{"entity": "{}_synonym", "value": "{}_s"} có số [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [mắc]{"entity": "getvirus_synonym", "value": "getvirus"} [Covid-19](covid_synonym)\n- tình hình [Covid-19](covid_synonym) ở [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- số liệu ở [{}]{"entity": "{}_synonym", "value": "{}_s"} [việt nam](vietnam_synonym)\n- thông tin về số [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} tại [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- có bao nhiêu [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} mắc [Covid-19](covid_synonym)\n- [Covid-19](covid_synonym) ở [{}]{"entity": "{}_synonym", "value": "{}_s"} thế nào\n- số [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [chết]{"entity": "die_synonym", "value": "die"} và mắc [Covid-19](covid_synonym) ở [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- số [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [chết]{"entity": "die_synonym", "value": "die"} và [khỏi]{"entity": "resolved_synonym", "value": "resolved"} [Covid-19](covid_synonym) ở [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- số [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} [khỏi]{"entity": "resolved_synonym", "value": "resolved"} và mắc ở [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- số [bệnh nhân]{"entity": "patient_synonym", "value": "patient"} bị bệnh [Covid-19](covid_synonym) ở [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- tình hình ở [{}]{"entity": "{}_synonym", "value": "{}_s"}\n- [{}]{"entity": "{}_synonym", "value": "{}_s"} [việt nam](vietnam_synonym)\n- tin tức [Covid-19](covid_synonym) ở [{}]{"entity": "{}_synonym", "value": "{}_s"}'.format(pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni,
pname, pname_nospace_lowercase_uni, pname_nospace_lowercase_uni)