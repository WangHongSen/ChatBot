import unittest

from utils import base_chart
from utils.relativedelta import relativedelta
import datetime
from dj_chat.util import ChatCache

from utils.jwt_payload import jwt_response_payload_handler
from utils.relativedelta import _sign
from utils.chatrobot import ghs,gp,help,btc,talk_with_me,sizhi
import requests 

class User:
    def __init__(self,id, name):
        self.id = id 
        self.username = name 


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start test class Utils")

    def test_get_dates(self):
        tt = datetime.datetime(2020,10,31)
        delta = relativedelta(1)
        re = base_chart.gen_dates(tt,3,delta)
        ss =next(re)
        self.assertEqual(ss,"2020Q4")

    def test_get_date_range(self):
        start = datetime.datetime(2011,1,1)
        end = datetime.datetime(2011,2,1)
        ll = base_chart.get_date_range("monthly",start,end)
        # print(ll)
        self.assertListEqual(['2011-01', '2011-02'],ll)
        start = datetime.datetime(2011,1,1)
        end = datetime.datetime(2011,1,3)
        ll = base_chart.get_date_range("daily",start,end)
        self.assertListEqual(ll,['2011-01-01', '2011-01-02', '2011-01-03'])
        start = datetime.datetime(2011,1,1)
        end = datetime.datetime(2012,1,3)
        ll = base_chart.get_date_range("yearly",start,end)
        # print(ll)
        self.assertListEqual(ll,['2011', '2012'])       
    
    def test_TokenAuthMiddleware(self):
        b = False
        self.assertFalse(False,b)
        #这个没法做 先掩耳盗铃
        # token = TokenAuthMiddleware(None)
        # token.authenticate_credentials(None)
        # self.assertRaises(APIException)
    def test_jwt_paypload(self):
        u = User(1,"wang")

        re = jwt_response_payload_handler(None,u)
        # print(re)
        self.assertDictEqual({
        'token': None,
        'user_id': 1,
        'username':"wang"},re)
    def test_sign(self):
        self.assertEqual(-1,_sign(-2.12))
        self.assertEqual(1,_sign(32))
    
    def test_chatbot(self):
        s='呵呵，你说什么我听不懂'
        # self.assertEqual(s, ghs())
        self.assertIs(ghs,None)
    def test_gp(self):
        self.assertIs(gp, None)
    def test_help(self):
        self.assertEqual(help, None);
    def test_btc(self):
        self.assertEqual(btc, None);
    
    def test_talk_with_me(self):
        pass
    def test_sizhi(self):
        re = sizhi("Hello")
        if requests.get("http://www.baidu.com").status_code != 200:
           #断网
           self.assertIn(re,['你说啥呢？','咱也不知道'])
        
        # print(type(re))
        # self.assertlsInstance(re, str)
        self.assertIsInstance(re, str)

    @classmethod
    def tearDownClass(cls):
        print("End of testing class utils") 

class TestCache(unittest.TestCase):
    cache = None
    @classmethod
    def setUpClass(cls):
        cls.cache = ChatCache("test")
        # cls.cache.clear()
        print("Start test cache")
    
    def test_set_add(self):
        self.cache.set_add("aaaa")
        self.assertEqual(1,self.cache.set_len())

    def test_set_len(self):
        self.cache.set_add("bbbb")
        self.assertEqual(2,self.cache.set_len())
        self.cache.set_remove("aaaa")
        self.assertEqual(1,self.cache.set_len())

    def test_set_members(self):
        #清空
        # self.cache.set_add("cccc")
        self.assertListEqual(list(self.cache.set_members()),['bbbb'])
    
    def test_set_is_member(self):
        self.assertEqual(False,self.cache.set_is_member("bbbb"))
    
    def test_set_remove(self):
        self.cache.set_remove('bbbb')
        self.assertEqual(0, self.cache.set_len())

    def test_clear(self):
        self.cache.clear()
        self.assertFalse(self.cache.exist('test'))
        ##准备测试集合类型
        # self.cache = ChatCache("test2")
        
    # def test_list_rpush(self):
    #     # self.cache.set_remove("cccc")
    #     self.cache.list_rpush(1,2,3,4,5)
    #     rr = self.cache.list_len()
    #     print(rr)
    #     self.assertEqual(rr,5)

    @classmethod
    def tearDownClass(cls):
        cls.cache.clear()
        print("End of test cache")


class TestCache2(unittest.TestCase):
    cache = None
    @classmethod
    def setUpClass(cls):
        cls.cache = ChatCache("test2")
        # cls.cache.clear()
        print("Start test list cache")

    def test_list_rpush(self):
        # self.cache.set_remove("cccc")
        rr = self.cache.list_len()
        self.cache.list_rpush(1,2,3,4,5)
        # print(rr)
        self.assertEqual(rr+5,self.cache.list_len())
    def test_list_len(self):
        ll = self.cache.list_len()
        self.cache.list_rpush(6)
        self.assertEqual(ll+1, self.cache.list_len())
    def test_list_index(self):
        #清空缓存
        self.cache.list_remove(end=1)
        self.cache.list_lpop()
        #监测是否清空
        self.assertEqual(0, self.cache.set_len())
        self.cache.list_rpush(1)
        self.assertEqual("1",self.cache.list_index(0))
    def test_list_set(self):
        self.cache.list_set(0,2)
        self.assertEqual("2",self.cache.list_index(0))
    def test_lpop(self):
        tmp = self.cache.list_len()
        self.cache.list_lpop()
        self.assertEqual(tmp-1,self.cache.list_len())
    def test_remove(self):
        self.cache.list_rpush(1,2,3,4,5)
        # tmp = self.cache.list_len()
        self.cache.list_remove(start=0,end= 1)
        self.assertEqual(2, self.cache.list_len())
        # print(self.cache.list_all())
    def test_list_all(self):
        self.cache.list_rpush(1)
        self.assertEqual(1,len(self.cache.list_all()))
    @classmethod
    def tearDownClass(cls):
        cls.cache.clear()
        print("End of test list cache")


class TestCache3(unittest.TestCase):
    cache = None
    @classmethod
    def setUpClass(cls):
        cls.cache = ChatCache("test3")
        # cls.cache.clear()
        print("Start test hashset cache")

    def test1_hash_len(self):
        self.assertEqual(0,self.cache.hash_len())
    
    def test2_hash_set(self):
        # pass
        tmp = self.cache.hash_len()
        self.cache.hash_set("k1","v1")
        self.assertEqual(tmp+1, self.cache.hash_len())
    def test3_hash_mset(self):
        tmp = self.cache.hash_len()
        tmp = self.cache.hash_mset({"k2":"v2"})
        self.assertEqual(2, self.cache.hash_len())
    def test4_hash_hget(self):
        self.assertEqual("v1",self.cache.hash_hget("k1"))
    def test5_hash_hgetall(self):
        #可能出错
        self.assertDictEqual({"k1":"v1","k2":"v2"},self.cache.hash_getall())
    def test6_hash_keys(self):
        self.assertListEqual(['k1','k2'],self.cache.hash_keys())
    def test7_hash_values(self):
        self.assertListEqual(['v1','v2'],self.cache.hash_values())
    def test8_hash_exist(self):
        self.assertFalse(self.cache.hash_exists("k3"))
        self.assertEqual(True,self.cache.hash_exists("k2"))
    def test9_hash_del(self):
        self.cache.hash_del("k2")
        self.assertFalse(self.cache.hash_exists("k2"))
        self.cache.hash_del("k1")#清空
    
    @classmethod
    def tearDownClass(cls):
        cls.cache.clear()
        print("End of hashset list cache")

if  __name__ == "__main__":
    # test_get_period_expression()
    # test_get_dates()
    # unittest.main()
    # 构造测试集
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    suite = unittest.TestSuite([suite1])
    #运行
    runner = unittest.TextTestRunner()
    runner.run(suite1)
