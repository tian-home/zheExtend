# STEP1 HTML基础

## S1-1 HTML基础

### 第1章 基础语法

#### 1-2 html基础语法

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
	</head>
<body bgcolor="gray">
   <p>HELLO, everyone. This is my first page!</p>
   <hr><!-- hr是水平线-->
</body>
</html>
```

 

### 第2章 文档段落

#### 2-1 文档声明和meta标签

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="gray">
   <p>HELLO, everyone. This is my first page!开始交往和</p>
   <hr><!-- hr是水平线-->
</body>
</html>
```

中文编码 

utf-8

gb2312

gbk

#### 2-6 文字与段落

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="gray">
	<h1>什么是HTML</h1>
	<h2>什么是HTML</h2>
	<h3>什么是HTML</h3>
	<h4>什么是HTML</h4>
	<h5>什么是HTML</h5>
	<h6>什么是HTML</h6>
	<p>《我的世界》（Minecraft）是一款沙盒类电子游戏，开创者为马库斯·阿列克谢·泊松（Notch）。游戏由Mojang Studios维护，现隶属于微软Xbox游戏工作室。中国版现由网易游戏代理 [27]  ，于2017年8月8日在中国大陆运营 [25]  。</p>
	<p align="left">《我的世界》（Minecraft）是一款沙盒类电子游戏，开创者为马库斯·阿列克谢·泊松（Notch）。游戏由Mojang Studios维护，现隶属于微软Xbox游戏工作室。中国版现由网易游戏代理 [27]  ，于2017年8月8日在中国大陆运营 [25]  。</p>
	<p align="right">《我的世界》（Minecraft）是一款沙盒类电子游戏，开创者为马库斯·阿列克谢·泊松（Notch）。游戏由Mojang Studios维护，现隶属于微软Xbox游戏工作室。中国版现由网易游戏代理 [27]  ，于2017年8月8日在中国大陆运营 [25]  。</p>
	<p align="center">《我的世界》（Minecraft）是一款沙盒类电子游戏，开创者为马库斯·阿列克谢·泊松（Notch）。游戏由Mojang Studios维护，现隶属于微软Xbox游戏工作室。中国版现由网易游戏代理 [27]  ，于2017年8月8日在中国大陆运营 [25]  。</p>
	<p align="justify"> &nbsp;  空格 &nbsp;&nbsp;&nbsp;《我的世界》（Minecraft）是一款沙盒类电子游戏，开创者为马库斯·阿列克谢·泊松（Notch）。<br>游戏由Mojang Studios维护，现隶属于微软Xbox游戏工作室。中国版现由网易游戏代理 [27]  ，于2017年8月8日在中国大陆运营 [25]  。</p>
	<pre>
		        《我的世界》（Minecraft）是一款沙盒类电子游戏，开创者为马库斯·阿列克谢·泊松（Notch）。游戏由Mojang 
		Studios维护，现隶属于微软Xbox游戏工作室。
		中国版现由网易游戏代理 [27]  ，于2017年8月8日在中国大陆运营 [25]
	</pre>
   <hr><!-- hr是水平线-->
</body>
</html>
```

#### 2-15 修饰标签和特殊符号

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="white">
	
	<p>《我的世界》（Minecraft）是一款沙盒类电子游戏，开创者为马库斯·阿列克谢·泊松（Notch）。游戏由Mojang Studios维护，现隶属于微软Xbox游戏工作室。中国版现由网易游戏代理 [27]  ，于2017年8月8日在中国大陆运营 [25]  。</p>
	<p><b>《我的世界》	</b><i>《我的世界》</i><sub>《我的世界》</sub><sup>《我的世界》</sup></p>
	<p>&lt;b&gt;&copy;《我的世界》	</p>

</body>
</html>
```



***



### 第3章 列表标签

#### 3-1 列表标签-无序列表

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="white">
	
	<h1>标题</h1>
	<p>段落内容</p>
	<ul type="disc">
		<li>项目1</li>
		<li>项目2</li>
		<li>项目3</li>
		<li>项目4</li>	
	</ul>
	<ul type="square">
		<li>项目1</li>
		<li>项目2</li>
		<li>项目3</li>
		<li>项目4</li>	                 
	</ul>
	<ul type="circle">
		<li>项目1</li>
		<li>项目2</li>
		<li>项目3</li>
		<li>项目4</li>	
	</ul>
</body>
</html>
```



#### 3-5 有序列表

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="white">
	
	<h1>标题</h1>
	<p>段落内容</p>
	<ol>
		<li>项目1</li>
		<li>项目2</li>
		<li>项目3</li>
		<li>项目4</li>	
	</ol>
	<ol type="a">
		<li>项目1</li>
		<li>项目2</li>
		<li>项目3</li>
		<li>项目4</li>	                 
	</ol>
	<ol type="i">
		<li>项目1</li>
		<li>项目2</li>
		<li>项目3</li>
		<li>项目4</li>	
	</ol>
</body>
</html>
```



#### 3-9 列表标签-定义列表

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="white">
	
	<h1>标题</h1>
	<p>段落内容</p>
	<dl>
		<dt>项目1</dt>
		<dd>项目2</dd>
		<dt>项目3</dt>
		<dd>项目4</dd>	
	</dl>
	
</body>
</html>
```



### 第4章 图像和超链接

#### 4-1 图像

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="white">
	
	
<img src="C:\Users\tianxingzhe\Pictures\Saved Pictures\极光.jpg" alt="" width="200px">
<br>
<img src="海边长桥.jpg" alt="" height="300px">
<img src="img/晚霞港.jpg" alt="" width="200px">
<img src="../高楼林立.jpg" alt="">	
</body>
</html>
```

 

#### 4-6 超链接

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="white">
	
	
<a href="内部链接.html"><img src="C:\Users\tianxingzhe\Pictures\Saved Pictures\极光.jpg" alt="" width="200px"></a>
<br>
<img src="海边长桥.jpg" alt="" height="300px">
<img src="img/晚霞港.jpg" alt="" width="200px">

<a href="https://www.bilibili.com/"><h2>外部链接</h2></a>	
</body>
</html>
```

#### 4-9 超链接2

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="white">
	
	
<a href="内部链接.html"><img src="C:\Users\tianxingzhe\Pictures\Saved Pictures\极光.jpg" alt="" width="200px"></a>
<br>
<img src="海边长桥.jpg" alt="" height="300px">
<img src="img/晚霞港.jpg" alt="" width="200px">

<a href="https://www.bilibili.com/"><h2>外部链接</h2></a>
<a href="https://www.bilibili.com/" target="_self"><h2>外部链接 原页面</h2></a>
<a href="https://www.bilibili.com/" target="_blank"><h2>外部链接 新页面</h2></a>
<a href="#" title="学习html"><h2>空链接</h2></a>	

</body>
</html>
```

#### 4-16 锚链接

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="white">
	
<a href="#mao-html">html</a>&nbsp; &nbsp;&nbsp;&nbsp;<a href="#mao-css">css</a>&nbsp;&nbsp;&nbsp;&nbsp; js
<a href="https://www.bilibili.com/" name="mao-html"><h2>html课程</h2></a>
<pre>
	第1章 课程导学
视频：
1-1 课程导学：为什么要学习 Kaggle 竞赛知识？(07:06)
第2章 学前基础知识
图文：
2-1 学前必读知识
视频：
2-2 Kaggle竞赛介绍(13:35)
视频：
2-3 Kaggle竞赛流程(08:58)
图文：
2-4 Kaggle Notebooks使用
视频：
2-5 XGBoost 、LightGBM和Catboost(13:54)
视频：
2-6 数据划分与交叉验证(16:58)
视频：
2-7 模型集成方法(19:39)
视频：
2-8 比赛案例Titanic幸存乘客预测(18:30)
视频：
2-9 本章小结(05:06)
作业：
2-10 【作业】注册Kaggle账号，参加Tiantic比赛并提交
第3章 结构化技能与案例分析
图文：
3-1 学前必读知识
视频：
3-2 结构化技能之特征工程（上）(14:12)
视频：
3-3 结构化技能之特征工程（下）(14:47)
视频：
3-4 结构化技能之特征筛选(18:14)
视频：
3-5 -1 Instant Gratification赛题介绍（上）最近学习
视频：
3-6 Instant Gratification赛题介绍（下）(19:14)
视频：
3-7 Instant Gratification赛题实践(23:02)
视频：
3-8 Instant Gratification优胜方案(16:23)
视频：
3-9 IEEE-CIS Fraud Detection赛题介绍(19:41)
视频：
3-10 IEEE-CIS Fraud Detection赛题实践(16:09)
视频：
3-11 IEEE-CIS Fraud Detection优胜方案(11:45)
视频：
3-12 Indoor Location & Navigation赛题介绍(16:02)
视频：
3-13 Indoor Location & Navigation动手实践(17:26)
视频：
3-14 Indoor Location & Navigation优胜方案(18:05)
视频：
3-15 Home Credit Default Risk赛题介绍(14:10)
视频：
3-16 Home Credit Default Risk赛题实践（上）(11:14)
视频：
3-17 Home Credit Default Risk赛题实践（下）(09:42)
视频：
3-18 Home Credit Default Risk优胜方案(17:05)
作业：
3-19 【作业】参加Kaggle平台比赛，并提交结果
视频：
3-20 本章小结(05:06)
第4章 文本技能与案例解析
图文：
4-1 学前必读知识
视频：
4-2 词向量基础与使用(12:53)
视频：
4-3 文本分类基础(17:47)
视频：
4-4 Quora Question Pairs赛题介绍(06:39)
视频：
4-5 Quora Question Pairs赛题实践(11:03)
视频：
4-6 Quora Question Pairs优胜方案(12:45)
视频：
4-7 高阶文本分类模型(13:48)
视频：
4-8 Quora Insincere Questions Classification赛题介绍(07:03)
视频：
4-9 Quora Insincere Questions Classification赛题实践(16:22)
视频：
4-10 Quora Insincere Questions Classification优胜方案(12:55)
视频：
4-11 Molecular Translation赛题介绍(08:37)
视频：
4-12 Molecular Translation动手实践（上）(13:32)
视频：
4-13 Molecular Translation动手实践（下）(11:16)
视频：
4-14 Molecular Translation优胜方案(14:09)
视频：
4-15 本章小结(05:47)
作业：
4-16 【作业】参加Kaggle平台比赛，并提交结果
第5章 语音技能与案例解析
图文：
5-1 学前必读知识
视频：
5-2 语音特征处理（上）(11:48)
视频：
5-3 语音特征处理（下）(10:56)
视频：
5-4 语音模型和数据扩增方法(15:10)
视频：
5-5 Cornell Birdcall Identification赛题介绍(11:57)
视频：
5-6 Cornell Birdcall Identification动手实践(13:15)
视频：
5-7 Cornell Birdcall Identification优胜方案(09:19)
视频：
5-8 本章小结(05:46)
作业：
5-9 【作业】参加Kaggle平台比赛，并提交结果
第6章 视觉技能与案例解析
视频：
6-1 数字图像基础（上）(18:00)
视频：
6-2 数字图像基础（下）(08:11)
视频：
6-3 图像分类模型和损失函数(20:47)
视频：
6-4 Quick, Draw! Doodle Recognition Challenge赛题介绍(07:05)
视频：
6-5 Quick, Draw! Doodle Recognition Challenge动手实践(17:54)
视频：
6-6 Quick, Draw! Doodle Recognition Challenge优胜方案(12:29)
视频：
6-7 语义分割模型和损失函数(12:49)
视频：
6-8 Severstal Steel Defect Detection赛题介绍(09:57)
视频：
6-9 Severstal Steel Defect Detection动手实践(15:23)
视频：
6-10 Severstal Steel Defect Detection优胜方案(11:58)
视频：
6-11 Shopee - Price Match Guarantee赛题介绍(09:54)
视频：
6-12 Shopee - Price Match Guarantee代码实践(24:14)
视频：
6-13 Shopee - Price Match Guarantee优胜方案(20:26)
视频：
6-14 章节知识点总结
</pre>
<a href="https://www.bilibili.com/" target="_self" name="mao-css"><h2>css 课程 </h2></a>

<a href="https://www.bilibili.com/" target="_blank" name="mao-js"><h2>Js 课程</h2></a>

<a href="#" title="学习html"><h2>空链接</h2></a>	

</body>
</html>
```

#### 4-27 链接扩展（邮箱,下载）

```html
<!DOCTYPE html>
<html>
	<head>
		<title>hello</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8">		
	</head>
<body bgcolor="white">
	
<a href="#mao-html">html</a>&nbsp; &nbsp;&nbsp;&nbsp;<a href="#mao-css">css</a>&nbsp;&nbsp;&nbsp;&nbsp; js    <a href="mailto:tian-xingzhe@outlook.com">反馈意见</a>
<a href="海边长桥.jpg">文件下载</a>
<a href="https://www.bilibili.com/" name="mao-html"><h2>html课程</h2></a>

<a href="https://www.bilibili.com/" target="_self" name="mao-css"><h2>css 课程 </h2></a>

<a href="https://www.bilibili.com/" target="_blank" name="mao-js"><h2>Js 课程</h2></a>

<a href="内部链接.html#mao-ji" title="学习html"><h2>空链接</h2></a>	

</body>
</html>
```



## S1-2 HTML表格

### 第1章 基础表格

#### 1-1 基础表格

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<table border="1">
		<tr>
			<td>2014</td>
			<td>2015</td>
			<td>2016</td>

		</tr>
		<tr>
			<td>8000</td>
			<td>11000</td>
			<td>14000</td>

		</tr>
	</table>
</body>
</html>
```

#### 2-1 删除表格（空）

#### 2-5 带标题,结构的表格

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<table border="1" width="500px">
		<caption>前端工程师工资</caption>
		<tr>
			<th>2014</th>
			<th>2015</th>
			<th>2016</th>

		</tr>
		<tr>
			<td>8000</td>
			<td>11000</td>
			<td>14000</td>

		</tr>
	</table>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<table border="1" width="500px">
		<caption>前端工程师工资</caption>
		<thead>
			<tr>
				<th>年份</th>
				<th>2014</th>
				<th>2015</th>
				<th>2016</th>

			</tr>
		</thead>

		<tbody>
			<tr>
				<td>北京</td>
				<td>8000</td>
				<td>11000</td>
				<td>14000</td>

			</tr>

			<tr>
				<td>上海</td>
				<td>8000</td>
				<td>11000</td>
				<td>14000</td>

			</tr>
		</tbody>

		<tfoot>
			<tr>
				<td>合计</td>
				<td>16000</td>
				<td>22000</td>
				<td>28000</td>

			</tr>
		</tfoot>
	</table>
</body>
</html>
```

#### 2-9 表格属性-1

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<table border="1" width="500px" bgcolor="#f4f4f4" cellspacing="0" cellpadding="5px" align="center" frame="box" rules="rows">
		<caption>前端工程师工资</caption>
		<thead>
			<tr>
				<th>年份</th>
				<th>2014</th>
				<th>2015</th>
				<th>2016</th>

			</tr>
		</thead>

		<tbody>
			<tr>
				<td>北京</td>
				<td>8000</td>
				<td>11000</td>
				<td>14000</td>

			</tr>

			<tr>
				<td>上海</td>
				<td>8000</td>
				<td>11000</td>
				<td>14000</td>

			</tr>
		</tbody>

		<tfoot>
			<tr>
				<td>合计</td>
				<td>16000</td>
				<td>22000</td>
				<td>28000</td>

			</tr>
		</tfoot>
	</table>
</body>
</html>
```

#### 2-14 表格属性-2

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<table border="1" width="500px" bgcolor="#f4f4f4" cellspacing="0" cellpadding="5px" align="center" >
		<caption>前端工程师工资</caption>
		<thead>
			<tr bgcolor="#d8e4bc">
				<th>年份</th>
				<th>2014</th>
				<th>2015</th>
				<th>2016</th>

			</tr>
		</thead>

		<tbody align="center" valign="middle">
			<tr>
				<td bgcolor="#b8cce4">北京</td>
				<td>8000</td>
				<td>11000</td>
				<td>14000</td>

			</tr>

			<tr>
				<td bgcolor="#b8cce4">上海</td>
				<td>8000</td>
				<td>11000</td>
				<td>14000</td>

			</tr>
		</tbody>

		<tfoot>
			<tr align="center" valign="middle">
				<td height="30px" bgcolor="#b8cce4">合计</td>
				<td>16000</td>
				<td>22000</td>
				<td>28000</td>

			</tr>
		</tfoot>
	</table>
</body>
</html>
```

#### 2-17 表格跨行跨列（空）

#### 2-19 表格嵌套（空）

#### 3-1 表格布局1（空）

#### 3-3 表格布局2（空）

## S1-3 HTML表单

### 第1章 表单基础结构

#### 1-1 表单介绍

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<form>
		姓名:<input type="text" name="username"/>
		密码:<input type="password" name="paw"/>
		<input type="submit"/>
	</form>
	
</body>
</html>
```

#### 1-6 搭建表单页面结构

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
<h1 align="center">注册信息</h1>
<hr color="#336699">
<form action="">
	<table width="600px" bgcolor="#f2f2f2" align="center">
		<tr>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
	</table>
</form>
</body>
</html>

```

### 第二章 表单元素

#### 2-1 input标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
<h1 align="center">注册信息</h1>
<hr color="#336699">
<form action="">
	<table width="600px" bgcolor="#f2f2f2" align="center">
		<tr>
			<td>姓名：</td>
			<td><input type="text" name="username" size="25" maxlength="6" placeholder="请输入姓名"></td>
		</tr>
		<tr>
			<td>邮箱：</td>
			<td><input type="text" name="email" value="@163.com"></td>
		</tr>
		<tr>
			<td>密码：</td>
			<td><input type="password" name="paw" size="25" maxlength="6" placeholder="请输入密码"></td>
		</tr>
		<tr>
			<td>确认密码：</td>
			<td><input type="password" name="paw_confirm" size="25" maxlength="6" placeholder="请再次输入密码"></td>
		</tr>
		<tr>
			<td>上传照片：</td>
			<td><input type="file" name="file"></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
	</table>
</form>
</body>
</html>
```

#### 2-10 input单选复选

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
<h1 align="center">注册信息</h1>
<hr color="#336699">
<form action="">
	<table width="600px" bgcolor="#f2f2f2" align="center">
		<tr>
			<td>姓名：</td>
			<td><input type="text" name="username" size="25" maxlength="6" placeholder="请输入姓名"></td>
		</tr>
		<tr>
			<td>邮箱：</td>
			<td><input type="text" name="email" value="@163.com"></td>
		</tr>
		<tr>
			<td>密码：</td>
			<td><input type="password" name="paw" size="25" maxlength="6" placeholder="请输入密码"></td>
		</tr>
		<tr>
			<td>确认密码：</td>
			<td><input type="password" name="paw_confirm" size="25" maxlength="6" placeholder="请再次输入密码"></td>
		</tr>
		<tr>
			<td>上传照片：</td>
			<td><input type="file" name="file"></td>
		</tr>
		<tr>
			<td>性别：</td>
			<td>
				男<input type="radio" name="sex" value="man">
				女<input type="radio" name="sex" value="woman">
				保密<input type="radio" name="sex" value="bm" checked>
			</td>
		</tr>
		<tr>
			<td>爱好：</td>
			<td>
				读书<input type="checkbox" name="dx1" value="read">
				唱歌<input type="checkbox" name="dx1" value="sing">
				跳舞<input type="checkbox" name="dx1" value="dance">
			</td>

		</tr>
		<tr>
			<td>运动：</td>
			<td>
				跑步<input type="checkbox" name="dx2" value="1">
				篮球<input type="checkbox" name="dx2" value="2">
				跳水<input type="checkbox" name="dx2" value="3">
			</td>
			
		</tr>
		<tr>
			<td></td>
			<td></td>
		</tr>
	</table>
</form>
</body>
</html>
```

#### 2-15 input按钮

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
<h1 align="center">注册信息</h1>
<hr color="#336699">
<form action="">
	<table width="600px" bgcolor="#f2f2f2" align="center">
		<tr>
			<td>姓名：</td>
			<td><input type="text" name="username" size="25" maxlength="6" placeholder="请输入姓名"></td>
		</tr>
		<tr>
			<td>邮箱：</td>
			<td><input type="text" name="email" value="@163.com"></td>
		</tr>
		<tr>
			<td>密码：</td>
			<td><input type="password" name="paw" size="25" maxlength="6" placeholder="请输入密码"></td>
		</tr>
		<tr>
			<td>确认密码：</td>
			<td><input type="password" name="paw_confirm" size="25" maxlength="6" placeholder="请再次输入密码"></td>
		</tr>
		<tr>
			<td>上传照片：</td>
			<td><input type="file" name="file"></td>
		</tr>
		<tr>
			<td>性别：</td>
			<td>
				男<input type="radio" name="sex" value="man">
				女<input type="radio" name="sex" value="woman">
				保密<input type="radio" name="sex" value="bm" checked>
			</td>
		</tr>
		<tr>
			<td>爱好：</td>
			<td>
				读书<input type="checkbox" name="dx1" value="read">
				唱歌<input type="checkbox" name="dx1" value="sing">
				跳舞<input type="checkbox" name="dx1" value="dance">
			</td>

		</tr>
		<tr>
			<td>运动：</td>
			<td>
				跑步<input type="checkbox" name="dx2" value="1">
				篮球<input type="checkbox" name="dx2" value="2">
				跳水<input type="checkbox" name="dx2" value="3">
			</td>
			
		</tr>
		<tr>
			<td>
				<input type="button" value="来点我" name="button">
				<input type="submit" value="submit" name="submit">
				<input type="reset" value="reset" name="reset">
				<input type="image" value="image_button" src="image\image01.webp">
			</td>  
			<td>
				<input type="hidden" name="hidden" value="隐藏按钮">
			</td>
		</tr>
	</table>
</form>
</body>
</html>
```

#### 2-19 input图像域和隐藏域

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
<h1 align="center">注册信息</h1>
<hr color="#336699">
<form action="">
	<table width="600px" bgcolor="#f2f2f2" align="center">
		<tr>
			<td>姓名：</td>
			<td><input type="text" name="username" size="25" maxlength="6" placeholder="请输入姓名"></td>
		</tr>
		<tr>
			<td>邮箱：</td>
			<td><input type="text" name="email" value="@163.com"></td>
		</tr>
		<tr>
			<td>密码：</td>
			<td><input type="password" name="paw" size="25" maxlength="6" placeholder="请输入密码"></td>
		</tr>
		<tr>
			<td>确认密码：</td>
			<td><input type="password" name="paw_confirm" size="25" maxlength="6" placeholder="请再次输入密码"></td>
		</tr>
		<tr>
			<td>上传照片：</td>
			<td><input type="file" name="file"></td>
		</tr>
		<tr>
			<td>性别：</td>
			<td>
				男<input type="radio" name="sex" value="man">
				女<input type="radio" name="sex" value="woman">
				保密<input type="radio" name="sex" value="bm" checked>
			</td>
		</tr>
		<tr>
			<td>爱好：</td>
			<td>
				读书<input type="checkbox" name="dx1" value="read">
				唱歌<input type="checkbox" name="dx1" value="sing">
				跳舞<input type="checkbox" name="dx1" value="dance">
			</td>

		</tr>
		<tr>
			<td>运动：</td>
			<td>
				跑步<input type="checkbox" name="dx2" value="1">
				篮球<input type="checkbox" name="dx2" value="2">
				跳水<input type="checkbox" name="dx2" value="3">
			</td>
			
		</tr>
		<tr>
			<td>
				<input type="button" value="来点我" name="button">
				<input type="submit" value="submit" name="submit">
				<input type="reset" value="reset" name="reset">
				<input type="image" value="image_button" src="image\image01.webp">
			</td>  
			<td>
				<input type="hidden" name="hidden" value="隐藏按钮">
			</td>
		</tr>
	</table>
</form>
</body>
</html>
```

#### 2-23 select标签(下拉菜单)

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
<h1 align="center">注册信息</h1>
<hr color="#336699">
<form action="">
	<table width="600px" bgcolor="#f2f2f2" align="center">
		<tr>
			<td>姓名：</td>
			<td><input type="text" name="username" size="25" maxlength="6" placeholder="请输入姓名"></td>
		</tr>
		<tr>
			<td>邮箱：</td>
			<td><input type="text" name="email" value="@163.com"></td>
		</tr>
		<tr>
			<td>密码：</td>
			<td><input type="password" name="paw" size="25" maxlength="6" placeholder="请输入密码"></td>
		</tr>
		<tr>
			<td>确认密码：</td>
			<td><input type="password" name="paw_confirm" size="25" maxlength="6" placeholder="请再次输入密码"></td>
		</tr>
		<tr>
			<td>上传照片：</td>
			<td><input type="file" name="file"></td>
		</tr>
		<tr>
			<td>性别：</td>
			<td>
				男<input type="radio" name="sex" value="man">
				女<input type="radio" name="sex" value="woman">
				保密<input type="radio" name="sex" value="bm" checked>
			</td>
		</tr>
		<tr>
			<td>爱好：</td>
			<td>
				读书<input type="checkbox" name="dx1" value="read">
				唱歌<input type="checkbox" name="dx1" value="sing">
				跳舞<input type="checkbox" name="dx1" value="dance">
			</td>

		</tr>
		<tr>
			<td>运动：</td>
			<td>
				跑步<input type="checkbox" name="dx2" value="1">
				篮球<input type="checkbox" name="dx2" value="2">
				跳水<input type="checkbox" name="dx2" value="3">
			</td>
			
		</tr>
		<tr>
			<td>城市：</td>
			<td>
				<select name="city" >

					<option value="xz">--请选择--</option>
					<option value="bj">北京</option>
					<option value="tj">天津</option>
					<option value="sh">上海</option>
					<option value="xm">厦门</option>
					<option value="fj">福建</option>
					<option value="sz">深圳</option>

				</select>
				<select name="city" size="6" multiple>
					<option value="bj">北京</option>
					<option value="tj">天津</option>
					<option value="sh">上海</option>
					<option value="xm">厦门</option>
					<option value="fj">福建</option>
					<option value="sz">深圳</option>

				</select>
			</td>
			
		</tr>
		<tr>
			<td>
				<input type="button" value="来点我" name="button">
				<input type="submit" value="submit" name="submit">
				<input type="reset" value="reset" name="reset">
				
			</td>  
			<td>
				<input type="hidden" name="hidden" value="隐藏按钮">
			</td>
		</tr>
	</table>
</form>
</body>
</html>
```

#### 2-29 textarea(文本域)

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
<h1 align="center">注册信息</h1>
<hr color="#336699">
<form action="">
	<table width="600px" bgcolor="#f2f2f2" align="center">
		<tr>
			<td><姓名：/td>
			<td><input type="text" name="username" size="25" maxlength="6" placeholder="请输入姓名"></td>
		</tr>
		<tr>
			<td>邮箱：</td>
			<td><input type="text" name="email" value="@163.com"></td>
		</tr>
		<tr>
			<td>密码：</td>
			<td><input type="password" name="paw" size="25" maxlength="6" placeholder="请输入密码"></td>
		</tr>
		<tr>
			<td>确认密码：</td>
			<td><input type="password" name="paw_confirm" size="25" maxlength="6" placeholder="请再次输入密码"></td>
		</tr>
		<tr>
			<td>上传照片：</td>
			<td><input type="file" name="file"></td>
		</tr>
		<tr>
			<td>性别：</td>
			<td>
				男<input type="radio" name="sex" value="man">
				女<input type="radio" name="sex" value="woman">
				保密<input type="radio" name="sex" value="bm" checked>
			</td>
		</tr>
		<tr>
			<td>爱好：</td>
			<td>
				读书<input type="checkbox" name="dx1" value="read">
				唱歌<input type="checkbox" name="dx1" value="sing">
				跳舞<input type="checkbox" name="dx1" value="dance">
			</td>

		</tr>
		<tr>
			<td>运动：</td>
			<td>
				跑步<input type="checkbox" name="dx2" value="1">
				篮球<input type="checkbox" name="dx2" value="2">
				跳水<input type="checkbox" name="dx2" value="3">
			</td>
			
		</tr>
		<tr>
			<td>城市：</td>
			<td>
				<select name="city" >

					<option value="xz">--请选择--</option>
					<option value="bj">北京</option>
					<option value="tj">天津</option>
					<option value="sh">上海</option>
					<option value="xm">厦门</option>
					<option value="fj">福建</option>
					<option value="sz">深圳</option>

				</select>
				<select name="city">
					<optgroup label="华北">
						<option value="bj">北京</option>
						<option value="tj">天津</option>
						<option value="sh">上海</option>
					</optgroup>
					<optgroup label="华东"> 
						<option value="xm">厦门</option>
						<option value="fj">福建</option>
						<option value="sz">深圳</option>
					</optgroup>
				</select>
			</td>
			
		</tr>
		<tr>
			<td>简介：</td>
			<td><textarea name="jj" id="" cols="30" rows="10" placeholder="请输入个人信息"></textarea>
			</td>
		</tr>
		<tr>
			<td>
				<input type="button" value="来点我" name="button">
				<input type="submit" value="submit" name="submit">
				<input type="reset" value="reset" name="reset">
				
			</td>  
			<td>
				<input type="hidden" name="hidden" value="隐藏按钮">
			</td>
		</tr>
	</table>
</form>
</body>
</html>
```

#### 3-1 表单页面整理

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
<h1 align="center">注册信息</h1>
<hr color="#336699">
<form action="">
	<table width="600px" bgcolor="#f2f2f2" align="center">
		<tr>
			<td align="right">姓名:</td>
			<td><input type="text" name="username" size="25" maxlength="6" placeholder="请输入姓名"></td>
		</tr>
		<tr>
			<td align="right">邮箱：</td>
			<td><input type="text" name="email" value="@163.com"></td>
		</tr>
		<tr>
			<td align="right">密码：</td>
			<td><input type="password" name="paw" size="25" maxlength="6" placeholder="请输入密码"></td>
		</tr>
		<tr>
			<td align="right">确认密码：</td>
			<td><input type="password" name="paw_confirm" size="25" maxlength="6" placeholder="请再次输入密码"></td>
		</tr>
		<tr>
			<td align="right">上传照片：</td>
			<td><input type="file" name="file"></td>
		</tr>
		<tr>
			<td align="right">性别：</td>
			<td>
				男<input type="radio" name="sex" value="man">
				女<input type="radio" name="sex" value="woman">
				保密<input type="radio" name="sex" value="bm" checked>
			</td>
		</tr>
		<tr>
			<td align="right">爱好：</td>
			<td>
				读书<input type="checkbox" name="dx1" value="read">
				唱歌<input type="checkbox" name="dx1" value="sing">
				跳舞<input type="checkbox" name="dx1" value="dance">
			</td>

		</tr>
		<tr>
			<td align="right">运动：</td>
			<td>
				跑步<input type="checkbox" name="dx2" value="1">
				篮球<input type="checkbox" name="dx2" value="2">
				跳水<input type="checkbox" name="dx2" value="3">
			</td>
			
		</tr>
		<tr>
			<td align="right">城市：</td>
			<td>
				<select name="city" >

					<option value="xz">--请选择--</option>
					<option value="bj">北京</option>
					<option value="tj">天津</option>
					<option value="sh">上海</option>
					<option value="xm">厦门</option>
					<option value="fj">福建</option>
					<option value="sz">深圳</option>

				</select >
				<select name="city">
					<optgroup label="华北">
						<option value="bj">北京</option>
						<option value="tj">天津</option>
						<option value="sh">上海</option>
					</optgroup>
					<optgroup label="华东"> 
						<option value="xm">厦门</option>
						<option value="fj">福建</option>
						<option value="sz">深圳</option>
					</optgroup>
				</select>
			</td>
			
		</tr>
		<tr>
			<td align="right">简介：</td>
			<td><textarea name="jj" id="" cols="30" rows="10" placeholder="请输入个人信息"></textarea>
			</td>
		</tr>
		<tr>
			<td align="center" colspan="2">
				<input type="button" value="来点我" name="button">
				<input type="submit" value="submit" name="submit">
				<input type="reset" value="reset" name="reset">
				
			</td>  
			<td>
				<input type="hidden" name="hidden" value="隐藏按钮">
			</td>
		</tr>
	</table>
</form>
</body>
</html>
```

## S1-4搭建网页结构

### 第二章 必备基础

#### 2-1 div和span标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
<div><img src="image/1.jpg" alt=""></div>
<div><img src="image/2.jpg" alt=""></div>
<div><img src="image/3.jpg" alt=""></div>

<span><img src="image/1.jpg" alt=""></span>
<span><img src="image/2.jpg" alt=""></span>
<span><img src="image/3.jpg" alt=""></span>
</body>
</html>
```

# STEP2 CSS样式

## S2-1 CSS选择的艺术

### 第二章 CSS基础语法

#### 2-1 CSS基础语法

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style type="text/css">
		/*p标签样式*/
		p,h1,h2,h3,h4{font-size:20px}
		p{font-size:20px;color:blue;font-family:隶书;}
		h1{color:red;}
		
	</style>
</head>
<body>
	<h1>css层叠样式表</h1>
	<h2>css层叠样式表</h2>
	<h3>css层叠样式表</h3>
	<h4>css层叠样式表</h4>
	<p>层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。</p>
</body>
</html>
```

#### 2-5 CSS使用方式1

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style type="text/css">
		p{color:skyblue;}
	</style>
</head>
<body>
<h1 style="color:green">CSS样式</h1>
<p>嵌入样式</p>
<p>嵌入样式</p>
<p>嵌入样式</p>
<p>嵌入样式</p>
<p>嵌入样式</p>
</body>
</html>
```

#### 2-9 CSS使用方法2

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
<h1 style="color:green">CSS样式</h1>
<p>嵌入样式</p>
<p>嵌入样式</p>
<p>嵌入样式</p>
<p>嵌入样式</p>
<p>嵌入样式</p>
</body>
</html>`
```

```css
p,h1,h2,h3,h4{font-size:20px}
p{font-size:20px;color:blue;font-family:隶书;}
h1{color:red;}
```

#### 2-14 CSS使用方法优先级(就近原则)

### 第三章 CSS选择器

#### 3-1 选择器1

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		p{color:red;}
		.special{color:blue;}
		p.special{font-size:20px}
		.one{text-decoration:underline;}
	</style>
</head>
<body>
	<h1 class="special">css层叠样式表</h1>
	<p><em>层叠样式表</em>XML（标准通用标记语言的一个子集）等文件样式的计算机语言。</p>
	<p class="special one">CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。</p>
	<p>是一种用来表现HTML（标准通用标记语言的一个应用）</p>
	<div>
		<h1>css层叠样式表</h1>
		<ul>
			<li>CSS1</li>		
			<li>CSS2</li>		
			<li>CSS3</li>		
			<li>CSS4</li>		
		</ul>
		<h1>css选择器</h1>
	</div>
</body>
</html>
```

#### 3-7 ID选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		p{color:red;}
		.special{color:blue;}
		p.special{font-size:20px}
		.one{text-decoration:underline;}
		#p1{color:lightgreen;}
	</style>
</head>
<body>
	<h1 class="special">css层叠样式表</h1>
	<p><em>层叠样式表</em>XML（标准通用标记语言的一个子集）等文件样式的计算机语言。</p>
	<p class="special one">CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。</p>
	<p>是一种用来表现HTML（标准通用标记语言的一个应用）</p>
	<div>
		<h1 id="p1">css层叠样式表</h1>
		<ul>
			<li>CSS1</li>		
			<li>CSS2</li>		
			<li>CSS3</li>		
			<li>CSS4</li>		
		</ul>
		<h1>css选择器</h1>
	</div>
</body>
</html>
```

#### 3-11 群组选择器和全局选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		/*p.special,#three,#p1{font-family:隶书}
		p{color:red;}
		.special{color:blue;}
		p.special{font-size:20px}
		.one{text-decoration:underline;}
		#p1{color:lightgreen;}*/
		*{color:lightblue;}
	</style>
</head>
<body>
	<h1 class="special">css层叠样式表</h1>
	<p><em>层叠样式表</em>XML（标准通用标记语言的一个子集）等文件样式的计算机语言。</p>
	<p class="special one">CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。</p>
	<p>是一种用来表现HTML（标准通用标记语言的一个应用）</p>
	<div>
		<h1 id="p1">css层叠样式表</h1>
		<ul id="three">
			<li>CSS1</li>		
			<li>CSS2</li>		
			<li>CSS3</li>		
			<li>CSS4</li>		
		</ul>
		<h1>css选择器</h1>
	</div>
</body>
</html>
```

#### 3-16 后代选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		/*p.special,#three,#p1{font-family:隶书}
		p{color:red;}
		.special{color:blue;}
		p.special{font-size:20px}
		.one{text-decoration:underline;}
		#p1{color:lightgreen;}*/
/*		 **{color:lightblue;}*/
		.classred{color:orangered;}
		p em{color:royalblue;}
		h1.special em{color:deeppink;}
	</style>
</head>
<body>
	<h1 class="special"><em>css</em>层叠样式表</h1>
	<p><em>层叠样式表</em>XML（标准通用标记语言的一个子集）等文件样式的计算机语言。</p>
	<p class="special one">CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。</p>
	<p>是一种用来表现HTML（标准通用标记语言的一个应用）</p>
	<div>
		<h1 id="p1"><em class="classred">css</em>层叠样式表</h1>
		<ul id="three">
			<li>CSS1</li>		
			<li>CSS2</li>		
			<li>CSS3</li>		
			<li>CSS4</li>	`	
		</ul>
		<h1>css选择器</h1>
	</div>
</body>
</html>
```

#### 3-20 伪类选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		a:link{color:royalblue;}
		a:visited{color:darkgray;}
		a:hover{color:greenyellow;}
		a:active{color:mediumvioletred;}
		p:hover{color:hotpink;}
		p:active{font-size:20px}
	</style>
</head>
<body>
	<a href="https://www.imooc.com/u/index/allcourses">课程链接</a>
	<p>慕课网</p>
</body>
</html>
```

### 第4章 CSS继承,层叠,优先级

#### 4-1 CSS继承和层叠

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
/*		div{font-size:20px;border:1px solid orangered;}*/
/*	body{font-size:12px}*/
		body,table,tr,td{font-size:12px}
	</style>
</head>
<body>
	<div>
		<p>CSS<span>继承</span></p>
		<div>CSS层叠</div>
	</div>
	<p>CSS继承与层叠</p>
	<table border="1px">
		<tr>
			<td>CSS1</td>
			<td>CSS2</td>
		</tr>
	</table>
	<h1>CSS继承与层叠</h1>
</body>
</html>
```

#### 4-4 CSS优先级

#### 4-11 CSS权值

#### 4-16 权值和优先级

! important > 行内样式 > id > class > 标签 > 通配符

## S2-2 CSS文本样式

### 第2章 字体样式

#### 2-1 字体属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		h1{font-family:微软雅黑}
		p{font-family:宋体}
	</style>
</head>
<body>
	<h1>CSS操作</h1>
	<p>css操作</p>
</body>
</html>
```

#### 2-5 字体大小

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
/*		p{font-size:50px}*/
		.larger{font-size:larger;}
		.smaller{font-size:smaller;}
		.em{font-size:2em}
		.percent{font-size:150%}
		#div{font-size:20px}
	</style>
</head>
<body>
	<p>css操作</p>
	<p>css<span class="larger">层叠和判断</span></p>
	<p>python<span class="smaller">分支循环</span></p>
	<div id="fontSize">
		<p>文字大小</p>
		<p class="percent">文字大小<span>相对值%</span></p>
		<p>文字大小<span class="em">相对值em</span></p>
	</div>

</body>
</html>
```

#### 2-8 字体颜色

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		h1{color:indianred;}
		p{color:rgb(0%, 100%, 0%);}
		div{color:#080;}
	</style>
</head>
<body>
	<h1>css基础</h1>
	<p>CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
	<div>CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</div>
</body>
</html>
```

#### 2-11 文字样式(其他)

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		.normal{font-weight:normal;}
		.italic{font-style:italic;}
	</style>
</head>
<body>
	<p><b>字体粗细</b></p>
	<p><strong>字体粗细</strong></p>
	<p class="normal">字体加粗</p>
	<p><em>斜体</em></p>
	<p><i>斜体</i></p>
	<p class="italic">斜体</p>
</body>
</html>
```

#### 2-16 简写font属性（无）

### 第3章 文本样式

#### 3-1 文本对齐方式

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		.text1{text-align:left;}
		.text2{text-align:right;}
		.text3{text-align:center;}
		.text4{text-align:justify;}
	</style>
</head>
<body>
	<p align="left">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
	<p align="right">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
	<p align="center">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
	<p align="justify">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>

	<p class="text1">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
	<p class="text2">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
	<p class="text3">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
	<p class="text4">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
</body>
</html>
```

#### 3-5 行高

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		.text1{text-align:left;line-height:40px;}
		.text2{text-align:right;line-height:2em}
		.text3{text-align:center;}
		.text4{text-align:justify;}
	</style>
</head>
<body>
	<p class="text1">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
	<p class="text2">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
	<p class="text3">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
	<p class="text4">CSS是一种定义样式结构如字体、颜色、位置等样式的语言，被用于为页面添加效果。本步骤主要介绍了CSS的基础语法、选择器、文本、背景、列表、盒子模型、浮动、定位以及网页的布局方式。</p>
</body>
</html>
```

#### 3-10 vertical-align（无）

#### 3-13 文本样式其他属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		.text1{text-decoration:underline;}
		.text2{text-decoration:overline;}
		.text3{text-decoration:line-through;}
		.text4{text-decoration:blink;}
		a{text-decoration: none}
	</style>	
</head>
<body>
	<a href="#">CSS是一种定义样式结构如字体</a>
	<p class="text1">CSS是一种定义样式结构如字体、width=device。</p>
	<p class="text2">CSS 是一种定义样式结构如字体、width=device。</p>
	<p class="text3">CSS是一种定义样式结构如字体、width=device。</p>
	<p class="text4">CSS是一种定义样式结构如字体、width=device。</p>
</body>
</html>
```

###  第4章 样式应用

#### 4-1 文本样式应用

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		P{background-color:#ececec;height:150px;text-align:center;line-height:150px	}
		.text1{font-size:80px;color:#c9394a;font-weight:bold}
		.text2{font-size:40px;color:gray;text-decoration:underline;letter-spacing:5px;vertical-align:15px}
		.text3{font-size:80px;color:gray;font-style:oblique;}
	</style>	
</head>
<body>
	<p><span class="text1">慕课网</span>&nbsp;&nbsp;<span class="text2">只学有用的</span><span class="text3">！</span></p>
</body>
</html>
```

## S2-3 盒子模型

### 第2章 盒子模型的概念

#### 2-1 盒子模型概念（无）

### 第3章 盒子模型属性

#### 3-1 width属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		p{background-color:#ececec;width:400px}
		.text1{max-width:300px}
		.text2{min-width:250px}
	</style>	
</head>
<body>
	<p>盒子模型宽度</p>
	<p class="text1">盒子模型最大宽度</p>
	<p class="text2">盒子模型最小宽度</p>
</body>
</html>
```

#### 3-5 height属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		p{background-color:#ececec;height:200px;float:left;}
		.text1{max-height:300px}
		.text2{min-height:300px}
	</style>	
</head>
<body>
	<p>盒子模型高度</p>
	<p class="text1">盒子模型最大高度</p>
	<p class="text2">盒子模型最小高度</p>
</body>
</html>
```

#### 3-9 width/height对那些元素起作用（无）

#### 3-13 border边框属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		p{background-color:#ececec;height:100px;width:200px;line-height:100px;border-width:10px;border-color:#0099ee;border-style:dotted;}
	</style>	
</head>
<body>
	<p>边框属性</p>
</body>
</html>
```

#### 3-19 padding属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		.text1{width:300px;height:300px;background-color:#acacac;padding-top:20px;}
		.content{width:100px;height:100px;background-color:#ececec;padding:20px 10px}
	</style>	
</head>
<body>
	<div class="text1"><div class="content">padding属性</div></div>
</body>
</html>
```

#### 3-23 margin属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		body,p{margin:0px}
		.text1{width:300px;height:300px;background-color:#acacac;}
		.text2{width:300px;height:300px;background-color:#acacac;}
		.content{width:100px;height:100px;background-color:#ececec;margin:auto}
	</style>	
</head>
<body>
	<div class="text1"><div class="content">margin属性</div></div>
	<div class="text2"><div class="content">margin属性</div></div>
	<p>123</p>
</body>
</html>
```

#### 3-29 盒子模型计算

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
	div{margin:10px;padding:5px;border:1px red solid;width:100px;height:80px ;}
	</style>	
</head>
<body>
	<div>盒子模型计算</div>
</body>
</html>
```

### 第4章 盒子模型应用

#### 4-1 display属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		div,span{background-color:#00aaee;border:1px #666 solid;}
		div{display:inline;font-size:16px;height:30px;width:100px;padding:5px;margin:10px; }
/*		span{display:block;width:100px;height:30px;padding:5px;margin:10px;}
		.text1{font-size:0px}*/
		span{display:none;}	
		a:hover span{display: block;}
	</style>	
</head>
<body>
	<div class="text1">
		<div>display-div</div>
		<div>display-div</div>
		<div>display-div</div>
	</div>
<hr>
	<span>display-span</span>
	<span>display-span</span>
	<span>display-span</span>
	<a href="#">指我······<span>和你捉迷藏</span></a>
</body>
</html>
```

#### 4-6 案例应用

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		body,p,div{margin:0px;padding:0px;font-family:"微软雅黑"}
		.course{width:220px;background-color:#f2f4f6;border:1px #ececec solid;margin:auto;}
		.text1{width:100%;height:90px;background-color:#040a10;padding-top:60px}
		.content{font-size:20px;color:#fff;font-weight:bold;text-align:center;}
		.text2{font-size:14px;border-bottom:1px #d9dde1 solid;margin:0px 15px;padding:10px 5px 5px 5px;line-height:1.5em;}
		.special{border-bottom:none;}
		span{color:#93999f;font-size:12px}
	</style>	
</head>
<body>
	<div class="course">
		<div class="text1">
			<p class="content">前端课程排列</p>
		</div>
		<div class="text2">
			<p>HTML+CSS基础课程</p>
			<span>466660人在学</span>
		</div>
		<div class="text2">
			<p>HTML+CSS基础课程</p>
			<span>466660人在学</span>
		</div>
		<div class="text2 special">
			<p>HTML+CSS基础课程</p>
			<span>466660人在学</span>
		</div>
	</div>
</body>
</html>
```

## S2-4 CSS背景和列表

### 第2章 CSS背景

#### 2-1 background-colour

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		div{width: 300px;
			height: 300px;
/*			background-color: transparent;*/
/*			background-color: red;*/
/*			background-color: #ff0000;*/
			background-color: rgb(255, 0, 0);
/*			padding: 10px;*/
/*			margin: 10px;*/
			border: 20px dotted;
		}
	</style>	
</head>
<body>
	<div>backgroundcolour</div>
</body>
</html>
```

#### 2-4 background-image

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		div{width: 300px;
			height: 300px;
			background-image:url(img/test01.jpg);
/*			padding: 20px;*/
/*			margin: 20px;*/
/*			border: 20px dashed;*/
			background-color:#ff0000;
		}
	</style>	
</head>
<body>
	<div></div>
</body>
</html>
```

#### 2-7 background-repeat

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		div{width: 300px;
			height: 300px;
			background-image:url(img/test01.jpg);
/*			background-repeat: no-repeat;*/
/*			background-repeat: repeat-x;*/
			background-repeat: repeat-y;
			border: 1px solid #ff0000;
		}
	</style>	
</head>
<body>
	<div></div>
</body>
</html>
```

#### 2-10 background-attachment

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		div{width: 300px;
			height: 1500px;
			background-image:url(img/test01.jpg);
			background-repeat: no-repeat;
			border: 1px solid #ff0000;
/*			background-attachment:fixed;*/
			background-attachment:scroll;
		}
	</style>	
</head>
<body>
	<div></div>
</body>
</html>
```

#### 2-11 background-position

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		div{width: 300px;
			height: 1500px;
			background-image:url(img/test01.jpg);
			background-repeat: no-repeat;
			border: 1px solid #ff0000;
/*			background-position:50px 50px;*/
			background-position:center2;
		}
	</style>	
</head>
<body>
	<div></div>
</body>
</html>
```

### 第3章 CSS列表

#### 3-1 list-style-type

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		ul li{
			list-style-type:circle;
		}
	</style>	
</head>
<body>
	<ul>
		<li>家用电器</li>
		<li>电脑</li>
		<li>手机</li>
	</ul>
</body>
</html>
```

#### 3-4 list-style-image（无）

#### 3-6 list-style-position

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		ul li{
			list-style-type:circle;
			list-style-position:outside;
		}
	</style>	
</head>
<body>
	<ul>
		<li>家用电器</li>
		<li>电脑</li>
		<li>手机</li>
	</ul>
</body>
</html>
```

#### 3-9 list-style（无）

## S2-5 float浮动

### 第2章 float属性介绍

#### 2-1 普通流介绍（无）

#### 2-2 浮动的基础知识

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		.container{
			width: 800px;
			height: 600px;
			border: 2px solid red;
		}
		.container img{
			float: left;
		}
	</style>	
</head>
<body>
	<div class="container">
		<img src="./img/test01.jpg">
		<p>
【本期金句】
我国广大科技工作者要以与时俱进的精神、革故鼎新的勇气、坚忍不拔的定力，面向世界科技前沿、面向经济主战场、面向国家重大需求、面向人民生命健康，把握大势、抢占先机，直面问题、迎难而上，肩负起时代赋予的重任，努力实现高水平科技自立自强！
——习近平2021年5月28日在中国科学院第二十次院士大会、中国工程院第十五次院士大会和中国科学技术协会第十次全国代表大会上的讲话
【学习笔记】
科技创新，关键在人才。作为青年科技工作者，要勇于担当，坚定科技报国的决心，为加快实现高水平科技自立自强贡献青春力量，为实现中华民族伟大复兴的中国梦提供科技支撑</p>
	</div>
</body>
</html>
```

#### 2-8 使用浮动产生的问题

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		.container{
			width: 500px;
			height: 500px;
			border: 2px solid #333;
			}	
		.box01{
			width: 100px;
			height: 100px;
			background: blue;
			color: #fff;
			float: left;
		}
		.box02{
			width: 100px;
			height: 100px;
			background: red;
			color: #fff;
			float: left;
		}
		.box03{
			width: 100px;
			height: 100px;
			background: green;
			color: #fff;
			float: left;
		}

	</style>	
</head>
<body>
	<div class="container">
		<div class="box01">111111</div>
		<div class="box02">222222</div>
		<div class="box03">333333</div>
	</div>
</body>
</html>
```

#### 2-10 清除浮动语法

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		.container{
			width: 500px;
			height: 500px;
			border: 2px solid #333;
			}	
		.box01{
			width: 100px;
			height: 100px;
			background: blue;
			color: #fff;
			float: left;
			clear: left;
		}
		.box02{
			width: 100px;
			height: 100px;
			background: red;
			color: #fff;
			float: left;
			clear: left;
		}
		.box03{
			width: 100px;
			height: 100px;
			background: green;
			color: #fff;
			float: left;
		
		}

	</style>	
</head>
<body>
	<div class="container">
		<div class="box01">111111</div>
		<div class="box02">222222</div>
		<div class="box03">333333</div>
	</div>
</body>
</html>
```

#### 2-11 清除浮动的常用方法（无）

#### 2-13 清除浮动的其他方法（无）

### 第3章 实际应用

#### 3-1 float案例演示

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		*{
			margin: 0;
			padding: 0;
		}
		ul{
			list-style:none;
		}
		a{
			text-decoration:none;
		}
		.container{
			width: 1200px;
			margin: 0 auto;
		}
		.header{
			width: 1200px;
			background-color:#ccc;
			overflow: hidden;
			zoom:1;
		}
		.header .logo{
			width: 200px;
			height: 80px;
			float: left;
			margin:0 40px;
		}
		.header .nav{
			padding-right:40px;
			float: right;
			overflow: hidden;
			zoom: 1 ;
		}
		.header .nav li{
			float: left ;
			margin-right:20px;
		}
		.header .nav li a{
			padding:0 20px;
			height: 80px;
			line-height: 80px;
			display: block;
			font-family: "微软雅黑";
			font-size: 16px;
			color: #333;
		}
		.header .nav li a:hover{
			color: #fff;
		}
		.main{
			width: 1200px;
		}
		.main .con{
			width: 1000px;
			height: 500px;
			background:blue;
		}
	</style>		
</head>
<body>
	<div class="container">
		<div class="header">
			<div class="logo">
				<a href="#"><img src="./img/logo.png"></a>
			</div>
			<ul class="nav">
				<li><a href="#">免费课程</a></li>
				<li><a href="#">职业路径</a></li>
				<li><a href="#">实战</a></li>
				<li><a href="#">猿问</a></li>
				<li><a href="#">手记</a></li>
			</ul>
		</div>
		<div class="main">
			<div class="con">content</div>
			<div class="sidebar">sidebar</div>
		</div>
		<div class="footer">footer</div>
	</div>
</body>
</html>
```

## S2-6 CSS定位（position）

### 第2章 position属性详解

#### 2-1 position-static

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .block{
            position: relative;
            top: 10px;
            width: 50px;
            height: 50px;
            line-height: 50px;
            text-align: center;
            border: 2px solid blue;
            box-sizing: border-box;
        }
        .block:nth-child(1){
            border: 2px solid red;
            margin: 30px;
        }
        .block:nth-child(2){
            border: 2px solid green;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div class="block">A</div>
    <div class="block">B</div>
    <div class="block">C</div>
    <div class="block">D</div>
</body>
</html>
```

#### 2-5 position-relative

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .block{
            width: 80px;
            height: 80px;
            line-height: 80px;
            border: 2px solid blue;
            text-align: center;
            float: left;
        }

        .block:nth-child(2){
            position: relative;
            top: 10px;
            left: 10px;
        }
    </style>
</head>
<body>
    <div class="block">A</div>
    <div class="block">B</div>
    <div class="block">C</div>
</body>
</html>
```

#### 2-8 position-adsolute

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .parent{
            position: relative;
            width: 200px;
            height: 150px;
            background: blue;
        }
        .child{

            width: 80px;
            height: 80px;
            background: red;
            position: absolute;
        }
    </style>
<body>
    <div class="parent">
        <div class="child">
            
        </div>
    </div>
</body>
```

#### 2-12 position-fixed

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .block{
            width: 80px;
            height: 80px;
            line-height: 80px;
            text-align: center;
            border: 2px solid black;
        }
        .block:nth-child(1){
            position: absolute;
            top: 10px;
            left: 20px;
        }
        .block:nth-child(2){
             position: fixed;
             top: 10px;
             left: 20px;
         }
    </style>
<body>
    <div class="block">绝对定位</div>
    <div class="block">固定定位</div>
</body>
</html>
```

#### 2-15 position-sticky

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .logo{
            width: 100%;
            height: 50px;
            background-color: gray;
        }
        .nav{
            position: sticky;
            top: 0;
            width: 100%;
            height: 50px;
            background: blue;
            color: #ffffff;
            cursor: pointer;
        }
        .content{
            position: relative;
            height: 150px;
            overflow: scroll;
        }
    </style>
<body>
    <div class="logo">
        想象我是网站头图
    </div>
    <div class="nav">
        想象这里是一堆的 banner | 分享 | 收藏
    </div>
    <div class="content">
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字 
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
        <p>
            假装自己是一段文字
            假装自己是一段文字
        </p>
    </div>
</body>
</html>
```

### 第3章 实际应用

#### 3-1 案例1

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        *{
            margin: 0;
            padding: 0;
        }
        .page{
            width: 100%;
            height: 4043px;
            background: url("./image/page.png") center top no-repeat;
        }
        .nav{
            width: 160px;
            height: 205px;
            position: fixed;
            left: 0;
            top: 50%;
            margin-top: -103px;
            font-family: 'Microsoft YaHei ';
        }
        .nav_li{
            width: 160px;
            height: auto;
            text-align: center;
            line-height: 40px;
            color: #fff;
            background: #333;
            border-bottom: 1px solid #fff;
            font-size: 16px;
            cursor: pointer;
        }
        .tit{
            width: 160px;
            height: 40px;
        }
        .nav_li:hover ul{
            display: block;
        }
        .nav_li ul{
            width: 160px;
            height: auto;
            background: #FFF;
            display: none;
        }
        .nav_li ul li{
            width: 160px;
            height: 40px;
            border-bottom: 1px dashed #666;
            color: #333;
            text-align: center;
            line-height: 40px;
            position: relative;
        }
        .nav_li ul li:hover .list-3{
            display: block;
        }
        .list-3{
            width: 160px;
            height: auto;
            position: absolute;
            left: 160px;
            top: 0px;
            display: none;
        }
        .list-3Dom{
            width: 160px;
            height: 40px;
            line-height: 40px;
            background: #444;
            text-align: center;
            border-bottom: 1px solid #FFF;
            color: #FFF;
        }
    </style>
<body>
    <div class="page">
        <div class="nav">
            <div class="nav_li">
                <div class="tit">标题</div>
                <ul>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
            <div class="nav_li">标题
                <ul>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
            <div class="nav_li">标题
                <ul>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
            <div class="nav_li">标题
                <ul>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                    <li>
                        二级栏目
                        <div class="list-3">
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                            <div class="list-3Dom">
                                三级栏目
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</body>
</html>
```

## S2-7 网页基础布局

### 第2章 基础布局

#### 2-1 经典的行布局

```html
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body{
            margin: 0;
            padding: 0;
            color: #fff;
            text-align: center;
        }
        .container{
            width: 800px;
            height: 200px;
            background: deepskyblue;
            position: absolute;
            top: 50%;
            left: 50%;
            margin-top: -100px;
            margin-left: -400px;
        }
    </style>
<body>
    <div class="container">这是一个页面</div>
</body>
</html>
```

#### 2-5 经典的行布局（2）

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body{
            margin: 0;
            padding: 0;
            text-align: center;
            color: #fff;
            font-size: 16px;
        }
        .header{
            width: 100%;
            height: 50px;
            background: #333;
            margin: 0 auto;
            line-height: 50px;
            position: fixed;
        }
        .banner{
            width: 800px;
            height: 300px;
            line-height: 300px;
            margin: 0 auto;
            background: #30a457;
        }
        .container{
            width: 800px;
            height: 1000px;
            margin: 0 auto;
            background: #4c77f5;
        }
        .footer{
            width: 800px;
            height: 100px;
            line-height: 100px;
            margin: 0 auto;
            background: #333;
        }
    </style>
<body>
    <div class="header">这是网页头部</div>
    <div class="banner">这是网页的banner图</div>
    <div class="container">这是网页内容</div>
    <div class="footer">这是网页底部</div>
</body>
</html>
```

#### 2-8 经典的两列布局

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body{
            margin: 0;
            padding: 0;
            color: #fff;
        }
        .container{
            width: 90%;
            height: 1000px;
            margin: 0 auto;
        }
        .left{
            width: 60%;
            height: 1000px;
            background: #1a5acd;
            float: left;
        }
        .right{
            width: 40%;
            height: 1000px;
            background: #5880f9;
            float: right;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="left">这是网页左侧</div>
        <div class="right">这是网页右侧</div>
    </div>
</body>
</html>
```

#### 2-11 经典的三列布局

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body{
            margin: 0;
            padding: 0;
            color: #fff;
        }
        .container{
            width: 100%;
            margin: 0 auto;
        }
        .left{
            width: 30%;
            height: 1000px;
            background: #67b581;
            float: left;
        }
        .right{
            width: 20%;
            height: 1000px;
            background: #67b581;
            float: right;
        }
        .middle{
            width: 50%;
            height: 1000px;
            background: #175bd8;
            float: left;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="left">这是网页左侧</div>
        <div class="middle">这是网页中部</div>
        <div class="right">这是网页右侧</div>
    </div>
</body>
</html>
```

#### 2-13 混合布局

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body{
            margin: 0;
            padding: 0;
            color: #fff;
            font-size: 16px;
            text-align: center;
        }
        .header{
            width: 100%;
            height: 50px;
            line-height: 50px;
            margin: 0 auto;
            background: #5880f9;
        }
        .banner{
            width: 100%;
            height: 200px;
            background: #8bad91;
            margin: 0 auto;
        }
        .container{
            width: 100%;
            height: 1000px;
            margin: 0 auto;
        }
        .container .left{
            width: 30%;
            height: 1000px;
            float: left;
            background: #67b581;
        }
        .container .right{
            width: 70%;
            height: 1000px;
            float: right;
            background: #d0d0d0;
        }
        .footer{
            width: 100%;
            height: 100px;
            margin: 0 auto;
            line-height: 100px;
            background: #ed817e;
        }
    </style>
</head>
<body>
    <div class="header">这是头</div>
    <div class="banner">这是轮播图</div>
    <div class="container">
        <div class="left">这是左</div>
        <div class="right">这是右</div>
    </div>
    <div class="footer">这是尾</div>
</body>
</html>
```

### 第3章 经典布局（选修）

#### 3-1 圣杯布局案例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        *{
            margin: 0;
            padding: 0;
        }
        body{
            min-width: 700px;
        }
        .header,
        .footer{
            width: 100%;
            height: 40px;
            line-height: 40px;
            text-align: center;
            background: #ddd;
            float: left;
        }
        .container{
            padding: 0 220px 0 200px;
        }
        .middle{
            width: 100%;
            background: #1a5acd;
        }
        .left{
            width: 200px;
            background: #f00;
            margin-left: -100%;
            left: -200px;
        }
        .right{
            width: 220px;
            background: #30a457;
            margin-left: -220px;
            right: -220px;
        }
        .left,
        .middle,
        .right{
            position: relative;
            float: left;
            min-height: 300px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h4>header</h4>

    </div>
    <div class="container">
        <div class="middle">
            <h4>middle</h4>
            <p>这是页面的中间这是页面的中间这是页面的中间这是页面的中间这是页面的中间</p>
        </div>
        <div class="left">
            <h4>left</h4>
            <p>这是左侧</p>
        </div>
        <div class="right">
            <h4>right</h4>
            <p>这是右侧</p>
        </div>
    </div>
    <div class="footer">
        <h4>footer</h4>
    </div>
</body>
</html>
```

#### 3-2 双飞翼布局案例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        *{
            margin: 0;
            padding: 0;
        }
        body{
            min-width: 700px;
        }
        .header,
        .footer{
            float: left;
            width: 100%;
            height: 40px;
            background: #ddd;
            line-height: 40px;
            text-align: center;
        }
        .sub,
        .main,
        .extra{
            float: left;
            min-height: 300px;
        }
        .main{
            width: 100%;
            min-height: 300px;
        }
        .main-inner{
            margin-left: 200px;
            margin-right: 220px;
            background: #30a457;
            min-height: 300px;
        }
        .sub{
            width: 200px;
            background: #f00;
            margin-left: -100%;
        }
        .extra{
            width: 220px;
            background: #1a5acd;
            margin-left: -220px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h4>header</h4>
    </div>
    <div class="main">
        <div class="main-inner">
            <h4>main</h4>
            <p>这是页面的中间这是页面的中间这是页面的中间这是页面的中间这是页面的中间这是页面的中间这是页面的中间</p>
        </div>
    </div>
    <div class="sub">
        <h4>sub</h4>
        <p>这是页面的左侧</p>
    </div>
    <div class="extra">
        <h4>extra</h4>
        <p>这是页面的右侧</p>
    </div>
    <div class="footer">
        <h4>footer</h4>x
    </div>
</body>
</html>
```

## S2-8 网页基础制作

#### 2-1 网页布局

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="css/index.css">
</head>
<body>
    <div class="header">
        <div class="logo">
            <img src="image/logo.png" alt="logo">
        </div>
        <div class="nav">
            <ul><li>首页</li>
                <li>图片</li>
                <li>视频</li>
                <li>手记</li>
            </ul>
        </div>
    </div>
    <div class="main">
        <div class="top">
            <img src="image/1.jpeg" alt="">
        </div>
        <div class="topLayer"></div>
        <div class="topLayer-top">
            <div class="word">MY BEAUTIFUL LIFE</div>
            <button>LOOK MORE &gt;</button>
        </div>
        <div class="middle">
            <div class="m-top">
                <div class="common weibo">
                    <img src="image/weibo.png">
                    <div class="comm">MICROBLOG</div>
                </div>
                <div class="common wechat">
                    <img src="image/weixin.png">
                    <div class="comm">WECHAT</div>
                </div>
                <div class="common qq">
                    <img src="image/QQ.png">
                    <div class="comm">QQ</div>
                </div>
                <div class="clear"></div>
            </div>
            <div class="m-middle">
                "I want to give good things to record down,<br>after the
                recall will be very beautiful"
            </div>
            <div class="m-bottom">

                <div class="m-con">
                    <img src="image/03-01.jpg">
                    <div class="des1">Cool Image</div>
                    <div class="des2">Record the Picture</div>
                </div>
                <div class="m-con">
                    <img src="image/03-02.jpg">
                    <div class="des1">Cool image</div>
                    <div class="des2">Record the Picture</div>
                </div>
                <div class="m-con">
                    <img src="image/03-03.jpg">
                    <div class="des1">Cool image</div>
                    <div class="des2">Record the Picture</div>
                </div>

            </div>
        </div>
        <div class="clear"></div>
        <div class="bottom">
            <div class="content">
                <div class="title">FROM THE PHOTO ALBUM</div>
                <div class="pic-content">
                    <dl>
                        <dt><img src="image/04-01.jpg"></dt>
                        <dd class="word">We must fully implement the Party's education policy, adhere to the people-centered development of education, proactively plan ahead, effectively respond to changes, and strive to explore new situations, accelerate the modernization of education,</dd>
                    </dl>
                    <dl>
                        <dt><img src="image/04-02.jpg"></dt>
                        <dd class="word">cultivate the foundation of people's happiness with the power of education, consolidate the foundation of national prosperity with the power of education, and provide strong support for the comprehensive promotion of the great rejuvenation of the Chinese nation,</dd>
                    </dl>
                </div>
                <div class="clear"></div>
            </div>
        </div>
    </div>
    <div class="footer">
        ™ 2016 imooc.com
    </div>
</body>
</html>
```

```css
*{
    margin: 0;
    padding: 0;
}
.header{
    width: 100%;
    height: 100px;
}
.header img{
    width: 300px;
    height: 85px;
    padding-left: 100px;
    padding-top: 8px;
}
.header .logo{
    float: left;
}
.header .nav{
    float: right;
}
.header .nav ul{
    padding-right: 100px;
}
.header .nav ul li{
    float: left;
    list-style: none;
    width: 80px;
    height: 100px;
    line-height: 100px;
    font-size: 15px;
    font-weight: bolder;
    color: #7D7D7D;
}

.main .top{
    width: 100%;
    height: 600px;
}
.main .top img{
    width: 100%;
    height: 600px;
}
.main .topLayer{
    position: absolute;
    top: 100px;
    width: 100%;
    height: 600px;
    left: 0;
    background: #000;
    opacity: 0.5;
}
.main .topLayer-top{
    width: 500px;
    height: 300px;
    top: 400px;
    position: absolute;
    margin-top: -150px;
    z-index: 2;
    right: 50%;
    margin-right: -250px;
}
.main .topLayer-top .word{
    padding-top: 100px;
    color: #fff;
    font-size: 45px;
    font-weight: bolder;
    text-align: center;
    font-family: "微软雅黑";
}
.main .topLayer-top button{
    width: 200px;
    height: 60px;
    margin-top: 50px;
    color: #fff;
    background: #F5704F;
    font-family: "微软雅黑";
    text-align: center;
    font-weight: bolder;
    font-size: 14px;
    border-radius: 8px;
    clear: both;
    margin-left: 150px;
}
.main .middle{
    width: 1000px;
    margin: 0 auto;
}
.main .middle .m-top .common{
    width: 33.3%;
    float: left;
    padding-top: 50px;
    text-align: center;
}
.main .middle .m-top .common img{
    width: 100px;
    height: 100px;
}
.main .middle .m-top .common .comm{
    font-size: 20px;
    color: #7D7C7F;
    font-weight: bold;
    padding-top: 20px;
}
.main .middle .m-middle{
    font-size: 22px;
    color: #E19796;
    padding-top: 50px;
    font-weight: bold;
    font-style: italic;
    text-align: center;
    padding-bottom: 50px;
}
.clear{
    clear: both;
}
.main .middle .m-bottom .m-con{
    padding: 10px;
    float: left;
    text-align: center;
    font-weight: bold;
    font-size: 20px;
}
.main .middle .m-bottom .m-con img{
    width: 310px;
    height: 260px;
}
.main .middle .m-bottom .m-con .des1{
    color: #7D7D7F;
    padding-top: 20px;
}
.main .middle .m-bottom .m-con .des2{
    color: #BDBDBC;
    padding-top: 10px;
}
.main .bottom{
    background-color: #F9F9F9;
}
.main .bottom .content{
    width: 1000px;
    margin:0 auto;
}
.main .bottom .content .title{
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: #7D7C7F;
    font-family: "微软雅黑";
    padding-top: 50px;
    padding-bottom: 50px;
}
.main .bottom .content .pic-content dl{
    float: left;
    width: 470px;
    margin: 10px 12px;
}
.main .bottom .content .pic-content dl img{
    width: 470px;
    height: 460px;
}
.main .bottom .content .pic-content dl .word{
    padding-top: 20px;
    font-size: 20px;
    font-weight: bold;
    color: #7D7C7F;
    padding-bottom: 50px;
}
.footer{
    width: 100%;
    height: 100px;
    background-color: #292C35;
    color: #ffffff;
    font-size: 15px;
    font-family: "微软雅黑";
    text-align: center;
    line-height: 100px;
}
```

# STEP3 JS基础

## S3-1 JS语法

### 第3章 JS数据类型

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<script>
    // 声明变量
    /*        var name_01;
            name_01="marry";
            var age=18;
            var email="marry@sina.com";*/
    var name_01="marry",age=18,email="marry@sohu.com",address;

    var id="16"

    // console.log(age)

    // console.log(typeof(address))
    // var distance=12.67980;

    // console.log(typeof(distance))

    // console.log(age-"abc")
    // console.log("abc"-age)

    id = Number(id);
    console.log(typeof(id));
    // var topval=parseInt("28px");
    // console.log(topval);

    var c="abc82";
    console.log(parseInt(c));

</script>
</body>
</html>
```

### 第4章 JS的STRING和BOOLEAN类型

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<script>
    var ids=78406;

    var idstr=ids.toString();

    var m;

    var isStudent=true;

    var isChild=false;

    console.log(typeof idstr);
    console.log(String(ids));
    console.log(String(m))

    console.log(typeof(isStudent))

    console.log(typeof(isStudent).toString())

    var x=0;

    console.log(Boolean(x))
</script>
</body>
</html>
```

### 第5章 算数操作符

#### 5-1 算数操作符

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<script>
    var num1=10,
        num2=5,
        num3=++num1+num2,
        x1=20,
        x2=30,
        x3=--x1+x2--;

    console.log(num1*num2)
    // console.log(typeof(num1+num2))
    //     console.log(num3)
    //     console.log(num1)

    console.log(x1)
    console.log(x2)
    console.log(x3)
</script>
</body>
</html>
```

#### 5-9 其他操作符

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var a=10;
        var b=20;
        var str="hello ";
        a+=5;
        str+="world";
        console.log(str);

        var x=10,
            y="10",
            m=15,
            // z=x==y;
            z=x===y,
            // n=y!=m;
            // n=y!=x;
            n=y!==x;
        console.log(n)
        console.log(null==undefined)
        console.log(null===undefined)
        
        var soce=55,
            result=(soce>=60)?"及格":"不及格";
        console.log(result)
    </script>
</body>
</html>
```

### 第6章 JS逻辑操作符

#### 6-1 逻辑与

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var num1=10,
            num2=20,
            num3=30,
            str="welcome",
            bool=true,
            n=null,
            m;
        // console.log(num1<num2 && num2<num3)
        console.log(num1<num2 && num2==num3)
        console.log(str && num3)

        console.log(0 && 88)
        console.log("" && 0 && 30>20)

        console.log(n && num3)
        console.log(33*"abc" && 55)
        console.log(m && true)
    </script> 
</body>
</html>
```

#### 6-6 逻辑或逻辑非

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var m;
        // console.log(55>88 || 33<66);
        // console.log(55!="55" || 88==="88");

        // console.log("hello" || 0);
        console.log(!false)
        console.log(!0)
        console.log(!88)
        console.log(!NaN)
        console.log(!null)

        console.log(!!"")
    </script> 
</body>
</html>
```

## S3-2 JS流程控制语句

### 第1章 JS分支语句

#### 1-1 if语句

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        // var age=15;
        // if(age<18){
        //     alert("您还未成年"); 
        // }
        var age=prompt("请输入您的年龄");
        // console.log(age)
        if(age<18){
            alert("您还未成年");
        }else if(age>=18 && age<=59){
            alert("您可以进入")
        }else{
            alert("您已超出年龄限制");
        }
    </script> 
</body>
</html> 
```

#### 1-5 if嵌套

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var passwd=prompt("请输入您的密码");
        if(passwd.length!=6){
            alert("请输入六位的数字密码");
        }else{
            if(isNaN(passwd)==true){
                alert("密码必须要是数字");
            }else{
                alert("密码设置正确"); 
            }
        }
    </script> 
</body>
</html> 
```

#### 1-9 switch

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var week=new Date().getDay();
        switch(week){
            case 0:
            document.write("今天是星期日")
            break;
            case 1:
            document.write("今天是星期一")
            break;
            case 2:
            document.write("今天是星期二")
            break;
            case 3:
            document.write("今天是星期三")
            break;
            case 4:
            document.write("今天是星期四")
            break;
            case 5:
            document.write("今天是星期五")
            break;
            default:
            document.write("今天是星期六")
        }
    </script>
</body>
</html> 
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var week=new Date().getDay();
        switch(week){
            case 0:
            weekstr="日";
            break;
            case 1:
            weekstr="一";
            break;
            case 2:
            weekstr="二";
            break;
            case 3:
            weekstr="三";
            break;
            case 4:
            weekstr="四";
            break;
            case 5:
            weekstr="五";
            break;
            default:
            weekstr="六";
        }
        document.write("今天是星期"+weekstr)
    </script>
</body>
</html> 
```

### 第二章 JS循环语句

#### 2-1 for语句

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        // for(var i=1;i<=100;i++){
        //     document.write(i + '<br />');
        // }
        for(var i=99;i>=1;i=i-2){
            document.write(i);
        }
        alert(i)
    </script>
</body>
</html> 
```

#### 2-9 for嵌套

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        for(var i=1;i<=3;i++){
            document.write(i + "<br />")
            for(var j=1;j<=5;j++){
                document.write(j + "<br />")
            }
            document.write("<br />")
        }
    </script>
</body>
</html> 
```

#### 2-18 while循环

##### while

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var i=1;
        while(i<=10){
            document.write(i + "<br />")
            i++
        }
    </script>
</body>
</html> 
```

#####  do-while

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var i=1;
        while(i<=10){
            document.write(i + "<br />")
            i++
        }

        var j=1;
        do{
            if(j%2==0){
                console.log(j)
            }
            j++
        }while(j<=10)
        
    </script>
</body>
</html> 
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var i=1;
        while(i<=10){
            document.write(i + "<br />")
            i++
        }

        var j=1;
        do{
            if(j%2==0){
                console.log(j)
            }
            j++
        }while(j<=10)
        
        var sum=0;

        var n = 1;
        do{
            sum = n + sum
            document.write(n + "<br />")
            n++
        }while(n<=100)
        console.log(sum)

        while(n<=100){
            sum+=n;
            n++;
        }
        document.write(sum)
    </script>
</body>
</html> 
```

### 第3章 break及continue语句

#### 3-1 break与contiue

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var num=0;
        for(var i=1;i<10;i++){
            if(i % 5 == 0){
                continue
            }
            num++
        }
        document.write(num)

        for(var s=0, j=1;j<10;j++){
            if(j % 5 == 0){
                // break
                continue
            }
            s+=j
        }
        console.log(s)
    </script>
</body>
</html> 
```

## S3-3 JS函数

### 第1章 JS函数

#### 1-1 函数的定义及调用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        function mySon(){
            alert("我是一个爸爸")
        }
        mySon()

        function add(num1, num2){
            var sum = num1 + num2
            alert(num1 + '和' + num2 + '的和是' + sum)
        }
        add(4, 6)
        add(-1, -9)
    </script>
</body>
</html> 
```

#### 1-7 函数的返回值

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        function add(num1, num2){
            var sum = num1 + num2
            return sum
        }
        console.log(add(4, 6))
        document.write(add(-1, -9))
        alert(add(789, 34))

        function myFunction(arg){
            if(isNaN(arg)) return;
            return arg*2;
        }
        document.write(myFunction("abc"))
    </script>
</body>
</html>
```

#### 1-12 arguments

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        function inner(){
            console.log(arguments.length);
            console.log(arguments[1]);
        }
        function add(num1, num2) {
            arguments[0]=99;
            console.log(num1);
        }
        add(55, 88) 
    </script>
</body>
</html>     
```

#### 1-17 求平均数

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <script>
        function getAvg() {
            console.log(arguments.length)
            var sum = 0;
            for (var i = 0; i < arguments.length; i++) {
                sum += arguments[i]
            }
            return sum / arguments.length
        }
        var avg = getAvg(4, 0, 35);
        console.log(avg)
    </script>
</body>
</html>
```

## S3-4 JS内置函数

### 第2章 JS对象之数组

#### 2-1 Array数组

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <script>
        var colours=new Array(3);
        var nums=new Array(1,3,6,9);
        var cols=["red","yellow","green"]
        console.log(cols[0]);
    </script>
</body>

</html>
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <script>
        var arr=["a","b","c","d"]
        console.log(arr.length)
        for(var i=0;i<arr.length;i++){
            console.log(arr[i])
        }
    </script>
</body> 
</html> 
```

#### 2-13 数组方法

##### push()-unish()-pop()和shift()

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <script>
        // push
        var colours=new Array("red", "green")
        var len=colours.push("blue", "yellow", "black")
        console.log(len)
        // unshift
        var nums=[2, 7, 8, 6]
        var size=nums.unshift(99, 66)
        console.log(size)
        // pop
        var n=nums.pop()
        console.log(n)
        // shift
        var m=colours.shift()
        console.log(colours)
    </script>
</body> 
</html>
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <script>
        // join
        var nums=[2, 4, 5];
        var str=nums.join()
        console.log(str)
        var words=["border", "left", "color"]
        var wordstr=words.join("-")
        console.log(wordstr)
        // reverse
        nums.reverse()
        console.log(nums)
</script>
</body> 
</html>
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    var arr1=["a", "b", "c", "d"],
        arr2=["e", "f", 1, 3],
        arr3;
    // concat
    arr3 = arr1.concat(arr2, ["m", 99, 8]);
    console.log(arr3)
    // slice
    var colors=["red", "green", "blue", "yellow"]
    // var newColors=colors.slice(1, 3)
    var newColors2=colors.slice(-2, 3)
    console.log(newColors2)
    
    var a=[1, "yes", 3],
        b;

    b=new Array();
     for(var i=0;i<a.length;i++){
         b.push(a[i])
    }
    b=[].concat(a)
    b=a.slice(0)
    
    console.log(b)
</script>
</body> 
</html>
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    var arr=["a", "b", "c", "d", "e", "f"]
    // var delArr=arr.splice(2, 2)
    // console.log(delArr)
    
    // var insertArr=arr.splice(3, 0, "m", "n")

    var replaceArr=arr.splice(1, 2, "x", "y", "z")
    // console.log(insertArr)
    console.log(replaceArr)
    console.log(arr)
</script>
</body> 
</html>
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    var nums=[1, 7, 2, 4, 3, 9, 7]
    // var pos=nums.indexOf(7)
    // var pos=nums.lastIndexOf(7)
    // console.log(pos)
    function ArrayIndexOf(arr, value){
        for(var i=0;i<arr.length;i++){
            if(nums[i] === value){
                return i
            }
        
        }
        return -1;
    }
    var pos2=ArrayIndexOf(nums, 4);
    console.log(pos2)
</script>
</body> 
</html>
```

### 第3章 JS对象之String

#### 3-1 String

##### charxAt()-charCodeAt()-indexOf()和lastIndexOf()

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    var str="hello world";
    console.log(str.charCodeAt(4));
    var email="marry@163.com";
    console.log(email.indexOf("@"))
    console.log(email	.lastIndexOf("."))
</script>
</body> 
</html>
```

##### slice()-substring()和substr()

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    var str="hello world"
    console.log(str.slice(7, 10))
    console.log(str.slice(-7, -2));
    console.log(str.substring(-7, 5))
    console.log(str.substr(-5, 4))
</script>
</body> 
</html>
```

##### String综合应用

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    var url="index.txt"
    function getFileFormat(url){
        var num=url.lastIndexOf(".")
        var result=url.slice(num)
        return result;
    }
    var formatName=getFileFormat(url)
    var picFormat=getFileFormat("114514.jpg")
    console.log(formatName)
    console.log(picFormat)
</script>
</body> 
</html>
```

##### split()和replace()

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    // split
    var str="welcome-to-beijing";
    var arr=str.split("-")

    
    console.log(arr)

    function mySplit(str, mark){
        return str.split(mark)
    }
     
    // result = mySplit("2016/03/09", "/")
    result = mySplit("welcome-to-beijing", "-")
    console.log(result)

    // replace
    var tel="103450699643, 01938476746, 1029384756"
    var newTel=tel.replace(",", ";")
    console.log(newTel)
</script>
</body> 
</html>
```

##### toUpperCase()和toLowerCase()

### 第4章 JS之Math对象

#### 4-1 Math对象(min()-max())

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    var min=Math.min(5, -4, 0, 9, 108, -55)
    var max=Math.max(88, 0, 6, 47, 199)
    console.log(min)
    console.log(max)
    var num=189.09
    var int1=Math.ceil(num)
    var int2=Math.floor(num)
    var int3=Math.round(num)
    var nums=-55
    console.log(int3)
    console.log(Math.abs(nums))
</script>
</body> 
</html>
```

#### 4-5 Math对象(random())

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    var random_num=Math.random()
    console.log(random_num)

    function getRandom(m,n){
        var choise=m-n+1
        return Math.floor(Math.random()*choise+n)
    }
    var random01 = getRandom(2, 6)
    var random02 = getRandom(10, 88)
    console.log(random01)
    console.log(random02)
</script>
</body> 
</html>
```

### 第5章 JS之Date对象

#### 5-1 date

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    var today=new Date(),
        year=today.getFullYear(),
        month=today.getMonth() + 1;
        week=today.getDay();
        weeks=["日", "一", "二", "三", "四", "五", "六"]

    // console.log(today);
    // console.log(year);  
    // console.log(month);
    time=year + '年' + month + '月 星期' + weeks[week]
    console.log(time)
</script>
</body> 
</html>
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<script>
    var today=new Date()
    today.setDate(today.getDate() + 50)
    console.log(today.getDay())
</script>
</body> 
</html>
```

## S3-5 JS DOM基础

### 第1章 dom基础

#### 1-1 DOM查找

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div class="box" id="box">
        元素
    </div>
    <ul id="list1">
        <li>前端开发</li>
        <li>服务器端开发</li>
        <li>UI设计</li>
    </ul>
    <ol>
        <li>JS原生</li>
        <li>JS框架</li>
    </ol>
    <script>
        var box=document.getElementById("box")
        console.log(box)
        var lis=document.getElementsByTagName("li")
        console.log(lis.length)
        var lis2=document.getElementById("list1").getElementsByTagName("li")
        console.log(lis2)
    </script>
</body> 
</html>
```

#### 1-8 DOM设置元素样式

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div class="box" id="box">
        元素
    </div>
    <ul id="list1">
        <li>前端开发</li>
        <li>服务器端开发</li>
        <li>UI设计</li>
    </ul>
    <ol>
        <li>JS原生</li>
        <li>JS框架</li>
    </ol>
    <script>
        var box=document.getElementById("box")
        box.style.color="#f00"
        box.style.fontWeight="bold"     
        var lis=document.getElementById("list1").getElementsByTagName("li")
        for(var i=0,len=lis.length;i < len;i++){
            lis[i].style.color="#00f"
            if (i==0) {
                lis[i].style.backgroundColor = "#ccc"
            }else if (i==1) {
                lis[i].style.backgroundColor = "#666"
            }else if (i==2){
                lis[i].style.backgroundColor = "#999"
            }else{
                lis[i].style.backgroundColor = "#333"
            }
        }   
    </script>
</body> 
</html>
```

#### 1-14 DOM(innerHTML和className)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .on{border-bottom:1px soild #0f0}
        .current{background:#ccc;color:#f00}
    </style>
</head>

<body>
    <div class="box" id="box">
        元素
    </div>
    <ul id="list1">
        <li><i>前端开发</i></li>
        <li class="on"><b>服务器端开发</b></li>
        <li>UI设计</li>
    </ul>
    <ol>
        <li>JS原生</li>
        <li>JS框架</li>
    </ol>
    <script>
        var box=document.getElementById("box")
        box.style.color="#f00"
        box.style.fontWeight="bold"     
        var lis=document.getElementById("list1").getElementsByTagName("li")
        for(var i=0,len=lis.length;i < len;i++){
            console.log(lis[i].innerHTML)
            lis[i].innerHTML=lis[i].innerHTML + "程序"
            lis[1].className="current"
        }
        console.log(document.getElementById("box").className);
    </script>
</body> 
</html>
```

#### 1-22 DOM属性设置与获取

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
    </style>
</head>

<body>
    <p id="text" class="text" align="center" data-type="title">文本</p>
    <input type="text" name="user" value="user" id="user">
    <script>   
    var p=document.getElementById("text")
    var user=document.getElementById("user")
    console.log(p.getAttribute("class"))
    console.log(user.type)
    p.setAttribute("data-color", "red")
    p.removeAttribute("align6")
    </script>
</body> 
</html>
```

## S3-6 DOM事件

### 第2章 事件的绑定

#### 2-1 HTML事件

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .btn{width:140px;height:30px;line-height:30px;background:#00f;
        color:#fff;font-size:14px;text-align:center;border-radius:5px;
        cursor:pointer;margin-top:30px;
    }
    </style>
</head>

<body>
    <input type="button" value="弹 出" onclick="alert('我是按钮')">
    <div class="btn" id="btn" onmouseover="mouseoverFn(this, '#f00')" onmouseout="mouseoutFn(this, '#ff0')">开始</div>
    <div class="btn" id="btn" onmouseover="mouseoverFn(this, '#0f0')" onmouseout="mouseoutFn(this, '#333')">结束</div>
    <script>
        function mouseoverFn(btn, bgcolor){
            btn.style.background=bgcolor
        }
        function mouseoutFn(btn, bgcolor) {
            btn.style.background=bgcolor
        }
    </script>
</body> 
</html>
```

#### 2-10 DOM0级事件

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .lock{width:140px;height:30px;line-height:30px;background:#00f;
        color:#fff;font-size:14px;text-align:center;border-radius:5px;
        cursor:pointer;margin-top:30px;}
        .unlock{width:140px;height:30px;line-height:30px;background:#666;
        color:#ccc;font-size:14px;text-align:center;border-radius:5px;
        cursor:pointer;margin-top:30px;}
    </style>
</head>

<body>
    <div class="lock" id="btn">锁定</div>
    <script>
        var btn=document.getElementById("btn")
        btn.onclick=function(){
            if(this.className=='lock'){
                this.className='unlock'
                this.innerHTML="解锁"
            }else{
                this.className='lock'
                this.innerHTML='锁定'
            }
        }
    </script>
</body> 
</html>
```

### 第3章 事件类型

#### 3-1 事件类型(onload)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script>
        window.onload=function(){
            var box = document.getElementById("box")
            var clicked = function () {
                alert('我被闪击了')
            }
            box.onclick = clicked;
        }
    </script>
</head>

<body>
    <div id="box">波兰</div>
</body> 
</html>
```

#### 3-5 事件类型(onfocus和onblur)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .box{
            padding: 50px;
        }
        .left,.tip{
            float: left;
        }
        .left{
            margin-right: 10px;
        }
        .tip{
            display:none;
            font-size: 14px;
        }
        
    </style>
    <script>
        window.onload=function(){
            var phone=document.getElementById("phone"),
                tip=document.getElementById("tip")
            phone.onfocus=function(){
                tip.style.display='block'
            }
            phone.onblur=function(){
                var phoneVal=this.value
                if(phoneVal.length==11 && isNaN(phoneVal)==false){
                    tip.innerHTML='<img src="img/确定.png">'
                }else{
                    tip.innerHTML = '<img src="img/取消.png">'
                }
            }
        }
    </script>
</head>

<body>
    <div class="box">
        <div class="left">
            <input type="text" id="phone" placeholder="请输入手机号码">
        </div>
        <div class="tip" id="tip">
            请输入有效的手机号码
        </div>
    </div>
</body> 
</html>
```

#### 3-10 事件类型(onchange)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script>
        window.onload=init;

        function init() {
            var menu=document.getElementById("menu")

            menu.onchange=function(){
                var bgcolor=this.value
                console.log(bgcolor)

                if(bgcolor=="")return
                document.body.style.background=bgcolor
            }
        }
    </script>
</head>
<body>
    <div class="box">
        请选择您喜欢的背景色： 
        <select name="" id="menu">
            <option value="">请选择</option>
            <option value="#f00">红色</option>
            <option value="#0f0">绿色</option>
            <option value="#00f">蓝色</option>
            <option value="#ff0">黄色</option>
            <option value="#ccc">灰色</option>
        </select>
    </div>
</body> 
</html>
```

#### 3-14 事件类型(onresize和onscroll)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .box{
            width: 200PX;
            height: 2000px;
            background: #f00;
        }
    </style>
</head>
<body>
    <div class="box" id="box">拖动</div>
    <script>
        var box=document.getElementById("box")
        box.onmousedown=function(){
            console.log("我被制裁了")
        }
        box.onmousemove=function(){
            console.log("我在移动")
        }
        box.onmouseup=function(){
            console.log("我复国了")
        }
        box.onclick=function(){
            console.log("我又被制裁了")
        }
        window.onresize=function(){
            console.log("我的尺寸变了")
        }
        window.onscroll=function(){
            console.log("我被拖动了")
        }
    </script>
</body> 
</html>
```

### 第4章 键盘事件

#### 4-1 键盘事件

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .text span{
            font-weight: bold;
            color: #f00;
        }
        em{
            font-style: normal;
        }
    </style>
</head>
<body>
    <div>
        <p class="text">您还可以输入<span><em id="count">30</em></span>/30</p>
        <div class="input">
            <textarea name="" id="text" cols="70" rows="4"></textarea>
        </div>
    </div>
    <script>
        var text=document.getElementById("text")
        var total=30
        var count=document.getElementById("count")
        document.onkeyup=function(){
            var len=text.value.length
            var allow=total-len
            count.innerHTML=allow
        }
    </script>
</body> 
</html>
```

## S3-7 BOM基础

### 第1章 window对象

#### 1-1 window对象(全局对象)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        var age=15;
        function sayAge() {
            alert("我" + age)
        }
        window.username="marry"
        window.sayName = function(){
            alert("我是" + this.username)
        }
        sayAge()
        window.sayName()
    </script>
</body> 
</html>
```

#### 1-4 window对象方法(alert-comfirm-prompt)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="box">
        <span>iphone6s</span>
        <input type="button" value="删除" id="btn">
    </div>
    <script>
        var age=15;
        function sayAge() {
            alert("我" + window.age)
        }
        window.username="marry"
        window.sayName = function(){
            alert("我是" + this.username)
        }
        // sayAge()
        // window.sayName()

        var btn=document.getElementById("btn")
        btn.onclick=function(){

            var result=window.confirm("您确定要删除吗? \n删除后该信息将不可恢复!")
            if(result){
                document.getElementById("box").style.display="none"
            }
        }
        var message=prompt("请输入您的星座", "天蝎座")
        console.log(message)
    </script>
</body> 
</html>
```

#### 1-10 window对象方法(open-close)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
    <title>Document</title>
</head>
<body>
    <input type="button" value="退 出" id="quit">
    <script>
        window.onload=function(){
            window.open("newwindow.html", "newwindow",
                    "width=400px;height=200px,left=0,top=0,toolbar=no,menubar=no,scrollbars=no,location=no,status=no"    
            )
        }
        var quit=document.getElementById("quit")
        quit.onclick=function(){
            window.close()
        }
    </script>
</body> 
</html>
```

#### 1-16 定时器setTimeout

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
    <title>Document</title>
</head>
<body>
    <script>
        var fnCall=function(){
            alert("world")
        }

        // setTimeout('alert("hello")', 2000)
        // setTimeout(function(){
        //     alert("hello")
        // },2000)

        var timeout1=setTimeout(function(){
            alert("hello")
        },2000)

        clearTimeout(timeout1)

        // setTimeout(fnCall, 5000)
    </script>
</body> 
</html>
```

#### 1-22 定时器setInterval

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
    <title>Document</title>
</head>
<body>
    <script>
        // var intervalId=setInterval(function(){
        //     console.log("您好")
        // },1000)

        // setTimeout(function(){
        //     clearInterval(intervalId)
        // }, 10000)

        var num=1,
            max=10,
            timer=null;

        // timer=setInterval(function(){
        //     num++
            // if(num>=max){
            //     clearInterval(timer)
            // }
            // console.log(num)
        //     console.log(num)
        //     num++
        //     if(num>=max){
        //         clearInterval(timer)
        //     }
        // }, 1000)
        function inCreamentNum(){
            console.log(num)
            num++
            if(num<=max){
                setTimeout(inCreamentNum, 1000)
            }else{
                clearTimeout(timer)
            }
        }
        timer=setTimeout(inCreamentNum, 1000)
    </script>
</body> 
</html>
```

### 第2章 location对象

#### 2-1 location对象属性

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
    <title>Document</title>
    <style>
        .box1{
            height: 400px;
            background: #ccc;
        }
        .box2{
            height: 600px;
            background: #666;
        }
    </style>
</head>
<body>
    <div class="box1" id="top"></div>
    <div class="box2"></div>
    <input type="button" id="btn" value="返回顶部">
    <script>
        // console.log(location.href)
        // console.log(location.hash)
        var btn=document.getElementById("btn")
        btn.onclick=function(){
            location.hash="#top"
        }
        console.log(location.pathname)
    </script>
</body> 
</html>
```

#### 2-5 location对象方法

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
    <title>Document</title>
</head>
<body>
    <input type="button" value="刷新" id="reload">
    <script>
        // setTimeout(function(){
             // location.href="newwindow.html"
         //    location.replace("newwindow.html")
        // },1000)
        document.getElementById("reload").oncilck=function(){
            location.reload(true)
        }
    </script>
</body> 
</html>
```

### 第3章 history对象

#### 3-1 history对象方法(无慈悲)

### 第4章 screen对象

#### 4-1 screen对象及属性

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
    <title>Document</title>
</head>
<body>
    <script>
        console.log("页面宽："+screen.availWidth)
        console.log("页面高："+screen.availHeight)

        console.log("pageWidth:"+window.innerWidth)
        console.log("pageHeight:"+window.innerHeight)
    </script>
</body> 
</html>
```

### 第5章 navigator对象及属性

#### 5-1 navigator对象及属性

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
    <title>Document</title>
</head>
<body>
    <script>
        function getBrowser(){
            // var explorer = navigator.userAgent.toLowerCase()
            var explorer = navigator.userAgent.toLowerCase(),browser
            if(explorer.indexOf("msie")>-1){
                browser = "IE"
            }else if(explorer.indexOf("chrome")>-1){
                browser = "chrome"
            }else if(explorer.indexOf("opera")>-1){
                browser = "opera"
            }else if(explorer.indexOf("firefox")>-1){
                browser = "firefox"
            }
            return browser
            // return explorer
        }
        var explorer = getBrowser()
        console.log("您目前使用的是："+explorer+"浏览器")
        // console.log(explorer)
    </script>
</body> 
</html>
```

## S3-8 项目实践

```html
```













