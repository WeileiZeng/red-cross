out=../index.md

cd page

echo "this script merge all parts of readme into one file $out"

cat head.md > $out
echo "物资流入表" >> $out
echo >> $out
cat inflow.md >> $out
echo >> $out
echo "物资流出表" >> $out
echo >> $out
cat outflow.md >> $out
echo >> $out

cat tail.md >> $out

cd ..
echo "finish merging"
#less README.md
