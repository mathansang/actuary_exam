import numpy as np
import actlib as al
from actlib as mort


a = np.array(1)

# 피보험자 (30)은 30년납 종신보험에 가입하였다.

# 보험료는 기시연납임
# 사망보험금은 1,000원이고, 사망년도 말에 지급됨
# 최초 10년 동안에는 평준순보험료 1,000 P_30 원을 납입하며, 다음 20년 동안에는 증가된 평준순보험료를 납입함

# (1) 40세부터 20년 동안 납입해야 하는 평준순보험료를 구하시오. (단, 소수점 이하 셋째 자리에서 반올림) (5점)
def problem_1_1():
    A30 = mort.Ax(30)
    P30 = mort.Px(30)

    ax1 = mort.ax_n(30, 10)
    ax2 = mort.u_ax_n(3, 30, 20)
    
    Px = ( 1000 * A30 - P30 * ax1 ) / ax2

    return Px


# (2) 계약자는 10년 말 시점에 최초 10년 동안 납입한 평준순보험료와 동일한
# 보험료를 다음 20년 동안에도 계속 납입할 수 있는 선택권을 가지고
# 있다. 이 선택권을 행사할 때 사망보험금은 감액되며, 10년 말 시점의
# 책임준비금과 장래보험료 수입을 기초로 하여 결정된다. 선택권을 행사한
# 후 40세 이후에 감액되어질 사망보험금을 구하시오. (단, 소수점 이하
# 셋째 자리에서 반올림) (5점)    
def problem_1_2():
    pass



# 3. 다음을 계산하시오. (단, 계산 시 아래 표를 참조함)
#  -0.1 -0.2 -0.3 -0.4 -0.5
# 
#  0.905 0.819 0.741 0.670 0.607
#  -0.6 -0.7 -0.8 -0.9 -1.0
# 
#  0.549 0.497 0.449 0.407 0.368
# (1) 다음의 가정을 이용하여 종신보험의 일시납순보험료를 계산하시오.
# (단, 소수점 이하 셋째자리에서 반올림) (5점)
# [보장조건]
# ○ 가입 후 10년 내 사망 시 : 일시납순보험료를 이력 
#   로
# 부리한 금액을 지급
# ○ 가입 후 10년 이후 사망 시 : 보험금 원을 지급
# [산출기준]
# ○ 사력  :   ≤  ≤ 
#   
# ○ 이력() : 
# (2) 탈퇴원인이 사망과 해약인 이중탈퇴모형에서 다음의 가정을
# 이용하여 
# 을 계산하시오. (단, 소수점 이하 여섯째자리에서 반올림) (10점)
# ○ 사망에 의한 탈퇴력 :  
#   
# 
# ○ 해약에 의한 탈퇴율 : 
#   
# ○ 사망과 해약은 절대탈퇴표에서 UDD가정을 따름(UDDSD)
def problem_3():
    pass

# 2017년도 40회
def problem_3():
    A50 = mort.Ax(50)
    A45 = mort.Ax(45)

    A50_45_min = mort.Axy_min(50,45)
    A50_45_max = mort.Axy_max(50,45)

    



if __name__ == "__main__":
    print(a)


