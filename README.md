# acturay_exam

actuarial library for exam

# 할것 구분

## 보험수리학

### 기초율 사망률, 생존률 계산 ( module ? )

s(x) : 생존함수
mu(x) : 사력
T(x) : 생존분포 확률 변수

사망률 함수?

mort = Mortality('12년')

mort.surv(x)
mort.force(x)
mort.cum_prob(x)

mort.Nx(30) = ?

mort.qx(30) = 30세가 1년이내...?
mort.n_qx(2,30) = 30세가 2년이내...?
mort.u_n_qx(2, 3, 30) = 30세가 2년 거치 3년이내...?

mort.px(30) = 30세가 1년이내...?
mort.n_px(2,30) = 30세가 2년이내...?
mort.u_n_px(2, 3, 30) = 30세가 2년 거치 3년이내...?

------------------------------------------------------------------

죄다 기말

종신
mort.Ax(30) = 30세, 종신
mort.u_Ax(5, 30) = 30세, 5년 거치 종신

생사혼합
mort.Ax_n(30, 10) = 30세, 10년 만기
mort.u_Ax_n(5, 30, 10) = 30세, 5년거치, 10년 만기

정기
mort.A1x_n(30, 10) = 30세, 10년 만기
mort.u_A1x_n(5, 30, 10) = 30세, 5년거치, 10년 만기

생존
mort.Ax_n1(30, 10) = 30세, 10년 만기
mort.n_Ex(30, 10)   = 30세, 10년 만기
mort.u_Ax_n1(5, 30, 10) = 30세, 5년거치, 10년 만기 - 이런게 가능한가...?


죄다 기시
mort.ax(30) = 30세 종신
mort.ax_n(30, 10) = 30세 10년 만기
mort.u_ax_n(3, 30, 10) = 30세, 3년 거치, 10년 만기


보험료
mort.Px = 종신

u_ax_n(30) =  종신 연금 - 기시? 기말? 연속? 월단위?
u_ax_n
ax(30, )
ax(30)
ax(30)

ax_n(30, 1) =  확정 연금 - 기시? 기말? 연속? 월단위?



1. 사력?


마코브 체인
Probability of Absorption

https://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/Chapter11.pdf

2. 

### 보험료 계산


### 준비금 계산



2. 연금수리학

3. 계리모형론

VHM 관련 수식 나와있는 것
https://www.soa.org/globalassets/assets/files/edu/c-24-05.pdf

regression 공식 외워야함
beta 구하는 거 , var(beta) , SST , SSR 등

greedwood 증명
http://www-personal.umich.edu/~yili/lect2notes.pdf

기출문제 3번
http://home.cc.umanitoba.ca/~farhadi/ACT4630Winter2017/Classical%20Credibility.pdf

4. 리스크관리

5. 금융공학
