#coding=utf-8
import time
import random
from nose.tools import *
import funcode_dict, msgbus_h as msgbus
from common_pb2 import MessageHead
from Trade_pb2 import MMTradeProto
from protobuf import assert_equal

bus_ip, bus_port, vhost, username, password = '192.168.31.160', 5679, 'TAS2', 'guest', 'guest'


def clear_queue(conn):
    conn.clear_queue_after_tests('testmoney_rsp', 1.0)


def setup():
    global conn
    conn = msgbus.Connection(bus_ip, bus_port, vhost, username, password, funcode_dict.funcode_dict)
    conn.bind_queue('entry', 'testmoney_rsp', routing_key='money_rsp')
    clear_queue(conn)
    print 'setup() complete'

def teardown():
    msgbus.close_all()
    print 'teardown() complete'


def before_each():
    global request_id, order_id, trade_day
    t = time.time()
    i = int(t*1000)-1450000000000  # 66.9天内不重复
    request_id = i
    order_id = i
    tm = time.localtime(t)
    trade_day = '%04d%02d%02d'%(tm.tm_year, tm.tm_mon, tm.tm_mday)


"""message MMTradeProto {
    required MessageHead Header = 1;       // 消息头
    optional int64 OrderID = 2;                 // 单号
    optional int64 OperateID = 3;               // 操作员ID
    optional int64 AccountID = 4;               // 资金账户ID
    optional int64 MatchID = 5;                 // 对手资金账户ID
    optional int32 GoodsID = 6;                  // 商品ID
    optional double Qty = 7;                    // 数量
    optional double Price = 8;                  // 价格
    optional int32 BuyOrSell = 9;               // 买卖方向
    optional int32 OrderType = 10;               // 订单类型
    optional int32 BuildType = 11;               // 下单类型, 建仓，平仓

    repeated MMCloseDetail CloseDetails = 12;   // 平仓明细

    optional int32 RetCode = 13;                // 返回码
    optional int64 MoneyTicket = 14;           // 资金流水号

    optional double FreezeMargin = 15;          // 冻结金额
    optional double UnfreezeMargin = 16;        // [解冻|建仓]解冻保证金
    optional double UsedMargin = 17;            // [建仓|平仓释放]占用保证金
    optional double OpenCharge = 18;            // 建仓手续费
    optional double CloseCharge = 19;           // 平仓手续费
    optional double WarehouseCharge = 20;       // [建仓|平仓]仓单服务费
    optional double TradeAmount = 21;           // [建仓|平仓释放]成交金额
    optional double ClosePL = 22;               // 平仓盈亏

    optional string TradeDate = 23;             // 交易日
    optional string TradeTime = 24;             // 发送时间
    optional int32 SettleStatus = 25;           // 结算状态
}"""


@nottest
def test_unfreeze_some_account():
    #解冻请求: 交易日, 被撤单委托单号, 操作员ID, 资金账户ID, 请求解冻数量
    unfreeze_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = 1, #optional int64 OrderID = 2;                 // 单号
        AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        Qty = 12.34, #optional double Qty = 7;                    // 数量
        TradeDate = '20160215', #optional string TradeDate = 23;             // 交易日
    )
    conn.publish('entry', 'money_req', 3, 0, unfreeze_req)
    funcode, session_id, rsp_data = conn.get('testmoney_rsp', 1.0)
    print 'funcode=', funcode, 'session_id=', session_id
    print rsp_data


@with_setup(before_each, None)
def test_smallest_freeze_req():
    #冻结保证金请求: 资金账户ID, 操作员ID, 商品ID, 买卖方向, 数量, 价格, 交易日, 委托单号, 单据类型, 商品所在市场ID
    freeze_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = order_id,
        AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
    )
    conn.publish('entry', 'money_req', 1, 0, freeze_req)
    rsp_data = conn.expect('testmoney_rsp', 2, 0, 1.0)
    eq_(0, rsp_data.Header.RequestID)
    eq_(order_id, rsp_data.OrderID)
    eq_(0, rsp_data.RetCode)


@with_setup(before_each, None)
def test_freeze_req_without_order_id():
    #冻结保证金请求: 资金账户ID, 操作员ID, 商品ID, 买卖方向, 数量, 价格, 交易日, 委托单号, 单据类型, 商品所在市场ID
    freeze_req = MMTradeProto(
        Header = MessageHead(),
        AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
    )
    conn.publish('entry', 'money_req', 1, 0, freeze_req)
    print 'freeze_req sent, funcode=%d, session_id=%d'%(1, 0)
    print freeze_req

    rsp_data = conn.expect('testmoney_rsp', 2, 0, 1.0)
    eq_(0, rsp_data.Header.RequestID)
    eq_(order_id, rsp_data.OrderID)
    assert_not_equal(0, rsp_data.RetCode)


@with_setup(before_each, None)
def test_repeat_freeze_req():
    #冻结保证金请求: 资金账户ID, 操作员ID, 商品ID, 买卖方向, 数量, 价格, 交易日, 委托单号, 单据类型, 商品所在市场ID
    freeze_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = order_id,
        AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
        Qty = 12.34, #optional double Qty = 7;                    // 数量
        Price = 12.34, #optional double Price = 8;                  // 价格
        BuyOrSell = 1, #optional int32 BuyOrSell = 9;               // 买卖方向
        TradeDate = trade_day, #optional string TradeDate = 23;             // 交易日 YYYYMMDDhh24mmss
        OrderType = 100, #optional int32 OrderType = 10;               // 订单类型, 做市/竞价/拍卖/挂牌
        BuildType = 0, #optional int32 BuildType = 11;               // 下单类型, 建仓，平仓
    )
    conn.publish('entry', 'money_req', 1, 0, freeze_req)
    rsp_data = conn.expect('testmoney_rsp', 2, 0, 1.0)
    eq_(0, rsp_data.RetCode)
    eq_(2, rsp_data.Header.FunCode)

    conn.publish('entry', 'money_req', 1, 0, freeze_req)
    funcode, sessid, rsp_data = conn.get('testmoney_rsp', 1.0)
    #eq_(0, rsp_data.RetCode)
    #eq_(2, rsp_data.Header.FunCode)

    unfreeze_req = MMTradeProto(
        Header = MessageHead(RequestID=request_id),
        OrderID = order_id, #optional int64 OrderID = 2;    // 单号
        AccountID = 8888, #optional int64 AccountID = 4;    // 资金账户ID
        TradeDate = trade_day, #optional string TradeDate = 23;    // 交易日
    )
    conn.publish('entry', 'money_req', 3, 0, unfreeze_req)
    rsp_data = conn.expect('testmoney_rsp', 4, 0, 1.0)
    eq_(0, rsp_data.RetCode)
    eq_(4, rsp_data.Header.FunCode)


@with_setup(before_each, None)
def test_freeze_req_without_account_id():
    #冻结保证金请求: 资金账户ID, 操作员ID, 商品ID, 买卖方向, 数量, 价格, 交易日, 委托单号, 单据类型, 商品所在市场ID
    freeze_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = order_id,
        #AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
    )
    conn.publish('entry', 'money_req', 1, 0, freeze_req)
    with assert_raises(msgbus.Timeout):
        funcode, sessid, rsp_data = conn.get('testmoney_rsp', 1.0)


@with_setup(before_each, None)
def test_freeze_req_with_invalid_account_id():
    #冻结保证金请求: 资金账户ID, 操作员ID, 商品ID, 买卖方向, 数量, 价格, 交易日, 委托单号, 单据类型, 商品所在市场ID
    freeze_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = order_id,
        AccountID = 6666, #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
    )
    conn.publish('entry', 'money_req', 1, 0, freeze_req)
    with assert_raises(msgbus.Timeout):
        funcode, sessid, rsp_data = conn.get('testmoney_rsp', 1.0)


@with_setup(before_each, None)
def test_freeze_req_with_invalid_goods_id():
    #冻结保证金请求: 资金账户ID, 操作员ID, 商品ID, 买卖方向, 数量, 价格, 交易日, 委托单号, 单据类型, 商品所在市场ID
    freeze_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = order_id,
        AccountID = 8888,
        GoodsID = 6666,
    )
    conn.publish('entry', 'money_req', 1, 0, freeze_req)
    rsp_data = conn.expect('testmoney_rsp', 2, 0, 1.0)
    eq_(2, rsp_data.Header.FunCode)
    eq_(order_id, rsp_data.OrderID)
    eq_(16012, rsp_data.RetCode)


@with_setup(before_each, None)
def test_unfreeze_invalid_order_id():
    unfreeze_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = order_id,
        AccountID = 8888,
    )
    conn.publish('entry', 'money_req', 3, 0, unfreeze_req)
    print 'unfreeze_req sent, funcode=%d, session_id=%d, req='%(3, 0)
    print unfreeze_req

    rsp_data = conn.expect('testmoney_rsp', 4, 0, 1.0)
    eq_(4, rsp_data.Header.FunCode)
    eq_(4020, rsp_data.RetCode)


@with_setup(before_each, None)
def test_freeze_req_without_goods_id():
    #冻结保证金请求: 资金账户ID, 操作员ID, 商品ID, 买卖方向, 数量, 价格, 交易日, 委托单号, 单据类型, 商品所在市场ID
    freeze_req = MMTradeProto(
        Header = MessageHead(RequestID=request_id),
        OrderID = order_id,
        AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        #GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
        Qty = 12.34, #optional double Qty = 7;                    // 数量
        Price = 12.34, #optional double Price = 8;                  // 价格
        BuyOrSell = 1, #optional int32 BuyOrSell = 9;               // 买卖方向
        TradeDate = trade_day, #optional string TradeDate = 23;             // 交易日 YYYYMMDDhh24mmss
        OrderType = 100, #optional int32 OrderType = 10;               // 订单类型, 做市/竞价/拍卖/挂牌
        BuildType = 0, #optional int32 BuildType = 11;               // 下单类型, 建仓，平仓
    )
    conn.publish('entry', 'money_req', 1, 0, freeze_req)
    rsp_data = conn.expect('testmoney_rsp', 2, 0, 1.0)
    eq_(request_id, rsp_data.Header.RequestID)
    eq_(order_id, rsp_data.OrderID)
    eq_(16012, rsp_data.RetCode)


@with_setup(before_each, None)
def test_open_req_without_freeze():
    #占用请求: 交易日, 委托单号, 操作员ID, 资金账户ID, 对手资金账户ID, 商品ID, 商品数量, 价格, 买卖方向, 结算状态
    open_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = order_id, #optional int64 OrderID = 2;                 // 单号
        AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
    )
    conn.publish('entry', 'money_req', 2007, 0, open_req)

    #conn.get('testmoney_rsp', 1.0)
    rsp_data = conn.expect('testmoney_rsp', 2009, 0, 1.0)
    eq_(2009, rsp_data.Header.FunCode)
    eq_(20004, rsp_data.RetCode)


@with_setup(before_each, None)
def test_close_without_open():
    # 平仓请求: 交易日, 资金账户ID, 对手资金账户ID, 操作员ID, 商品ID, 成交数量, 成交价格, 买卖方向, 委托单号, 平仓明细, 结算状态
    # 平仓明细: 被平持仓单号, 平仓数量
    close_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = order_id, #optional int64 OrderID = 2;       // 单号
        AccountID = 8888, #optional int64 AccountID = 4;   // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;       // 商品ID
        #Qty = 12.34, #optional double Qty = 7;          // 数量
        #Price = 12.34, #optional double Price = 8;      // 价格
        #BuyOrSell = 1, #optional int32 BuyOrSell = 9;   // 买卖方向
        #TradeDate = trade_day, #optional string TradeDate = 23;  // 交易日
        #SettleStatus = 1, #optional int32 SettleStatus = 25;        // 结算状态
    )
    close_req.CloseDetails.add(OrderID=1, Qty=1)  # 平仓明细
    conn.publish('entry', 'money_req', 2008, 0, close_req)
    rsp_data = conn.expect('testmoney_rsp', 2010, 0, 1.0)
    eq_(2010, rsp_data.Header.FunCode)
    eq_(order_id, rsp_data.OrderID)
    eq_(4078, rsp_data.RetCode)


@with_setup(before_each, None)
def test_freeze_open():
    #冻结保证金请求: 资金账户ID,	操作员ID, 商品ID, 买卖方向, 数量, 价格, 交易日, 委托单号, 单据类型, 商品所在市场ID
    freeze_req = MMTradeProto(
        Header = MessageHead(RequestID=request_id),
        OrderID = order_id,
        AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
        Qty = 12.34, #optional double Qty = 7;                    // 数量
        Price = 12.34, #optional double Price = 8;                  // 价格
        BuyOrSell = 1, #optional int32 BuyOrSell = 9;               // 买卖方向
        TradeDate = trade_day, #optional string TradeDate = 23;             // 交易日 YYYYMMDDhh24mmss
        OrderType = 100, #optional int32 OrderType = 10;               // 订单类型, 做市/竞价/拍卖/挂牌
        BuildType = 0, #optional int32 BuildType = 11;               // 下单类型, 建仓，平仓
    )
    conn.publish('entry', 'money_req', 1, 0, freeze_req)
    rsp_data = conn.expect('testmoney_rsp', 2, 0, 1.0)
    eq_(0, rsp_data.RetCode)
    eq_(2, rsp_data.Header.FunCode)

    #占用请求: 交易日, 委托单号, 操作员ID, 资金账户ID, 对手资金账户ID, 商品ID, 商品数量, 价格, 买卖方向, 结算状态
    open_req = MMTradeProto(
        Header = MessageHead(RequestID=request_id),
        OrderID = order_id, #optional int64 OrderID = 2;                 // 单号
        AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
        Qty = 12.34, #optional double Qty = 7;                    // 数量
        Price = 12.34, #optional double Price = 8;                  // 价格
        BuyOrSell = 1, #optional int32 BuyOrSell = 9;               // 买卖方向
        TradeDate = trade_day, #optional string TradeDate = 23;             // 交易日
        SettleStatus = 1, #optional int32 SettleStatus = 25;           // 结算状态
    )
    conn.publish('entry', 'money_req', 2007, 0, open_req)
    rsp_data = conn.expect('testmoney_rsp', 2009, 0, 1.0)
    eq_(0, rsp_data.RetCode)
    eq_(2009, rsp_data.Header.FunCode)


@with_setup(before_each, None)
def test_freeze_open_close():
    #冻结保证金请求: 资金账户ID, 操作员ID, 商品ID, 买卖方向, 数量, 价格, 交易日, 委托单号, 单据类型, 商品所在市场ID
    freeze_req = MMTradeProto(
        Header = MessageHead(FunCode=1),
        OrderID = order_id,
        AccountID = 8888,  #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888,    #optional int32 GoodsID = 6;                  // 商品ID
        Qty = 1.0,       #optional double Qty = 7;                    // 数量
        Price = 1.0,     #optional double Price = 8;                  // 价格
        BuyOrSell = 1,     #optional int32 BuyOrSell = 9;               // 买卖方向
        TradeDate = trade_day, #optional string TradeDate = 23;             // 交易日
        OrderType = 100,
        BuildType = 0,
    )
    conn.publish('entry', 'money_req', 1, 0, freeze_req)

    rsp_data = conn.expect('testmoney_rsp', 2, 0, 1.0)
    eq_(0, rsp_data.RetCode)
    eq_(2, rsp_data.Header.FunCode)

    #占用请求: 交易日, 委托单号, 操作员ID, 资金账户ID, 对手资金账户ID, 商品ID, 商品数量, 价格, 买卖方向, 结算状态
    open_req = MMTradeProto(
        Header = MessageHead(FunCode=2007),
        OrderID = order_id, #optional int64 OrderID = 2;                 // 单号
        AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
        Qty = 1.0, #optional double Qty = 7;                    // 数量
        Price = 1.0, #optional double Price = 8;                  // 价格
        BuyOrSell = 1, #optional int32 BuyOrSell = 9;               // 买卖方向
        TradeDate = trade_day, #optional string TradeDate = 23;             // 交易日
        SettleStatus = 0, #optional int32 SettleStatus = 25;           // 结算状态
    )
    conn.publish('entry', 'money_req', 2007, 0, open_req)
    rsp_data = conn.expect('testmoney_rsp', 2009, 0, 1.0)
    eq_(order_id, rsp_data.OrderID)
    eq_(2009, rsp_data.Header.FunCode)
    eq_(0, rsp_data.RetCode)

    # 平仓请求: 交易日, 资金账户ID, 对手资金账户ID, 操作员ID, 商品ID, 成交数量, 成交价格, 买卖方向, 委托单号, 平仓明细, 结算状态
    # 平仓明细: 被平持仓单号, 平仓数量
    close_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = order_id, #optional int64 OrderID = 2;       // 单号
        AccountID = 8888, #optional int64 AccountID = 4;   // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;       // 商品ID
        Qty = 1.0, #optional double Qty = 7;          // 数量
        Price = 1.0, #optional double Price = 8;      // 价格
        BuyOrSell = 1, #optional int32 BuyOrSell = 9;   // 买卖方向
        TradeDate = trade_day, #optional string TradeDate = 23;  // 交易日
        SettleStatus = 0, #optional int32 SettleStatus = 25;        // 结算状态
    )
    freeze_req.CloseDetails.add(OrderID=order_id, Qty=1.0)  # 平仓明细
    conn.publish('entry', 'money_req', 2008, 0, close_req)
    rsp_data = conn.expect('testmoney_rsp', 2010, 0, 1.0)
    eq_(0, rsp_data.RetCode)
    eq_(2010, rsp_data.Header.FunCode)
    eq_(order_id, rsp_data.OrderID)


@with_setup(before_each, None)
def test_freeze_rsp_delay():
    #冻结保证金请求: 资金账户ID, 操作员ID, 商品ID, 买卖方向, 数量, 价格, 交易日, 委托单号, 单据类型, 商品所在市场ID
    total_t, N = 0.0, 10
    for i in range(order_id, order_id+N):
        print 'new loop i=%d'%i
        freeze_req = MMTradeProto(
            Header = MessageHead(FunCode=1),
            OrderID = i,
            AccountID = 8888,  #optional int64 AccountID = 4;               // 资金账户ID
            GoodsID = 8888,    #optional int32 GoodsID = 6;                  // 商品ID
            Qty = 1.0,       #optional double Qty = 7;                    // 数量
            Price = 1.0,     #optional double Price = 8;                  // 价格
            BuyOrSell = 1,     #optional int32 BuyOrSell = 9;               // 买卖方向
            TradeDate = trade_day, #optional string TradeDate = 23;             // 交易日
            OrderType = 100,
            BuildType = 0,
        )
        t0 = conn.publish_t('entry', 'money_req', 1, 0, freeze_req)

        rsp_data, t1 = conn.expect_t('testmoney_rsp', 2, 1, 1.0)
        print 'rsp_delay=%f'%(t1-t0)
        total_t += t1-t0
    print 'total_t=%f, avg_delay=%f'%(total_t, total_t/N)

    return

    #占用请求: 交易日, 委托单号, 操作员ID, 资金账户ID, 对手资金账户ID, 商品ID, 商品数量, 价格, 买卖方向, 结算状态
    open_req = MMTradeProto(
        Header = MessageHead(FunCode=2007),
        OrderID = order_id, #optional int64 OrderID = 2;                 // 单号
        AccountID = 8888, #optional int64 AccountID = 4;               // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;                  // 商品ID
        Qty = 1.0, #optional double Qty = 7;                    // 数量
        Price = 1.0, #optional double Price = 8;                  // 价格
        BuyOrSell = 1, #optional int32 BuyOrSell = 9;               // 买卖方向
        TradeDate = trade_day, #optional string TradeDate = 23;             // 交易日
        SettleStatus = 0, #optional int32 SettleStatus = 25;           // 结算状态
    )
    conn.publish('entry', 'money_req', 2007, 0, open_req)
    rsp_data = conn.expect('testmoney_rsp', 2009, 0, 1.0)
    eq_(order_id, rsp_data.OrderID)
    eq_(2009, rsp_data.Header.FunCode)
    eq_(0, rsp_data.RetCode)

    # 平仓请求: 交易日, 资金账户ID, 对手资金账户ID, 操作员ID, 商品ID, 成交数量, 成交价格, 买卖方向, 委托单号, 平仓明细, 结算状态
    # 平仓明细: 被平持仓单号, 平仓数量
    close_req = MMTradeProto(
        Header = MessageHead(),
        OrderID = order_id, #optional int64 OrderID = 2;       // 单号
        AccountID = 8888, #optional int64 AccountID = 4;   // 资金账户ID
        GoodsID = 8888, #optional int32 GoodsID = 6;       // 商品ID
        Qty = 1.0, #optional double Qty = 7;          // 数量
        Price = 1.0, #optional double Price = 8;      // 价格
        BuyOrSell = 1, #optional int32 BuyOrSell = 9;   // 买卖方向
        TradeDate = trade_day, #optional string TradeDate = 23;  // 交易日
        SettleStatus = 0, #optional int32 SettleStatus = 25;        // 结算状态
    )
    freeze_req.CloseDetails.add(OrderID=order_id, Qty=1.0)  # 平仓明细
    conn.publish('entry', 'money_req', 2008, 0, close_req)
    rsp_data = conn.expect('testmoney_rsp', 2010, 0, 1.0)
    eq_(0, rsp_data.RetCode)
    eq_(2010, rsp_data.Header.FunCode)
    eq_(order_id, rsp_data.OrderID)
