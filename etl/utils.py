#!/usr/bin/python 
#!-*- coding: utf-8 -*-

from datetime import datetime
import time
from datetime import timedelta
import os
import re
import subprocess

def make_datetime(sec):
    if len(str(sec)) == 13:
        sec = int(sec) / 1000
    t = time.localtime(sec)
    return datetime(year = t.tm_year, month = t.tm_mon, day = t.tm_mday, hour = t.tm_hour, minute = t.tm_min, second = t.tm_sec)

def get_time(sec, df='%H:%M:%S'):
    dt = make_datetime(sec)
    return dt.strftime(df)

def writelines(lines, path, mode = 'w'):
    out = open(path, mode)
    for line in lines:
        out.write(str(line).strip() + os.linesep)
    out.close()

def legal_content(content):
    content = content.strip()
    content = re.sub('中国联通[^"]*', '中国联通', content) 
    content = re.sub('中国移动[^"]*', '中国移动', content) 
    content = re.sub('中国电信[^"]*', '中国电信', content) 
    return content

def execute(command, tryrun = False, ret_stdout = False):
    print 'Execute --> %s' % command
    if not tryrun and not ret_stdout:
        return subprocess.call(command, shell=True)
    if not tryrun and ret_stdout:
        return subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

def writelines(lines, path, mode = 'w'):
    out = open(path, mode)
    for line in lines:
        out.write(str(line).strip() + os.linesep)
    out.close()
    
def make_line(items, sep = '\t'):
    cols = []
    for item in items:
        cols.append(str(item))
    return sep.join(cols)

def _lines_to_insertsqls(insert_sql, lines, has_seq = False, batch_size=1000, delimiter = '\t'):
    if not re.match('insert into \w+\([^\(\)]*\) values \(%s\);', insert_sql):
        raise TypeError, "The input insert_sql's format is illegal."
    sqls, insert_values = [], []
    for line in lines:
        line = line.replace('\\', '\\\\')
        line = line.replace('\'', '\\\'')
        items = line.split(delimiter)
        for i in range(len(items)):
            items[i] = '\'%s\'' % str(items[i])
	insert_values.append(','.join(items))
    
    for i in range(int(len(lines) / batch_size) + 1):
        insert_val = '),('.join(insert_values[i * batch_size : (i+1) * batch_size])
	if not insert_val:
	    continue
        sql = insert_sql % insert_val
	if has_seq:
	    sql = sql.replace('\'seq\'', 'seq')
        sqls.append(sql)
    return sqls

def lines_2_insertsqls(table, cols, lines, has_seq = False, batch_size = 1000, delimiter = '\t'):
    lines = dedup_list(lines)
    insert_sql = 'insert into %s(%s) values (%s);' % (table, ','.join(cols), '%s')
    return _lines_to_insertsqls(insert_sql, lines, has_seq, batch_size, delimiter)

def combine_sqlin_format(items):
    cols = []
    for item in items:
        item = str(item)
        col = item.replace('\\', '\\\\').replace('\'', '\\\'')
        col = '\'%s\'' % col 
	cols.append(col)
    return ','.join(cols)

def delete_then_insertsqls(table, cols, lines, key_cols, batch_size=500, has_seq = False, dedup=True, delimiter = '\t'):
    if not cols or not lines: return []
    if dedup:
        lines = dedup_list(lines)
    if type(key_cols) == type(''): key_cols = [key_cols]
    inserts, del_ins, insert_values = [], [], []
    key_indexes = []
    for key_col in key_cols:
        key_indexes.append(cols.index(key_col))
    key_cols = ','.join(key_cols)
    pattern = "delete from %s where (%s) in ((%s));insert into %s(%s) values (%s);" % (table, key_cols, '%s', table, ','.join(cols), '%s')
    for line in lines:
        items = line.split(delimiter)
	insert_values.append(combine_sqlin_format(items))
	del_values = []
	for key_index in key_indexes:
	    del_values.append(items[key_index])
        del_ins.append(combine_sqlin_format(del_values))

    for i in range(int(len(lines) / batch_size) + 1):
        in_str = '),('.join(del_ins[i * batch_size : (i+1) * batch_size])
	if not in_str:
	    continue
        values_str = '),('.join(insert_values[i * batch_size : (i+1)*batch_size])
	insert_sql = pattern % (in_str, values_str)
	if has_seq:
	    insert_sql = insert_sql.replace('\'seq\'', 'seq')
        inserts.append(insert_sql)
    return inserts

def insert_on_duplicates(table, cols, lines, update_keys=None, batch_size=500, dedup=False, delimiter='\t'):
    if not cols or not lines: return []
    if dedup:
        lines = dedup_list(lines)
    pattern = "insert into %s(%s) values (%s) on duplicate key update %s;" % (table, ','.join(cols), '%s', '%s');
    update_cols = update_keys or cols
    update_str = ','.join(['%s=VALUES(%s)' % (col, col) for col in update_cols])
    inserts, insert_values = [], []
    for line in lines:
        items = line.split(delimiter)
        insert_values.append(combine_sqlin_format(items))
    for i in range(int(len(lines) / batch_size) + 1):
        values_str = '),('.join(insert_values[i * batch_size : (i+1)*batch_size])
	insert_sql = pattern % (values_str, update_str)
        inserts.append(insert_sql)
    return inserts    

def dedup_list(lines):
    deduped = []
    for line in lines:
        if line not in deduped:
	    deduped.append(line)
    return deduped

def make_datetime(sec):
    if len(str(sec)) == 13:
        sec = int(sec) / 1000
    t = time.localtime(int(sec))
    return datetime(year = t.tm_year, month = t.tm_mon, day = t.tm_mday, hour = t.tm_hour, minute = t.tm_min, second = t.tm_sec)

def day(sec, df = '%Y-%m-%d'):
    dt = make_datetime(sec)
    return dt.strftime(df)

def first_second_of_day(sec):
    # In sina, "2013-05-10 15:54" means "1368172477000", so here use localtime, not gmtime
    if len(str(sec)) == 13:
        sec = int(sec) / 1000
    t = time.localtime(int(sec))
    dt = datetime(year = t.tm_year, month = t.tm_mon, day = t.tm_mday)
    return int(time.mktime(dt.timetuple())) * 1000

def today(df = '%Y-%m-%d'):
    return str(datetime.now().strftime(df))

def get_datetime(time_str, df = '%Y-%m-%d %H:%M:%S'):
    return datetime.strptime(time_str, df);

def is_before(datestr, baseday=today()):
    return re.sub('-','',datestr) <= re.sub('-', '', baseday)

def yesterday(dt = datetime.now(), df = '%Y-%m-%d'):
    return str((dt - timedelta(days=1)).strftime(df))

def before_datestr(datestr, delta, df='%Y-%m-%d'):
    d = datetime.strptime(datestr, df)
    d = d - timedelta(days=delta)
    return d.strftime(df)

def first_second_of_datestr(datestr):
    if len(datestr) != 8 and len(datestr) != 10:
        raise TypeError, 'Input str\'s length must be 8 or 10, but input is %s.' % datestr
    if len(datestr) == 8:
        return int(time.mktime(time.strptime(datestr, '%Y%m%d'))) * 1000
    if len(datestr) == 10:
        return int(time.mktime(time.strptime(datestr, '%Y-%m-%d'))) * 1000

def make_items_from_sqlout(path, strip_first_line = True):
    items = []
    open_path = open(path)
    lines = open_path.readlines()
    open_path.close()
    if not lines or lines[0].startswith('mysql'):
        return []
    for line in lines[int(strip_first_line):]:
        items.append(line.strip(os.linesep).split('\t'))
    return items

def make_items_from_sql(sql, out_f = None):
    out_path = out_f or 'make_items_from_sql_path.temp'
    out_path = os.path.abspath(out_path)
    execute(db_login + " -e\"%s\" > %s" % (sql, out_path))
    items = make_items_from_sqlout(out_path)
#    if os.path.exists('make_items_from_sql_path.temp'):
#        os.remove('make_items_from_sql_path.temp')
    return items

def make_lines_from_sql(sql):
    items = make_items_from_sql(sql)
    lines = []
    for item in items:
        line = '\t'.join(item)
        lines.append(line)
#    print lines
    return lines

def sub_string_between(s, begin, end):
    if not s or s.strip() == '' or begin not in s or end not in s: return None
    index_begin = s.find(begin)
    index_end = s.find(end, index_begin)
    return s[index_begin+1 : index_end]

def sub_string_after(s, begin, start=0):
    index = s.find(begin, start)
    if index == -1:
        return s
    return s[(index+len(begin)):]

def hadoop_listdir(dir_path, print_list=False):
    hadoop_bin = '%s/bin/hadoop' % constants.HADOOP_HOME
    out = execute('%s fs -ls %s' % (hadoop_bin, dir_path), ret_stdout = True)
    paths = []
    if print_list: print out
    lines = out.split(os.linesep)
    for line in lines[1:]:
        if not line.strip(): continue
        paths.append(line.split()[-1])
    return paths

def make_items_from_hqlout(path, strip_first_line = True):
    items = []
    open_path = open(path)
    lines = open_path.readlines()
    open_path.close()
    if not lines or lines[0].startswith('mysql'):
        return []
    for line in lines[int(strip_first_line):]:
        items.append(line.strip(os.linesep).split('\t'))
    return items

def intersection(colls):
    if colls == None or len(colls) == 0: return set()
    temp_sec = None
    for coll in colls:
        if temp_sec == None:
	    temp_sec = coll 
	else:
	    temp_sec = [item for item in temp_sec if item in coll]
    return set(temp_sec)

def hadoop_put(src, dest, overwrite=False):
    if pydoop.exists(dest):
        pydoop.rm(dest)
    return pydoop.put(src, dest)

def now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S');

def get_agau_day(dt):
    if(dt.hour < 20):
        return yesterday(dt)
    return dt.strftime('%Y-%m-%d')

def get_paper_day(dt):
    return dt.strftime('%Y-%m-%d')

def at_night(dt):
    if dt.hour >= 20 or dt.hour <= 3:
        return True
    return False

def in_morning(dt):
    if dt.hour >= 8 and dt.hour <= 11:
        return True
    return False 

def in_afternoon(dt):
    if dt.hour >= 13 and dt.hour <= 15:
        return True
    return False 

def at_bid_time(dt):
    if dt.hour == 20 or (dt.hour == 13 and dt.minute < 30) or dt.hour == 8:
        return True
    return False

def substract(a, b, default_value=None):
    if a == 0 or b == 0:
        return default_value
    return int (100 * a - b * 100 ) / 100.0

def average(nums):
    s, n = 0, 0
    for num in nums:
        if num == 0: continue
	s += num 
	n += 1
    if n ==0: return 0
    return s / n

def abs_average(nums):
    s, n = 0, 0
    for num in nums:
        if num == 0: continue
	s += abs(num)
	n += 1
    if n ==0: return 0
    return s / n
