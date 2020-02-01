import pytablereader as ptr
import pytablewriter as ptw
from pytablewriter import MarkdownTableWriter

def main():
    # prepare data ---
    csv_file_path = "data.csv"
    markdown_file_path = ("data.md")
    print("this python script read table in ",csv_file_path, " and then write it into markdown file ",markdown_file_path)
    print("converting...")
    writer = MarkdownTableWriter()
    writer.from_csv(csv_file_path)
    writer.margin = 1 
    writer.dump(markdown_file_path)
    print("done")
    
if __name__=="__main__":
    main()

