# -*- coding: utf-8 -*-
"""[카카오 부트캠프] Numpy & Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s9YAcdh7DsAm3Padz6n9gSalUP08SEKt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""# 차원 미니퀘스트"""

#1
array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
array.ndim

#2
b1 = np.array([10, 20, 30, 40, 50, 60])
print(b1.reshape(2,3))
print(b1.ndim) # 이경우는 얕은 복사

k1 = b1.copy()
k =k1.reshape(2,3)
print(k)
print(k.ndim) # 이경우는 깊은 복사

b2 = np.array([10, 20, 30, 40, 50, 60])
b2.resize(2,3)
print(b2)
print(b2.ndim) # 이경우는 깊은 복사

#3
array = np.array([7, 14, 21])
k1 = array[ : , np.newaxis]
k2 = array[np.newaxis,:]
print(k1)
print(k2)

"""# 형태 미니퀘스트"""

#1
# 주어진 2차원 NumPy 배열의 형태(Shape)를 출력하는 코드를 작성하세요.
import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6]])
k = array.shape
print(k)

# 형태2
# 1차원 배열 [10, 20, 30, 40, 50, 60]을 (2, 3) 형태로 변경한 후, 새로운 배열의 형태를 출력하는 코드를 작성하세요.

a = np.array([10, 20, 30, 40, 50, 60])
b = a.reshape(2,3) # 얖은복사
print(b)

#형태 3
# 다음 3차원 배열의 형태를 변경하여 (3, 2, 2) 형태로 조정하고, 최종 배열의 형태를 출력하는 코드를 작성하세요.
import numpy as np
array = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])
# print(array.resize(3,2,2))
print(array.reshape(3,2,2))

"""# 데이터타입 미니퀘스트"""

#1
# 아래의 NumPy 배열의 데이터 타입을 확인하는 코드를 작성하세요.
import numpy as np
array = np.array([10, 20, 30])
array.dtype

#2
# 정수형 배열 [1, 2, 3]을 부동소수점형 배열로 변환하고, 변환된 배열의 데이터 타입을 출력하는 코드를 작성하세요.
k = np.array([1,2,3])
k.astype(np.float64)

#3
# NumPy 배열 [100, 200, 300]을 uint8로 변환한 후, 메모리 사용량(바이트)을 출력하는 코드를 작성하세요.
k = np.array([100,200,300])
k1=k.astype(np.uint8)
k1.nbytes

"""# 인덱싱 미니퀘스트"""

#1
# 주어진 1차원 배열에서 첫 번째 요소와 마지막 요소를 출력하는 코드를 작성하세요.
import numpy as np
array = np.array([10, 20, 30, 40, 50])
print(array[0],array[-1])

#2
# 주어진 2차원 배열에서 첫 번째 열과 두 번째 행을 출력하는 코드를 작성하세요.
import numpy as np
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix[0],matrix[1])

#3
# 주어진 배열에서 10보다 큰 요소들만 선택하고, 해당 요소들의 인덱스를 출력하는 코드를 작성하세요.
import numpy as np
array = np.array([5, 15, 8, 20, 3, 12])
k = np.where(array > 10)
k[0] # 인덱스는 첫번째 요소에 저장됨!

"""# 연산 미니퀘스트"""

#1
# 주어진 NumPy 배열에서 요소별(Element-wise) 덧셈을 수행하는 코드를 작성하세요.
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)

#2
# 다음 NumPy 배열에서 브로드캐스팅을 활용하여 각 행에 [1, 2, 3]을 더하는 코드를 작성하세요.
import numpy as np
matrix = np.array([[10, 20, 30], [40, 50, 60]])
vector = np.array([1, 2, 3])

print(matrix+vector)

#3
# 주어진 2차원 NumPy 배열에 대해, 축(axis)을 기준으로 최댓값을 구하고 최종 배열의 차원을 출력하는 코드를 작성하세요.
import numpy as np
array = np.array([[3, 7, 2], [8, 4, 6]])
k = array.max(axis=0) #각 열에 대해서 기준
print(k)
k.ndim #number of dimensions

"""# 유니버설 함수 미니퀘스트"""

#1
# 배열 [1, 2, 3, 4]에 대해 NumPy의 유니버설 함수를 사용하여 모든 요소를 제곱한 결과를 출력하는 코드를 작성하세요.
k = np.array([1,2,3,4])
np.power(k,2)

#2
# 다음 두 배열의 요소별 합을 계산하고, 결과를 새로운 배열이 아닌 기존 배열에 저장하는 코드를 작성하세요.
array1 = np.array([10, 20, 30])
array2 = np.array([1, 2, 3])
k = np.add(array1,array2,out =k)
k

#3
# 다음 배열에 대해 NumPy 유니버설 함수를 사용하여 요소별로 자연로그(log)를 계산하고, 특정 조건(log 값 > 1)을 만족하는 요소만 출력하는 코드를 작성하세요.
array = np.array([1, np.e, 10, 100]) #numpy.e(자연상수)
np.log10(array)

"""# 시리즈 미니퀘스트"""

#1
# Pandas의 Series를 리스트 [5, 10, 15, 20]을 사용하여 생성하고, Series의 인덱스를 확인하는 코드를 작성하세요.
import pandas as pd
s = pd.Series([5,10,15,20])
print(s.index)

#2
# 다음 딕셔너리를 이용하여 Pandas Series를 생성하고, 인덱스를 활용하여 'b'의 값을 출력하는 코드를 작성하세요.
data = {'a': 100, 'b': 200, 'c': 300}
k = pd.Series(data)
print(k)
k['b']

#3
# 다음 Pandas Series에 대해 결측값(NaN)을 확인하고, 모든 결측값을 0으로 채운 후 Series의 값을 출력하는 코드를 작성하세요.
import pandas as pd
series = pd.Series([1, 2, None, 4, None, 6])
series1=series.fillna(0) #원본은 안바뀌어서 지정해야함
series1

"""# 데이터 프레임 - 미니퀴스트"""

#1
# 다음 데이터프레임에서 열(column)의 이름들을 출력하는 코드를 작성하세요.
import pandas as pd

data = {'이름': ['홍길동', '김철수', '박영희'],
        '나이': [25, 30, 28],
        '성별': ['남', '남', '여']}
df = pd.DataFrame(data)
df.columns

#2
# 다음 데이터프레임에서 나이 열(age)을 기준으로 오름차순으로 정렬된 새로운 데이터프레임을 생성하고 출력하는 코드를 작성하세요.
import pandas as pd

data = {'이름': ['홍길동', '김철수', '박영희'],
        '나이': [25, 30, 28],
        '성별': ['남', '남', '여']}
df = pd.DataFrame(data)
df = df.sort_values(by='나이')
df

#3
# 아래와 같은 데이터프레임이 있습니다.
import pandas as pd

data = {'이름': ['홍길동', '김철수', '박영희', '이순신'],
        '국어': [85, 90, 88, 92],
        '영어': [78, 85, 89, 87],
        '수학': [92, 88, 84, 90]}
df = pd.DataFrame(data)
# 각 학생의 총점을 계산하는 새로운 열을 추가한 후, 총점이 250점 이상인 학생들만 포함된 데이터프레임을 생성하세요.
df['총점'] = df['국어'] + df['영어'] + df['수학']
df[df['총점'] >= 250]

"""# 필터링 미니퀘스트"""

#1
# 주어진 데이터프레임에서 나이가 30 이상인 행만 필터링하는 코드를 작성하세요.
import pandas as pd

data = {'이름': ['홍길동', '김철수', '박영희', '이순신', '강감찬'],
        '나이': [25, 30, 35, 40, 45],
        '도시': ['서울', '부산', '서울', '대구', '부산']}

df = pd.DataFrame(data)
df1 = df[df['나이'] >= 30]
print(df1)
df2 = df.query('나이 >= 30')
print(df2)

#2
# 주어진 데이터프레임에서 도시가 '서울'이거나 점수가 80점 이상인 데이터를 필터링하는 코드를 작성하세요.
import pandas as pd

data = {'이름': ['홍길동', '김철수', '박영희', '이순신', '강감찬'],
        '나이': [25, 30, 35, 40, 45],
        '도시': ['서울', '부산', '서울', '대구', '부산'],
        '점수': [85, 90, 75, 95, 80]}

df = pd.DataFrame(data)
print(df[(df['도시'] == '서울') | (df['점수'] >= 80)])

#3
# 주어진 데이터프레임에서 query()를 사용하여 나이가 35 이상이고 점수가 80점 초과인 데이터를 필터링하는 코드를 작성하세요.
import pandas as pd

data = {'이름': ['홍길동', '김철수', '박영희', '이순신', '강감찬'],
        '나이': [25, 30, 35, 40, 45],
        '도시': ['서울', '부산', '서울', '대구', '부산'],
        '점수': [85, 90, 75, 95, 80]}

df = pd.DataFrame(data)
k = df.query('나이 >= 35 & 점수 > 80') #query는 한문장에다가 모든 조건을 기입하기!
k

"""# 그룹화 미니퀘스트"""

#1
# 주어진 데이터프레임에서 groupby()를 사용하여 '부서'별로 급여의 합계를 구하는 코드를 작성하세요.
import pandas as pd

data = {
    '이름': ['홍길동', '김철수', '박영희', '이순신'],
    '부서': ['영업', '영업', '인사', '인사'],
    '급여': [5000, 5500, 4800, 5100]
}

df = pd.DataFrame(data)
df = df.groupby('부서')['급여'].sum()
df

#2
# 아래 데이터프레임에서 groupby()와 agg()를 사용하여 '부서'별 급여의 합계(sum)와 평균(mean)을 계산하는 코드를 작성하세요.
import pandas as pd

data = {
    '이름': ['홍길동', '김철수', '박영희', '이순신', '강감찬', '신사임당'],
    '부서': ['영업', '영업', '인사', '인사', 'IT', 'IT'],
    '급여': [5000, 5500, 4800, 5100, 6000, 6200]
}

df = pd.DataFrame(data)
df = df.groupby('부서')['급여'].agg('mean','add')
df

#3
# 부서별로 데이터를 그룹화한 뒤, 각 부서의 평균 급여가 5000 이상인 경우만 필터링하는 코드를 작성하시오.
import pandas as pd

data = {
    '이름': ['홍길동', '김철수', '박영희', '이순신', '강감찬', '신사임당'],
    '부서': ['영업', '영업', '인사', '인사', 'IT', 'IT'],
    '급여': [5000, 5500, 4800, 5100, 6000, 6200]
}

df = pd.DataFrame(data)
df1 = df.groupby('부서').filter(lambda x: x['급여'].mean() >= 5000)
df2 = df.groupby('부서').apply(lambda x: x['급여'].mean() >= 5000) # 이것은 '적용'이기에 출력값이 불리안으로 나옴
print(df1)
print(df2)

"""# 병합 미니퀘스트"""

#1
# 두 개의 데이터프레임을 고객ID를 기준으로 내부 조인(inner join)하여 공통된 데이터를 병합하는 코드를 작성하세요.
import pandas as pd

df1 = pd.DataFrame({'고객ID': [1, 2, 3], '이름': ['홍길동', '김철수', '이영희']})
df2 = pd.DataFrame({'고객ID': [2, 3, 4], '구매액': [10000, 20000, 30000]})
k = pd.merge(df1,df2, on='고객ID', how = 'inner')
k

#2
# 왼쪽 데이터프레임을 기준으로 병합(left join)을 수행하고, 구매액이 없는 경우 NaN을 유지하는 코드를 작성하세요.
import pandas as pd

df1 = pd.DataFrame({'고객ID': [1, 2, 3], '이름': ['홍길동', '김철수', '이영희']})
df2 = pd.DataFrame({'고객ID': [2, 3, 4], '구매액': [15000, 25000, 35000]})
k = pd.merge(df1,df2 ,how ='left')
k

#3
# 두 개 이상의 열을 기준으로 병합하고, 중복 열의 이름을 구분하도록 접미사(suffixes)를 지정하는 코드를 작성하세요.
import pandas as pd

df1 = pd.DataFrame({
    '고객ID': [1, 2, 3],
    '도시': ['서울', '부산', '대전'],
    '구매액': [10000, 20000, 30000]
})

df2 = pd.DataFrame({
    '고객ID': [1, 2, 3],
    '도시': ['서울', '부산', '광주'],
    '구매액': [15000, 25000, 35000]
})

k = pd.merge(df1,df2,on = ('고객ID','도시') , suffixes=('_a','_b'))
k

"""# 결측치처리 미니퀘스트"""

#1
# 주어진 데이터프레임에서 결측치를 탐지하고, 열별 결측치 개수를 출력하는 코드를 작성하세요.
import pandas as pd
import numpy as np

data = {'이름': ['홍길동', '김철수', np.nan, '이영희'],
        '나이': [25, np.nan, 30, 28],
        '성별': ['남', '남', '여', np.nan]}

df = pd.DataFrame(data)
df.isna().sum()

#2
# 주어진 데이터프레임에서 결측치가 포함된 행을 삭제하고, 새로운 데이터프레임을 출력하는 코드를 작성하세요.
import pandas as pd
import numpy as np

data = {'이름': ['홍길동', '김철수', np.nan, '이영희'],
        '나이': [25, np.nan, 30, 28],
        '성별': ['남', '남', '여', np.nan]}

df = pd.DataFrame(data)
k =df.dropna()
k

#3
# 결측치가 포함된 '나이' 열을 평균값으로 대체하고, 새로운 데이터프레임을 출력하는 코드를 작성하세요.
import pandas as pd
import numpy as np

data = {'이름': ['홍길동', '김철수', np.nan, '이영희'],
        '나이': [25, np.nan, 30, 28],
        '성별': ['남', '남', '여', np.nan]}

df = pd.DataFrame(data)
df['나이'] = df['나이'].fillna(df['나이'].mean())
df

"""# 피벗(Pivot)"""

#1
# 주어진 데이터프레임을 pivot() 함수를 사용하여 날짜(날짜)를 행 인덱스로, 제품(제품)을 열로, 판매량(판매량)을 값으로 설정하는 코드를 작성하세요.
import pandas as pd

data = {
    '날짜': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    '제품': ['A', 'B', 'A', 'B'],
    '판매량': [100, 200, 150, 250]
}

df = pd.DataFrame(data)
k = pd.pivot(data=df ,index='날짜', columns= '제품' , values = '판매량')
k

#2
# pivot_table()을 사용하여 주어진 데이터프레임에서 카테고리(카테고리)를 행 인덱스로, 제품(제품)을 열로 설정하고, 판매량(판매량)의 합계를 출력하는 코드를 작성하세요.
import pandas as pd

data = {
    '카테고리': ['전자', '가전', '전자', '가전'],
    '제품': ['A', 'B', 'A', 'B'],
    '판매량': [100, 200, 150, 250]
}

df = pd.DataFrame(data)
k = pd.pivot_table(data = df, index='카테고리', columns ='제품',values='판매량', aggfunc='sum')
k

#3
# 주어진 데이터프레임에서 여러 값을 동시에 피벗하여, pivot()을 사용해 날짜(날짜)를 행으로, 제품(제품)을 열로 설정하고,
# 판매량(판매량)과 이익(이익)을 동시에 피벗하는 코드를 작성하세요.
import pandas as pd

data = {
    '날짜': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    '제품': ['A', 'B', 'A', 'B'],
    '판매량': [100, 200, 150, 250],
    '이익': [20, 50, 30, 60]
}

df = pd.DataFrame(data)
k = pd.pivot(data = df ,index = '날짜',columns ='제품',  values= ['판매량','이익'])
k

"""# 중복제거 미니퀘스트"""

#1
# 주어진 데이터프레임에서 기본적으로 중복된 행을 제거하는 코드를 작성하세요.
import pandas as pd

data = {
    '이름': ['김철수', '이영희', '김철수', '박민수'],
    '나이': [25, 30, 25, 40],
    '성별': ['남', '여', '남', '남']
}

df = pd.DataFrame(data)

k = df.drop_duplicates()
k

#2
# 다음 데이터프레임에서 특정 열을 기준으로 중복을 제거한 후, 중복 여부를 확인하는 코드를 작성하세요.
import pandas as pd

data = {
    '제품': ['노트북', '태블릿', '노트북', '스마트폰'],
    '가격': [1500000, 800000, 1500000, 1000000],
    '카테고리': ['전자기기', '전자기기', '전자기기', '전자기기']
}

df = pd.DataFrame(data)
df.drop_duplicates(subset = ['제품'], inplace = True)
df.duplicated()

#3
# 다음 데이터프레임에서 중복된 모든 행을 삭제한 후, 남은 데이터를 저장하고 다시 불러오는 코드를 작성하세요.
import pandas as pd

data = {
    '학생': ['김민수', '박지현', '김민수', '이정훈'],
    '성적': [90, 85, 90, 88],
    '학교': ['A고', 'B고', 'A고', 'C고']
}

df = pd.DataFrame(data)
df.drop_duplicates(keep = False, inplace = True)
df

"""# 문자열 처리 미니퀘스트"""

#1
# Pandas의 .str 접근자를 사용하여 아래 시리즈의 모든 문자열을 소문자로 변환하는 코드를 작성하세요.
import pandas as pd
data = pd.Series(["HELLO", "WORLD", "PYTHON", "PANDAS"])

k = data.str.lower()
k

#2
# 다음 데이터프레임에서 '이름' 컬럼의 문자열 앞뒤 공백을 제거하고, 특정 문자열 "Doe"가 포함된 행을 필터링하는 코드를 작성하세요.
import pandas as pd
df = pd.DataFrame({"이름": [" John Doe ", "Alice ", " Bob", "Charlie Doe "]})
# k =df[(df['이름'].str.strip()) & (df['이름'].filter(lambda x : x['이름'] == 'Doe'))]
j = df[df['이름'].str.strip().apply(lambda x : 'Doe' in x)]
j

#3
# 아래 데이터프레임에서 '설명' 컬럼의 문자열을 공백을 기준으로 나누고, 각 단어의 첫 글자만 추출하여 새로운 컬럼 '약어'를 생성하는 코드를 작성하세요.
import pandas as pd
df = pd.DataFrame({"설명": ["빅데이터 분석", "데이터 과학", "머신 러닝", "딥 러닝"]})
df['약어'] = df['설명'].str.split(" ").apply(lambda x: x[0][0] + x[1][0])
df

import copy

# 리스트 내부에 리스트가 있는 경우
a = [1, 2, [3, 4]]

# 깊은 복사
b = copy.deepcopy(a)

# b의 내용을 변경
b[0] = 10
b[2][0] = 30

print(a)  # [1, 2, [3, 4]] (a는 변경되지 않음)
print(b)  # [10, 2, [30, 4]] (b는 독립적임)

import copy

# 리스트 내부에 리스트가 있는 경우
a = [1, 2, [3, 4]]

# 깊은 복사
b = a.copy()

# b의 내용을 변경
b[0] = 10
b[2][0] = 30

print(a)  # [1, 2, [3, 4]] (a는 변경되지 않음)
print(b)  # [10, 2, [30, 4]] (b는 독립적임)

x = [0,1,2,3,4,5,6,7,8,9]
print(x.ndim, x.shape)

x = np.arange(9).reshape(3,3)
print(x)

y = x[[1,2]] # [x[1],x[2]]
print(y)

y = [x[0],x[2]]
print(y)

