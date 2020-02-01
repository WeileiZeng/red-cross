# render csv to markdown
# note: the markdown for github is a little bit hard to render. The table must have an extra blank line in front of it and right after it. Also, Chinese blanket ( ) is also not supported in the table


import pytablereader as ptr
import pytablewriter as ptw
from pytablewriter import HtmlTableWriter
from pytablewriter import MarkdownTableWriter

def convert(csv_file_path, html_file_path,table_name):
    print("this python script read table in ",csv_file_path, " and then write it into html file ",html_file_path)
    print("converting...")
    #writer = HtmlTableWriter()
    writer = MarkdownTableWriter()
    writer.from_csv(csv_file_path)
    writer.table_name = table_name

    #modify the link in the fourth row to be an html link
    for row in writer.value_matrix:
        #row[3]='\n <a href="'+row[3]+'"> link </a> \n'
        row[3]='[link]('+row[3]+')'
    #print('tag ->',writer.is_escape_html_tag)
    #writer.is_escape_html_tag=True
    #print('tag ->',writer.is_escape_html_tag)
    writer.dump(html_file_path)
    #writer.write_table()
    print("done with ",table_name)

def main():
    data_path=""
    build_path="./../page/"
    csv_file_path = "inflow.csv"
    html_file_path = "inflow.md"
    table_name = '' #"物资流入表"
    convert(data_path + csv_file_path, build_path + html_file_path,table_name)
    csv_file_path = "outflow.csv"
    html_file_path = "outflow.md"
    table_name = '' #"物资流出表"
    convert(data_path + csv_file_path, build_path + html_file_path,table_name)
    
if __name__=="__main__":

    main()

