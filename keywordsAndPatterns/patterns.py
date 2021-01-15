import re
# All the patterns in regular expression for filtering tweets.

pattern_0 = re.compile("(((I|I've|I have) (test|tested) (positive)))|(my test came back positive)",re.IGNORECASE)
pattern_1 = re.compile("(I).*?(test).*?(positive)", re.IGNORECASE)
pattern_2 = re.compile("( my family| uncle| aunt| mother| father| mom| mum| mommy| mummy| dad| daddy| sister| \
 brother| sibling| grandmother| grandma| grandmom| grandfather| grandpa| aunth| cousin| nephew| children| child|\
 daughter| son)+.*?(test).*?(positive)", re.IGNORECASE)


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
 abdominal pain| hot flush| arthralgia| nasal dryness| rash| other symptoms)", re.IGNORECASE)

pattern_4 = re.compile("((I have)|(I've)|(I'm)|(I am))\
( cancer| chronic kidney disease| kidney| COPD| chronic obstructive pulmonary disease|\
 immunocompromised| organ transplant| obesity| asthma| cerebrovascular| cystic fibrosis|\
 hypertension| high blood pressure| weak immune system| neurologic conditions| dementia|\
 liver disease| overweight| pregnancy| pregnant| pulmonary fibrosis| lung| thalassemia|\
 diabetes| diabetic)", re.IGNORECASE)

pattern_5 = re.compile("(my)?( family| uncle| aunt| mother| father| mom| mum| mommy|\
 mummy| dad| daddy| sister| brother| sibling| grandmother| grandma| grandmom|\
 grandfather| grandpa| aunth| cousin| nephew| children| child| daughter| son)\
( has| have| is| are)( cancer| chronic kidney disease| kidney| COPD|\
 chronic obstructive pulmonary disease| immunocompromised| organ transplant| obesity|\
 asthma| cerebrovascular| cystic fibrosis| hypertension| high blood pressure| weak immune system|\
 neurologic conditions| dementia| liver disease| overweight| pregnancy| pregnant| pulmonary fibrosis|\
 lung| thalassemia| diabetes| diabetic)", re.IGNORECASE)
pattern_6 = re.compile("fever|dry cough|shortness of breath", re.IGNORECASE)

pattern_7 = re.compile("#?highrisk|#?high_risk|#covidhighrisk|#?highriskcovid", re.IGNORECASE )