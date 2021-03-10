battery_allowedValues = {
        'temperature'      : {'min': 0, 'max': 45},
        'state_of_charge'  : {'min': 20, 'max': 80},
        'charge_rate'      : {'min': 0,'max': 0.8}
                     }

def battery_validationcheck(battery_inputs):
        outOfIndex_Values = []
        for bmsParam_name,bmsParam_value in battery_inputs.items() :
            battery_Limit_Check(bmsParam_name,bmsParam_value,outOfIndex_Values)
        return outOfIndex_Values

def battery_Limit_Check(bmsParam_name,bmsParam_value,outOfIndex_Values): 
        if (bmsParam_value < battery_allowedValues[bmsParam_name]['min']) or (bmsParam_value > battery_allowedValues[bmsParam_name]['max']):
            outOfIndex_Values.append(bmsParam_name)
                   
def battery_is_ok(battery_inputs):
        battery_range_check = battery_validationcheck(battery_inputs)
        if len(battery_range_check) == 0:
            return True
        else :
            return False

if __name__ == '__main__':
        assert(battery_is_ok({'temperature': 15,'state_of_charge': 65, 'charge_rate': 0.6}) is True) 
        assert(battery_is_ok({'temperature': 70,'state_of_charge': 90, 'charge_rate': 0.9}) is False)  
        assert(battery_is_ok({'temperature': 46,'state_of_charge': 10, 'charge_rate': 0.9}) is False)
