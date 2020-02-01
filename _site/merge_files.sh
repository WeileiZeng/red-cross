out=../index.md

cd page

echo "this script merge all parts of readme into one file $out"

cat head.md > $out
echo "物资流入表" >> $out 
cat inflow.html >> $out
echo "<br>" >> $out
echo "物资流出表" >> $out
cat outflow.html >> $out
echo "<br>" >> $out
cat tail.md >> $out

cd ..
echo "finish merging"
#less README.md
