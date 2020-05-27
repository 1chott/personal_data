-- 数据的准备
    -- 创建一个数据库


    -- 使用一个数据库


    -- 显示使用的当前数据库是哪个?


    -- 创建students表
    -- 字段有id,name,age,height,gender,cls_id,is_delete


    -- 创建classes表
    -- 字段有id,name



-- 查询
    -- 查询所有字段
    -- select * from 表名;

    -- 查询students、classes表中的所有数据
    select * from students;
    select * from classes;


    -- 查询指定字段
    -- select 列1,列2,... from 表名;
    -- 从students表中查询name,age字段
    select name,age from students;

    
    -- 使用 as 给字段起别名
    -- select 字段 as 名字.... from 表名;
    -- 从students表中查询name,age字段，并且将name命名为姓名，将age命名为年龄
    select name as 姓名,age as 年龄 from students;
    
    
    -- select 表名.字段 .... from 表名;
    -- 从students表中查询name,age字段，字段使用 数据表名.字段名的方式
    select students.name, students.age from students;
    
    
    -- 可以通过 as 给表起别名
    -- select 别名.字段 .... from 表名 as 别名;
    -- 从students表中查询name,age字段，并且给students表命名为s，字段使用 数据表别名.字段名的方式
    -- 失败的select students.name, students.age from students as s;  -- 已经给数据表起别名后，不能再使用原数据表的名字
    
    select s.name, s.age from students as s;
    
    -- 消除重复行
    -- distinct 字段
    -- 查询students表中所有的不重复的性别
    select gender from students;
    select distinct gender from students;


-- 条件查询
    -- 比较运算符
        -- select .... from 表名 where .....
        -- >
        -- 查询students表中，年龄大于18岁的所有信息
        select * from students where age>18;


        -- 查询students表中，年龄大于18岁的id,name,gender
        select id,name,gender from students where age>18;


        -- <
        -- 查询students表中，年龄小于18岁的所有信息
        select * from students where age<18;


        -- >=
        -- <=
        -- 查询小于或者等于18岁的信息
        select * from students where age>=18;

        -- =
        -- 查询students表中，年龄为18岁的所有学生的信息
        select * from students where age=18;


        -- != 或者 <>
        select * from students where age!=18;
        
        
        

    -- 逻辑运算符
        -- and
        -- 查询students表中，年龄在18到28之间的所有学生信息
        select * from students where age >=18 and age <= 28;

        -- 失败select * from students where age>18 and <28;
        -- 失败select * from students where 18<age<28;

        -- 查询students表中，年龄在18岁以上的所有女性的信息

        -- or
        -- 查询students表中，年龄在18以上或者身高查过180(包含)以上的所有信息
        select * from students where age >=18 or height >= 180;

        -- not
        -- 查询students表中，年龄 不在 18岁以上的女性 这个范围内的信息
        -- select * from students where not age>18 and gender=2;


        -- 查询students表中，年龄 不 小于或者等于18 并且 是女性
        select * from students where not age<=18 and gender=2;
        
        -- (age<=18 and gender=2) 小于18并且是女性
        select * from students where age<=18 and gender=2;
        
        -- not (age<=18 and gender=2) 只要不是（小于18并且是女性）就要
        select * from students where not (age<=18 and gender=2);


    -- 模糊查询
        -- like 
        -- % 替换0个或者多个
        -- _ 替换1个
        -- 查询students表中，姓名中 以 "小" 开始的名字
        select * from students where name like "小%";
        select * from students where name like "%杰";


        -- 查询students表中，姓名中 有 "小" 所有的名字
        select * from students where name like "%小%";
        
        -- 查询students表中，有2个字的名字
        select * from students where name like "__";


        -- 查询students表中，有3个字的名字
        select * from students where name like "___";
   

        -- 查询students表中，至少有2个字的名字
         select * from students where name like "%__%";



    -- 范围查询
        -- in (1, 3, 8)表示在一个非连续的范围内
        -- 查询students表中，年龄为18或者34的姓名
        select name,age from students where age in (18, 34);


        -- not in 不非连续的范围之内
        -- 查询students表中，年龄不是 18、34岁之间的信息
        select name,age from students where age not in (18, 34);

        -- between ... and ...表示在一个连续的范围内
        -- 查询students表中，年龄在18到34之间的的信息
        select name,age from students where age between 18 and 34;
        select name,age from students where age >=18 and age <=34;

        
        -- not between ... and ...表示不在一个连续的范围内
        -- 查询students表中，年龄不在在18到34之间的的信息
        select name,age from students where age not between 18 and 34;

        -- 失败的select * from students where age not (between 18 and 34);
        


    -- 空判断
        -- 判空is null
        -- 查询students表中，没有填写身高的学生的所有信息
        select * from students where height is null;


        -- 判非空is not null
        -- 查询students表中，填了了身高的学生的所有信息
        select * from students where height is not null;


-- 排序
    -- order by 字段
    -- asc从小到大排列，即升序
    -- desc从大到小排序，即降序

    -- 查询students表中，年龄在18到34岁之间的男性，按照年龄从小到大排序
    -- select * from students where (age between 18 and 34) and gender=1;
    
    select * from students where (age between 18 and 34) and gender=1 order by age;
    
    select * from students where (age between 18 and 34) and gender=1 order by age asc; -- 和上面的等价的


    -- 查询students表中，年龄在18到34岁之间的女性，身高从高到矮排序
    select * from students where (age between 18 and 34) and gender=2 order by height desc;


    -- order by 多个字段
    -- 查询students表中，年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从小到大排序
    
     update students set age=22 where id=1;
    
      select * from students where (age between 18 and 34) and gender=2 order by height desc, age asc;


    -- 查询students表中，年龄在18到34岁之间的女性，身高从高到矮排序, 
    -- 如果身高相同的情况下按照年龄从小到大排序,
    -- 如果年龄也相同那么按照id从大到小排序
    
      select * from students order by height desc, age asc, id desc;

    
    -- 查询students表中，所有的学生 按照年龄从小到大、身高从高到矮的排序
     select * from students order by age asc, height desc;


-- 聚合函数
    -- 总数
    -- count(*)统计列数，count(字段)一样
    -- 查询students表中，男性有多少人，女性有多少人
    -- select * from students where gender=1;
    select count(*) from students where gender=1;
    select count(*) from students where gender=2;

    -- 查询students表中，男性有多少人，女性有多少人，并且将查询出来的人数字段起名为 男/女性人数
    
    select count(*) as "男性" from students where gender=1;
    select count(*) as "女性" from students where gender=2;
    
    select * from students where gender=1 or gender=2;


    -- 最大值
    -- max
    -- 查询students表中，最大的年龄
    select max(age) from students;


    -- 查询students表中，女性的最高 身高
    select max(height) from students where gender=2;

    -- 最小值
    -- min

    
    -- 求和
    -- sum
    -- 在students表中，计算所有人的年龄总和
    select sum(age) from students;
    
    -- 平均值
    -- avg
    -- 在students表中，计算所有的人的平均年龄
    select sum(age)/14 from students;


    -- 在students表中，计算平均年龄 sum(age)/count(*)
    select sum(age)/count(*) from students;
    select avg(age) from students;


    -- 四舍五入 round(123.23 , 1) 保留1位小数
    -- 在students表中，计算所有人的平均年龄，保留2位小数
    select round(avg(age), 2) from students;

    -- 在students表中，计算男性的平均身高 保留2位小数
    -- select name, round(avg(height), 2) from students where gender=1;


-- 分组
    -- group by
    -- 在students表中，按照性别分组,查询所有的性别
    select gender from students group by gender;
    
    -- 失败select * from students group by gender;

    -- 在students表中，计算每种性别中的人数
    select gender, count(*) from students group by gender;

    -- 在students表中，计算男性的人数
    select gender, count(*) from students where gender=1 or gender=2 group by gender;

    -- group_concat(...)
    -- 在students表中，查询男性中的姓名
    select gender, group_concat(name) from students group by gender;
    select gender, group_concat(name, id) from students group by gender;
    select gender, group_concat(name, "%", id) from students group by gender;


    -- having
    -- 在students表中，按照性别分组，查询平均年龄超过30岁的性别，以及姓名 having avg(age) > 30
    
    select gender, group_concat(age) from students group by gender having avg(age) > 30;

    
    -- 在students表中，查询每种性别中的人数多于2个的信息
    select gender, group_concat(name) from students group by gender having count(*) > 2;
    
    select gender, count(*) from students group by gender with rollup;
    

-- 分页
    -- limit start, count
    
    -- 从第0行开始查，每次显示3个
    -- 这里的0就是现实中的1，列表的下标，索引
    select * from students limit 3;
    select * from students limit 0, 3;
    
    -- 分页显示，每页显示3个                   
    -- (第几页-1)*每一页显示的个数，每一页显示的个数
    -- 显示第10页，每页显示5个，   (10-1)*5, 5
    select * from students limit 0, 3; --第1页，  (1-1)*3, 3
    select * from students limit 3, 3; --第2页，  (2-1)*3, 3
    select * from students limit 6, 3; --第3页，  (3-1)*3, 3
    select * from students limit 9, 3; --第4页，  (4-1)*3, 3
    select * from students limit 12, 3; --第5页，  (5-1)*3, 3

    -- 在students表中，限制查询出来的男性信息个数为2
    select * from students where gender=1 limit 0, 2;


    -- 在students表中，查询前5个数据
    select * from students limit 0, 5;


    -- 在students表中，查询id6-10（包含）的信息
    select * from students limit 5, 5;


    -- 在students表中，每页显示2个，第1个页面 (1-1)*2
    select * from students limit 0, 2


    -- 在students表中，每页显示2个，第2个页面 (2-1)*2
    select * from students limit 2, 2


    -- 在students表中，每页显示2个，第3个页面 (3-1)*2
    select * from students limit 4, 2

    
    -- 在students表中，每页显示2个，第4个页面
    -- select * from students limit 6,2; -- -----> limit (第N页-1)*每个的个数, 每页的个数;

    -- 在students表中，每页显示2个，显示第6页的信息, 按照年龄从小到大排序
    -- 失败select * from students limit 2*(6-1),2;
    -- 失败select * from students limit 10,2 order by age asc;


    -- 在students表中，查询女性信息 并且按照身高从高到矮排序 只显示前2个
    select * from students where gender=2 order by height desc limit 0, 2

    
-- 连接查询
    -- inner join ... on

    -- select ... from 表A inner join 表B;
    
    
    select * from students inner join classes on students.cls_id=classes.id;
    select * from students as s inner join classes as c on s.cls_id=c.id;
    select s.*, c.name from students as s inner join classes as c on s.cls_id=c.id;
    select s.id,s.name,s.age,s.height,s.gender, c.name from students as s inner join classes as c on s.cls_id=c.id;

    -- 查询 有能够对应班级的学生以及班级信息
    select * from students inner join classes on students.cls_id=classes.id;


    -- 按照要求显示姓名、班级
    select s.name, c.name from students as s inner join classes as c on s.cls_id=c.id;


    -- 给数据表起名字


    -- 查询 有能够对应班级的学生以及班级信息，显示学生的所有信息，只显示班级名称
    select s.*, c.name from students as s inner join classes as c on s.cls_id=c.id;

    
    -- 在以上的查询中，将班级姓名显示在第1列
    select c.name, s.*from students as s inner join classes as c on s.cls_id=c.id;


    -- 查询 有能够对应班级的学生以及班级信息, 按照班级进行排序
    -- select c.xxx s.xxx from student as s inner join clssses as c on .... order by ....;
    select c.name, s.*from students as s inner join classes as c on s.cls_id=c.id order by c.id;


    -- 当是同一个班级的时候，按照学生的id进行从小到大排序
     select c.name, s.*from students as s inner join classes as c on s.cls_id=c.id order by c.id, s.id;


    -- left join
    -- 查询每位学生对应的班级信息
    select * from students left join classes on students.cls_id=classes.id;


    -- 查询没有对应班级信息的学生
    -- select ... from xxx as s left join xxx as c on..... where .....
    -- select ... from xxx as s left join xxx as c on..... having .....
    
    select * from students left join classes on students.cls_id=classes.id where classes.id is null;


    -- right join   on
    -- 将数据表名字互换位置，用left join完成

-- 自关联
    -- 省级联动 url:http://demo.lanrenzhijia.com/2014/city0605/

    -- 查询所有省份
    select * from areas where pid is null;
    select count(*) from areas where pid is null;

    -- 查询出广东省有哪些市
    
    select * from areas as p inner join areas as c on c.pid=p.aid where p.atitle="广东省";
    select p.atitle,c.atitle from areas as p inner join areas as c on c.pid=p.aid where p.atitle="广东省";


    -- 查询出深圳市有哪些区
    select p.atitle,c.atitle from areas as p inner join areas as c on c.pid=p.aid where p.atitle="深圳市";



-- 子查询
    select max(age) from students;
    
    select * from students where age=(select max(age) from students);


    -- 标量子查询
    -- 查询出高于平均身高的信息
    select * from students where height>(select avg(height) from students);

    -- 查询最高的男生信息
    select * from students where ( height=(select max(height) from students) ) and gender=1;


    -- 列级子查询
    -- 查询学生的班级号能够对应的学生信息
    -- select * from students where cls_id in (select id from classes);
    
    
    select * from students where (age, height)=(22, 180);
    select * from students where age=22 and height=180;












