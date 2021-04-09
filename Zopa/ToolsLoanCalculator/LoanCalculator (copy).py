def test(num):
    print('This is the number: {}'.format(num))
    return num*2      



def LoanCalculatorFun (money_requested=0):
    
    # Import libraries and read the file with investor info.
    import pandas as pd
    import sys
    sys.path.append('..')
    data = pd.read_csv('../Data/MarketDataforTechnicalExercise_2.csv')
    
    # Sort data by expected rate and create a column with expected amount (for each investor to receive in return).
    data = data.sort_values(by=['exp_rate'])
    data['exp_return'] = data['money_lent']*(1+data['exp_rate'])
    
    # Rename DataFrame and reset indexes.
    df = data.reset_index(drop=True)
    
    # Check that the money requested is valid and available.
    pos_req = list(range(1000,15100,100))
    if money_requested not in pos_req:
        return 'Invalid amount - It must be any £100 increment between £1000 and £15000 inclusive'
    elif money_requested > df['money_lent'].sum():
        return 'Invalid amount  - Not enough money in the bucket'
    
    else:
    
    
        remainder = money_requested   # Money to return from a part of "the last" lender.
        to_return = 0                 # Money to return in exact amounts.
        next_count_ind = 0            # Current index in the loop.
        
        # Loop through the investors data.
        for element in list(range(0,(df.shape[0]+1))):
            
            # We start from the total requested amount and subtract each investor block until needed.
            if remainder >= df.loc[next_count_ind,'money_lent']:
                remainder-= df.loc[next_count_ind,'money_lent']
                to_return+= df.loc[next_count_ind,'exp_return']
                next_count_ind +=1
        
        # Calculate the extra part if it didn't fit exactly with the investors money lent.
        extra = remainder * (1+df.loc[next_count_ind,'exp_rate'])
        total_return = to_return+extra
        
        # Calculate monthly repay and rate
        mon_repay = total_return/36
        rate = (total_return/money_requested-1)*100

        # Create a DF of the updated CSV (same as old without the money that was lent)
        df_2 = df.drop(list(range(0,next_count_ind))).reset_index(drop=True)
        df_2.loc[0,'money_lent'] = df_2.loc[0,'money_lent']-remainder
        df_2['exp_return'] = df_2['money_lent']*(1+df_2['exp_rate'])
        df_2.to_csv(path_or_buf='../Data/MarketDataforTechnicalExercise_2.csv', index=False)
        
        return print('Requested amount: £'+ '%.2f'%(money_requested)+
              '\n' + 'Rate: '+ str(rate.round(1)) + '%' +
              '\n' + 'Monthly repayment: £'+ str(mon_repay.round(2)) +
              '\n' + 'Total repayment: £' + str(total_return.round(2)))


    
    # each group of investors (with 7 participants) is able to provide 2.330 EUR at different rates.
def FillTheBucket (n_groups_of_7_investors):

    # Import libraries and read the file with investor info.
    import pandas as pd
    import sys
    sys.path.append('..')
    data = pd.read_csv('../Data/MarketDataforTechnicalExercise_2.csv')
    df = data
    
    # Create a standard  investor dataframe.
    new_inv_dict = {'lender_name': ['Bob', 'Jane', 'Fred', 'Mary', 'John', 'Dave', 'Angela'], 
                  'exp_rate': [0.075, 0.069, 0.071, 0.104, 0.081, 0.074, 0.071], 
                 'money_lent': [640, 480, 520, 170, 320, 140, 60]}
    new_inv_df = pd.DataFrame(data=new_inv_dict)
    
    # Append as many groups as required.
    n_groups = list(range(0,n_groups_of_7_investors))
    
    for n in n_groups:
        df = df.append(new_inv_df)
    
    # Sort data by expected rate and create a column with expected amount (for each investor to receive in return).
    df = df.sort_values(by=['exp_rate'])
    df['exp_return'] = df['money_lent']*(1+df['exp_rate'])
    
    # Reset indexes
    data = df.reset_index(drop=True)
    
    # Save to CSV.
    data.to_csv(path_or_buf='../Data/MarketDataforTechnicalExercise_2.csv', index=False)
    
    return data


