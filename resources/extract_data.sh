#!/bin/bash

# 日期　开盘　收盘　最高　最低
# cat KLine.html | grep dataCell.cell | grep -o -E "\".*\"" -T | sed -r "s/;dataCell.cell[0-9] = /\t/g" | tr -d \" | uniq

dir=$1
if [[ -z $dir ]];
then
echo "./$0 [DIR]";
exit;
fi

#cat "$dir/*month*/KLine.html" | grep dataCell.cell | grep -o -E "\".*\"" -T | sed -r "s/;dataCell.cell[0-9] = /\t/g" | tr -d \" | uniq > monthly.ag  # FAILED
cat `find $dir -path *month*/KLine.html` | grep dataCell.cell | grep -o -E "\".*\"" -T | sed -r "s/;dataCell.cell[0-9] = /\t/g" | tr -d \" | uniq > monthly.ag
cat `find $dir -path *week*/KLine.html` | grep dataCell.cell | grep -o -E "\".*\"" -T | sed -r "s/;dataCell.cell[0-9] = /\t/g" | tr -d \" | uniq > weekly.ag
cat `find $dir -path *daily*/KLine.html` | grep dataCell.cell | grep -o -E "\".*\"" -T | sed -r "s/;dataCell.cell[0-9] = /\t/g" | tr -d \" | uniq > daily.ag
