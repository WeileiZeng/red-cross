import pytablereader as ptr
import pytablewriter as ptw

def main():
    # prepare data ---
    csv_file_path = "data.csv"


        
    
        # load from a csv text ---
        

    # load from a csv file ---
    loader = ptr.CsvTableFileLoader(csv_file_path)
    for table_data in loader.load():
        text = ("\n".join([
            "load from file",
            "==============",
            "{:s}".format(ptw.dumps_tabledata(table_data)),
        ]))
    markdown_file_path="data.md"
    with open(markdown_file_path, "w") as f:
        f.write(text)
    print(text)

if __name__=="__main__":
    main()

