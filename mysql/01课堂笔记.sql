-- 数据库的操作

    -- 链接数据库
    -- mysql -u用户名 -p密码
        mysql -uroot -pmysql
        
        mysql -uroot -p


    -- 退出数据库
        exit/quit/ctrl+d


    -- sql语句最后需要有分号;结尾
    -- 显示数据库版本
        -- select后面通常都是有()
        select version();

    -- 显示时间
        select now();
 

    -- 查看所有数据库
    show databases;

 
    -- 创建数据库
    -- create database 数据库名 charset=utf8;
        create database xxx;
        create database school charset=utf8;


    -- 查看创建数据库的语句
    -- show crate database ....
        show create database xxx;
        show create database school; --后面无需加编码语句
    

    -- 查看当前使用的数据库
        select database();

    -- 使用数据库
    -- use 数据库的名字
        use school;
    

    -- 删除数据库
    -- drop database 数据库名;
        drop database xxx;
        


-- 数据表的操作

    -- 查看当前数据库中所有表
         show tables;

    -- 创建表的基本用法
    -- auto_increment表示自动增长
    -- not null 表示不能为空
    -- primary key 表示主键
    -- default 默认值
    -- create table 数据表名字 (字段 类型 约束[, 字段 类型 约束]);
    -- create table students(字段的名字 类型 约束, 字段2的名字 类型 约束);
        create table classes(
            id int unsigned not null auto_increment primary key,
            name varchar(50) not null
        );


    -- 查看表结构
    -- desc 数据表的名字;
        desc classes;
        
    +-------+------------------+------+-----+---------+----------------+
    | Field | Type             | Null | Key | Default | Extra          |
    +-------+------------------+------+-----+---------+----------------+
    | id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
    | name  | varchar(50)      | NO   |     | NULL    |                |
    +-------+------------------+------+-----+---------+----------------+
    2 rows in set (0.01 sec)

    -- 创建students表(id、name、age、high、gender、cls_id)
    create table students(
        id int unsigned not null auto_increment primary key,
        name varchar(50) not null default "张三",
        age tinyint unsigned not null default 18,
        high decimal(5,2) not null,
        gender enum("男", "女", "保密") default "保密", 
        cls_id int unsigned not null
    );
    
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
    insert into classes values(0, "基础班");
    insert into classes values(0, "就业班");
    

    -- 查询classes表中所有的数据
    select * from classes;

    -- 插入一个数据到students表中
    insert into students values(0, "mike", 18, 1.45, "保密", 2);
    
    -- 下面的错误的，"中信"不是枚举中的选项
    insert into students values(0, "yoyo", 18, 1.45, "中信", 2);
    
    -- 枚举可以用数字代替，1->男  2->女
    insert into students values(0, "yoyo", 18, 1.45, 2, 2);
    

    -- 查询students表中的所有数据
    select * from students;

    
    -- 查看表的创建语句
    -- show create table 表名字;
    show create table students;
    

    -- 修改表-添加字段
    -- alter table 表名 add 列名 类型;
    alter table students add birth datetime;

    
    -- 修改表-修改字段：不重命名版
    -- alter table 表名 modify 列名 类型及约束;
    alter table students modify birth date;
    

    -- 修改表-修改字段：重命名版
    -- alter table 表名 change 原名 新名 类型及约束;
    alter table students change birth  birthday date default "2020-01-01";

    

    -- 修改表-删除字段
    -- alter table 表名 drop 列名;
        alter table students drop cls_id;
    
    -- drop database 数据库名;
        drop database xxx;
    
    -- 删除表
    -- drop table 表名
        drop table skill;

    
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
        insert into students values(null, "lily", 22, 178, 2, "1990-01-01");

        
        -- 失败
        -- insert into students values(default, "司马懿", 20, 201.1, "第4性别", "1990-02-01");

        -- 枚举中 的 下标从1 开始 1---“男” 2--->"女"....

        
        -- 部分插入
        -- insert into 表名(列1,...) values(值1,...)
        insert into students(high) values(180.1);


        -- 多行插入
        insert into students(name, high) values("李四", 180.1), ("王五", 1.22);
        
        insert into students values(null, "lily", 22, 178, 2, "1990-01-01"), (null, "yyyy", 22, 178, 2, "1990-01-01");

        

    -- 修改
    -- update 表名 set 列1=值1,列2=值2... where 条件;
        update students set age=30; -- 全部的年龄
        update students set age=18 where id=1;

    
    -- 查询基本使用
        -- 查询所有列
        -- select * from 表名;
        select * from students;
        

        ---定条件查询
        select * from students where id=1;
        select * from students where id>=1 and id<=4;

        
        -- 查询指定列
        -- select 列1,列2,... from 表名;
        
        select id, name from students where id>=1 and id<=4;
        select name, id from students where id>=1 and id<=4;
        

        -- 字段的顺序
        -- 可以使用as为列或表指定别名
        -- select 字段[as 别名] , 字段[as 别名] from 数据表 where ....;
         select name as 姓名, id as 学号 from students where id>=1 and id<=4;

        


    -- 删除
        -- 物理删除
        delete from students where id=6;
    
        

        -- 逻辑删除
        -- 用一个字段来表示 这条信息是否已经不能再使用了
        -- 给students表添加一个is_delete字段 bit 类型
        alter table students add is_delete bit default 0;
        
        update students set is_delete=1 where id=1;
        
        create table xxx(
            id int unsigned not null auto_increment primary key, 
            name varchar(30) default "aaaa"
        )
        
        
        
    
        

        