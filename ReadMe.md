#成都理工大学教务系统课程表爬取

###分析：

登录一个学生的账号，即可拿到全校所有的课表。

###结果：

爬取了商学院经济学2016级所有学生的课表

###实现流程：

用scrapy框架和selenium进行登录和爬取


###不足：

- 用selenium爬取时间过长
- 拿到课表后解析数据的算法复杂度较高


###改进方向：

- 写一个爬虫用selenium模仿登录后，拿到登录后的cookie中保存的userToken存到本地。再写一个爬虫拿到本地保存的cookie的值，不使用selenium爬取课程表。 
- 解析课程表尚未想到更好的算法，后续继续琢磨。
- 数据保存，后续将改为mongodb。