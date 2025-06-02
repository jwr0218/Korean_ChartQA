from openai import OpenAI
import matplotlib.pyplot as plt
import subprocess
# from matplotlib import font_manager
from datasets import load_dataset
import random 
import json


api_key = 'Your API Key'
client = OpenAI(api_key=api_key)


nia_path = '/workspace/data_moder/Nia_Chart2Table.json'
dataset = load_dataset('json',  data_files = nia_path )
dataset_train = dataset['train'][10000:]

idx = 0 
json_lst = []
total_lst = []

# ===================================== ChartQA 작성 =====================================
for image_dir, query, label in zip(dataset_train['image'], dataset_train['query'], dataset_train['label']):

    prompt = f'''ChartQA 한글판을 작성하라. 위의 Table을 읽고 적절한 Query문과, 이에 대응하는 Answer를 작성하라.
조건1: 다음과 같은 Fortmat으로 작성하라. 
    QUERY : ~~~~ 
    ANSWER : ~~~~
조건2: 부연설명 없이 내용만 작성하라.
조건3: 2~4쌍의 query, answer를 추출하라.
조건4: 논리적으로 유추할 수 있는 질문만을 작성하라.
조건5: [명사형 문장,명령형 문장,부탁형 문장,일반 문장] 어투중 두가지로 작성하라.
'''

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. 지금부터 주는 데이터는 Table데이터를 Text화 한 것이다. 이를 바탕으로 아래의 명령을 수행하라."},
            {"role": "user", "content": label},
            {"role": "assistant", "content": "어떤 명령을 수행할까요?"},
            {"role": "user", "content":prompt}
        ]
    )
    content = response.choices[0].message.content  # 줄 단위로 분리
    lines = content.strip().split('\n')
    # print(lines)
    # 결과를 저장할 리스트
    queries_answers = [{"image" : image_dir,"query": query, "label": label}]

    # 빈 문자열을 제외하고 QUERY와 ANSWER를 짝지어 저장
    try:
        for i in range(0, len(lines), 3):  # QUERY와 ANSWER는 3번째 간격으로 나오므로 3단위로 처리
            if i + 1 < len(lines) and lines[i].startswith("QUERY") and lines[i+1].startswith("ANSWER"):
                query_gpt = lines[i].split(": ", 1)[1].strip()  # QUERY 값 추출
                answer_gpt = lines[i+1].split(": ", 1)[1].strip()  # ANSWER 값 추출
                queries_answers.append({"image" : image_dir,"query": query_gpt, "label": answer_gpt})
    except:
        # 이상하게 됐다 싶으면 다 삭제하고 넘기기
        continue

    total_lst.extend(queries_answers)
    print('Check for Progressing')
    print('생성 query & Answer : ',len(queries_answers))
    print(label)
    print(total_lst[-1])
    print('----------'*15)
    print('\n')
    # JSON 파일로 저장
    with open("Query_Answer.json", "w", encoding="utf-8") as f:
        json.dump(total_lst, f, ensure_ascii=False, indent=4)
