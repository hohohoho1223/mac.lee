# -*- coding: utf-8 -*-
"""[카카오 부트캠프] 4주차_미니퀘스트(CNN).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K5FR4jwz7VceQ81nZFsJ6FrC40WFV0N0
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

"""#데이터전처리

<aside>
👉 간단한 데이터셋을 사용하여 데이터 전처리 과정을 단계별로 진행해보세요.

각 단계에서 필요한 코드를 작성하고, 그 결과를 확인합니다.

### 데이터셋

- 가상의 학생 성적 데이터
- 예시데이터
    
    ```python
    # 가상의 데이터셋 생성
    data = {
        '학생': ['A', 'B', 'C', 'D', 'E'],
        '수학': [90, np.nan, 85, 88, np.nan],
        '영어': [80, 78, np.nan, 90, 85],
        '과학': [np.nan, 89, 85, 92, 80]
    }
    ```
    

### 문제 설명

1. 데이터 수집
    - 가상의 학생 성적 데이터를 생성합니다.
2. 결측값 처리
    - 데이터셋에 누락된 값이 있을 때, 이를 평균값으로 대체합니다.
3. 이상치 제거
    - 데이터셋에 이상치가 없는지 확인하고, 필요하면 제거합니다.
4. 데이터 정규화
    - 수학, 영어, 과학 점수를 0과 1 사이의 값으로 스케일링합니다.
5. 데이터 분할
    - 데이터셋을 학습용과 검증용으로 나눕니다.
</aside>
"""

#1 데이터 수집

data = {
        '학생': ['A', 'B', 'C', 'D', 'E'],
        '수학': [90, np.nan, 85, 88, np.nan],
        '영어': [80, 78, np.nan, 90, 85],
        '과학': [np.nan, 89, 85, 92, 80]
}

df = pd.DataFrame(data)
df

#2 결측값 처리

# df['수학'].fillna(df['수학'].mean(), inplace=True)
# df['영어'].fillna(df['영어'].mean(), inplace=True)
# df['과학'].fillna(df['과학'].mean(), inplace=True)

df['수학'] = df['수학'].fillna(df['수학'].mean()) # 덮어 씌우는 방식이 더 직관적이다
df['영어'] = df['영어'].fillna(df['영어'].mean())
df['과학'] = df['과학'].fillna(df['과학'].mean())

df

df.dtypes

#3 이상치 제거

score = df[(df.iloc[:,1:].values >= 0) & (df.iloc[:,1:].values <= 100)] # 점수가 0이상만 취급
# score = df[(df.values[:,1:] >= 0) & (df.values[:,1:] <= 100)] # 이것도 가능
score

#3 이상치 제거

# score = df[(df.iloc[:,1:] >= 0) & (df.iloc[:,1:] <= 100)] # 점수가 0이상만 취급
# score

#4 데이터 정규화
# 0~1 사이 값으로 스케일링
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler() # 각데이터의 최대,최소값을 기반으로 0~1 사이값으로 변환함

df[['수학','영어','과학']] = scaler.fit_transform(df[['수학','영어','과학']])
df

#5 데이터 분할

from sklearn.model_selection import train_test_split


train , test = train_test_split(df, test_size = 0.2, random_state = 42) # `random_state`를 설정해줘야 동일한 결과를 계속 얻을 수 있다.
print(train)
print(test)

"""<aside>
👉 가상의 데이터셋을 사용하여 전처리 과정을 직접 구현해 보세요.

각 단계에 맞춰 코드를 작성하고, 최종적으로 학습용과 검증용 데이터로 나누는 작업을 합니다.

### 데이터셋

- 가상의 제품 판매 데이터
    
    ```python
    # 가상의 데이터셋 생성
    data = {
        '제품': ['A', 'B', 'C', 'D', 'E'],
        '가격': [100, 150, 200, 0, 250],
        '판매량': [30, 45, np.nan, 55, 60]
    }
    ```
    

### 문제

1. 결측값을 중앙값으로 대체합니다.
2. 이상치를 제거합니다. (예: 가격이 0 이하인 경우)
3. 데이터를 표준화합니다. (평균 0, 표준편차 1)
4. 데이터를 학습용과 검증용으로 나눕니다. (학습용 70%, 검증용 30%)

### 문제 설명

1. 데이터 수집
    - 가상의 제품 판매 데이터를 생성합니다.
2. 결측값 처리
    - 데이터셋에 누락된 값이 있을 때, 이를 중앙값으로 대체합니다.
3. 이상치 제거
    - 가격이 0 이하인 데이터를 제거합니다.
4. 데이터 표준화
    - 가격과 판매량 데이터를 평균 0, 표준편차 1로 변환합니다.
5. 데이터 분할
    - 데이터셋을 학습용과 검증용으로 나눕니다
</aside>
"""

#1 데이터수집

data = {
      '제품': ['A', 'B', 'C', 'D', 'E'],
      '가격': [100, 150, 200, 0, 250],
      '판매량': [30, 45, np.nan, 55, 60]
  }

df = pd.DataFrame(data)
df

#2 결측값 처리

df['판매량'] = df['판매량'].fillna(df['판매량'].median())
df

#3 이상치 제거

df = df[df['가격'].dropna() > 0]
# df[df.dropna()] -> 모든 결측치 제거인건 알았는데
# df[df.dropna() > 0] -> 0 초과인값 제외 삭제 한다는 뜻임!!
df

#4 데이터 표준화

from sklearn.preprocessing import StandardScaler

df[['가격','판매량']] = StandardScaler().fit_transform(df[['가격','판매량']])
df

#5 데이터 분할

from sklearn.model_selection import train_test_split

train,test = train_test_split(df, test_size= 0.2, random_state = 42)

print("\n 트레이닝 데이터")
print(train) # 트레이닝 데이터
print("\n 테스트 데이터")
print(test) # 테스트 데이터

"""#데이터증강

<aside>
👉 Python과 Pillow를 사용하여 이미지 회전, 뒤집기, 이동, 확대/축소, 색상 변형, 노이즈 추가를 해보세요.

### 이미지 예시 (출처: [위키피디아](https://ko.wikipedia.org/wiki/%EB%A0%88%EB%82%98_%28%EC%9D%B4%EB%AF%B8%EC%A7%80%29))

[Lenna.jpg](attachment:476de136-2de8-464b-91c2-dfa9c6865e61:Lenna.jpg)

### 문제 설명

1. 필요한 라이브러리 설치 및 불러오기
2. 이미지 불러오기
3. 이미지 증강 기법 적용
</aside>
"""

#1 필요한 라이브러리 설치 및 불러오기

from PIL import Image # 이미지를 생성하고 조작하기 위한 라이브러리
import numpy as np # 배열 및 행렬 연산을 위한 라이브러리
import matplotlib.pyplot as plt # 시각화를 위한 라이브러리

#2 이미지 불러오기

image = Image.open("/content/drive/MyDrive/Colab Notebooks/[카카오 부트캠프]/Lenna.png")

def show_image(image, title = "image"):
        import matplotlib.pyplot as plt
        plt.imshow(image)
        plt.title(title)
        plt.axis('off')
        plt.show()

show_image(image)

#3 이미지 증강 기법 적용

# 이미지 회전

def rotate_image(image, angle):
    return image.rotate(angle)

rotated_image = rotate_image(image, 45)
show_image(rotated_image, "Rotated Image")

# 3 이미지 증강 기법 적용

#이미지 뒤집기

from PIL import ImageOps

def flip_image(image,direction):
    if direction == 'horizontal':
        return ImageOps.mirror(image)
    elif direction == 'vertical':
        return ImageOps.flip(image)

flipped_image = flip_image(image, 'horizontal')
show_image(flipped_image, "Flipped Image")

#3 이미지 증강 기법 적용

#이미지 이동

def translate_image(image,x,y):
    array = np.array(image) # np.array() 입력 데이터를 Numpy 배열로 변환
    translated_array = np.roll(array, shift = (y,x), axis=(0,1))
    return Image.fromarray(translated_array)

translated_image = translate_image(image, 30, 50)
show_image(translated_image, "Translated Image")

#3 이미지 증강 기법

#이미지 크기 조정

def resize_image(image, scale):
    width , height = image.size
    return image.resize((int(width*scale), int(height*scale)))

resized_image = resize_image(image, 1.5) # 1.5배 확대
resized_image

#3 이미지 증강 기법

#이미지 밝기 조절

from PIL import ImageEnhance

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

brightened_image = adjust_brightness(image, 1.5) #1.5배 밝기
brightened_image

#3 이미지 증강 기법

#이미지에 노이즈 추가

def add_noise(image):
    array = np.array(image)
    noise = np.random.normal(loc = 0, scale = 10, size = array.shape)
    # 노이즈의 평균값 = 0, 노이즈의 평균편차 = 10
    noisy_image = np.clip(array + noise , 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_image)
    # 노이즈가 추가된 배열을 다시 이미지 객체로 변환하여 반환

noisy_image = add_noise(image)
#노이즈가 추가된 이미지를 화면에 표시한다.
show_image(noisy_image, "Noisy Image")

"""# 데이터셋 분할

<aside>
👉 데이터셋을 랜덤으로 분할하고 각 데이터셋의 크기를 출력하여 분할이 제대로 이루어졌는지 확인해 보세요.

### 문제 설명

1. 데이터 로드
    - 샘플 데이터셋을 로드합니다.
    - 예제데이터
    
    ```python
    # 샘플 데이터 생성
    data = {
        'feature1': range(1, 101),
        'feature2': range(101, 201),
        'label': [1 if x % 2 == 0 else 0 for x in range(1, 101)]
    }
    df = pd.DataFrame(data)
    ```
    
2. 데이터셋 분할
    - 데이터를 학습, 검증, 테스트 데이터셋으로 나눕니다.
3. 결과 확인
    - 각 데이터셋의 크기를 출력하여 분할 결과를 확인합니다.
</aside>
"""

#1

#데이터 로드

data = {
    'feature1': range(1, 101),
    'feature2': range(101, 201),
    'label': [1 if x % 2 == 0 else 0 for x in range(1, 101)]
}

df = pd.DataFrame(data)
df

#2

#데이터 셋 분할(트레이닝)

train_size = int(0.6 * len(df)) # 60%학습데이터 비율

train_data = df[:train_size] # 트레이닝 데이터

print("트레이닝 데이터 크기:", len(train_data))

#2

#데이터 셋 분할(검정)

validate_size = int(0.2 * len(df)) # 20%학습데이터 비율

validate_data = df[train_size: train_size + validate_size] # 검증 데이터

print("검증 데이터 크기:", len(validate_data))

#2

#데이터 셋 분할(학습)

test_size = int(0.2 * len(df)) # 40%학습데이터 비율

test_data = df[train_size + validate_size:] # 테스트 데이터

print("테스트 데이터 크기:", len(test_data))

#3

#결과 확인

from sklearn.model_selection import train_test_split

train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

print("트레이닝 데이터:",train_data)
print("테스트 데이터:",test_data)

"""#머신러닝

<aside>
👉 **간단한 분류 문제를 해결해보세요.**

### 문제 설명

1. **데이터 수집**
    - 간단한 꽃 데이터셋을 사용합니다.
    각 꽃의 특성(예: 길이와 너비)과 클래스(예: 꽃의 종류)를 포함합니다.
    - 예시 데이터
        
        ```python
        X = np.array([[1.4, 0.2], [1.3, 0.2], [1.5, 0.2], [4.5, 1.5], [4.1, 1.0], [5.1, 1.8]])
        y = np.array([0, 0, 0, 1, 1, 1])
        ```
        
2. **모델 선택 및 학습**
    - k-최근접 이웃(K-Nearest Neighbors, KNN) 알고리즘을 사용합니다.
    - 꽃 데이터의 특성을 바탕으로 새로운 꽃의 종류를 예측하는 모델을 학습시킵니다.
    
    <aside>
    ❓ k-최근접 이웃(K-Nearest Neighbors, KNN) 알고리즘이란?
    
        - K-최근접 이웃(KNN)은 새로운 데이터를 기존 데이터와 비교하여 가장 가까운 K개의 데이터로부터 그룹이나 값을 예측하는 방법
    </aside>
    
3. **평가 및 검증**
    - 학습된 모델을 사용하여 새로운 꽃 데이터의 클래스를 예측합니다.
    - 예측값을 실제값과 비교하여 모델의 정확도를 평가합니다.
4. **예측 및 최적화**
    - 모델이 예측한 값을 출력합니다.
</aside>
"""

#1
#데이터수집

x = np.array([[1.4, 0.2], [1.3, 0.2], [1.5, 0.2], [4.5, 1.5], [4.1, 1.0], [5.1, 1.8]])
y = np.array([0, 0, 0, 1, 1, 1])

#2
#데이터 분할

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#3
#모델선택 및 학습

knn = KNeighborsClassifier(n_neighbors=1) # k= 3->1로 조정 : knn의 하이퍼 파라미터가 된다!
#데이터가 크면 k의 수를 늘리면 된다. 근데 여기서 k값을 홀수로 한 이유가 따로 있다.
#'동점회피' :  1:2 or 2:1로 나오므로 한쪽 클래스로 결정하여 예측의 일관성을 높인다.
knn.fit(x_train, y_train) # 모델학습

#4
#예측 및 최적화

y_pred = knn.predict(x_test) # 예측
print("예측값:", y_pred)

accuracy = accuracy_score(y_test, y_pred) #정확도계산
print("정확도:", accuracy) # 0~1 사이 범위이며 1에 가까울수록 모델성능이 좋음

# 5
# 새로운 데이터 예측

new_flower = np.array([[1.5, 0.2], [4.0, 1.5]])  # 새로운 꽃 데이터
predictions = knn.predict(new_flower)  # 예측
print("새로운 꽃의 예측 클래스:", predictions)

"""- knn : x,y 테스트 데이터셋 비율을정하고 (데이터 분할) -> x_test데이터로 y의 예측값을 도출해본다음 -> 해당 y 예측값이 실제 y_test값과 비교하여 모델 정확도를 비교한다.
- `Expected n_neighbors <= n_samples_fit, but n_neighbors = 5, n_samples_fit = 4, n_samples = 2` -> 데이터 샘플 수보다 k값이 커서 오류가 생긴다.(k값을 낮추자 홀수값으로)

# 딥러닝_미니퀘스트

<aside>
👉 실습 프로젝트 코드에서 신경망의 은닉층 수와 각 층의 뉴런 수를 변경해 보고, 모델의 성능이 어떻게 달라지는지 비교해보세요.


XOR 데이터를 활용합니다.

```python
# XOR 데이터 정의
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])
```

1. **기본 모델 구조**
    - 은닉층 1개, 뉴런 수 2개 (사용 예제 코드의 기본 구조)
2. **변경 모델 구조**
    - 은닉층 2개, 첫 번째 층 뉴런 수 4개, 두 번째 층 뉴런 수 2개
        
        ![스크린샷 2025-02-12 10.52.18.png](attachment:0933d57b-977d-4563-a6e8-d3188005fd34:스크린샷_2025-02-12_10.52.18.png)
        
        ```python
        입력층:                   은닉층1:                 은닉층2:           출력층:
           (x1) ----o--> [ 뉴런1 (ReLU) ] ----o--> [ 뉴런5 (ReLU) ] ----o---+
                                      ^                  ^                  |
                                      |                  |                  v
                                      o                  o              [ 뉴런7 (Sigmoid) ] ---> (y)
                                      |                  |                  ^
           (x2) ----o--> [ 뉴런2 (ReLU) ] ----o--> [ 뉴런6 (ReLU) ] ----o---+ |
                                      ^                  |                  
                                      |                  |                  
                                      o                  o                  
                                      |                  |                  
                          [ 뉴런3 (ReLU) ] ---------------+                  
                                      |                                    
                                      |                                    
                          [ 뉴런4 (ReLU) ]                                    
        
        ```
        
    - 은닉층 1개, 뉴런 수 4개
        
        ![스크린샷 2025-02-12 10.53.05.png](attachment:f200f1ee-3668-42e6-b775-a22ed7c5e8d9:스크린샷_2025-02-12_10.53.05.png)
        
        ```python
        입력층:                   은닉층:               출력층:
        
          (x1) ----o--> [ 뉴런1 (ReLU) ] ----o---+
                                                 |
          (x2) ----o--> [ 뉴런2 (ReLU) ] ----o---+
                                                 |
          (x3) ----o--> [ 뉴런3 (ReLU) ] ----o---+
                                                 |
          (x4) ----o--> [ 뉴런4 (ReLU) ] ----o---+
                                                 |
                                                 v
                                             [ 뉴런5 (Sigmoid) ] ---> (y)
        
        ```
        
3. 예제 코드를 기반으로 신경망 모델을 두 가지 다른 구조로 변경해 봅니다.
4. 각각의 모델을 학습시키고 평가하여, 성능 차이를 비교합니다.
</aside>

### 뉴런수 2개, 은닉층 1개
"""

#라이브러리 임포트 밑 데이터 정의
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# XOR 데이터 정의
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

#Tensor로 변환
x = torch.tensor(x, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32)

print("X:", x)
print("Y:", y)

class XORModel(nn.Module):
    def __init__(self):
        super(XORModel, self).__init__()
        self.layer1 = nn.Linear(2, 2) #은닉층임 (입력+출력 통틀어서ㅇㅇ)
        self.layer2 = nn.Linear(2, 1) #출력층
        self.relu = nn.ReLU() #ReLu 활성화
        self.sigmoid = nn.Sigmoid()

    def forward(self, k):
        k = self.relu(self.layer1(k))
        k = self.sigmoid(self.layer2(k)) #두번째 레이어에 시그모이드 함수
        # ReLU 함수는 은닉층에서 선형관계의 입력값을 비선형결합으로 재결합해서 모델링을 함
        # Sigmoid 함수는 보통 출력층에 적용하며, 입력 데이터의 확률값이 출력됨
        return k
    # ReLU 함수는 은닉층에서 선형관계의 입력값을 비선형결합으로 재결합해서 모델링을 함
        # Sigmoid 함수는 보통 출력층에 적용하며, 입력 데이터의 확률값이 출력됨
model = XORModel() #인스턴스 생성

#모델 컴파일
criterion = nn.BCELoss()  # Binary_Cross_Entropy_Loss : 예측값과 실제값 간의 차이를 측정
optimizer = optim.Adam(model.parameters(), lr=0.01) #Adaptive Moment Estimation,
#학습률을 0.01로 설정 (한번 할때 가중치를 얼만큼 조정할건지 수치화)

#모델 학습
num_epochs = 1000  # 총 에포크 수

for epoch in range(num_epochs):
    model.train()  # 모델을 훈련 모드로 설정
    optimizer.zero_grad()  # 옵티마이저의 변화도(gradient)를 초기화
    outputs = model(x)  # 모델에 입력 데이터를 넣어 출력 계산
    loss = criterion(outputs, y)  # 출력과 실제 레이블을 비교하여 손실 계산
    loss.backward()  # 역전파를 통해 손실에 대한 그래디언트 계산
    optimizer.step()  # 옵티마이저가 매개변수를 업데이트

    if (epoch + 1) % 100 == 0:  # 100 에포크마다 손실 출력
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

#모델 평가
model.eval()  # 모델을 평가 모드로 전환
with torch.no_grad():  # 평가 중에는 그래디언트를 계산하지 않음
    outputs = model(x)  # 모델에 입력 데이터를 전달하여 출력값 계산
    predicted = (outputs > 0.5).float()  # 출력값이 0.5보다 크면 1, 아니면 0으로 변환 (이진 분류)
    accuracy = (predicted == y).float().mean()  # 예측값과 실제값을 비교하여 정확도 계산
    loss = criterion(outputs, y)  # 손실 함수(크로스 엔트로피 손실)를 사용하여 손실 계산
    print(f'Loss: {loss.item()}, Accuracy: {accuracy.item()}')  # 손실과 정확도 출력
    print(f'Predicted: {predicted.squeeze().numpy()}')

"""### 은닉층 2개, 첫 번째 층 뉴런 수 4개, 두 번째 층 뉴런 수 2개"""

# 은닉층 2개, 첫 번째 층 뉴런 수 4개, 두 번째 층 뉴런 수 2개
#라이브러리 임포트 밑 데이터 정의
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# XOR 데이터 정의
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

#Tensor로 변환
x = torch.tensor(x, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32)

print("X:", x)
print("Y:", y)

class XORModel(nn.Module):
    def __init__(self):
        super(XORModel, self).__init__()
        self.layer1 = nn.Linear(2, 4) #은닉층1
        # x데이터가 2차원 이므로 `nn.Linear(2, 4)`로 설정
        self.layer2 = nn.Linear(4, 2) #은닉층2
        self.layer3 = nn.Linear(2, 1) #출력층
        # 출력층의 뉴런 수가 2개인 경우, 이진 분류 문제에서는 일반적으로 1개의 뉴런을 갖는 것이 일반적
        self.relu = nn.ReLU() #ReLu 활성화
        self.sigmoid = nn.Sigmoid()

    def forward(self, k):
        k = self.relu(self.layer1(k))
        k = self.relu(self.layer2(k))
        k = self.sigmoid(self.layer3(k)) #세번째 레이어에 시그모이드 함수
        # ReLU 함수는 은닉층에서 선형관계의 입력값을 비선형결합으로 재결합해서 모델링을 함
        # Sigmoid 함수는 보통 출력층에 적용하며, 입력 데이터의 확률값이 출력됨
        return k
    # ReLU 함수는 은닉층에서 선형관계의 입력값을 비선형결합으로 재결합해서 모델링을 함
        # Sigmoid 함수는 보통 출력층에 적용하며, 입력 데이터의 확률값이 출력됨
model = XORModel() #인스턴스 생성

#모델 컴파일
criterion = nn.BCELoss()  # Binary_Cross_Entropy_Loss : 예측값과 실제값 간의 차이를 측정
optimizer = optim.Adam(model.parameters(), lr=0.01) #Adaptive Moment Estimation,
#학습률을 0.01로 설정 (한번 할때 가중치를 얼만큼 조정할건지 수치화)

#모델 학습
num_epochs = 1000  # 총 에포크 수

for epoch in range(num_epochs):
    model.train()  # 모델을 훈련 모드로 설정
    optimizer.zero_grad()  # 옵티마이저의 변화도(gradient)를 초기화
    outputs = model(x)  # 모델에 입력 데이터를 넣어 출력 계산
    loss = criterion(outputs, y)  # 출력과 실제 레이블을 비교하여 손실 계산
    loss.backward()  # 역전파를 통해 손실에 대한 그래디언트 계산
    optimizer.step()  # 옵티마이저가 매개변수를 업데이트

    if (epoch + 1) % 100 == 0:  # 100 에포크마다 손실 출력
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

#모델 평가
model.eval()  # 모델을 평가 모드로 전환
with torch.no_grad():  # 평가 중에는 그래디언트를 계산하지 않음
    outputs = model(x)  # 모델에 입력 데이터를 전달하여 출력값 계산
    predicted = (outputs > 0.5).float()  # 출력값이 0.5보다 크면 1, 아니면 0으로 변환 (이진 분류)
    accuracy = (predicted == y).float().mean()  # 예측값과 실제값을 비교하여 정확도 계산
    loss = criterion(outputs, y)  # 손실 함수(크로스 엔트로피 손실)를 사용하여 손실 계산
    print(f'Loss: {loss.item()}, Accuracy: {accuracy.item()}')  # 손실과 정확도 출력
    print(f'Predicted: {predicted.squeeze().numpy()}')

"""### 은닉층 1개, 뉴런 수 4개"""

#은닉층 1개, 뉴런수 4개
#라이브러리 임포트 밑 데이터 정의
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# XOR 데이터 정의
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

#Tensor로 변환
x = torch.tensor(x, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32)

print("X:", x)
print("Y:", y)

class XORModel(nn.Module):
    def __init__(self):
        super(XORModel, self).__init__()
        self.layer1 = nn.Linear(2, 4) #은닉층1
        # x데이터가 2차원 이므로 `nn.Linear(2, 4)`로 설정
        self.layer2 = nn.Linear(4, 1) #출력층
        # 출력층의 뉴런 수가 2개인 경우, 이진 분류 문제에서는 일반적으로 1개의 뉴런을 갖는 것이 일반적
        self.relu = nn.ReLU() #ReLu 활성화
        self.sigmoid = nn.Sigmoid()

    def forward(self, k):
        k = self.relu(self.layer1(k))
        k = self.sigmoid(self.layer2(k)) #두번째 레이어에 시그모이드 함수
        # ReLU 함수는 은닉층에서 선형관계의 입력값을 비선형결합으로 재결합해서 모델링을 함
        # Sigmoid 함수는 보통 출력층에 적용하며, 입력 데이터의 확률값이 출력됨
        return k
    # ReLU 함수는 은닉층에서 선형관계의 입력값을 비선형결합으로 재결합해서 모델링을 함
        # Sigmoid 함수는 보통 출력층에 적용하며, 입력 데이터의 확률값이 출력됨
model = XORModel() #인스턴스 생성

#모델 컴파일
criterion = nn.BCELoss()  # Binary_Cross_Entropy_Loss : 예측값과 실제값 간의 차이를 측정
optimizer = optim.Adam(model.parameters(), lr=0.01) #Adaptive Moment Estimation,
#학습률을 0.01로 설정 (한번 할때 가중치를 얼만큼 조정할건지 수치화)

#모델 학습
num_epochs = 1000  # 총 에포크 수

for epoch in range(num_epochs):
    model.train()  # 모델을 훈련 모드로 설정
    optimizer.zero_grad()  # 옵티마이저의 변화도(gradient)를 초기화
    outputs = model(x)  # 모델에 입력 데이터를 넣어 출력 계산
    loss = criterion(outputs, y)  # 출력과 실제 레이블을 비교하여 손실 계산
    loss.backward()  # 역전파를 통해 손실에 대한 그래디언트 계산
    optimizer.step()  # 옵티마이저가 매개변수를 업데이트

    if (epoch + 1) % 100 == 0:  # 100 에포크마다 손실 출력
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

#모델 평가
model.eval()  # 모델을 평가 모드로 전환
with torch.no_grad():  # 평가 중에는 그래디언트를 계산하지 않음
    outputs = model(x)  # 모델에 입력 데이터를 전달하여 출력값 계산
    predicted = (outputs > 0.5).float()  # 출력값이 0.5보다 크면 1, 아니면 0으로 변환 (이진 분류)
    accuracy = (predicted == y).float().mean()  # 예측값과 실제값을 비교하여 정확도 계산
    loss = criterion(outputs, y)  # 손실 함수(크로스 엔트로피 손실)를 사용하여 손실 계산
    print(f'Loss: {loss.item()}, Accuracy: {accuracy.item()}')  # 손실과 정확도 출력
    print(f'Predicted: {predicted.squeeze().numpy()}')

"""- 은닉층이 많아야 복잡한 모델링일수록 성능이 좋아진다.
- 하지만 은닉층이 과다하면 학습이 어려워질수 있다.(기울기 손실 문제)
    > 역전파 과정에서 기울기(gradient)가 점점 작아지는 현상
    - 시그모이드(sigmoid) & Tanh 함수와 같은 '비선형 활성화 함수'에서 기울기 소실 문제가 발생함(입력값이 극단적일때)

- 뉴런 수가 적으면 모델의 표현력이 감소한다.
- 그러나 너무 많은 뉴런의 수는 과적합(overfitting)의 위험이 발생할수 있다.
> 드롭 아웃이나, 배치 정규화를 통해 과적합을 방지하고 모델의 일반화 능력을 향상 시킬수 있다.
-  드롭아웃 : '무작위'로 '뉴런'을 없애는것 -> 해당 뉴런의 출력값을 0으로 지정
        - 일반적으로 각 훈련단계에서 0.2~0.5 확률로 드랍
- 배치 정규화 : 각 미니베치에 대해 '입력 데이터'의 평균과 분산을 계산하여 정규화 함.(평균0, 분산1인 정규분포)
    - 내부 공변량 변화(Internal Covariate Shift)를 줄여준다
    - 내부 공변량 변화란?
    > 학습중 가중치가 업데이트 되면, 각 층의 입력 데이터(=직전 층의 출력값) 분포가 변하게 된다. 이렇게 되면 각 모델층이 학습해야하는 분포가 계속 변화하여 훈련속도와 최적화가 어려워질수 있다.
    - 신경망 학습 과정중 '역전파과정'에서 발생. -> 계속 가중치를 업데이트 하므로
"""

