
-- 创建表
create table checking(
	id int unsigned primary key not null auto_increment,
	balance int unsigned,
	name varchar(50) default "小明"
);

-- 插入数据
insert into checking(balance) values(200);

-- 创建表
create table saving(
	id int unsigned primary key not null auto_increment,
	balance int unsigned,
	name varchar(50) default "小明"
);

-- 插入数据
insert into saving(balance) values(0);



select id, price from goods where name=""%()
name="商务双肩背包" or name="x240 超极本"

(select id, price from goods where name=%s, [name])
"商务双肩背包" or "name= x240 超极本"

"""商务双肩背包" or name= "x240 超极本"""




-- 有个查询结果，这个结果表作为创建视图基础，这个结果中不能出现同名字段
select g.id, g.name, c.name as cate_name, b.name as brand_name, g.price from goods as g inner join goods_brands as b on g.brand_id=b.id inner join goods_cates as c on c.id=g.cate_id;

-- 新建了一个视图，这个视图它是一个虚拟表，这个表字段是原表字段的引用，可以简单理解为软链接
create view v_info as select g.id, g.name, c.name as cate_name, b.name as brand_name, g.price from goods as g inner join goods_brands brands as b on g.brand_id=b.id inner join goods_cates as c on c.id=g.cate_id;

-- 不成文规定，视图主要用于查，尽量不要改

-- 删除视图
drop view v_info;

-- 1) 切换数据库
use mysql;

-- 查看所有用户
select host,user,authentication_string from user;


-- 增加一个用户
-- 在管理员下面操作
-- 创建一个用户老王，只能本地连接数据库，密码为123456，权限：只允许查询京东所有表的权限
grant select on jing_dong1.* to 'laowang'@'localhost' identified by '123456';

-- 查看用户有哪些权限
show grants for laowang@localhost;

-- 创建一个用户，可以任意ip连接，密码为123456，对京东所有表具备所有权限
grant all privileges on jing_dong.* to "leijun"@"%" identified by "123456"

-- 创建一个用户，可以任意ip连接，密码为123456，对所有表具备所有权限
grant all privileges on *.* to "leijun"@"%" identified by "123456";

-- 远程登录
-- 1) 改配置文件
    sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
    # bind-address = 127.0.0.1 前面加一个#注释
  
-- 2) 重启服务器
    sudo service mysql restart
    
-- 3) 添加一个用户，具备相应权限
grant all privileges on *.* to "leijun"@"%" identified by "123456";

-- 4) 刷新，生效
    flush privileges;
    
-- 5) 
   远程登录的客户端和服务器，ip能平通




change master to master_host='192.168.25.115', master_user='slave', master_password='slave',master_log_file='mysql-bin.000008', master_log_pos=590;


















