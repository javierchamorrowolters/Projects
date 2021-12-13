import argparse
def loan_request(arg):
    import pandas as pd
    import sys
    global lenders
    
    lenders = pd.read_csv(filepath_or_buffer='../Data/MarketDataforTechnicalExercise.csv')
    lenders.sort_values(by='exp_rate', inplace=True)
    lenders['interest'] = lenders['exp_rate'] * lenders['money_lent']
    
    #answer = input('Loan request ')
    #answer = int(answer)
    
    money_requested = int(arg)
    money_lent_total = 0
    lenders_count = 0
    interest = 0
    
    if int(arg) not in list(range(1000,15001,100)):
        print('\nPlease choose of any 100 increment between 1000 and 15000 inclusive')
    elif int(arg) > lenders['money_lent'].sum():
        print('\nSorry there is not enough money right now, try again later!')
    else:    
        for i, money in enumerate(lenders['money_lent']):
            money_lent_total += money
            lenders_count += 1
            
            if money_lent_total < money_requested:
                interest += lenders.iloc[i, 3]
    
            if money_lent_total == money_requested:
                lenders_count += 1
                interest += lenders.iloc[i, 3]
                lenders.iloc[i,2] = (money_lent_total - money_requested)
                break
                
            if money_lent_total > money_requested:
                interest += (money_lent_total - money - money_requested) * lenders.iloc[i, 1] *-1
                lenders.iloc[i,2] = (money_lent_total - money_requested)
                break
                
        interest_rate = interest / money_requested *100
        repayment_total = money_requested + interest
        repayment_monthly = repayment_total/36
        
        #print('Number of Lenders:',lenders_count)
        print('\nInterest Amount:  '+ str(interest.round(2)) +
              '\nInterest Rate: '+ str(interest_rate.round(1))+'%'+
              '\n36 Monthly Repayment: '+ str(repayment_monthly.round(2)) +
              '\nTotal repayment: '+ str(repayment_total.round(2)))
        
        lenders = lenders.iloc[(lenders_count-1): , :]
        lenders.sort_values(by='exp_rate', inplace=True, ignore_index = True)
        lenders.to_csv('../Data/MarketDataforTechnicalExercise.csv', index = False)
    

def fill_the_bucket_2(name=1):
    import pandas as pd
    import sys

    global lenders

    lenders = pd.read_csv(filepath_or_buffer='../Data/MarketDataforTechnicalExercise.csv')

    n_times = int(name)

    filler = {
        'lender_name': ['Louis', 'Maximillian', 'Peter', 'Rose', 'Margarette', 'Alfred', 'Hunter', 'Logan'],
        'exp_rate': [0.069, 0.072, 0.088, 0.067, 0.074, 0.075, 0.063, 0.079],
        'money_lent': [100, 200, 500, 800, 700, 100, 900, 300],
        'interest': [1, 1, 1, 1, 1, 1, 1, 1]
    }
    filler = pd.DataFrame(filler)
    
    for i in list(range(n_times)):
        lenders = pd.concat([lenders, filler], axis=0)
        
    
    print('\nNow there are ' + str(lenders['money_lent'].sum()) + ' pounds in the bucket\n')

    lenders.sort_values(by='exp_rate', inplace=True, ignore_index = True)
    lenders['interest'] = lenders['exp_rate'] * lenders['money_lent']
    lenders.to_csv('../Data/MarketDataforTechnicalExercise.csv', index = False)
    print(lenders.head(10))

def currentmoney():
    import pandas as pd
    import sys

    global lenders
    lenders = pd.read_csv(filepath_or_buffer='../Data/MarketDataforTechnicalExercise.csv')
    print('\nThere are ' + str(lenders['money_lent'].sum()) + ' pounds in the bucket')
    
def test(x=0):
    import pandas as pd
    import sys
    print('\nI am printing ' + str(x))
    r = 'I am returning ' + str(x)
    return r
def bucketstatus():
    import pandas as pd
    import sys
    global lenders
    
    lenders = pd.read_csv(filepath_or_buffer='../Data/MarketDataforTechnicalExercise.csv')
    lenders.sort_values(by='exp_rate', inplace=True)
    lenders['interest'] = lenders['exp_rate'] * lenders['money_lent']
    print('\n',lenders)
    return lenders

