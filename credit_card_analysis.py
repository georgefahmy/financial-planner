import os
import sys
import pandas as pd


credit_card_path = "/Users/GFahmy/Documents/Finances/credit_cards/george_apple_card/"

files = os.listdir(credit_card_path)
all_data = pd.DataFrame()
for filename in files:
    filepath = credit_card_path + filename
    all_data = pd.concat([all_data, pd.read_csv(filepath)])

all_data.sort_values("Transaction Date", inplace=True)
purchases = all_data.loc[all_data["Type"] == "Purchase"]
installments = all_data.loc[all_data["Type"] == "Installment"]
all_data.to_csv(credit_card_path + "all_data.csv")
