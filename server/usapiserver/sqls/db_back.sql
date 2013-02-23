--数据库
CREATE DATABASE if not exists `db_usdb`;
USE `db_usdb`;
/*User 表，用于储存用户资料
	字段列表：
		ID: 用户内部标识
		name: 用户登录用名字
		group: 用户组（区分用户类型）
		pwd: 用户密码
		company: 用户公司id
*/
DROP TABLE if exists `us_user`;
CREATE TABLE `us_user` (
`user_id`  char(8) NOT NULL ,
`user_name`  varchar(12) NOT NULL ,
`user_group`  varchar(20) NOT NULL ,
`user_pwd`  tinytext NOT NULL ,
`comp_name`  varchar(30) NOT NULL ,
`comp_type`  varchar(20) NOT NULL ,
`comp_manager`  char(8) NOT NULL ,
`comp_phone`  int(12) NOT NULL ,
PRIMARY KEY (`user_id`, `user_name`)
);
