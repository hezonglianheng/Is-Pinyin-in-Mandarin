# Is-Pinyin-in-Mandarin

项目来源：https://mp.weixin.qq.com/s/DYbosH_EXBSO9R_byAx4LQ <br>

结构：
source文件夹下的是程序使用时使用的资源文件。<br>
分为pinyin.txt和pinyin_set.json两个文件。其中pinyin.txt文件来源于北京大学中国语言学计算语言中心。<br>
initialize.py主要是读取pinyin.txt文件信息，转化为pinyin_set.json文件。
main.py主要是基于tkinter的GUI设计和程序执行部分。

本程序力图复现推文中宣传的由4名中文系学生开发的《计算概论C》作业内容。<br>
主要功能为判断由使用者输入的拼音音节是否是现代汉语中的合法音节。<br>
出于汉语拼音学习的特点，本程序将汉语拼音拆分为声母、韵母和声调三个方面。其中、汉语声调使用了数字进行代替：<br>
1——阴平（第一声）<br>
2——阳平（第二声）<br>
3——上声（第三声）<br>
4——去声（第四声）<br>
0——轻声<br>

改进空间：<br>
1.可以使用数据库重构；<br>
2.GUI优化；<br>
3.可以添加更多功能，更符合汉语学习者的需要；<br>
……
