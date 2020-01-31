import pytablereader as ptr
import pytablewriter as ptw
from pytablewriter import HtmlTableWriter

def main():
    # prepare data ---
    csv_file_path = "inflow.csv"
    html_file_path = "inflow.html"
    print("this python script read table in ",csv_file_path, " and then write it into html file ",html_file_path)
    print("converting...")
    writer = HtmlTableWriter()
    writer.from_csv(csv_file_path)
    writer.table_name = "物资流入表"
    writer.dump(html_file_path)
    #writer.write_table()
    print("done")
    
if __name__=="__main__":
    main()

