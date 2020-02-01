echo "rebuild all..."

# convert csv to html table
cd data
python3 csv2html.py

# merge all files into index.md
cd ..
./merge_files.sh

echo "finish building"

#less inflow.html
