#Cost table reference function for Electricity (euro/kwh)
def cost_table_elec(kwh_per_annum):
    if kwh_per_annum < 1000:
        elec_cost = 0.4100
        ##elec_band = 'DA'
    elif 1000<=kwh_per_annum < 2500:
        elec_cost = 0.2800
        #elec_band = 'DB'
    elif 2500 <= kwh_per_annum < 5000:
        elec_cost = 0.2300
        #elec_band = 'DC'
    elif 5000 <= kwh_per_annum < 15000:
        elec_cost = 0.2000
        #elec_band = 'DD'
    elif 15000 <= kwh_per_annum < 20000:
        elec_cost = 0.1700
        #elec_band = 'DE'
    #elif 20000 <= kwh_per_annum < 500000:
    #   elec_cost = 0.2904
    #   #elec_band = 'IA'
    elif 20000 <= kwh_per_annum < 500000:
        elec_cost = 0.1806
        #elec_band = 'IB'
    elif 500000 <= kwh_per_annum < 2000000:
        elec_cost = 0.1498
        #elec_band = 'IC'
    elif 2000000 <= kwh_per_annum < 20000000:
        elec_cost = 0.1126
        #elec_band = 'ID'
    elif 500000 <= kwh_per_annum < 70000000:
        elec_cost = 0.0976
        #elec_band = 'IE'
    elif 70000000 <= kwh_per_annum < 150000000:
        elec_cost = 0.0894
        #elec_band = 'IF'
    
    return elec_cost

#Cost Table reference function for gas
def cost_table_gas(kwh_per_annum):
    if kwh_per_annum < 5556:
        gas_cost = 0.0730
        #gas_band = 'D1'
    elif 5556 <= kwh_per_annum < 55560:
        gas_cost = 0.0650
        #gas_band = 'D2'
    elif 55560 <= kwh_per_annum  :
        gas_cost = 0.0611
        #gas_band = 'D3'
    #elif kwh_per_annum < 2777800:
    #    gas_cost = 0.0580
    #    #gas_band = 'I1'
    elif 277800 <= kwh_per_annum < 2778000:
        gas_cost = 0.0450
        #gas_band = 'I2'
    elif 2778000 <= kwh_per_annum < 27780000:
        gas_cost = 0.0360
        #gas_band = 'I3'
    elif 27780000 <= kwh_per_annum < 277800000:
        gas_cost = 0.02580
        #gas_band = 'I4' 
    return gas_cost

       
