import math
import tax

PENSION_INSURANCE_RATE =  0.045
HEALTH_INSURANCE_RATE = 0.03545
LONGTERM_CARE_INSURANCE_RATE = 0.1281
EMPLOYMENT_INSURANCE_RATE = 0.009

def floor(x,base):
    return math.floor(x / base) * base

def floor10(x):
    return floor(x,10)

def floor1000(x):
    return floor(x,1000)

def get_income_tax_from_table(pay,family_num):
    family_num = f'{family_num}person'
    income_tax = int(tax.tax_table[(tax.tax_table["geq"] <= pay) & (tax.tax_table["less"] > pay)][family_num].item())
    return income_tax

def get_income_tax_10m_from_table(family_num):
    income_tax = get_income_tax_from_table(10000000,family_num)
    return income_tax

def compute_income_tax(pay,family_num):
    if pay < 1060000:
        return 0
    if pay <= 10000000:
        return get_income_tax_from_table(pay,family_num)
    if pay <= 14000000:
        # TODO
        # 10000000초과 14000000이하일 떄
        # (10,000,000원인 경우의 해당 세액) + (10,000,000원을 초과하는 금액 중 98%를 곱한 금액의 35% 상당액) + (25,000원)
        # (10,000,000원인 경우의 해당 세액)의 경우 get_income_tax_10m_from_table(가족수)를 이용해서 구할 수 있습니다.
        return
    if pay <= 28000000:
        # TODO
        # 14000000초과 28000000이하일 떄
        # (1천만원인 경우의 해당세액) + (1,397,000원) + (14,000천원을 초과하는 금액 중 98퍼센트를 곱한 금액의 38퍼센트 상당액)
        # (10,000,000원인 경우의 해당 세액)의 경우 get_income_tax_10m_from_table(가족수)를 이용해서 구할 수 있습니다.
        return
    if pay <= 30000000:
        # TODO
        # 28000000초과 30000000이하일 떄
        # (10,000천원인 경우의 해당세액) + (6,610,600원) + (28,000천원을 초과하는 금액에 98퍼센트를 곱한 금액의 40퍼센트 상당액)
        # (10,000,000원인 경우의 해당 세액)의 경우 get_income_tax_10m_from_table(가족수)를 이용해서 구할 수 있습니다.
        return
    if pay <= 45000000:
        # TODO
        # 30000000초과 45000000이하일 떄
        # (10,000천원인 경우의 해당세액) + (7,394,600원) + (30,000천원을 초과하는 금액의 40퍼센트 상당액)
        # (10,000,000원인 경우의 해당 세액)의 경우 get_income_tax_10m_from_table(가족수)를 이용해서 구할 수 있습니다.
        return
    if pay <= 87000000:
        # TODO
        # 45000000초과 87000000이하일 떄
        # (10,000천원인 경우의 해당세액) + (13,394,600원) + (45,000천원을 초과하는 금액의 42퍼센트 상당액)
        # (10,000,000원인 경우의 해당 세액)의 경우 get_income_tax_10m_from_table(가족수)를 이용해서 구할 수 있습니다.
        return

    # TODO
    # 87000000 초과일 떄
    # (10,000천원인 경우의 해당세액) + (31,034,600원) + (87,000천원을 초과하는 금액의 45퍼센트 상당액)
    # (10,000,000원인 경우의 해당 세액)의 경우 get_income_tax_10m_from_table(가족수)를 이용해서 구할 수 있습니다.
    return

# 지방세 계산
# 지방세는 국세의 10%입니다.
def compute_local_income_tax(income_tax):
    # TODO
    return

# 총 근로소득세 계산
# 국세 더하기 지방세
def compute_total_income_tax(income_tax,local_income_tax):
    # TODO
    return

# 연금보험 계산
# 급여의 4.5%(근로자 4.5% / 사업장 4.5% => 총 9%)
def compute_pension_insurance(pay):
    # TODO
    return

# 건강보험 계산
# 급여의 3.545%(근로자 3.545% / 사업장 3.545% => 총 7.09%)
def compute_health_insurance(pay):
    # TODO
    return

# 장기요양보험 계산
# 건강보험료의 12.81%(근로자 3.545%의 12.81% / 사업장 3.545%의 12.81% => 총 7.09%의 12.81%)
def compute_longterm_care_insurance(health_insurance):
    # TODO
    return

# 총 건강보험료 계산
# 건강보험 더하기 장기요양보험
def compute_total_health_insurance(health_insurance,longterm_care_insurance):
    # TODO
    return

# 고용보험 계산
# 급여의 0.9%(근로자는 0.9% / 사업장은 0.9+@%)
def compute_employment_insurance(pay):
    # TODO
    return

# 총 보험료 계산
# 연금보험 더하기 총 건강보험 더하기 고용보험
def compute_total_insurance(pension,total_health,employment):
    # TODO
    return

# 총 원천징수 계산
# 총 근로소득세 더하기 총 보험료
def compute_total_withholding(total_income_tax,total_insurance):
    # TODO
    return