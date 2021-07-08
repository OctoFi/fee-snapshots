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


#######################
## RECREATE OLD SNAPSHOTS
#######################

##################
## FEBRUARY SNAPSHOT
##################

# to 11769165
trns_11769165 = get_contract_transfers(contract, from_block="0xB28720", to_block="0xB3954D")
transfers += trns_11769165

## Feb-01-2021 08:08:26 AM +UTC
filename = 'balances/02-01-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)


# to 11944679
trns_11944679 = get_contract_transfers(contract, from_block="0xB3954D", to_block="0xB642E7")
transfers += trns_11944679

## Feb-28-2021 08:08:21 AM +UTC
filename = 'balances/02-28-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)

##################
## MARCH SNAPSHOT
##################

# to 11951174
trns_11951174 = get_contract_transfers(contract, from_block="0xB642E7", to_block="0xB65C46")
transfers += trns_11951174

## Mar-01-2021 08:08:10 AM +UTC
filename = 'balances/03-01-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)

# to 12145960
trns_12145960 = get_contract_transfers(contract, from_block="0xB65C46", to_block="0xB95528")
transfers += trns_12145960

## Mar-31-2021 08:08:28 AM +UTC
filename = 'balances/03-31-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)

##################
## APRIL SNAPSHOT
##################

# to 12152444
trns_12152444 = get_contract_transfers(contract, from_block="0xB95528", to_block="0xB96E7C")
transfers += trns_12152444

## Apr-01-2021 08:08:08 AM +UTC
filename = 'balances/04-01-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)

# to 12340696
trns_12340696 = get_contract_transfers(contract, from_block="0xB96E7C", to_block="0xBC4DD8")
transfers += trns_12340696

## Apr-30-2021 08:08:18 AM +UTC
filename = 'balances/04-30-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)


#######################
## NEW SNAPSHOTS
#######################


##################
## MAY SNAPSHOT
##################

# to 12347119
trns_12347119 = get_contract_transfers(contract, from_block="0xBC4DD8", to_block="0xBC66EF")
transfers += trns_12347119

## May-01-2021 08:08:12 AM +UTC
filename = 'balances/05-01-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)

# to 12540966
trns_12540966 = get_contract_transfers(contract, from_block="0xBC66EF", to_block="0xBF5C26")
transfers += trns_12540966

## May-31-2021 08:08:31 AM +UTC
filename = 'balances/05-31-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)


##################
## JUNE SNAPSHOT
##################

# to 12547387
trns_12547387 = get_contract_transfers(contract, from_block="0xBF5C26", to_block="0xBF753B")
transfers += trns_12547387

## Jun-01-2021 08:08:01 AM +UTC
filename = 'balances/06-01-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)

# to 12734165
trns_12734165 = get_contract_transfers(contract, from_block="0xBF753B", to_block="0xC24ED5")
transfers += trns_12734165

## Jun-30-2021 08:08:05 AM +UTC
filename = 'balances/06-30-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)


##################
## JULY SNAPSHOT
##################

# to 12740599
trns_12740599 = get_contract_transfers(contract, from_block="0xC24ED5", to_block="0xC267F7")
transfers += trns_12740599

## Jul-01-2021 08:08:11 AM +UTC
filename = 'balances/07-01-2021.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)



###
### INSERT NEW SNAPSHOTS HERE
### Update from_block for trns_latest using the new to_block
###



##################
## TO LATEST BLOCK
##################

# to latest
trns_latest = get_contract_transfers(contract, from_block="0xC267F7", to_block="latest")
transfers += trns_latest

## latest
filename = 'balances/latest.csv'
balances = get_balances_list(transfers)
write_csv_file(filename, balances)
