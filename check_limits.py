battery_allowedValues = {
        'temperature'      : {'min': 0, 'max': 45},
        'state_of_charge'  : {'min': 20, 'max': 80},
        'charge_rate'      : {'min': 0,'max': 0.8}
                     }
Display_Message               = {
				'low_breach':   { 'DE' : 'Untergrenze überschritten für ', 
                                                  'EN' : 'Lower Limit Breached for ' }   ,
                                'warning_L' : 	{ 'DE' : 'Unterer Schwellenwert nähert sich '  ,   
                                                  'EN' : 'Lower Threshold Nearing '},
                                'high_breach' : { 'DE' : 'Obergrenze überschritten für '  , 
                                                  'EN' : 'Higher Limit Breached for ' }   ,
                                'warning_H'	: 	{ 'DE' : 'Höhere Schwelle nähert sich ', 
                                                  'EN' : 'Higher Threshold Nearing ' } 
				 } 
Temp_unit = {
                          'C': 'Celsius',
                          'F': 'Fahrenheit'
            }
			
Lang = "EN"    
                  
def lower_limit(value):
	allowed_limit = 5
	return (value * allowed_limit) / 100
	
Valuee = 1	
def battery_status():
	if(valuee == 1):
		status=True
	else :
		status=False
	return status
	
def rangeValidation(bmsParam_value,bmsParam_name,Lang,high,minimum):
	bottom_level= battery_allowedValues[bmsParam_name]['min']
	high_level = battery_allowedValues[bmsParam_name]['max']
	threshold = lower_limit(maximum)
	lower_value = minimum+threshold
	high_value =  maximum-threshold
	if (bmsParam_value < lower_value):
		 print(Display_Message  ['warning_L'][lang]+bmsParam_name)
	if (bmsParam_value > high_value):
		 print(Display_Message  ['warning_H'][lang]+bmsParam_name)

	
def battery_validationcheck(battery_inputs,Value):
        outOfIndex_Values = []
        for bmsParam_name,bmsParam_value in battery_inputs.items() :
            battery_Limit_Check(bmsParam_name,bmsParam_value,outOfIndex_Values)
        return outOfIndex_Values

def battery_Limit_Check(bmsParam_name,bmsParam_value,outOfIndex_Values,Lang): 
        if (bmsParam_value < battery_allowedValues[bmsParam_name]['min']):
			print(Display_Message  ['low_breach'][Lang]+bmsParam_name)
			status=True
	elif(bmsParam_value > battery_allowedValues[bmsParam_name]['max']):
			print(Display_Message  ['high_breach'][Lang]+bmsParam_name)
			status=False
        else:
			Check_range(bmsParam_value,bmsParam_name,Lang,maximum,minimum) 
			
def fahrenheit_to_celsius(bmsParam_name, bmsParam_value):
    if (Temp_unit == 'F'):
        Celsius_Value = (bmsParam_value-32)*(5/9)
    else:
        Celsius_Value = bms_param_value
    return Celsius_Value
                   
def battery_is_ok(temperature,state_of_charge,charge_rate,Lang):
        battery_Limit_Check(temperature,state_of_charge,charge_rate,Lang)
		return battery_status()

if __name__ == '__main__':
        assert(battery_is_ok({'temperature': 15,'state_of_charge': 65, 'charge_rate': 0.6,'EN'}) is True) 
        assert(battery_is_ok({'temperature': 70,'state_of_charge': 90, 'charge_rate': 0.9,'EN'}) is False)  
        assert(battery_is_ok({'temperature': 46,'state_of_charge': 10, 'charge_rate': 0.9,'EN'}) is False)
	assert(battery_is_ok({'temperature': 15,'state_of_charge': 65, 'charge_rate': 0.6,'DE'}) is True) 
        assert(battery_is_ok({'temperature': 70,'state_of_charge': 90, 'charge_rate': 0.9,'DE'}) is False)  
        assert(battery_is_ok({'temperature': 46,'state_of_charge': 10, 'charge_rate': 0.9,'DE'}) is False)

