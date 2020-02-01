import pytablereader as ptr
import pytablewriter as ptw
from pytablewriter import HtmlTableWriter

def convert(csv_file_path, html_file_path,table_name):
    print("this python script read table in ",csv_file_path, " and then write it into html file ",html_file_path)
    print("converting...")
    writer = HtmlTableWriter()
    writer.from_csv(csv_file_path)
    writer.table_name = table_name

    #modify the link in the fourth row to be an html link
    for row in writer.value_matrix:
        #row[3]='\n <a href="'+row[3]+'"> link </a> \n'
        row[3]='link'
    #print('tag ->',writer.is_escape_html_tag)
    #writer.is_escape_html_tag=True
    #print('tag ->',writer.is_escape_html_tag)
    writer.dump(html_file_path)
    #writer.write_table()
    print("done with ",table_name)

def main():
    csv_file_path = "inflow.csv"
    html_file_path = "inflow.html"
    table_name = "物资流入表"
    convert(csv_file_path, html_file_path,table_name)
    csv_file_path = "outflow.csv"
    html_file_path = "outflow.html"
    table_name = "物资流出表"
    convert(csv_file_path, html_file_path,table_name)
    
if __name__=="__main__":
    main()

