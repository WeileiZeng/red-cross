out=../index.md

cd page

echo "this script merge all parts of readme into one file $out"

cat head.md > $out

echo "### [湖北省红十字会](http://hbsredcross.org.cn/)累计捐赠情况" >> $out
echo >> $out
cat donate.md >> $out
echo >> $out

#echo "### 物资流入表" >> $out
#echo >> $out
#cat inflow.md >> $out
#echo >> $out

echo "### [1月30日公布物资使用情况](http://www.hbsredcross.org.cn/xxgk/4704.jhtml)" >> $out
echo >> $out
cat outflow.md >> $out
echo >> $out

cat tail.md >> $out

cd ..
echo "finish merging"
#less README.md
