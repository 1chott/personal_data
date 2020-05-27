-- 数据库的操作

    -- 链接数据库
	mysql -uroot -pmysql

    -- 退出数据库
       quit/exit/ctrl+D


    -- sql语句最后需要有分号;结尾
    -- 显示数据库版本
	select version();
        

    -- 显示时间
    select now()


    -- 查看所有数据库
	show databases;

 
    -- 创建数据库
	create database school charset=utf8


    -- 查看创建数据库的语句
	show create database school;
    

    -- 查看当前使用的数据库
	select database();


    -- 使用数据库
	use school
    

    -- 删除数据库
	drop database school;
        


-- 数据表的操作

    -- 查看当前数据库中所有表



    -- 创建表的基本用法
    -- auto_increment表示自动增长
    -- not null 表示不能为空
    -- primary key 表示主键
    -- default 默认值




    -- 查看表结构

        
    +-------+------------------+------+-----+---------+----------------+
    | Field | Type             | Null | Key | Default | Extra          |
    +-------+------------------+------+-----+---------+----------------+
    | id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
    | name  | varchar(50)      | NO   |     | NULL    |                |
    +-------+------------------+------+-----+---------+----------------+
    2 rows in set (0.01 sec)

    -- 创建students表(id、name、age、high、gender、cls_id)




    +--------+----------------------------+------+-----+---------+----------------+
| Field  | Type                       | Null | Key | Default | Extra          |
+--------+----------------------------+------+-----+---------+----------------+
| id     | int(10) unsigned           | NO   | PRI | NULL    | auto_increment |
| name   | varchar(50)                | NO   |     | 张三    |                |
| age    | tinyint(3) unsigned        | NO   |     | 18      |                |
| high   | decimal(5,2)               | NO   |     | NULL    |                |
| gender | enum('男','女','保密')     | YES  |     | 保密    |                |
| cls_id | int(10) unsigned           | NO   |     | NULL    |                |
+--------+----------------------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)



    -- 插入一条数据到classes表中

    

    -- 查询classes表中所有的数据



    -- 插入一个数据到students表中

    

    -- 枚举可以用数字代替，1->男  2->女



    -- 查询students表中的所有数据


    
    -- 查看表的创建语句

    

    -- 修改表-添加字段


    
    -- 修改表-修改字段：不重命名版

    


    -- 修改表-修改字段：重命名版


    

    -- 修改表-删除字段

    

    -- drop database 数据库名;


    
    -- 删除表



    
-- 增删改查(curd)

+----------+----------------------------+------+-----+------------+----------------+
| Field    | Type                       | Null | Key | Default    | Extra          |
+----------+----------------------------+------+-----+------------+----------------+
| id       | int(10) unsigned           | NO   | PRI | NULL       | auto_increment |
| name     | varchar(50)                | NO   |     | 张三       |                |
| age      | tinyint(3) unsigned        | NO   |     | 18         |                |
| high     | decimal(5,2)               | NO   |     | NULL       |                |
| gender   | enum('男','女','保密')     | YES  |     | 保密       |                |
| birthday | date                       | YES  |     | 2020-01-01 |                |
+----------+----------------------------+------+-----+------------+----------------+

    -- 增加
        -- 全列插入
        -- insert [into] 表名 values(...)
        -- 主键字段 可以用 0  null   default 来占位
        -- 向classes表中插入 一个班级
        -- 向students表插入 一个学生信息
        -- 全部都要写
       


        
        -- 失败
        -- insert into students values(default, "司马懿", 20, 201.1, "第4性别", "1990-02-01");

        -- 枚举中 的 下标从1 开始 1---“男” 2--->"女"....

        
        -- 部分插入



        -- 多行插入




        

    -- 修改



    
    -- 查询基本使用
        -- 查询所有列

        

        ---定条件查询


        
        -- 查询指定列



        -- 字段的顺序
        -- 可以使用as为列或表指定别名


        


    -- 删除
        -- 物理删除

    
        

        -- 逻辑删除
        -- 用一个字段来表示 这条信息是否已经不能再使用了
        -- 给students表添加一个is_delete字段 bit 类型

        
        
  

-- 查询
    -- 查询所有字段



    -- 查询指定字段


    
    -- 使用 as 给字段起别名

    
    
    -- select 表名.字段 .... from 表名;
    -- 从students表中查询name,age字段，字段使用 数据表名.字段名的方式
    select students.name, students.age from students;
    
    
    -- 可以通过 as 给表起别名
    -- select 别名.字段 .... from 表名 as 别名;
    -- 从students表中查询name,age字段，并且给students表命名为s，字段使用 数据表别名.字段名的方式
    -- 失败的select students.name, students.age from students as s;  -- 已经给数据表起别名后，不能再使用原数据表的名字



    
    -- 消除重复行
    -- 查询students表中所有的不重复的性别



-- 条件查询
    -- 比较运算符

        -- 查询students表中，年龄大于18岁的所有信息
 


        -- 查询students表中，年龄大于18岁的id,name,gender



        -- <
        -- 查询students表中，年龄小于18岁的所有信息



        -- >=
        -- <=
        -- 查询小于或者等于18岁的信息



        -- =
        -- 查询students表中，年龄为18岁的所有学生的信息



        -- != 或者 <>

        
        
        

    -- 逻辑运算符
        -- and
        -- 查询students表中，年龄在18到28之间的所有学生信息



        -- 失败select * from students where age>18 and <28;
        -- 失败select * from students where 18<age<28;

        -- 查询students表中，年龄在18岁以上的所有女性的信息



        -- or
        -- 查询students表中，年龄在18以上或者身高查过180(包含)以上的所有信息




        -- not
        -- 查询students表中，年龄 不在 18岁以上的女性 这个范围内的信息
        -- select * from students where not age>18 and gender=2;


        -- 查询students表中，年龄 不 小于或者等于18 并且 是女性


        
        -- (age<=18 and gender=2) 小于18并且是女性


        
        -- not (age<=18 and gender=2) 只要不是（小于18并且是女性）就要




    -- 模糊查询
        -- 查询students表中，姓名中 以 "小" 开始的名字



        -- 查询students表中，姓名中 有 "小" 所有的名字
  

        
        -- 查询students表中，有2个字的名字



        -- 查询students表中，有3个字的名字

   

        -- 查询students表中，至少有2个字的名字




    -- 范围查询
        -- 查询students表中，年龄为18或者34的姓名




        -- not in 不非连续的范围之内
        -- 查询students表中，年龄不是 18、34岁之间的信息



        -- between ... and ...表示在一个连续的范围内
        -- 查询students表中，年龄在18到34之间的的信息


        
        -- not between ... and ...表示不在一个连续的范围内
        -- 查询students表中，年龄不在在18到34之间的的信息



        -- 失败的select * from students where age not (between 18 and 34);
        


    -- 空判断
        -- 判空is null
        -- 查询students表中，没有填写身高的学生的所有信息




        -- 判非空is not null
        -- 查询students表中，填了了身高的学生的所有信息




-- 排序
    -- order by 字段
    -- asc从小到大排列，即升序
    -- desc从大到小排序，即降序

    -- 查询students表中，年龄在18到34岁之间的男性，按照年龄从小到大排序
    -- select * from students where (age between 18 and 34) and gender=1;




    -- 查询students表中，年龄在18到34岁之间的女性，身高从高到矮排序




    -- order by 多个字段
    -- 查询students表中，年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从小到大排序
    




    -- 查询students表中，年龄在18到34岁之间的女性，身高从高到矮排序, 
    -- 如果身高相同的情况下按照年龄从小到大排序,
    -- 如果年龄也相同那么按照id从大到小排序
    



    
    -- 查询students表中，所有的学生 按照年龄从小到大、身高从高到矮的排序




-- 聚合函数
    -- 总数
    -- count(*)统计列数，count(字段)一样
    -- 查询students表中，男性有多少人，女性有多少人
    -- select * from students where gender=1;





    -- 查询students表中，男性有多少人，女性有多少人，并且将查询出来的人数字段起名为 男/女性人数
    





    -- 最大值
    -- max
    -- 查询students表中，最大的年龄




    -- 查询students表中，女性的最高 身高




    -- 最小值
    -- min

    

    -- 求和
    -- sum
    -- 在students表中，计算所有人的年龄总和



    
    -- 平均值
    -- avg
    -- 在students表中，计算所有的人的平均年龄



    -- 在students表中，计算平均年龄 sum(age)/count(*)



    -- 四舍五入 round(123.23 , 1) 保留1位小数
    -- 在students表中，计算所有人的平均年龄，保留2位小数



    -- 在students表中，计算男性的平均身高 保留2位小数
    -- select name, round(avg(height), 2) from students where gender=1;


-- 分组
    -- group by
    -- 在students表中，按照性别分组,查询所有的性别



    
    -- 失败select * from students group by gender;

    -- 在students表中，计算每种性别中的人数




    -- 在students表中，计算男性的人数




    -- group_concat(...)
    -- 在students表中，查询男性中的姓名





    -- having
    -- 在students表中，按照性别分组，查询平均年龄超过30岁的性别，以及姓名 having avg(age) > 30
    
    select gender, group_concat(age) from students group by gender having avg(age) > 30;

    
    -- 在students表中，查询每种性别中的人数多于2个的信息
    select gender, group_concat(name) from students group by gender having count(*) > 2;
    


        

        
