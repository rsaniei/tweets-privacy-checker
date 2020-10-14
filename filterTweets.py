
# This function get a .json file, which has a complete tweet (id, fulltext, etc.) in each line
# Then, one by one, it checks if a certain pattern can be found in the full_text of a tweet
# It also ignores the replicate tweets
import re
import json

from cleanTweets import *

def find_pattern(id_file, seen_tweets):

    tweets_list = []
    print(id_file)

    pattern_0 = re.compile("(((I|I've|I have) (test|tested) (positive)))|(my test came back positive)")
    pattern_1 = re.compile("(I).*?(test).*?(positive)")
    pattern_2 = re.compile("( my family| uncle| aunt| mother| father| mom| mum| mommy| mummy| dad| daddy| sister| \
 brother| sibling| grandmother| grandma| grandmom| grandfather| grandpa| aunth| cousin| nephew| children| child|\
 daughter| son)+.*?(test).*?(positive)")

    pattern_3_1 = re.compile("(my| his| her| their)( symptoms are)")

    pattern_3 = re.compile("(symptoms are)?( fever| chills| chill|\
 cough| dry cough| tiredness| tired| shortness of breath| difficulty breathing| breath|\
 nasal congestion| runny nose| sore throat| Fatigue| muscle achesor| body aches|\
 headache| loss of taste| loss of smell| Sore throat| congestion| runny nose| nausea|\
 vomiting| diarrhea| trouble breathing| pain in the chest| pain in the pressure| confusion| inability to wake|\
 inability to stay awake| bluish lips or face| pneumonia| headache| pyrexia| cough| body ache|\
 general pain| fatigue| headache| dyspnea| anosmia|\
 ageusia| oropharyngeal pain| chest pain| chest tightness|\
 hyperhidrosis| sweating| sweat|\
 loss of appetite| nausea| rhinorrhea| vomiting| vomit| anxiety|\
 stress| general mental health| mental health| migraine| diarrhea|\
 GI issues| eye pain| eye infection| dizziness| dizzy| disorientation| confusion|\
 lethargic| myalgia| sneezing| sneez| insomnia| sleep disturbance|\
 paranasal sinus discomfort| sinus| upper respiratory tract infection|\
 wheezing| wheeze| ear infection| ear pain| dehydration| dehydrate| palpitation|\
 abdominal pain| hot flush| arthralgia| nasal dryness| rash| other symptoms)")

    pattern_4 = re.compile("((I have)|(I've)|(I'm)|(I am))\
( cancer| chronic kidney disease| kidney| COPD| chronic obstructive pulmonary disease|\
 immunocompromised| organ transplant| obesity| asthma| cerebrovascular| cystic fibrosis|\
 hypertension| high blood pressure| weak immune system| neurologic conditions| dementia|\
 liver disease| overweight| pregnancy| pregnant| pulmonary fibrosis| lung| thalassemia|\
 diabetes| diabetic)")

    pattern_5 = re.compile("(my)?( family| uncle| aunt| mother| father| mom| mum| mommy|\
 mummy| dad| daddy| sister| brother| sibling| grandmother| grandma| grandmom|\
 grandfather| grandpa| aunth| cousin| nephew| children| child| daughter| son)\
( has| have| is| are)( cancer| chronic kidney disease| kidney| COPD|\
 chronic obstructive pulmonary disease| immunocompromised| organ transplant| obesity|\
 asthma| cerebrovascular| cystic fibrosis| hypertension| high blood pressure| weak immune system|\
 neurologic conditions| dementia| liver disease| overweight| pregnancy| pregnant| pulmonary fibrosis|\
 lung| thalassemia| diabetes| diabetic)")
    pattern_6 = re.compile("fever|dry cough|shortness of breath")


    patterns = [ pattern_1, pattern_2, pattern_3]


    with open(id_file, encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            try:
                data = json.loads(line)

                if data["lang"] == "en" and data["full_text"] not in seen_tweets:

                    original_data = data['full_text']
                    data['full_text'] = remove_emoji(data['full_text'])
                    data['full_text'] = remove_URL(data['full_text'])
                    data['full_text'] = remove_html(data['full_text'])
                    # data['full_text'] = remove_punct(data['full_text'])

                    # result = list(map((lambda x: x.findall(data['full_text'])), patterns))
                    # res_0 = pattern_0.findall(data['full_text'])
                    # res_1 = pattern_1.findall(data['full_text'])
                    # res_2 = pattern_2.findall(data['full_text'])
                    # res_3 = pattern_3.findall(data['full_text'])
                    # res_3_1 = pattern_3_1.findall(data['full_text'])
                    # res_4 = pattern_4.findall(data['full_text'])
                    res_6 = pattern_6.findall(data['full_text'])


                    if len(res_6) != 0:
                        write_to_file([{'id': data['id'],'id_str': data['id_str'], 'text': data['full_text'], 'created_at':data['created_at']}])
                        # write_to_file([data])
                        seen_tweets.add(original_data)
            except ValueError as e:
                pass



def write_to_file(myList):
    with open('pattern6.txt', 'a') as f:
        for item in myList:
            f.write("%s\n" % item)
