
LOW_CREDIT_SCORE = 0
LTV_EQ_OR_EXCEEDS_80 = 1
LTV_EXCEEDS_95 = 2
DTI_EXCEEDS_36 = 10
DTI_EXCEEDS_43 = 11
HIGH_FEDTI = 20


def validBuy(gross_monthly_income, credit_card_payment, car_payment, student_loan_payment, 
                 appraised_value,down_payment,loan_amount,mortgage_payment,credit_score):
    violation = []
    if (credit_score < 640):
        violation.append(LOW_CREDIT_SCORE)
    if (100 * loan_amount >= 80 * appraised_value):
        violation.append(LTV_EQ_OR_EXCEEDS_80)
    if(100 * loan_amount > 95 * appraised_value):
        violation.append(LTV_EXCEEDS_95)
    monthly_debt = credit_card_payment + car_payment + student_loan_payment + mortgage_payment
    if(100 * monthly_debt > 36 * gross_monthly_income):
        violation.append(DTI_EXCEEDS_36)
    if(100 * monthly_debt > 43 * gross_monthly_income):
        violation.append(DTI_EXCEEDS_43)
    if(100 * mortgage_payment > 28 * gross_monthly_income):
        violation.append(HIGH_FEDTI)
        
    return violation