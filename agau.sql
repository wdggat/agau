CREATE TABLE IF NOT EXISTS ag_history(
  kind VARCHAR(50) NOT NULL COMMENT '交易品种Ag(T+D)',
  day VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '日期',
  open FLOAT NOT NULL COMMENT '开盘价',
  current FLOAT NOT NULL COMMENT '最新价',
  lastsettle FLOAT NOT NULL COMMENT '昨结算',
  high FLOAT NOT NULL COMMENT '最高价',
  low FLOAT NOT NULL COMMENT '最低价',
  close FLOAT NOT NULL COMMENT '收盘价',
  increase FLOAT NOT NULL COMMENT '涨跌值',
  increrate FLOAT NOT NULL COMMENT '涨跌幅',
  aveprice FLOAT NOT NULL COMMENT '加权平均价',
  tradenum FLOAT NOT NULL COMMENT '成交量(千克)',
  tradeamount BIGINT NOT NULL COMMENT '成交金额(元)',
  position INT NOT NULL COMMENT '持仓量',
  alternate VARCHAR(50) NOT NULL COMMENT '交收方向'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Ag(T+D)每日行情表';

CREATE TABLE IF NOT EXISTS au_history(
  kind VARCHAR(50) NOT NULL COMMENT '交易品种Au(T+D)',
  day VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '日期',
  open FLOAT NOT NULL COMMENT '开盘价',
  current FLOAT NOT NULL COMMENT '最新价',
  lastsettle FLOAT NOT NULL COMMENT '昨结算',
  high FLOAT NOT NULL COMMENT '最高价',
  low FLOAT NOT NULL COMMENT '最低价',
  close FLOAT NOT NULL COMMENT '收盘价',
  increase FLOAT NOT NULL COMMENT '涨跌值',
  increrate FLOAT NOT NULL COMMENT '涨跌幅',
  aveprice FLOAT NOT NULL COMMENT '加权平均价',
  tradenum FLOAT NOT NULL COMMENT '成交量(千克)',
  tradeamount BIGINT NOT NULL COMMENT '成交金额(元)',
  position INT NOT NULL COMMENT '持仓量',
  alternate VARCHAR(50) NOT NULL COMMENT '交收方向'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Au(T+D)每日行情表';

CREATE TABLE IF NOT EXISTS au9995_history(
  kind VARCHAR(50) NOT NULL COMMENT '交易品种Au99.95',
  day VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '日期',
  open FLOAT NOT NULL COMMENT '开盘价',
  current FLOAT NOT NULL COMMENT '最新价',
  lastsettle FLOAT NOT NULL COMMENT '昨结算',
  high FLOAT NOT NULL COMMENT '最高价',
  low FLOAT NOT NULL COMMENT '最低价',
  close FLOAT NOT NULL COMMENT '收盘价',
  increase FLOAT NOT NULL COMMENT '涨跌值',
  increrate FLOAT NOT NULL COMMENT '涨跌幅',
  aveprice FLOAT NOT NULL COMMENT '加权平均价',
  tradenum FLOAT NOT NULL COMMENT '成交量(千克)',
  tradeamount BIGINT NOT NULL COMMENT '成交金额(元)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Au99.95每日行情表';

CREATE TABLE IF NOT EXISTS au9999_history(
  kind VARCHAR(50) NOT NULL COMMENT '交易品种Au99.99',
  day VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '日期',
  open FLOAT NOT NULL COMMENT '开盘价',
  current FLOAT NOT NULL COMMENT '最新价',
  lastsettle FLOAT NOT NULL COMMENT '昨结算',
  high FLOAT NOT NULL COMMENT '最高价',
  low FLOAT NOT NULL COMMENT '最低价',
  close FLOAT NOT NULL COMMENT '收盘价',
  increase FLOAT NOT NULL COMMENT '涨跌值',
  increrate FLOAT NOT NULL COMMENT '涨跌幅',
  aveprice FLOAT NOT NULL COMMENT '加权平均价',
  tradenum FLOAT NOT NULL COMMENT '成交量(千克)',
  tradeamount BIGINT NOT NULL COMMENT '成交金额(元)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Au99.99每日行情表';

CREATE TABLE IF NOT EXISTS au100g_history(
  kind VARCHAR(50) NOT NULL COMMENT '交易品种Au100g',
  day VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '日期',
  open FLOAT NOT NULL COMMENT '开盘价',
  current FLOAT NOT NULL COMMENT '最新价',
  lastsettle FLOAT NOT NULL COMMENT '昨结算',
  high FLOAT NOT NULL COMMENT '最高价',
  low FLOAT NOT NULL COMMENT '最低价',
  close FLOAT NOT NULL COMMENT '收盘价',
  increase FLOAT NOT NULL COMMENT '涨跌值',
  increrate FLOAT NOT NULL COMMENT '涨跌幅',
  aveprice FLOAT NOT NULL COMMENT '加权平均价',
  tradenum FLOAT NOT NULL COMMENT '成交量(千克)',
  tradeamount BIGINT NOT NULL COMMENT '成交金额(元)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Au100g每日行情表';
