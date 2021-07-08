from ethereum import *
contract = "0x7240aC91f01233BaAf8b064248E80feaA5912BA3"

#######################
## HISTORICAL TRANSFERS
#######################

# from 10678548 (Genesis) to 10900000
trns_1090 = get_contract_transfers(contract, from_block="0xA2F114", to_block="0xA65220")
transfers = trns_1090

# to 11000000
trns_1100 = get_contract_transfers(contract, from_block="0xA65220", to_block="0xA7D8C0")
transfers += trns_1100

# to 11100000
trns_1110 = get_contract_transfers(contract, from_block="0xA7D8C0", to_block="0xA95F60")
transfers += trns_1110

# to 11200000
trns_1120 = get_contract_transfers(contract, from_block="0xA95F60", to_block="0xAAE600")
transfers += trns_1120

# to 11300000
trns_1130 = get_contract_transfers(contract, from_block="0xAAE600", to_block="0xAC6CA0")
transfers += trns_1130

# to 11400000
trns_1140 = get_contract_transfers(contract, from_block="0xAC6CA0", to_block="0xADF340")
transfers += trns_1140

# to 11500000
trns_1150 = get_contract_transfers(contract, from_block="0xADF340", to_block="0xAF79E0")
transfers += trns_1150

# to 11600000
trns_1160 = get_contract_transfers(contract, from_block="0xAF79E0", to_block="0xB10080")
transfers += trns_1160

# to 11700000
trns_1170 = get_contract_transfers(contract, from_block="0xB10080", to_block="0xB28720")
transfers += trns_1170

# to 11800000
trns_1180 = get_contract_transfers(contract, from_block="0xB28720", to_block="0xB40DC0")
transfers += trns_1180

# to 11900000
trns_1190 = get_contract_transfers(contract, from_block="0xB40DC0", to_block="0xB59460")
transfers += trns_1190

# to 12000000
trns_1200 = get_contract_transfers(contract, from_block="0xB59460", to_block="0xB71B00")
transfers += trns_1200

# to 12100000
trns_1210 = get_contract_transfers(contract, from_block="0xB71B00", to_block="0xB8A1A0")
transfers += trns_1210

# to 12200000
trns_1220 = get_contract_transfers(contract, from_block="0xB8A1A0", to_block="0xBA2840")
transfers += trns_1220

# to 12300000
trns_1230 = get_contract_transfers(contract, from_block="0xBA2840", to_block="0xBBAEE0")
transfers += trns_1230


#######################
## SNAPSHOTS
#######################

#######################
## MAY SNAPSHOT
#######################

# to 12347119
trns_12347119 = get_contract_transfers(contract, from_block="0xBBAEE0", to_block="0xBC66EF")
transfers += trns_12347119

## May-01-2021 08:08:12 AM +UTC
# balances_12347119_json = open('balances/05-01-2021.json', 'w')
# balances_12347119 = get_balances_list(transfers)
# print(balances_12347119, file = balances_12347119_json)
# balances_12347119_json.close()

# to 12540966
trns_12540966 = get_contract_transfers(contract, from_block="0xBC66EF", to_block="0xBF5C26")
transfers += trns_12540966

## May-31-2021 08:08:31 AM +UTC
# balances_12540966_json = open('balances/05-31-2021.json', 'w')
# balances_12540966 = get_balances_list(transfers)
# print(balances_12540966, file = balances_12540966_json)
# balances_12540966_json.close()


#######################
## JUNE SNAPSHOT
#######################

# to 12547387
trns_12547387 = get_contract_transfers(contract, from_block="0xBF5C26", to_block="0xBF753B")
transfers += trns_12547387

## Jun-01-2021 08:08:01 AM +UTC
# balances_12547387_json = open('balances/06-01-2021.json', 'w')
# balances_12547387 = get_balances_list(transfers)
# print(balances_12547387, file = balances_12547387_json)
# balances_12547387_json.close()

# to 12734165
trns_12734165 = get_contract_transfers(contract, from_block="0xBF753B", to_block="0xC24ED5")
transfers += trns_12734165

## Jun-30-2021 08:08:05 AM +UTC
# balances_12734165_json = open('balances/06-30-2021.json', 'w')
# balances_12734165 = get_balances_list(transfers)
# print(balances_12734165, file = balances_12734165_json)
# balances_12734165_json.close()


#######################
## JULY SNAPSHOT
#######################

# to 12740599
trns_12740599 = get_contract_transfers(contract, from_block="0xC24ED5", to_block="0xC267F7")
transfers += trns_12740599

## Jul-01-2021 08:08:11 AM +UTC
# balances_12740599_json = open('balances/07-01-2021.json', 'w')
# balances_12740599 = get_balances_list(transfers)
# print(balances_12740599, file = balances_12740599_json)
# balances_12740599_json.close()



###
### INSERT NEW SNAPSHOTS HERE
### Update from_block for trns_latest using the new to_block
###



#######################
## TO LATEST BLOCK
#######################

trns_latest = get_contract_transfers(contract, from_block="0xC267F7", to_block="latest")
transfers += trns_latest

## latest
balances_json = open('balances/latest.json', 'w')
balances_latest = get_balances_list(transfers)
print(balances_latest, file = balances_json)
balances_json.close()
