import pytablereader as ptr
import pytablewriter as ptw
from pytablewriter import MarkdownTableWriter

def main():
    # prepare data ---
    csv_file_path = "data.csv"


        
    
        # load from a csv text ---
        

    # load from a csv file ---
    loader = ptr.CsvTableFileLoader(csv_file_path)
    for table_data in loader.load():
        #print(table_data)
        #print(ptw.dumps_tabledata(table_data))
        text = ("\n".join([
            "load from file",
            "==============",
            "{:s}".format(ptw.dumps_tabledata(table_data)),
        ]))
    markdown_file_path="data.md"
    with open(markdown_file_path, "w") as f:
        f.write(text)
    print(text)




    writer = MarkdownTableWriter()

    writer.from_csv(csv_file_path)
    writer.dump("mm.md")
    writer.table_name = "example_table"
    writer.headers = ["int", "float", "str", "bool", "mix", "time"]
    writer.value_matrix = [
        [0,   0.1,      "hoge", True,   0,      "2017-01-01 03:04:05+0900"],
        [2,   "-2.23",  "foo",  False,  None,   "2017-12-23 45:01:23+0900"],
        [3,   0,        "bar",  "true",  "inf", "2017-03-03 33:44:55+0900"],
        [-10, -9.9,     "",     "FALSE", "nan", "2017-01-01 00:00:00+0900"],
    ]
    writer.table_data=(table_data)
    writer.write_table()
    
if __name__=="__main__":
    main()

