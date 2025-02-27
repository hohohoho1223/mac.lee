# -*- coding: utf-8 -*-
"""[카카오 부트캠프] 3주차_미니퀘스트.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/149cZe6L6R0e9z06muHc7_v2Xn7kvEi8C
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats  # SciPy의 통계 모듈을 불러옴

"""#정형데이터_미니퀘스트"""

#1
# 샘플 데이터프레임을 생성한 후, 데이터의 기본 정보를 출력하는 코드를 작성하세요.
# 샘플 데이터 생성
data = {
    '이름': ['김철수', '이영희', '박민수', '최지현', '홍길동'],
    '나이': [25, 30, 35, 28, 40],
    '직업': ['개발자', '마케터', '개발자', '디자이너', 'CEO'],
    '연봉': [4000, 3500, 5000, 4200, 10000],
    '가입일': ['2020-05-21', '2019-07-15', '2021-01-10', '2018-11-03', '2017-09-27']
}

df = pd.DataFrame(data)
df.info()

#2
# 샘플 데이터에서 나이가 30 이상이고 연봉이 5000 이하인 사람들만 필터링하는 코드를 작성하세요.
# 샘플 데이터 생성
data = {
    '이름': ['김철수', '이영희', '박민수', '최지현', '홍길동', '정지훈', '이지은'],
    '나이': [25, 30, 35, 28, 40, 50, 22],
    '직업': ['개발자', '마케터', '개발자', '디자이너', 'CEO', '디자이너', '마케터'],
    '연봉': [4000, 3500, 5000, 4200, 10000, 4600, 3300],
    '가입일': ['2020-05-21', '2019-07-15', '2021-01-10', '2018-11-03', '2017-09-27', '2016-04-11', '2022-03-19']
}

df = pd.DataFrame(data)
df_filtered = df[(df['나이'] >= 30) & (df['연봉'] <= 5000)]
df_filtered

#3
# 샘플 데이터에서 가입 연도가 2019년 이전인 사람들을 찾아 연봉을 10% 인상한 후, 전체 평균 연봉을 계산하는 코드를 작성하세요.
# 샘플 데이터 생성
data = {
    '이름': ['김철수', '이영희', '박민수', '최지현', '홍길동', '정지훈', '이지은'],
    '나이': [25, 30, 35, 28, 40, 50, 22],
    '직업': ['개발자', '마케터', '개발자', '디자이너', 'CEO', '디자이너', '마케터'],
    '연봉': [4000, 3500, 5000, 4200, 10000, 4600, 3300],
    '가입일': ['2020-05-21', '2019-07-15', '2021-01-10', '2018-11-03', '2017-09-27', '2016-04-11', '2022-03-19']
}

df = pd.DataFrame(data)

df_before_2019 = df[df['가입일']< '2019-01-01']
df_before_2019['연봉'] = df_before_2019["연봉"] * 1.1
# df_before_2019 += 1.1 랑 같은표현이다.
df_before_2019['연봉'].mean()

"""#비정형데이터_미니퀘스트

"""

#1
# JSON 형식의 데이터를 직접 생성한 후, Pandas 데이터프레임으로 변환하는 코드를 작성하세요.
# JSON 데이터 직접 생성
import pandas as pd

data = '''
[
    {"이름": "김철수", "나이": 25, "직업": "개발자", "연봉": 4000},
    {"이름": "이영희", "나이": 30, "직업": "마케터", "연봉": 3500},
    {"이름": "박민수", "나이": 35, "직업": "디자이너", "연봉": 4200}
]
'''
# JSON 데이터를 Pandas 데이터프레임으로 변환
df = pd.read_json(data)
df

#2
# 아래 샘플 데이터에서 한글과 공백을 제외한 모든 문자를 제거하고, 공백을 하나로 정리하는 코드를 작성하세요.
# 샘플 데이터 (비정형 텍스트)
text = "안녕하세요!!! 저는 AI 모델-입니다. 12345 데이터를   정리해 보겠습니다."

#3
# 주어진 텍스트 데이터를 문장 단위로 분리한 후, 각 문장의 단어 개수를 데이터프레임으로 변환하는 코드를 작성하세요.
# 샘플 텍스트 데이터
text = "자연어 처리는 재미있다. 파이썬과 pandas를 활용하면 편리하다. 데이터 분석은 흥미롭다."

"""#막대그래프_미니퀘스트"""

#1
# matplotlib을 활용하여 5개의 카테고리와 각각의 값이 포함된 기본 세로 막대 그래프를 생성하는 코드를 작성하세요
# 샘플 데이터 생성
categories = ['A', 'B', 'C', 'D', 'E']
values = [12, 25, 18, 30, 22]
plt.plot(categories, values)
plt.show()

#2
# 누적형 막대 그래프를 생성하여, 두 개의 연도별 데이터를 각각 다른 색상으로 누적하여 표현하는 코드를 작성하세요.
# 샘플 데이터 생성
categories = ['A', 'B', 'C', 'D', 'E']
values_2023 = [10, 15, 20, 25, 30]
values_2024 = [5, 10, 12, 18, 22]

x = np.arange(len(categories))

plt.bar(x, values_2023, color='red')
plt.bar(x, values_2024, bottom=values_2023,color='blue')

plt.show()

#3
# 한 기업의 부서별 연간 성과(2023년 vs 2024년)를 비교하는 그룹형 막대 그래프를 생성하는 코드를 작성하세요.
# 샘플 데이터 생성
departments = ['Sales', 'Marketing', 'IT', 'HR', 'Finance']
performance_2023 = [80, 70, 90, 60, 75]
performance_2024 = [85, 75, 95, 65, 80]

bar_width =0.4

x = np.arange(len(departments))

plt.bar(x-bar_width/2, performance_2023, width=bar_width, color='purple', label='2023')
plt.bar(x+bar_width/2, performance_2024, width=bar_width, color ='green', label='2024')

plt.xticks(x, departments)
plt.xlabel('Departments')
plt.ylabel('Performance')
plt.legend()

plt.show()

"""#히스토그램_미니퀘스트"""

#1
# 정규 분포를 따르는 1000개의 데이터를 생성한 후, 구간을 15개로 설정한 히스토그램을 그리는 코드를 작성하세요.

# 정규 분포를 따르는 1000개의 데이터 생성
data = np.random.randn(1000)

plt.hist(data, bins =15, color = 'skyblue', edgecolor = 'black')
plt.show()

#2
# 두 개의 서로 다른 정규 분포를 따르는 데이터셋을 생성한 후, 두 히스토그램을 같은 그래프에서 겹쳐서 비교하는 코드를 작성하세요.
# 첫 번째 데이터셋 (평균 0, 표준편차 1)
data1 = np.random.randn(1000)

# 두 번째 데이터셋 (평균 3, 표준편차 1)
data2 = np.random.randn(1000) + 3

plt.hist(data1,bins = 15,color='green',edgecolor ='black')
plt.hist(data2,bins = 15,color='red', edgecolor ='black')
plt.show()

#3
# 한 데이터셋의 누적 히스토그램을 그린 후, X축과 Y축의 적절한 레이블을 설정하는 코드를 작성하세요.
# 정규 분포를 따르는 1000개의 데이터 생성
data = np.random.randn(1000)

plt.hist(data, bins=20, cumulative=True, color='skyblue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Cumulative Frequency')
plt.show()

"""#산점도_미니퀘스트"""

#1
# 두 개의 리스트 x = [1, 2, 3, 4, 5], y = [3, 1, 4, 5, 2]를 사용하여 산점도를 그리고,
#  X축과 Y축의 라벨을 추가하는 코드를 작성하세요.
# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [3, 1, 4, 5, 2]

plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.scatter(x,y)
plt.show()

#2
# numpy를 활용하여 난수를 생성한 후, 산점도를 그리고 점의 색상과 투명도를 설정하는 코드를 작성하세요.
# 난수 데이터 생성
np.random.seed(42)
x = np.random.rand(50) * 10  # 0~10 범위의 난수 50개
y = np.random.rand(50) * 10  # 0~10 범위의 난수 50개

plt.scatter(x, y, c='blue', alpha=0.5) #절반 투명도
plt.show()

#3
# numpy를 활용하여 세 개의 그룹('A', 'B', 'C')에 속하는 데이터의 산점도를 서로 다른 색상으로 그리는 코드를 작성하세요.
# 데이터 생성
np.random.seed(10)
x = np.random.randn(50) * 2
y = np.random.randn(50) * 2
categories = np.random.choice(['A', 'B', 'C'], size=50)
colors = {'A': 'red', 'B': 'green', 'C': 'blue'}

for i in np.unique(categories):
    idx = categories == i # 이렇게 처리하는게 인상적이었.
    plt.scatter(x[idx],y[idx], color= colors[i],alpha=0.6,s=80)

"""#박스플롯_미니퀘스트"""

#1
# 평균 0, 표준편차 1을 따르는 정규분포 난수 50개를 생성한 후, 해당 데이터를 이용해 기본 박스 플롯을 출력하는 코드를 작성하세요.
# 정규분포를 따르는 난수 50개 생성
np.random.seed(42)
data = np.random.randn(50)

plt.boxplot(data)
plt.show()

#2
# 세 개의 그룹(Group A, Group B, Group C) 에 대해 각각 다른 평균을 가지는 데이터를 생성하고,
# 이를 이용해 다중 박스 플롯을 그리는 코드를 작성하세요.
# 랜덤 데이터 생성 (각 그룹별 평균 다르게 설정)
np.random.seed(42)
group_a = np.random.randn(50) * 1.5  # 표준편차 1.5, 평균 0
group_b = np.random.randn(50) * 1.5 + 3  # 표준편차 1.5, 평균 3
group_c = np.random.randn(50) * 1.5 - 3  # 표준편차 1.5, 평균 -3

plt.boxplot([group_a,group_b,group_c]) #리스트 형태로 입력
plt.show()

#3
# 평균이 **서로 다른 두 개의 그룹(Group X, Group Y)** 을 비교하는 박스 플롯을 그리세요.
# 단, **이상값을 강조하고, 스타일을 커스터마이징**해야 합니다.

# 랜덤 데이터 생성 (두 그룹의 평균 다르게 설정)
np.random.seed(42)
group_x = np.random.randn(50) * 2  # 표준편차 2, 평균 0
group_y = np.random.randn(50) * 2 + 5  # 표준편차 2, 평균 5

plt.boxplot([group_x,group_y],flierprops=dict(marker='o'),patch_artist=True)
plt.show()

"""#고급 다중 그래프_미니퀘스트"""

#1
# plt.subplots()를 사용하여 2x1 형태의 서브플롯을 만들고, 첫 번째 서브플롯에는 y = x^2, 두 번째 서브플롯에는 y = x^3을 그리는 코드를 작성하세요.
# 데이터 생성
x = np.linspace(-5, 5, 100)
y1 = x ** 2  # x의 제곱
y2 = x ** 3  # x의 세제곱

fig, axis = plt.subplots(nrows=2,ncols=1)
axis[0].plot(x,y1)
axis[1].plot(x,y2)

plt.show()

#2
# X축을 공유하는 1행 2열 형태의 서브플롯을 생성하고, 첫 번째 서브플롯에는 정규 분포를 따르는 난수의 히스토그램,
# 두 번째 서브플롯에는 균등 분포를 따르는 난수의 히스토그램을 그리세요.

# 데이터 생성
normal_data = np.random.randn(1000)  # 정규 분포 난수 1000개
uniform_data = np.random.rand(1000)  # 균등 분포 난수 1000개
fig,axis = plt.subplots(nrows=1,ncols=2,sharex=True)
axis[0].hist(normal_data,bins=20,color='green',edgecolor='black')
axis[1].hist(uniform_data,bins=10,color='red',edgecolor='black')
plt.show()

#3
# gridspec을 사용하여 불규칙한 레이아웃의 서브플롯을 생성하고, 각각 선 그래프, 산점도, 막대 그래프, 히스토그램을 그리세요.
# 데이터 생성
import matplotlib.gridspec as gridspec

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.random.randn(100)
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 5, 2, 8]

fig = plt.figure(figsize=(10,8))
gs = gridspec.GridSpec(3,2,figure=fig)

ax1 = fig.add_subplot(gs[0,:])
ax1.plot(x,y1)

ax2 = fig.add_subplot(gs[1,0])
ax2.scatter(x,y2)

ax3 = fig.add_subplot(gs[1,1])
ax3.bar(categories,values)

ax4 = fig.add_subplot(gs[2,:])
ax4.hist(y2,bins=10)

plt.show()

"""#벤다이어그램_미니퀘스트"""

#1
# 두 개의 과일 집합을 정의하고, 두 집합의 차집합(한 집합에만 존재하는 요소)을 출력하는 코드를 작성하세요.
# 두 개의 과일 집합 정의

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

set_A = {"사과", "바나나", "체리", "망고"}
set_B = {"바나나", "망고", "포도", "수박"}

venn2([set_A,set_B],set_labels=('과일 집합 A', '과일 집합 B'))
plt.show()

#2
# 벤 다이어그램을 그리지 않고, 세 개의 집합을 비교하여 각 집합이 단독으로 가지는 요소 개수와 교집합 개수를 계산하는 코드를 작성하세요.
# 세 개의 과일 집합 정의
from matplotlib_venn import venn3

set_A = {"사과", "바나나", "체리", "망고"}
set_B = {"바나나", "망고", "포도", "수박"}
set_C = {"망고", "수박", "딸기", "오렌지"}

venn3([set_A,set_B,set_C],set_labels=('과일 집합 A', '과일 집합 B','과일 집합 C'))
plt.show()

#3
# **벤 다이어그램을 그리면서, 특정 조건을 만족하는 경우 색상을 다르게 지정하는 코드**를 작성하세요.
# - **조건:** 두 개의 집합을 비교할 때, **교집합이 2개 이상이면 노란색, 그렇지 않으면 기본 색상**을 사용하세요.

# 두 개의 집합 정의
set_A = {"사과", "바나나", "체리", "망고"}
set_B = {"바나나", "망고", "포도", "수박"}

diagram = venn2([set_A,set_B],set_labels=("set_A","set_B"))

intersec = set_A.intersection(set_B)

if len(intersec)>=2:
    diagram.get_patch_by_id('11').set_color('yellow')
# 나머지 부분의 색상은 기본 색상으로 두기
else:
    diagram.get_patch_by_id('11').set_color('white')

diagram.get_patch_by_id('10').set_color('lightblue')
diagram.get_patch_by_id('01').set_color('lightgreen')

plt.show()

"""#범주형 데이터_미니퀘스트"""

#1
# 샘플 데이터를 직접 생성한 후 Seaborn을 활용하여 막대 그래프(bar plot)를 생성하는 코드를 작성하세요.
# 샘플 데이터 생성
# 라이브러리 불러오기
import seaborn as sns  # Seaborn: 데이터 시각화 라이브러리
import matplotlib.pyplot as plt  # Matplotlib: 그래프 출력을 위한 라이브러리
import pandas as pd  # Pandas: 데이터프레임 생성 및 처리 라이브러리

data = pd.DataFrame({
    "카테고리": ["X", "X", "Y", "Y", "Z", "Z", "Z", "X", "Y", "Z"],
    "값": [5, 9, 4, 6, 12, 10, 14, 7, 5, 18]
})
sns.barplot(x="카테고리",y="값", data=data)
plt.show()

#2
# Seaborn의 sns.boxplot()을 활용하여 범주형 데이터의 분포를 시각화하는 코드를 작성하세요
# 샘플 데이터 생성
data = pd.DataFrame({
    "group": ["A", "A", "B", "B", "C", "C", "C", "A", "B", "C"],
    "score": [65, 70, 55, 60, 90, 85, 95, 72, 58, 88]
})

sns.boxplot(x="group",y="score",data= data)
plt.show()

#3
# Seaborn의 sns.violinplot()과 sns.stripplot()을 함께 사용하여 범주형 데이터의 분포를 더욱 자세히 시각화하는 코드를 작성하세요.
# 샘플 데이터 생성
data = pd.DataFrame({
    "category": ["A", "A", "B", "B", "C", "C", "C", "A", "B", "C"],
    "score": [80, 85, 70, 75, 95, 90, 100, 82, 72, 98]
})

sns.violinplot(x="category",y="score", data=data)
sns.stripplot(x="category",y="score",data=data,jitter=True)
plt.show()

"""#연속형 데이터_미니퀘스트"""

#1
# 평균 0, 표준편차 1을 따르는 정규 분포 데이터를 500개 생성한 후, 히스토그램과 KDE를 함께 시각화하는 코드를 작성하세요.
# 정규 분포를 따르는 데이터 생성
np.random.seed(42)
data = np.random.randn(500)

sns.histplot(data, kde=True)
plt.show()

#2
# 0부터 20까지 균등한 간격으로 생성된 데이터를 사용하여, 사인 함수의 선 그래프를 그리는 코드를 작성하세요.
# X 값 생성 (0부터 20까지 100개의 균등한 값)
x = np.linspace(0, 20, 100)
y = np.sin(x)

sns.lineplot(x=x,y=y)
plt.show()

#3
# 랜덤한 100개의 연속형 데이터를 생성하여, 산점도와 회귀선을 포함한 그래프를 그리는 코드를 작성하세요.
# 난수 생성 (재현 가능성 유지)
np.random.seed(0)
x = np.random.rand(100) * 10  # 0~10 사이 난수
y = 2 * x + np.random.randn(100)  # x와 비례하는 관계, 약간의 변동 추가
sns.scatterplot(x=x,y=y)
sns.regplot(x=x,y=y)
plt.show()

"""- R프로그램보다 코드구현이 깔끔한것 같다. 라이브러리 이용을 해서 그런가?

#관계 데이터_미니퀘스트
"""

#1
# Seaborn의 `scatterplot`을 활용하여 "총 결제 금액"(`total_bill`)과 "팁"(`tip`)의 관계를 시각화하는 코드를 작성하세요.
# 단, `scatterplot`의 색상과 스타일을 다르게 설정하여 출력해야 합니다.

# 라이브러리 불러오기
import seaborn as sns  # Seaborn 라이브러리 (관계 데이터 시각화를 위한 라이브러리)
import matplotlib.pyplot as plt  # 그래프 출력을 위한 Matplotlib 라이브러리
import pandas as pd  # 데이터프레임 생성 및 처리
import numpy as np  # 수치 연산을 위한 NumPy 라이브러리

# 예제 데이터 로드 (Seaborn 내장 데이터셋: tips)
tips = sns.load_dataset("tips")

sns.scatterplot( y= "tip",x='tip', data=tips,)
plt.show()

#2
# `sns.regplot`을 사용하여 "총 결제 금액"(`total_bill`)과 "팁"(`tip`)의 관계를 나타내는 회귀선 그래프를 그리고, 산점도의 투명도를 조정하는 코드를 작성하세요.
# **단, 산점도에서 특정 성별(`sex`)만 필터링하여 표시해야 합니다.**
# 예제 데이터 로드
tips = sns.load_dataset("tips")

filtered_tips = tips[tips['sex'] == 'Female']

sns.regplot(x='total_bill',y='tip',data=filtered_tips,scatter_kws={'alpha':0.5}) #kws = Keyword Arguments
plt.show()

#3
# `sns.pairplot`을 사용하여 다중 변수(`total_bill`, `tip`, `size`) 간의 관계를 성별(`sex`)과 요일(`day`)에 따라 시각화하는 코드를 작성하세요.
# 단, 요일(`day`)에 따라 다른 색상을 적용해야 합니다.
# 예제 데이터 로드
tips = sns.load_dataset("tips")

sns.pairplot(tips, vars=["total_bill","tip","size"], hue='day') #hue='' : 특정 '범주형' 카테고리를 지정해서 보는기능
plt.show()

"""#시계열데이터_미니퀘스트"""

#1
# 100일간의 시계열 데이터를 생성하고, 이를 선 그래프로 시각화하는 코드를 작성하세요.

# 필수 라이브러리 불러오기
import seaborn as sns  # Seaborn 라이브러리 (데이터 시각화)
import pandas as pd  # Pandas (데이터프레임 처리)
import numpy as np  # NumPy (수학 연산 및 난수 생성)
import matplotlib.pyplot as plt  # Matplotlib (그래프 출력)

# 시계열 데이터 생성
np.random.seed(42)
date_range = pd.date_range(start="2023-01-01", periods=100, freq="D")  # 100일간의 날짜 생성
values = np.cumsum(np.random.randn(100))  # 랜덤 값의 누적합

df = pd.DataFrame({"Date" : date_range, "Value" : values})
sns.lineplot(x="Date",y="Value",data=df)
plt.show()

#2
# 1번 퀘스트에서 생성한 데이터를 기반으로 7일 이동 평균을 계산하고, 원본 데이터와 함께 그래프로 비교하는 코드를 작성하세요.
# 시계열 데이터 생성
np.random.seed(42)
date_range = pd.date_range(start="2023-01-01", periods=100, freq="D")
values = np.cumsum(np.random.randn(100))

df = pd.DataFrame({"Date" : date_range, "value" : values})
df["Moving_Average"] = df["value"].rolling(window=7).mean()

sns.lineplot(x ="Date" , y = "value", data = df)
sns.lineplot(x="Date",y="Moving_Average", data=df)
plt.show()

#3
# **1번 퀘스트에서 생성한 시계열 데이터에서 이상치를 탐지하고, 이상치만 강조하여 그래프에 표시하는 코드**를 작성하세요.
# 이상치는 사분위수 범위(IQR)를 이용해 판단합니다.
# 시계열 데이터 생성
np.random.seed(42)
date_range = pd.date_range(start="2023-01-01", periods=100, freq="D")
values = np.cumsum(np.random.randn(100))

Q1 = df["value"].quantile(0.25)
Q3 = df["value"]*0.75

IQR = Q3-Q1

lower_bound= Q1 - IQR*1.5
upper_bound = Q3 + IQR*1.5

df["outlier"] = (df["value"] < lower_bound) | (df["value"] > upper_bound)
k = df["outlier"]

sns.lineplot(x="Date",y="value",data=df)
sns.scatterplot(x="Date",y="value",data=df[k],color="red",label="Outliers", s=80)
#s=이상치 크기
#같은 데이터를 중복해서 그릴수 있다
plt.show()

"""- 분명 이상치는 scatter()함수로 인자를 받는데 linplot()에 동기화가 되는이유
    - seaborndms soqnwjrdmfh matplotlib으로 그래프를 그리기 때문에 lineplot()을 호풀하면 하나의 Axes 객체가 생성된다.
    - 이 Axes객체에 이후에 추가적으로 그리는 모든 그래프는 포함된다!
        * 참고로 matplotlib()으로 그리는 다중그래프도 axis[0], axis[1] 객체를 이용하여 그래프를 그리고 여러개 서브플롯을 생성하고 관리한다!
        - 오키?

#리샘플링_미니퀘스트
"""

#1
# `pandas`를 사용하여 **3시간 간격의 시계열 데이터를 생성한 후**,
#  하루 단위(`D`)로 **평균을 구하는 다운샘플링을 수행하는 코드**를 작성하세요.
# 3시간 간격의 시계열 데이터 생성 (2024년 1월 1일부터 5일까지)
date_rng = pd.date_range(start="2024-01-01", end="2024-01-05", freq="3h")#3시간 간격
df = pd.DataFrame({"datetime": date_rng, "value": np.random.randint(50, 150, size=len(date_rng))})
df.set_index("datetime", inplace=True)

# 다운샘플링 (하루 단위로 평균 구하기
df_daily = df.resample("d").mean()
df_daily

#2
# 3시간 간격으로 생성된 시계열 데이터에서 1시간 단위로 업샘플링한 후,
# 선형 보간(linear)을 적용하는 코드를 작성하세요.
# 3시간 간격의 시계열 데이터 생성
date_rng = pd.date_range(start="2024-01-01", end="2024-01-03", freq="1h")
df = pd.DataFrame({"datetime": date_rng, "value": np.random.randint(50, 150, size=len(date_rng))})
df.set_index("datetime",inplace = True)

df_daily = df.resample("h").asfreq() #asfreq : "as frequency"
df_daily = df_daily.interpolate(method="linear") # 선형보간
df_daily #널값이 출력되는데, 이는 보간법으로 보충을 해야한다.

#3
# 3시간 간격으로 생성된 시계열 데이터에서 하루 단위(D)로 다운샘플링을 수행한 후,
# 각 날짜에 해당하는 최소(min) 값과 최대(max) 값을 출력하는 코드를 작성하세요.
# 3시간 간격의 시계열 데이터 생성
date_rng = pd.date_range(start="2024-01-01", end="2024-01-07", freq="3h")

df_daily = df.resample("d").agg({"value" : ["min","max"]})
df_daily

"""#이동평균_미니퀘스트"""

#1
# 주어진 시계열 데이터에서 **7일 단순 이동평균(SMA)** 을 계산하여 새로운 컬럼을 추가하는 코드를 작성하세요.
# 샘플 시계열 데이터 생성
date_rng = pd.date_range(start="2024-01-01", end="2024-01-20", freq="D")
df = pd.DataFrame({
    "datetime": date_rng,
    "value": np.random.randint(50, 150, size=len(date_rng))
})

df["SMA"] = df["value"].rolling(window=7).mean()
df

#2
# 시계열 데이터에서 7일 지수 이동평균(EMA) 을 계산하고, 기존 데이터와 비교하여 출력하는 코드를 작성하세요.
# 샘플 시계열 데이터 생성
date_rng = pd.date_range(start="2024-01-01", end="2024-01-20", freq="D")
df = pd.DataFrame({
    "datetime": date_rng,
    "value": np.random.randint(50, 150, size=len(date_rng))
})

df["EMA"] = df["value"].ewm(span=7, adjust=False).mean()
#adjust = False : 기존값보다 새로운값에 더높은 가중치 부여 -> 지수 이동평균(EMA)
df

#3
# 주어진 시계열 데이터에서 **이동평균을 활용하여 변동성이 큰 날을 탐색하는 코드**를 작성하세요.
# **7일 단순 이동평균(SMA)과 비교하여 특정 일자의 값이 이동평균보다 ±20% 이상 차이가 나는 경우만 출력**하세요.
# 샘플 시계열 데이터 생성
date_rng = pd.date_range(start="2024-01-01", end="2024-01-20", freq="D")
df = pd.DataFrame({
    "datetime": date_rng,
    "value": np.random.randint(50, 150, size=len(date_rng))
})

df['SMA'] = df["value"].rolling(window =7).mean()
weights= np.arange(1,8)
df["WMA"] = df["value"].rolling(window=7).apply(lambda x: np.dot(x, weights) / weights.sum(),raw =True)
# np.dot() : 내적을 하는이유는 배열의 곱 형태이기 때문임

df[(df["value"] > df["SMA"]*1.2) | (df["value"] < df["SMA"]*0.8)]

"""#금융데이터_미니퀘스트"""

#1
# 샘플 금융 데이터프레임을 직접 생성한 후, 데이터의 기본 정보(행 개수, 열 개수, 데이터 타입 등)를 출력하는 코드를 작성하세요.
# 샘플 금융 데이터 생성
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Open': [100, 102, 105, 103, 108, 107, 110, 112, 115, 118],
    'High': [102, 106, 108, 107, 110, 109, 112, 115, 117, 120],
    'Low': [98, 100, 103, 101, 106, 105, 108, 110, 113, 116],
    'Close': [101, 104, 106, 105, 109, 108, 111, 113, 116, 119],
    'Volume': [1000, 1200, 1500, 1300, 1600, 1400, 1700, 1800, 1900, 2000]
}
df = pd.DataFrame(data=data)
df.info()

#2
# 주어진 df 데이터프레임에서 5일 이동평균(SMA)과 5일 지수 이동평균(EMA)을 계산하는 코드를 작성하세요.
# 샘플 금융 데이터 생성
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Close': [101, 104, 106, 105, 109, 108, 111, 113, 116, 119]
}
df = pd.DataFrame(data=data)

df['SMA'] = df['Close'].rolling(window =5).mean()
df['EMA'] = df['Close'].ewm(span=5, adjust=False).mean()
df

#3
# df 데이터프레임에서 주간(7일) 단위로 종가(Close) 평균을 리샘플링한 후, 이를 바탕으로 주간 변동성(표준편차)을
# 계산하는 코드를 작성하세요.
# 샘플 금융 데이터 생성 (30일치)
date_rng = pd.date_range(start='2024-01-01', periods=30, freq='D')
close_prices = np.random.uniform(100, 200, size=len(date_rng))  # 100~200 사이의 랜덤 종가 생성

df = pd.DataFrame({'Date': date_rng, 'Close': close_prices})

df["SMA_7"] = df["Close"].rolling(window=7).mean()
df["volatility"] = df["Close"].rolling(window=7).std()
df

"""#정규분포_미니퀘스트"""

#1
# 평균 60, 표준 편차 15를 갖는 정규 분포에서 500개의 데이터를 생성한 후,
# 데이터의 기본 통계 정보(평균, 표준 편차, 최소값, 최대값)를 출력하는 코드를 작성하세요.
# 평균 60, 표준 편차 15인 정규 분포에서 500개의 난수 생성

data = np.random.normal(loc=60, scale=15, size=500)
df = pd.DataFrame(data)
df.describe()

#2
# 평균 50, 표준 편차 10을 갖는 정규 분포에서 특정 값 x=65의 확률 밀도 함수(PDF) 값을 계산하고 출력하는 코드를 작성하세요.
x_value = 65
pdf_value = stats.norm.pdf(x_value, loc=50, scale=10)
print(f"PDF at x={x_value}: {pdf_value}")

#3
# 평균 70, 표준 편차 8을 갖는 정규 분포에서 (1) 특정 값 x=80 이하일 확률을 CDF로 계산하고, (2) 상위 5%에 해당하는 점수를 PPF로 계산하여 출력하는 코드를 작성하세요.
cdf_value = stats.norm.cdf(80, loc=70, scale=8)
print(f"CDF at x=80: {cdf_value}")

ppf_value = stats.norm.ppf(0.95, loc=70, scale=8)
print(f"PPF for 95% percentile: {ppf_value}")

"""#기술통계_미니퀘스트"""

#1
# 주어진 데이터에서 평균과 중앙값의 차이를 계산하는 코드를 작성하세요.
# 샘플 데이터 생성
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=100)  # 평균 50, 표준편차 10인 정규 분포 데이터 생성
df = pd.DataFrame(data, columns=["value"])  # 데이터프레임 생성

mean_value = np.mean(df["value"])
median_value = np.median(df["value"])

print("평균과 중앙값의 차이:" , mean_value - median_value)

#2
# **데이터에서 이상값(Outlier)을 찾아 제거한 후, 원래 데이터와 이상값 제거 후 데이터의 평균을 비교하는 코드**를 작성하세요.

# 이상값은 **IQR(사분위 범위)를 사용하여 탐지**하세요.
# 샘플 데이터 생성
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=100)  # 평균 50, 표준편차 10인 정규 분포 데이터 생성
df = pd.DataFrame(data, columns=["value"])  # 데이터프레임 생성

Q1 = df["value"].quantile(0.25)
Q3 = df["value"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR

outliers = df[(df["value"] < lower_bound) | (df["value"] > upper_bound)]

filtered_df = df[(df["value"] <= upper_bound) & (df["value"] >=  lower_bound)] # 이상치 제거
print("원래 데이터 평균:", df.mean())
print("이상값 제거후 데이터의 평균:",filtered_df.mean())

#3
# 데이터의 왜도(Skewness)와 첨도(Kurtosis)를 계산하여 데이터의 분포 특성을 분석하는 코드를 작성하세요.
# 샘플 데이터 생성
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=100)  # 평균 50, 표준편차 10인 정규 분포 데이터 생성
df = pd.DataFrame(data, columns=["value"])  # 데이터프레임 생성

skewness = stats.skew(df["value"])
kurtosis = stats.kurtosis(df["value"])

print("왜도 :",skewness)
print("첨도 :",kurtosis)

"""- 왜도와 첨도가 뭘까?
    - 왜도(skewness) : 데이터 분포의 비대칭성을 나타냄. 왜도값 = 0 이면 대칭분포이다.
    - 첨도(kurtosis) : 데이터 분포의 뾰족함을 나타냄 기준은 "3임" 3보다 크면 뾰족.
        - 왜 3이 기준이냐?
        -> 4차 모먼트를 사용하여 계산함.
        - Kurtosis = \frac{E[(X - μ)^4]}{(σ^2)^2}

#가설검정_미니퀘스트
"""

#1
# **단일 표본 t-검정(One-Sample t-test)** 을 수행하여 샘플 데이터의 평균이 특정 값과 유의미한 차이가 있는지 검정하는 코드를 작성하세요.
# (평균 `50`, 표준 편차 `5`를 따르는 정규 분포에서 30개의 데이터를 생성하고, 해당 데이터가 평균 `52`와 차이가 있는지 확인하세요.)

from scipy import stats  # 가설 검정을 위한 SciPy stats 모듈 불러오기

# 샘플 데이터 생성
np.random.seed(42)
sample_data = np.random.normal(loc=50, scale=5, size=30)  # 평균 50, 표준편차 5인 데이터 30개 생성

t_stat, p_value = stats.ttest_ind(sample_data, np.full(30,52))
print("t-통계량:" , t_stat)
print("p-값:", p_value)

#2
# 카이제곱 검정(Chi-Square Test) 을 수행하여 관측된 데이터와 기대값이 유의미한 차이가 있는지 확인하는 코드를 작성하세요.

# 관측된 데이터 (Observed)
observed = np.array([50, 60, 90])

# 기대값 (Expected)
expected = np.array([66, 66, 66]) * (observed.sum() / np.sum([66, 66, 66]))

print(stats.chisquare(observed,expected))

#3
# 분산 분석(ANOVA, Analysis of Variance) 을 수행하여 여러 그룹의 평균이 서로 다른지 검정하는 코드를 작성하세요.
# 샘플 데이터 생성
np.random.seed(42)
group_1 = np.random.normal(loc=50, scale=10, size=30)  # 평균 50, 표준편차 10
group_2 = np.random.normal(loc=55, scale=10, size=30)  # 평균 55, 표준편차 10
group_3 = np.random.normal(loc=60, scale=10, size=30)  # 평균 60, 표준편차 10

stats.f_oneway(group_1, group_2, group_3)

"""#통계적 시각화_미니퀘스트"""

#1
# NumPy를 사용하여 평균 70, 표준편차 20을 따르는 정규 분포 데이터 1000개를 생성한 후, Matplotlib을 활용하여 박스플롯을 그리는 코드를 작성하세요.
# 데이터 생성 (평균=70, 표준편차=20인 정규 분포 데이터 1000개)
np.random.seed(42)
data = np.random.normal(loc=70, scale=20, size=1000)

df = pd.DataFrame(data, columns=["value"])

plt.boxplot(df["value"], vert=False, patch_artist=True, boxprops=dict(facecolor="green"))
plt.show()

#2
# 평균이 각각 55와 60이고, 표준편차가 8인 두 개의 그룹(A, B) 데이터를 생성한 후, **두 그룹의 데이터 분포를 Seaborn을 활용하여 KDE(커널 밀도 함수)와 함께 히스토그램으로 시각화**하세요.
# 이후, **두 그룹 간 평균 차이가 유의미한지 t-검정을 수행하는 코드**를 작성하세요.
# 데이터 생성
np.random.seed(42)
group_A = np.random.normal(loc=55, scale=8, size=200)  # 평균 55, 표준편차 8
group_B = np.random.normal(loc=60, scale=8, size=200)  # 평균 60, 표준편차 8

df_1 = pd.DataFrame(group_A, columns=["value"])
df_2 = pd.DataFrame(group_B, columns=["value"])

sns.kdeplot(df_1["value"], label="Group A", shade=True)
sns.kdeplot(df_2["value"], label="Group B", shade=True)
plt.hist(df_1["value"], alpha=0.3)
plt.hist(df_2["value"], alpha=0.3)
plt.legend()

t_stat,p_value = stats.ttest_ind(group_A, group_B, equal_var=False)
#_ind : independent(독립)
#equal_var = False :두 그룹의 분산이 다르다고 가정한 것. -> Welch의 t-검정으로, 분산이 다를때 높은 정확도를 제공함.
print("t-통계량:", t_stat)
print("p-값:", p_value)
plt.show()

#3
# 광고 A를 본 500명 중 120명이 클릭하였고, 광고 B를 본 500명 중 150명이 클릭을 한 데이터가 있습니다.
# 이 데이터를 바탕으로 **카이제곱 검정을 수행하여 광고 A와 B의 클릭률 차이가 유의미한지 분석하고,
# Seaborn의 barplot을 사용하여 클릭률을 비교하는 그래프를 그리는 코드**를 작성하세요.

# 데이터 생성 (광고 A와 B의 클릭 여부)
observed_data = pd.DataFrame({
    "Ad_A": [120, 380],  # 광고 A 클릭(120명) vs 미클릭(380명)
    "Ad_B": [150, 350]   # 광고 B 클릭(150명) vs 미클릭(350명)
}, index=["Click", "No Click"])

# 카이제곱 검정
chi2_stat, p_value, dof, expected = stats.chi2_contingency(observed_data)
print("카이제곱 통계량:", chi2_stat)

if p_value < 0.05:
    print("p-값:", p_value)
    print("클릭률 차이가 유의미하다")
else:
    print("p-값:", p_value)
    print("클릭률 차이가 유의미하지 않다")

# 클릭률 계산
click_rates_A = observed_data.loc["Click","Ad_A"] / observed_data["Ad_A"].sum()
click_rates_B = observed_data.loc["Click","Ad_B"] / observed_data["Ad_B"].sum()

click_rate_df = pd.DataFrame({
    "Ad": ["Ad_A", "Ad_B"],
    "Click Rate": [click_rates_A, click_rates_B]
})

plt.figure(figsize=(8, 5))
sns.barplot(x="Ad", y="Click Rate", data=click_rate_df, palette="viridis")
plt.title("Click Rate Comparison between Ad A and Ad B")
plt.xlabel("Advertisements")
plt.ylabel("Click Rate")
plt.ylim(0, 1)  # 클릭률은 0에서 1 사이의 값
plt.axhline(0, color='grey', linewidth=0.8)   # y=0 선 추가
plt.grid(axis='y', linestyle='--', alpha=0.7)  # y축 그리드 추가
plt.show()

observed_data

click_rate_df

"""- 데이터프레임 형식은 pd.DataFrame({"컬럼 1" : [값1,값2], "컬럼 2" : [값1,값2] })"""
