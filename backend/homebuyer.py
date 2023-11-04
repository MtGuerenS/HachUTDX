
LOW_CREDIT_SCORE = 0
LTV_EQ_OR_EXCEEDS_80 = 1
LTV_EXCEEDS_95 = 2
DTI_EXCEEDS_36 = 10
DTI_EXCEEDS_43 = 11
HIGH_FEDTI = 20
LIQUID_ASSETS_EXCEEDED = 30

# checks if params cause valid purchase
def validBuy(gross_monthly_income, credit_card_payment, car_payment, student_loan_payment,
             other_payments, appraised_value,down_payment,loan_amount,mortgage_payment,
             credit_score,age,liquid_assets,education):
    violation = []
    if (credit_score < 640):
        violation.append(LOW_CREDIT_SCORE)
    if(100 * loan_amount > 95 * appraised_value):
        violation.append(LTV_EXCEEDS_95)
    elif (100 * loan_amount >= 80 * appraised_value):
        violation.append(LTV_EQ_OR_EXCEEDS_80)
    
    monthly_debt = credit_card_payment + car_payment + student_loan_payment + mortgage_payment + other_payments
    if(100 * monthly_debt > 43 * gross_monthly_income):
        violation.append(DTI_EXCEEDS_43)
    elif(100 * monthly_debt > 36 * gross_monthly_income):
        violation.append(DTI_EXCEEDS_36)
    
    if(100 * mortgage_payment > 28 * gross_monthly_income):
        violation.append(HIGH_FEDTI)
    if(down_payment > liquid_assets):
        violation.append(LIQUID_ASSETS_EXCEEDED)
        
    return violation

# DEPRECATED
# algorithmic solutions to violations of validBuy
def findSolutions(gross_monthly_income, credit_card_payment, car_payment, student_loan_payment, 
                  other_payments, appraised_value,down_payment,loan_amount,mortgage_payment,
                  credit_score, age,liquid_assets,education):
    violation = validBuy(gross_monthly_income, credit_card_payment, car_payment, student_loan_payment, 
                  other_payments, appraised_value,down_payment,loan_amount,mortgage_payment,
                  credit_score)
    for i in violation:
        if(i == LOW_CREDIT_SCORE):
            # is there even a fix for this?
            continue
        elif(i == LTV_EXCEEDS_95):
            # find min takeable loan
            new_loan_amount = appraised_value - liquid_assets
        elif(i == LTV_EQ_OR_EXCEEDS_80):
            # try loan decres
            continue
        elif(i == DTI_EXCEEDS_43):
            continue
        elif(i == DTI_EXCEEDS_36):
            continue
        elif(i == HIGH_FEDTI):
            continue
        else:
            print("invalid violation code")
    return