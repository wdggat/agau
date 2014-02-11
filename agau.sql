CREATE TABLE IF NOT EXISTS ag_history(
  kind VARCHAR(50) NOT NULL COMMENT '����Ʒ��Ag(T+D)',
  day VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '����',
  open FLOAT NOT NULL COMMENT '���̼�',
  current FLOAT NOT NULL COMMENT '���¼�',
  lastsettle FLOAT NOT NULL COMMENT '�����',
  high FLOAT NOT NULL COMMENT '��߼�',
  low FLOAT NOT NULL COMMENT '��ͼ�',
  close FLOAT NOT NULL COMMENT '���̼�',
  increase FLOAT NOT NULL COMMENT '�ǵ�ֵ',
  increrate FLOAT NOT NULL COMMENT '�ǵ���',
  aveprice FLOAT NOT NULL COMMENT '��Ȩƽ����',
  tradenum FLOAT NOT NULL COMMENT '�ɽ���(ǧ��)',
  tradeamount BIGINT NOT NULL COMMENT '�ɽ����(Ԫ)',
  position INT NOT NULL COMMENT '�ֲ���',
  alternate VARCHAR(50) NOT NULL COMMENT '���շ���'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Ag(T+D)ÿ�������';

CREATE TABLE IF NOT EXISTS au_history(
  kind VARCHAR(50) NOT NULL COMMENT '����Ʒ��Au(T+D)',
  day VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '����',
  open FLOAT NOT NULL COMMENT '���̼�',
  current FLOAT NOT NULL COMMENT '���¼�',
  lastsettle FLOAT NOT NULL COMMENT '�����',
  high FLOAT NOT NULL COMMENT '��߼�',
  low FLOAT NOT NULL COMMENT '��ͼ�',
  close FLOAT NOT NULL COMMENT '���̼�',
  increase FLOAT NOT NULL COMMENT '�ǵ�ֵ',
  increrate FLOAT NOT NULL COMMENT '�ǵ���',
  aveprice FLOAT NOT NULL COMMENT '��Ȩƽ����',
  tradenum FLOAT NOT NULL COMMENT '�ɽ���(ǧ��)',
  tradeamount BIGINT NOT NULL COMMENT '�ɽ����(Ԫ)',
  position INT NOT NULL COMMENT '�ֲ���',
  alternate VARCHAR(50) NOT NULL COMMENT '���շ���'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Au(T+D)ÿ�������';

CREATE TABLE IF NOT EXISTS au9995_history(
  kind VARCHAR(50) NOT NULL COMMENT '����Ʒ��Au99.95',
  day VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '����',
  open FLOAT NOT NULL COMMENT '���̼�',
  current FLOAT NOT NULL COMMENT '���¼�',
  lastsettle FLOAT NOT NULL COMMENT '�����',
  high FLOAT NOT NULL COMMENT '��߼�',
  low FLOAT NOT NULL COMMENT '��ͼ�',
  close FLOAT NOT NULL COMMENT '���̼�',
  increase FLOAT NOT NULL COMMENT '�ǵ�ֵ',
  increrate FLOAT NOT NULL COMMENT '�ǵ���',
  aveprice FLOAT NOT NULL COMMENT '��Ȩƽ����',
  tradenum FLOAT NOT NULL COMMENT '�ɽ���(ǧ��)',
  tradeamount BIGINT NOT NULL COMMENT '�ɽ����(Ԫ)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Au99.95ÿ�������';

CREATE TABLE IF NOT EXISTS au9999_history(
  kind VARCHAR(50) NOT NULL COMMENT '����Ʒ��Au99.99',
  day VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '����',
  open FLOAT NOT NULL COMMENT '���̼�',
  current FLOAT NOT NULL COMMENT '���¼�',
  lastsettle FLOAT NOT NULL COMMENT '�����',
  high FLOAT NOT NULL COMMENT '��߼�',
  low FLOAT NOT NULL COMMENT '��ͼ�',
  close FLOAT NOT NULL COMMENT '���̼�',
  increase FLOAT NOT NULL COMMENT '�ǵ�ֵ',
  increrate FLOAT NOT NULL COMMENT '�ǵ���',
  aveprice FLOAT NOT NULL COMMENT '��Ȩƽ����',
  tradenum FLOAT NOT NULL COMMENT '�ɽ���(ǧ��)',
  tradeamount BIGINT NOT NULL COMMENT '�ɽ����(Ԫ)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Au99.99ÿ�������';

CREATE TABLE IF NOT EXISTS au100g_history(
  kind VARCHAR(50) NOT NULL COMMENT '����Ʒ��Au100g',
  day VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '����',
  open FLOAT NOT NULL COMMENT '���̼�',
  current FLOAT NOT NULL COMMENT '���¼�',
  lastsettle FLOAT NOT NULL COMMENT '�����',
  high FLOAT NOT NULL COMMENT '��߼�',
  low FLOAT NOT NULL COMMENT '��ͼ�',
  close FLOAT NOT NULL COMMENT '���̼�',
  increase FLOAT NOT NULL COMMENT '�ǵ�ֵ',
  increrate FLOAT NOT NULL COMMENT '�ǵ���',
  aveprice FLOAT NOT NULL COMMENT '��Ȩƽ����',
  tradenum FLOAT NOT NULL COMMENT '�ɽ���(ǧ��)',
  tradeamount BIGINT NOT NULL COMMENT '�ɽ����(Ԫ)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Au100gÿ�������';
