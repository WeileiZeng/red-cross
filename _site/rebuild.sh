echo "rebuild all..."
python3 csv2html.py
./merge_files.sh
less inflow.html
