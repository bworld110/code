# -*- coding:utf-8 -*-

import mysql.connector

config = {
    'user': 'root',
    'password':  '123456',
}
conn = mysql.connector.connect(**config)
curs = conn.cursor()


def create_database():
    sql = 'create database cfs'
    try:
        curs.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def create_bstbl():
    controller = 'create table controller(id int not null auto_increment,sv_tag varchar(20) unique,\
                 pid varchar(20),os_type varchar(20),primary key (id))'
    sv_cmd = 'create table cmd(id int not null auto_increment,pid varchar(20) unique,sv_cmd text,\
             primary key (id))'
    kanban = 'create table kanban(id int not null auto_increment,sv_tag varchar(20),\
             status varchar(10),start_time timestamp, \
             end_time timestamp on update current_timestamp, \
             fail_times int(4) unsigned, \
             primary key (id),\
             unique(sv_tag))'
    logs = 'create table logs(id int not null auto_increment,sv_tag varchar(20),logs longtext,primary key (id),\
           unique(sv_tag))'

    bstbls = [controller, kanban, logs, sv_cmd]
    curs.execute('use cfs')
    for i in bstbls:
        try:
            curs.execute(i)
        except Exception as e:
            print(e)
            conn.rollback()
    conn.commit()


create_database()
create_bstbl()
conn.close()













