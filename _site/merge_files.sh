out=../index.md

cd page

echo "this script merge all parts of readme into one file $out"

cat head.md > $out

echo "### [湖北省红十字会](http://hbsredcross.org.cn/)累计捐赠表" >> $out
echo >> $out
cat hubei-donation.md >> $out
echo >> $out

#echo "### 物资流入表" >> $out
#echo >> $out
#cat inflow.md >> $out
#echo >> $out

echo "### [1月30日公布物资使用情况](http://www.hbsredcross.org.cn/xxgk/4704.jhtml)" >> $out
echo >> $out
cat hubei-outflow.md >> $out
echo >> $out
echo "注：“N95口罩36000个”更正为“KN95口罩36000个”，其流向“武汉仁爱医院1.6万、武汉天佑医院1.6万”更正为“武汉仁爱医院1.8万个、武汉天佑医院1.8万个”  [link](http://www.hbsredcross.org.cn/xxgk/8667.jhtml)" >> $out
echo >> $out

cat news.md >> $out

cat tail.md >> $out

cd ..
echo "finish merging"
#less README.md
