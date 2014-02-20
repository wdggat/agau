#Ag(T+D) documentation

    createdAt: 2013-11-10, author: 刘小龙, email: wdggat@163.com

**目标**

1. 作为熟悉perl的练习项目
2. 获得的数据用来实践数据挖掘及各种指标分析思路
3. 了解贵金属投资，关注国际经济大环境

**待办**

1. 拿下工行网银里记录的每天最高最低价和成交量信息
2. 抓取下的dat数据定期上传至网盘或其他网络存储设备

##爬虫部分##

* 爬虫目标地址：http://www.icbc.com.cn/ICBCDynamicSite/Charts/GoldTendencyPicture.aspx
* 使用正则： 
 
        m{<td style=\"[^>]+\">\s+(?<item>[^>]*?)\s+</td>}sig
        ----- 匹配出结果 -----：

        人民币账户黄金  251.43  252.23  251.83  252.42  251.44  
        人民币账户白银  4.18    4.22    4.20    4.21    4.17    
        人民币账户铂金  281.48  283.88  282.68  282.97  282.09  
        人民币账户钯金  147.24  149.64  148.44  148.73  148.14  
        美元账户黄金    1284.50 1287.50 1286.00 1288.98 1283.95 
        美元账户白银    21.36   21.51   21.44   21.51   21.30   
        美元账户铂金    1437.50 1449.50 1443.50 1445.00 1440.50 
        美元账户钯金    752.00  764.00  758.00  759.50  756.50  
        Ag(T+D) 4298.00 -1.19%  1731702 4364.00 4364.00 4392.00 4280.00 2013-11-09 02:30:00     
        Au(T+D) 253.38  -1.50%  19210   257.45  257.34  258.10  253.00  2013-11-09 02:29:55     
        Au100g  255.00  -1.16%  416     258.00  258.01  258.00  253.60  2013-11-09 02:29:59     
        Au99.95 180.77  0.00%   0       0.00    257.42  0.00    0.00    2013-11-09 02:29:59     
        Au99.99 253.90  -1.40%  13570   257.00  257.52  257.94  252.10  2013-11-09 02:29:55

* spider.pl负责抓取网页，cron.pl负责控制哪个时间段抓取什么内容.

##需研究问题##

* 请保证数据至少三个月情况下进行，防止过拟合

### preparation ###

1. 人民币账户白银与Ag(T+D)的价格变动关系，是否纸白银的价格变动会先于Ag(T+D)的变动
2. 每周5出经济数据后，到下次出数据之前，价格变化方向是否唯一，即周5 -> 周4这一区间里价格变动是否单调
    NO
3. 每天的最高价和最低价时间点是否有规律
    extrame_price_reducer.py
4. 每天价格最大波动多少，众数
    grep -e "Ag" ../agau.dat | python extrame_price_reducer => 基本在20以上
5. 出重大经济数据后，市场反应多大(21:29 -> 21:34间变动多大)?
    grep -e "Ag" ../agau.dat | python tipping_point_variations.py > tipping_points.ag  => 变化不大，大多在10以内
6. 第二天的开盘价与第一天的收盘价，一般相差多少? 是否与第一天涨跌方向一致？
    done. => 无关系
7. 连续跌，一般几天，连续涨，一般又会几天？ 
    done. => 貌似无规律
8. 若以开盘价+10卖出开仓，-10价委托平仓（如没达到，当天也必须平仓），盈利如何？ 反之呢？
    => 亏，只有一半的概率中途会回到开盘价
9. 同月份或同季度的价格是否相似？
10. Ag(T+D)一般与哪些价格正相关，与哪些价格负相关？
    正相关： 实物金价，实物银价
    负相关： 美元
11. 上午，下午的涨跌方向是否和当个工作日的晚市一致
    price_alter_direction_reducer.py  => 无关系
12. 上午，下午，晚市的涨跌幅每日各是多少
    grep -e "Ag" ../agau.dat | python price_alter_direction_reducer.py
    => 三个涨幅方向毫无关系
13. 晚市价格有多大的概率在某刻以后还能回到开盘值
    grep -e "Ag" ../agau.dat | python backto_open_reducer.py 
    22:00 => 32/59
    23:00 => 27/59
14. 既然有一半的概率会在22:00以后重新回到开盘价，是否想一个高概率的收益的交易策略呢
15. 想一个策略不必每天交易，只到计算出盈利点时才交易
16. 做个根据金价查询银价的服务，当有Ag价与理论价不符时，报警通知(短信|易信|weibo).如何确定不是金价虚高呢? m
18. 每天　last_close -> night_begin -> night_end -> am_begin -> am_end -> pm_begin -> pm_end,6个区间涨跌方向
    grep -e "Ag" ../agau.dat | python stage_alter_direction.py
    => 6个区间变化方向相互的概率(+=-) (25, 0, 36) | (31, 4, 25) | (28, 0, 32) | (17, 15, 30) (变化为0时取方向相同，am_end -> pm_begin间变化太小，不考虑) | (28, 4, 28)
    => 晚市,上午  　上午,下午    晚市,下午
      (29, 0, 31), (31, 4, 26), (30, 4, 27)
19. 6个时间点价格打印.
    grep -e "Ag" ../agau.dat | python boundary_prices.py
20. 3个竞价时间和3个交易时段，任意排列组合求变化方向
    cat stage_alters.txt | python stage_diraction_relations.py
  =>
    (NIGHT$-^, --AM^): (31, 4, 25)
    (--NIGHT^, NIGHT$-^): (25, 0, 35)
    (--AM^, PM^-$): (24, 3, 33)
    (NIGHT$-^, AM^-$): (29, 0, 31)
    (--PM^, PM^-$): (30, 4, 28)
    (NIGHT$-^, --PM^): (24, 15, 21)
    (--AM^, --PM^): (25, 15, 20)
    (NIGHT$-^, PM^-$): (30, 4, 27)
    (--AM^, AM^-$): (28, 0, 32)
    (--NIGHT^, --PM^): (20, 15, 25)
    (--NIGHT^, PM^-$): (31, 3, 26)
    (--NIGHT^, AM^-$): (32, 0, 28)
    (AM^-$, --PM^): (17, 15, 30)
    (--NIGHT^, --AM^): (24, 4, 32)
    (AM^-$, PM^-$): (32, 4, 26)
21. 分析竞价方向与晚市变动方向在哪个区间内75%相同，或哪个区间内75%不同.
    liu@hzliuxiaolong-hp:~/workspace/agau/etl$ cat stage_alters.ag | python stage_threshold_odds.py
    12	(--AM^, AM^-$): (10, 0, 3)
    13	(--AM^, AM^-$): (9, 0, 2)
    14	(--AM^, AM^-$): (9, 0, 2)
    15	(--AM^, AM^-$): (9, 0, 2)
    16	(--AM^, AM^-$): (8, 0, 2)
    28	(--NIGHT^, AM^-$): (8, 0, 2)

22. 接上20,细分区间(0, 10), [10, 20), [20, 30), [30, 40), [40, 50), [50, ..] (数据较少,不宜参考)
23. 细分晚市各个小时间的变化方向, *貌似是max_min对比更有价值哈*
    grep -e "Ag" ../agau.dat | python hour_alters.py > hour_alters.ag
    grep -e "Ag" ../agau.dat | python hour_extrames.py > hour_extrames.ag 

## Strategy (Must: >=80%) ##
1. 开盘价买, +15卖 or-15卖      ---- N
    grep -e "Ag" ../agau.dat | python deal_fixed_reducer.py 15 => 30/59 成交
    grep -e "Ag" ../agau.dat | python deal_fixed_reducer.py -15 => 29/59 成交
    grep -e "Ag" ../agau.dat | python deal_fixed_reducer.py 12 => 35/59 成交

2. 晚市开市时开仓，以竞价方向相反变动15委托.    ---- N
    grep -e "Ag" ../agau.dat | python deal_opposite_bid.py 20  =>  29/64
    grep -e "Ag" ../agau.dat | python deal_opposite_bid.py 18  =>  33/64
    grep -e "Ag" ../agau.dat | python deal_opposite_bid.py 15  =>  37/64
    grep -e "Ag" ../agau.dat | python deal_opposite_bid.py 13  =>  43/64
    grep -e "Ag" ../agau.dat | python deal_opposite_bid.py 10  =>  50/64
    grep -e "Ag" ../agau.dat | python deal_opposite_bid.py  8  =>  52/64   ---Y

