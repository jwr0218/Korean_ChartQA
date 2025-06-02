# Korean_ChartQA

## 개요
Korean_ChartQA는 차트 이미지 또는 표 데이터를 기반으로 한국어 질문-답변(QA) 쌍을 생성하고 활용할 수 있도록 돕는 프로젝트입니다. 이 저장소에는 샘플 데이터(JSON)와 GPT 모델(OpenAI API)을 사용해 차트에 대한 질의를 자동 생성하는 스크립트가 포함되어 있습니다.


## 주요 파일 및 폴더 구조
Korean_ChartQA/
├── Query_Answer_sample.json
├── chart_gpt_query_make.py
└── README.md



- **Query_Answer_sample.json**  
  - 차트 데이터에 대해 생성된 QA 쌍의 예시를 JSON 형식으로 담고 있습니다.  
  - 각 항목은 `"query"`(질문)와 `"answer"`(답변) 필드를 갖고 있습니다.

- **chart_gpt_query_make.py**  
  - 차트와 관련된 질의를 자동으로 생성하기 위해 작성된 Python 스크립트입니다.  
  - OpenAI의 GPT 모델을 호출하여, 입력된 차트 데이터(또는 차트 설명)에 근거한 한국어 질문을 만들어 줍니다.  
  - 이 스크립트를 실행하면, 지정된 형식으로 QA 쌍이 생성되어 JSON 형태로 저장하거나 콘솔에 출력할 수 있습니다.

- **README.md**  
  - 이 파일 자체로, 프로젝트 사용법과 구성 요소, 주의사항 등을 설명합니다.


## 요구 사항
- Python 3.7 이상
- 아래 Python 패키지
  - `openai` (OpenAI API 호출용)
  - `json` (파이썬 기본 모듈, JSON 입출력)
  - (`pandas`, `numpy` 등 추가 데이터 처리용 패키지가 필요할 수 있으나, 현재 스크립트 내 의존성은 `openai` 정도입니다.)

```bash
# 예시) pip를 사용해서 필요한 패키지 설치
pip install openai
```

## Query_Answer_sample.json
Query_Answer_sample.json 파일은 실제로 GPT를 통해 생성된 예시 QA 쌍을 보여 줍니다.
아래는 일부 발췌 예시입니다.

```json

[
  {
    "query": "2020년 월별 매출이 가장 높았던 달은 언제인가요?",
    "answer": "2020년 매출 데이터를 보면 12월이 가장 높은 매출을 기록했습니다."
  },
  {
    "query": "2019년 대비 2020년 매출 변화율은 얼마인가요?",
    "answer": "2019년 매출이 50억, 2020년 매출이 60억이므로 약 20% 증가했습니다."
  }
]

```

### 필드 설명

"query": 차트나 표를 보고 사람이 묻는 자연스러운 한국어 질문

"answer": 해당 질문에 대한 간단한 답변(차트의 값/비교/추세 등을 요약)

