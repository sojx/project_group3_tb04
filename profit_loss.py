from pathlib import Path

fp_read= Path.cwd()/"csv_reports"/"profit_and_loss.csv"
fp_read.touch()

pattern_netprofit="Net Profit.+"

for file in fp_read.glob("*_txt"):
    with file.open(mode="r", encoding="UTF-8") as file:
        data=file.read()

        netprofit=re.search(pattern=pattern_netprofit)
