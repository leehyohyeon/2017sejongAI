


# 감성 분석기 코드 분석 보고서

## 가설1 도출 배경 

Review: 

The Intern ....
The sweetest, most perfect And heart touching I have seen in a long time. Of
course it helps that Robert De Niro is there but what a movie! This is what all
movies should be.The story is perfect, with the perfect practical ending, as
life is always more practical than idealistic.

Predicted
sentiment: Positive

Probability:
0.99

#### ->최상급은 성질이나 상태의 정도가 가장 큰 것을 나타내기 때문에 최상급을 쓰면 수치가 높아질 것이라고 예상했다
 
## 가설1. 최상급 표현을 쓰면 긍정 수치가 높아질 것이다.

### 증명1. 최상급 표현 포함 vs 미포함 비교

-Review: The
Intern .... sweet, perfect and heart
touching I have seen in a long time. 

Predicted
sentiment: Positive

Probability:
0.93

 

-Review: The
Intern .... The sweetest, most perfect and heart touching
I have seen in a long time. Predicted sentiment: Positive

Probability:
0.94

Review: The
Intern .... The sweetest, most perfect and heart
touching I have seen in a long time. Of course it helps that Robert De
Niro is there but what a movie! 

Predicted
sentiment: Positive

Probability:
0.96

#### 검증결과=> 최상급 표현이 포함된 문장이 미포함 문장보다 긍정 수치가 높았다.

### 증명2. 최상급 표현 포함 vs 미포함 비교2

-Review: The
story is perfect, with the perfect
practical ending, as life is always more practical than idealistic. 

Predicted
sentiment: Positive

Probability: 0.9

-Review: The
story is the most perfect, with the perfect
practical ending, as life is always more practical than idealistic. 

Predicted
sentiment: Positive

Probability:
0.91

### 증명3. 최상급 표현 포함 vs 미포함 비교3

Review: Wonderful
contemporary story, great acting. What more can one ask for? DeNiro totally inhabits
the role of a bored NewYorker retiree who quietly, commandingly changes
everyone around him for the better. 

Predicted
sentiment: Positive

Probability: 0.8

Review: The most wonderful contemporary story, the greatest acting.
What more can one ask for? DeNiro totally inhabits the role of a bored
NewYorker retiree who quietly, commandingly changes everyone around him for the
better. 

Predicted
sentiment: Positive

Probability:
0.94

#### 검증결과=> 검증2,3 또한 최상급 표현이 포함된 문장이 미포함 문장보다 긍정 수치가 높았다.

 

### 증명4. 최상급문장을 미포함시켰을 경우

Review: Of
course it helps that Robert De Niro is there but what a movie! 

Predicted
sentiment: Positive

Probability:
0.63

#### 검증결과=> 미포함 문장일 때 긍정 수치가 0.3 감소했다.

 
> 종합 검증결과=> the sweetest, most perfect, the greatest와 같은 최상급 표현이 포함된 문장이 최상급이 포함 안 된 문장보다 긍정(pos) 수치가 높았다.

 

## 가설2 도출 배경 

Review: Wonderful
contemporary story, great acting. What more can one ask for? DeNiro totally
inhabits the role of a bored NewYorker retiree who quietly, commandingly
changes everyone around him for the better. There were little bits of
sentimental predictability but not many.

Predicted
sentiment: Positive

Probability:
0.81

#### ->not이라는 부사가 단어 또는 구를 부정할 때, 부정적인 대답을 할 때 쓰므로 not이 포함된 문장이 부정 수치가 높고 긍정 수치의 경우 낮아질 것으로 예상했다


<br><br><br>

## 가설2. 부정부사 not이 포함되면 긍정 수치가 반드시 낮아질 것이다. 

### 증명1. not이 포함된 문장 제거

-Review: Wonderful
contemporary story, great acting. What more can one ask for? DeNiro totally
inhabits the role of a bored NewYorker retiree who quietly, commandingly
changes everyone around him for the better. 

Predicted
sentiment: Positive

Probability: 0.8

### 증명2. 긍정 수치로 기록된 not문장을 포함시켰을 때 

-Review: There
were not sentimental predictability at all.

Predicted
sentiment: Positive

Probability: 0.55

-Review:
Wonderful contemporary story, great acting. What more can one ask for? DeNiro
totally inhabits the role of a bored NewYorker retiree who quietly,
commandingly changes everyone around him for the better. There were not sentimental predictability at all

Predicted
sentiment: Positive

Probability:
0.84

#### 검증결과=> 긍정 수치로 기록된 not 문장을 포함시켰더니 pos 0.81에서 pos 0.84로 긍정 수치가 증가했다

### 증명3. 높은 부정 수치를 기록한 not문장을 포함시켰을 때 

-Review: I just
can't imagine anyone spending so much money to come out with dribble like this.

Predicted
sentiment: Negative

Probability:
0.89

-Review:
Wonderful contemporary story, great acting. What more can one ask for? DeNiro
totally inhabits the role of a bored NewYorker retiree who quietly,
commandingly changes everyone around him for the better.I just can't imagine
anyone spending so much money to come out with dribble like this. 

Predicted
sentiment: Negative

Probability:
0.66

#### 검증결과=> 부정 수치로 기록된 not 문장을 포함시켰더니 pos 0.81에서 neg 0.66로 부정 감성으로 바꼈다


> 종합 검증결과=> 부정부사 not이 포함되면 부정 수치가 반드시 아질 것이다는 가설2는 진실이 아니다.  Not이 포함된 문장해석이 긍정인지 부정인지 여부에 따라 결과값이 바뀐다. 

 


## 가설3 도출 배경 

Review: Sometimes you don't need a film to try and change the world,
make bold political or societal statements or even be shocking. Sometimes
it's good enough to be an audience member who can just sit back, relax and
enjoy the show… and smile.

Predicted
sentiment: Positive

Probability:
1.0

Review: Sometimes you don't need a film to try and change the world,
make bold political or societal statements or even be shocking.

Predicted
sentiment: Positive

Probability:
1.0

#### ->일부 문장을 제외시켜도 동일한 긍정 수치 1.0이 나와 긍정 수치에 특정 문장이 핵심적인 영향을 미칠 것이라 예상했다




## 가설3. 전체 문장의 긍정 수치를 높게 만드는 ‘특정 표현’이 있다.

#### 특정 표현= Sometimes you don't need a film to try and change the world, make bold political or societal statements or even be shocking.

### 증명1. ’특정 표현’제거해 보기

Review:
Sometimes it's good enough to be an audience member who can just sit back,
relax and enjoy the show… and smile.

Predicted
sentiment: Positive

Probability:
0.53

### 증명2. 부정적 의미를 가진 문장과 결합해 보기1

Review: Sometimes you don't need a film to try and change the world,
make bold political or societal statements or even be shocking. It hits
all the necessary notes for this sort of comedy but misses the point of what
a movie is supposed to be, like a paint by the numbers painting misses the
point of art. 

Predicted
sentiment: Positive

Probability:
0.99

###  증명3.부정적 의미를 가진 문장과 결합해 보기2

Review: Sometimes you don't need a film to try and change the world,
make bold political or societal statements or even be shocking. It hits
all the necessary notes for this sort of comedy but misses the point of what
a movie is supposed to be, like a paint by the numbers painting misses the
point of art .Also, there were not sentimental predictability, not perfect
structure,and not suitable for thinking adults 

Predicted
sentiment: Positive

Probability: 1.0

#### 검증결과->특정 문장을 제거했을 때 pos 수치가 확연히 낮아졌고, but missed the point of what a movie is supposed to be ~ 라는 부정적 의미를 한 문장과 결합 했을 때도 “특정 문장”을 포함했을 때 긍정 수치가 0.99, 1.0로 아주 높았다.

### 증명4. 부정 수치가 높은 문장을 포함시켜 보기

Review: What a
piece of junk. How could anyone sit through this? I was ready to throw my TV
out the window watching this. I just can't imagine anyone spending so much
money to come out with dribble like this. 


Predicted
sentiment: Negative

Probability:
0.97

Review: Sometimes you don't need a film to try and change the world,
make bold political or societal statements or even be shocking. But what
a piece of junk. How could anyone sit through this? I was ready to throw my TV
out the window watching this. I just can't imagine anyone spending so much
money to come out with dribble like this. 


Predicted
sentiment: Positive

Probability:
0.85


> 종합검증결과-> neg수치가 1에 가까운 문장을 포함시켰을 때 pos 수치가 0.85로 떨어지긴 했으나 높은 neg 수치를 띄는 문장이 포함됐음에도 불구, 상대적으로 높은 pos 수치가 나왔다. 전체 문장의 긍정 수치가 높게 만드는 ‘특정 표현’이 있다는 가설 3은 어느 정도 신뢰성이 있다.

 

