Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib,urllib2,httplib,cookielib
>>> import time
>>> import random
>>> import re
>>> name='kom9ing@163.com'
>>> password='3310571'
>>> url_login = "http://my.jjwxc.net/login.php?action=login&amp;referer=http%3A%2F%2Fmy.jjwxc.net%2Fbackend%2Flogininfo.php"
>>> print name
kom9ing@163.com
>>> cookie = cookielib.CookieJar()
>>> opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
>>> urllib2.install_opener(opener)
>>> user = { 
             'loginname'     : name,
             'loginpassword' : password,
           }
>>> headers = { 
               'User-Agent'      : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'
             }
>>> postdata = urllib.urlencode(user)
>>> request = urllib2.Request(url_login,postdata,headers=headers)
>>> response = urllib2.urlopen(request)
>>> thePage = response.read()
>>> print thePage
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

    <head>

        <meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>

        <title>晋江文学城[登陆信息]</title>

        <link href="http://s8.static.jjwxc.net/css/index.css" rel="stylesheet" type="text/css"/>

        <style type="text/css">

            <!--

            .STYLE1 {

                color: red;

                font-weight: bold;

            }

            -->

        </style>

    </head>

    <body topmargin="0">

                                

<div style="display:none;" class="cnzz"><script src='http://w.cnzz.com/c.php?id=30075907' language='JavaScript'></script></div>

<link href="http://static.jjwxc.net/css/channel_2010/index2010.css?ver=20140728" rel="stylesheet" type="text/css" media="screen" />

<style>

    #showNovelTro{position:absolute;display:none;padding:6px;border:1px solid #009900;background-color:#FFFFFF;width:240px;z-index:9999;}

    #showNovelTro ul{list-style-type:none;padding:0;margin:0;}

    #showNovelTro ul li{margin:0;padding:0;list-style-type:none;}

</style>

<script>

    var _czc = _czc||[];

    _czc.push(["_setAccount", "30075907"]);

</script>

<script type="text/javascript">!window.jQuery&&document.write('<script src="http://static.jjwxc.net/scripts/jquery-1.8.0.min.js"><\/script>');</script>

<script type="text/javascript" src="http://static.jjwxc.net/scripts/jquery.blockUI.pack.js"></script>

<script type="text/javascript" src="http://static.jjwxc.net/scripts/jjlogin.js?ver=201502021312"></script>  

<script type="text/javascript" src="http://static.jjwxc.net/scripts/main.120724.js?ver=20150122"></script>

<script type='text/javascript' src='http://js.adm.cnzz.net/js/abase.js'></script>

<script>

    function isonlinedoublered(type) {

        if (type==2) {

            return true;

        }

        if (type!=1) {

            return false;

        }

        //2015.02.18-2015.03.05

        var localtime = Math.round(new Date().getTime()/1000);

        if (parseInt(localtime)>=1424188800&&parseInt(localtime)<=1425571199) {

            return true;

        }

        return false;

    }

    $(function() {

        if (isonlinedoublered(1)) {

            // 翻倍红包公告提示

            $.ajax({

                type: "get",

                async: true, //同步异步 true为异步(默认),false为同步

                url: "http://s8.static.jjwxc.net/public_notice.php", //实际上访问时产生的地址为: test.php?callbackfun=jsonpCallback&id=10

                cache: true, //默认值false false时生成随机的&_=随机数

                dataType: "jsonp",

                jsonpCallback: "red_envelope_150204",

                ifModified: true,

                success: function(json) {

                    var msg = '';

                    $.each(json.publicMsg, function(index, v) {

                        msg += v+"&nbsp;&nbsp;&nbsp;&nbsp;";

                    });

                    if (msg!='') {

                        $("#public_notice_new").css('display', 'block');

                        $("#public_info_show").html(msg);

                    }

                }

            });

        }

        var version = 0;

        var caretPos = 0;

        $('#autoComplete').bind('input propertychange', function() {

            var checkUrl = window.location.pathname;

            var checkType = $("#tj option:selected").val();

            if (checkUrl.indexOf("search.php")<0||checkType!=1) {

                return false;

            }

            var words = encodeURIComponent($(this).val());

            var type = 1;//按作品搜索

            var html = "";

            var left = 168;

            var top = 70;

            version++;

            var inputObj = document.getElementById("autoComplete");

            var thisCaretPos = getCursortPosition(inputObj);

            if (thisCaretPos!=caretPos) {

                caretPos = thisCaretPos;

                $('#showNovelTro').hide();

                $.getJSON("http://www.jjwxc.net/search/search_ajax.php?action=search&keywords="+words+"&type="+type+"&version="+version, function(data) {

                    if (data.status==200&&data.version==version) {

                        html += "<ul>";

                        $.each(data.data, function(i, v) {

                            html += "<li><a href='http://my.jjwxc.net/search/result.php?novelid="+v.novelid+"&searchkey="+encodeURIComponent(data.searchkey)+"&type="+data.type+"'>"+v.novelname+"</a> -----<a href='http://www.jjwxc.net/oneauthor.php?authorid="+v.authorid+"'>"+v.authorname+"</a> </li>"

                        })

                        html += "</ul>";

                        $('#showNovelTro').css({

                            left: left+'px',

                            top: top+'px'

                        }).html(html).show();

                    }

                })

            }

        });

        $(document).click(function() {

            $('#showNovelTro').hide();

        });

    })

    function getCursortPosition(ctrl) {//获取光标位置函数

        var CaretPos = 0;    // IE Support

        if (document.selection) {

            ctrl.focus();

            var Sel = document.selection.createRange();

            Sel.moveStart('character', -ctrl.value.length);

            CaretPos = Sel.text.length;

        }

        // Firefox support

        else if (ctrl.selectionStart||ctrl.selectionStart=='0')

            CaretPos = ctrl.selectionStart;

        return (CaretPos);

    }

</script>

<div id="sitetop" class="c99" style="position: relative; z-index: 3;"><div style="float:left"><span id="serverTime"></span></div>

    <div class="toplogin">

        <div class="top_right" style="position:relative; z-index:2000;">

            <div id="t_user_info"></div> <div id="t_user_sms"></div> <div id="t_user_nav"></div>

            <noscript>由于您的浏览器禁用了javascript，无法正常使用本网站功能，<a href="http://help.jjwxc.net/user/article/136" target="_blank"><font color="blue">请参考此方法重新开启javascript</font></a></noscript>

        </div>

    </div>

    <script>checkLogin();</script>

    <!--待审核提示消息框-->

    <div class="blockUI blockMsg" id ="examine_num" style="z-index: 1002; position: absolute; height:45px; width:140px; top: 35px; left: 820px; text-align: center; color: rgb(0, 0, 0);  background-color:#FFFFF7;border:1px solid #FFCC00;display: none;line-height:15px">

        <a href="#" style="float: right;margin-right: 8px" id="examine_num_close">关闭</a><br/>

        <div id ="examine_num_content"></div>

    </div>

</div>

<!--整站头部结束-->

<!--js加载判断，从以前的foot_opt.php中的标签调整至此-->

<p id="checkJs" style="text-align:center"></p>

<!--logo 导航条-->

<div id="sitehead" style="position:relative; z-index:2;line-height: 22px;">

    <div class="logo"><a href="http://www.jjwxc.net/" rel="nofollow"><img src="http://static.jjwxc.net/images/channel_2010/logo.gif" width="120" height="120" alt="晋江文学城logo" title="晋江文学城" /></a></div>

    <div class="nav1">

        <div class="fl" style="width:371px;">

            <div class="link1"><a href="http://www.jjwxc.net/fenzhan/yq/" class="a1"></a><a href="http://www.jjwxc.net/fenzhan/yc/" class="a2"></a><a href="http://www.jjwxc.net/fenzhan/noyq/" class="a3"></a><a href="http://www.jjwxc.net/fenzhan/ys/" class="a4"></a></div>

            <div class="link2">

                <a href="http://www.jjwxc.net/fenzhan/by/" target="_blank">完结文库</a><a href="http://www.jjwxc.net/fenzhan/bq/" target="_blank">出版影视</a><a href="http://www.jjwxc.net/jjgame/" target="_blank" >游戏娱乐</a><a href="http://bbs.jjwxc.net" target="_blank">论坛</a><a href="http://www.jjwxc.net/sp/JJ-app-download/" onclick="_czc.push(['_trackEvent', 'WWW分页', '点击', '手机频道']);" target="_blank"><font style="color:red;font-weight:700">手机版</font></a><a onclick="trans(0);

                        return false;" id="S2TLink" href="#">繁体版</a>



            </div>

        </div>

        <!--全站通发顶部banner广告-->

        <div  style="float: right; width: 468px;" ><script>CNZZ_SLOT_RENDER('256809');</script></div>

        <div id="ad3"></div>

        <div class="clear"></div>

    </div>

    <div class="nav2">

        <div class="left1"></div>

        <div class="right1"></div>

        <div id="dymenu">

            <ul class="root">

                <li>

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://www.jjwxc.net/bookbase_slave.php">作品库<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?endstr=true&orderstr=1">完结作品</a></li>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?booktype=sp">驻站作品</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe></li>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?booktype=vip">VIP作品</a></li>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?booktype=package">完结半价/包月</a></li>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?booktype=scriptures">经典文库</a></li>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?booktype=free">免费文库</a></li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>

                <li class="topen">

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://www.jjwxc.net/topten.php">排行榜<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=1">官推言情榜</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=1&t=1">官推纯爱同人榜</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=3">新晋作者榜</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=5">月度排行榜</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=4">季度排行榜</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=6">半年排行榜</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=7">总分排行榜</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=8">字数排行榜</a></li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>

                <li>

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://www.jjwxc.net/channel/comment.html">评论频道<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/comment.php?orderstr=1">发表排序</a></li>

                        <li><a href="http://www.jjwxc.net/comment.php?orderstr=2">点击排序</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:45px;"></iframe></li>

                        <li><a href="http://www.jjwxc.net/spcomment.php">特邀评论</a></li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>

                <li>

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://www.jjwxc.net/authorlist.php">作者专区<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/authorlist.php">字母排序</a></li>

                        <li><a href="http://www.jjwxc.net/scorelist.php">积分排序</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe></li>

                        <li><a href="http://help.jjwxc.net/user/more/23/0">写作导航</a></li>

                        <li><a href="http://www.jjwxc.net/starshow.php">明星作者</a></li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>

                <li>

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://www.jjwxc.net/fenzhan/bq/">出版专区<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/fenzhan/bq/">封面欣赏</a></li>

                        <li><a href="http://www.jjwxc.net/fenzhan/bq/">最新签约</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:35px;"></iframe></li>

                        <li><a href="http://www.jjwxc.cn/zhuanlan/index/zhuanlantype/yuanchuang">图书销售</a></li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>

                <li>

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://www.jjwxc.net/aboutus/#fragment-33">新闻活动<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/onebook.php?novelid=494708">晋江新闻</a></li>

                        <li><a href="http://www.jjwxc.net/aboutus/#fragment-33">网站活动</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:45px;"></iframe></li>

                        <li><a href="http://www.jjwxc.net/aboutus/#fragment-33">媒体报道</a></li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>

                <li>

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://my.jjwxc.net/pay/paycenter.php"><font color="red">充值</font><img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://my.jjwxc.net/pay/paycenter.php">快捷充值</a></li>

                        <li><a href="http://my.jjwxc.net/pay/tutorial.php">充值流程</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:45px;"></iframe></li>

                        <li><a href="http://www.jjwxc.net/fenzhan/yq/action_center.html">包月卡激活</a></li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>

                <li>

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://my.jjwxc.net/backend/auto.php">求助投诉<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://help.jjwxc.net/user/article/49">更改笔名</a></li>

                        <li><a href="http://my.jjwxc.net/backend/auto.php?act=3">笔名自杀</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe></li>

                        <li><a href="http://my.jjwxc.net/backend/auto.php?act=4">删除文章</a></li>

                        <li><a href="http://www.jjwxc.net/report_center.php">检举文章</a></li>

                        <li><a href="http://my.jjwxc.net/backend/auto.php?act=6">投诉书评</a></li>

                        <li><a href="http://my.jjwxc.net/backend/auto.php?act=7">修改授权</a></li>

                        <li><a href="http://my.jjwxc.net/backend/auto.php?act=8">笔名排序错误</a></li>

                        <li><a href="http://help.jjwxc.net/user/password">忘记密码</a></li>

                        <li><a href="http://bbs.jjwxc.net/board.php?board=22&page=1">意见建议簿</a></li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>

                <li>

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://my.jjwxc.net/login.php">注册/登录<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://my.jjwxc.net/register/index.html" rel="nofollow">用户注册</a></li>

                        <li><a href="http://my.jjwxc.net/login.php">登陆管理</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe></li>

                        <li><a href="http://my.jjwxc.net/backend/logout.php" title="退出登录状态">退出登陆</a></li>

                        <li><a href="http://help.jjwxc.net/user/password">忘记密码</a></li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>



                <li>

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://help.jjwxc.net/user/index">帮助<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://help.jjwxc.net/user/index">帮助中心</a></li>

                        <li><a href="http://help.jjwxc.net/user/contact">客服中心</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:20px;"></iframe></li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>



                <li>

                    <!--[if IE]><a

                href="#">

                <table>

                  <tbody>

                  <tr>

                    <td><![endif]-->

                    <div class="title"><a href="http://game.jjwxc.net"><font color="red">游戏</font><img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul id="jjgames">

                        <li>

                            <a style="width:110px" href="http://ktpd.jjqj.net/" target="_blank">晋江开天辟地2

                                <img src="http://static.jjwxc.net/images/channel_2010/new.gif" width="22px" />   

                            </a>    

                        </li>

                        <li>

                            <a style="width:110px" href="http://jjhgll.175wan.com/" target="_blank">晋江后宫来了

                            </a>    

                        </li>

                        <!--                        <li>

                                                    <a style="width:110px" href="http://jjzsxy.3737.com/" target="_blank">晋江再世仙缘

                                                    </a>    

                                                </li>-->

                        <li><a style="width:110px" href="http://xxd.jjqj.net/" target="_blank">晋江仙侠道</a>    

                        </li>

                        <li><a style="width:110px" href="http://jjwxc.tgm.9917.com/" target="_blank">晋江唐宫梦</a>

                        </li>

<!--                        <li><a href="http://jjwxc.zcl.2g.cn/" target="_blank">晋江总裁令</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe>

                        </li>-->

                        <li><a style="width:110px" href="http://jjwxc.aoshitang.com/gcld" target="_blank">晋江攻城掠地

                            </a>    

                        </li>



                        <li><a style="width:110px" href="http://jjwxc.9917.com/servers_yyzq.html?wait=alert">晋江凤凰决



                            </a>    

                        </li>

                        <li><a style="width:110px" href="http://jjwxc.aoshitang.com/">晋江名将传说

                            </a>    

                        </li>

                        <li><a style="width:110px" href="http://jjwxc.9917.com/">晋江宫廷计</a>

                        </li>

                    </ul>

                    <!--[if IE]></td></tr></tbody></table></a><![endif]-->

                </li>

            </ul>

        </div>

    </div>

    <div class="nav3">

        <div class="left2"></div>

        <div class="mainnavbox">

            <div class="mainnav">



                <a href="http://www.jjwxc.net/fenzhan/yq/dp.html">短篇</a>

                <a href="http://www.jjwxc.net/fenzhan/dm/ys.html">同人言情小说</a>

                <a href="http://www.jjwxc.net/fenzhan/dm/tr.html">同人言情动漫</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/kh.html">科幻悬疑网游</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/wx.html">玄幻奇幻</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/chy.html">古代穿越</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/qc.html">幻想现言</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/bgx.html">都市青春</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/bgg.html">古代言情</a>

            </div>

            <div class="search">

                <a class="limitFree" href="http://www.jjwxc.net/sp/novelfree/" target="_blank" style="float:left"><img width="51" style="margin-left: 40px;" src="http://static.jjwxc.net/images/Channel/xmyd.gif" ></a>

                <div class="search_right">

                    <form  method="get" action="http://www.jjwxc.net/bookbase.php" target="_top"  id="formright">

                        <input type="hidden" name="s_typeid" value="1" />

                        <select name="fw" id="fwfw" class="input2">

                            <option value="0">-范围-</option>

                                                                                        <option value="1" >全站</option>

                                                                    <option value="2" >完结半价</option>

                                                                    <option value="3" >VIP库</option>

                                                            </select>

                        <select name="ycx" id="ycyc" class="input2" style="width:73px">

                            <option value="0">-原创性-</option>

                                                                                        <option value="1" >原创</option>

                                                                    <option value="2" >同人</option>

                                                            </select>

                        <select name="xx" id="xxxx" class="input2">

                            <option value="0">-性向-</option>

                                                                                        <option value="1" >言情</option>

                                                                    <option value="2" >纯爱</option>

                                                                    <option value="3" >百合</option>

                                                                    <option value="4" >女尊</option>

                                                                    <option value="5" >无CP</option>

                                                            </select>

                        <select name="sd" id="sdsd" class="input2">

                            <option value="0">-时代-</option>

                                                                                        <option value="1" >近代现代</option>

                                                                    <option value="2" >古色古香</option>

                                                                    <option value="4" >架空历史</option>

                                                                    <option value="5" >幻想未来</option>

                                                            </select>

                        <select name="lx" id="lxlx" class="input2">

                            <option value="0">-类型-</option>

                                                                                        <option value="1" >爱情</option>

                                                                    <option value="2" >武侠</option>

                                                                    <option value="3" >奇幻</option>

                                                                    <option value="4" >仙侠</option>

                                                                    <option value="5" >网游</option>

                                                                    <option value="6" >传奇</option>

                                                                    <option value="7" >科幻</option>

                                                                    <option value="8" >童话</option>

                                                                    <option value="9" >恐怖</option>

                                                                    <option value="10" >侦探</option>

                                                                    <option value="11" >动漫</option>

                                                                    <option value="12" >影视</option>

                                                                    <option value="13" >小说</option>

                                                                    <option value="14" >真人</option>

                                                                    <option value="15" >其他</option>

                                                                    <option value="16" >剧情</option>

                                                            </select>

                        <select name="fg" id="fgfg" class="input2">

                            <option value="0">-风格-</option>

                                                                                        <option value="1" >悲剧</option>

                                                                    <option value="2" >正剧</option>

                                                                    <option value="3" >轻松</option>

                                                                    <option value="4" >爆笑</option>

                                                                    <option value="5" >暗黑</option>

                                                            </select>

                        <select name="bq" id="ss_tags" class="input2" style="width: 71px;"><!--原来代码是 id="s_tags" 。由于js文件的原因，如果启用该id会导致下拉框多出很多很多标签，混乱，因此修改掉！-->

                            <option value="-1">-标签-</option>

                            <!--标签改为Ajax获取，在 main.120724_.js 中-->

                        </select>

                        <input name="submit" type="submit" onclick="_czc.push(['_trackEvent', 'WWW分页', '点击', '分类查询']);" class="searchbutton input3" id="submit" value="查询" />

                    </form>

                </div>

                <div class="search_left">

                    <form name="form8" method="get" action="http://www.jjwxc.net/search.php" target=_blank id="formleft">

                                                    <input name = "kw" id = "autoComplete" autocomplete = "off" type = "text" onfocus = "if (this.value!='')

                                            this.value = '';

                                        $(this).css('color', 'black');" style = "width: 110px;color:#B2B2B2;" value = "请输入关键字">

                                   



                        <div id="showNovelTro"></div>

                        <select name="t" class="input2" id="tj">

                            <option value="1" selected>作品</option>

                            <option value="2">作者</option>

                            <option value="4">主角</option>

                            <option value="5">配角</option>

                            <option value="6">其它关键字</option>

                        </select>

                        <input name="submit" type="submit" onclick="_czc.push(['_trackEvent', 'WWW分页', '点击', '关键字查询']);" value="查询" class="searchbutton input3" />

                        <!--super165-->

                    </form>

                </div>

            </div>

        </div>

        <div class="right2"></div>

    </div>

</div>

<script>headChange();</script>

<div style="width:984px; margin:5px auto;display: none;" id="public_notice_new">

    <div style="width:30px;float:left">

        <img src="http://s8.statiac.jjwxc.net/images/laba.png">

    </div>

    <div style="width:945px;float:left">

        <marquee scrollAmount="3" id="public_info_show" onmouseover="this.stop()" onmouseout="this.start()"></marquee>

    </div>

</div>

    <div class="h8px"></div>

    <!--logo 导航条结束-->                

</head>

<!--281948-->

<meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>

<link rel="stylesheet" type="text/css" href="http://static.jjwxc.net/scripts/jquerycssmenu/jquerycssmenu.css" />

<script type="text/javascript" src="http://static.jjwxc.net/scripts/jquerycssmenu/jquerycssmenu.js?var=20130115"></script>

<script type="text/javascript">

    // --- 提示窗口

    var alert_blockUI = function(message) {

        $.blockUI('<div align="center"><div style="float:right"><img src="http://static.jjwxc.net/images/close.gif" width="12" height="12" style="cursor:pointer" onClick="$.unblockUI()"/></div><b>'+message+'</b><br><br><br><br><input type="button" value="确 定" onClick="$.unblockUI()"/></div>', {

            width: '330px',

            height: '100px',

            cursor: 'default'

        });

    }



    $(function() {

        $.getJSON('getSMS.php', {action: 'get', r: Math.random()}, function(json) {

            if (json.status==200) {

                var html = '';

                var i = 0;

                var bgcolors = new Array('#FF6633', '#FFFFB0', '#FFFFCC');

                var smssubject = '';



                if (json.message_vip!=0) {

                    html += '<table id="vip_message" width="984" border="0" align="center" cellpadding="4" cellspacing="1" bgcolor="#ff6633">';

                    html += '<tr><td bgcolor="#ffffb0">〖<b>您最近订阅的VIP文章更新情况提醒</b>〗</td></tr>';

                    html += '<tr><td bgcolor="#ffffcc">'+json.message_vip['body']+'</td></tr>';

                    html += '</table><div style="height: 12px"></div>';

                }



                $.each(json.message_sms, function(index, value) {

                    if (value['smstype']==0||value['smstype']==4) {

                        bgcolors[0] = '#FF6633';

                        bgcolors[1] = '#FFFFB0';

                        bgcolors[2] = '#FFFFCC';

                        smssubject = '<b>'+value['smssubject']+'</b>　<font color="#999999">〖'+value['smsdate']+'〗　</font><a id="sms_'+value['smsid']+'" onclick="smsclick('+value['smsid']+', 1)" style="cursor:pointer;">【已阅关闭】</a>';

                    } else if (value['smstype']==1||value['smstype']==3) {

                        bgcolors[0] = '#CCCCCC';

                        bgcolors[1] = '#D8E3F4';

                        bgcolors[2] = '#FFFFFF';

                        smssubject = '<b>'+value['smssubject']+'</b>　<font color="#999999">〖'+value['smsdate']+'〗　</font><a id="sms_'+value['smsid']+'" onclick="smsclick('+value['smsid']+', 1)" style="cursor:pointer;">【已阅关闭】</a>';

                    } else if (value['smstype']==2) {

                        smssubject = '〖'+value['sendname']+'〗 <font color="#999999">于</font> '+value['smsdate']+' <font color="#999999">发信给您：</font>〖'+value['smssubject']+'〗　　<a id="sms_'+value['smsid']+'" onclick="smsclick('+value['smsid']+', 2)" style="cursor:pointer;">【<b>已阅关闭</b>】</a>';

                        if (value['deadline']=='0000-00-00 00:00:00') {

                            bgcolors[0] = '#FF6633';

                            bgcolors[1] = '#FFFFB0';

                            bgcolors[2] = '#FFFFCC';

                        } else {

                            bgcolors[0] = '#CCCCCC';

                            bgcolors[1] = '#D8E3F4';

                            bgcolors[2] = '#FFFFFF';

                        }

                    }

                    html += '<div id="'+value['smsid']+'"><table width="984" border="0" align="center" cellpadding="4" cellspacing="1" bgcolor="'+bgcolors[0]+'">';

                    html += '<tr align="left"><td bgcolor="'+bgcolors[1]+'">'+smssubject+'</td></tr>';

                    html += '<tr align="left"><td bgcolor="'+bgcolors[2]+'">'+value['smsbody']+'</td></tr></table>';

                    html += '<div style="height: 12px"></div></div>';

                    i++;

                })



                if (html!='') {

                    html = '<div style="height: 12px"></div>'+html;

                    $('#sms_box').html(html);



                    $('.sendSMS').bind('click', function() {

                        var orderId = $(this).attr('rel');

                        location.href = 'sms.php?orderId='+orderId;

                    })



                    $('.confirmDelivery').bind('click', function() {

                        var id = $(this).parents().parents().parents().parents().find('a').attr('id');

                        var orderId = $(this).attr('rel');



                        if (confirm('确认已经收到定制作品了吗？')) {

                            $.blockUI('<img src="http://static.jjwxc.net/images/loading.gif">  <strong>请稍候...</strong>');

                            $.getJSON('subscribe_print.php', {action: 'confirmDelivery', orderId: orderId, r: Math.random()}, function(json) {

                                if (json.status==200) {

                                    alert_blockUI(json.message);

                                    $('#'+id).click();

                                } else {

                                    alert_blockUI(json.message);

                                }

                            })

                        }

                    })



                    $("#delaylist").click(function() {

                        var order_id = $(this).attr('rel');

                        var message = '&nbsp;&nbsp;如您收到的印刷品有磨损，请在此上传磨损照片(照片内容包括印刷品磨损部位和快递单号),以供印刷方核对,给您重寄。<br>如上传照片有误，可重新上传。<br>上传图片格式为JPG，大小在2M以内，限1张';

                        $.blockUI('<div align="center"><div style="float:right"><img src="http://static.jjwxc.net/images/close.gif" width="12" height="12" style="cursor:pointer" onClick="$.unblockUI()"/></div><br><br><b>'+message+'</b><br><br><br><input type="button" value="点击上传图片" class="pic" id="'+order_id+'"/>&nbsp;&nbsp;&nbsp;&nbsp;<input type="button" value="放  弃" onClick="$.unblockUI()"/></div>', {width: '330px', height: '200px', cursor: 'default'});

                        $('.pic').each(function() {

                            new AjaxUpload('#'+order_id, {

                                action: 'subscribe_print1.php?action=delayupload',

                                onSubmit: function(file, ext) {

                                    if (ext&&/(jpg){1}$/i.test(ext)) {

                                        $.blockUI('<img src="http://static.jjwxc.net/images/loading.gif">  <strong>请稍候...</strong>');

                                        this.setData({

                                            'id': order_id

                                        });

                                    } else {

                                        alert_blockUI('文件格式错误，只支持上传jpg文本格式');

                                        return false;

                                    }

                                },

                                onComplete: function(file, json) {

                                    json = eval('('+json+')');

                                    if (json.status==200) {

                                        $('#showimg').html('<a href="http://my.jjwxc.net/'+json.url+'" target="_block"><img src="'+json.url+'?" width="500px"/></a>');

                                        alert_blockUI(json.message);

                                    } else {

                                        alert_blockUI(json.message);

                                    }

                                }

                            });



                        })

                    });



                    if (i>0&&(getCookie("sms_total")==null||getCookie("sms_total")!=i)) {

                        var now = new Date();

                        var randId = Math.round((Math.random()*10))+20;

                        now.setTime(now.getTime()+randId*60*1000);

                        setCookie("sms_total", i, now, "/", ".jjwxc.net");

                        getMessage();

                    }

                }

            }

        })

    });



    function smsclick(id, smstype) {

        if (smstype<=3) {

            $("#sms_"+id).html("<img src=\"http://static.jjwxc.net/images/loading.gif\" width=\"16\" height=\"16\"> <font color=\"red\">请稍候</font>");

            $.post("sms.php", {smsid: id, smstype: smstype});

            $("#"+id).animate({opacity: 'hide'}, "slow");

            var total = parseInt($('#sms_total').html());

            if (total-1<=0) {

                $('#sms').html('◆短信<span id="sms_total"></span>');

            } else {

                total = total-1;

                $('#sms_total').html(total);

            }

        } else {

            $("#vip_message1").html("<img src=\"http://static.jjwxc.net/images/loading.gif\" width=\"16\" height=\"16\"> <font color=\"red\">请稍候</font>");

            $.post("sms.php", {smsid: id, smstype: smstype});

            $("#vip_message").animate({opacity: 'hide'}, "slow");

        }

    }

</script>

<body>

    <div id="myjquerymenu" class="jquerycssmenu">

        <ul>

                        <li>

                <a href="javascript:">【我的晋江】</a>

                <ul>

                    <li><a href="logininfo.php?jsid=837021.1424156929">安全信息</a></li>

                    <li><a href="userinfo.php?jsid=837021.1424156929">基本信息</a></li>

                    <li><a href="sms.php?jsid=837021.1424156929">站内短信</a></li>

                </ul>

            </li>

            <li>

                <a href="javascript:">【读书】</a>

                <ul>

                    <li><a href="favorite.php?jsid=837021.1424156929">收藏列表</a></li>

                    <li><a href="commentshistory.php?jsid=837021.1424156929">我发出的评论</a></li>

                    <li><a href="vip_services.php?jsid=837021.1424156929">vip服务</a></li>

                                     

                </ul>

            </li>       

            <script type="text/javascript">

                function demo() {

                    if (confirm('只有要发表文章才需要成为作者，你确认要申请吗？'))

                        location.href = ('http://my.jjwxc.net/registeauthor.php?jsid=837021.1424156929');

                }

            </script>

            <!--string(6) "281948"
 -->

            <li>

                <a href="javascript:">【写作】</a>

                                    <ul>

                        <li><a href="publish.php?jsid=837021.1424156929">发表新文</a></li>

                        <li><a href="oneauthor_login.php?jsid=837021.1424156929">更新旧文</a></li>

                        <li><a href="series.php?jsid=837021.1424156929">文章系列</a></li>

                        <li><a href="setcolumn.php?jsid=837021.1424156929">设置专栏</a></li>

                        <li><a href="novelcomment.php?jsid=837021.1424156929">我收到的评论</a></li>

                        <li><a href="goodnovelrecommend.php?jsid=837021.1424156929">作者推文</a></li>

                        <li><a href="contract.php?jsid=837021.1424156929"><b>-我要签约-</b></a></li>

                    </ul>

                

            </li>	

            <li>

                <a href="javascript:">【签约服务】</a>

                <ul>

                    <li><a href="#">申请榜单</a></li>

                                            <li><a href="vipnovel.php?jsid=837021.1424156929">自荐申v</a></li>

                                            

                    <li><a href="complaint.php?jsid=837021.1424156929">盗文投诉</a></li>

                                            <li><a href="novel_free_vip.php?jsid=837021.1424156929" style="color:red;font-weight:bold;">限时免费</a></li>

                        

                </ul>

            </li>

            <li>

                <a href="javascript:">【账务】</a>

                <ul>

                    <li> <a href="bankbook.php?jsid=837021.1424156929">我的余额</a></li>

                    <li><a href="sendpointlist.php?jsid=837021.1424156929">积分记录</a></li>

                    <li><a href="consumerecord.php?jsid=837021.1424156929">消费记录</a></li>

                                            <li><a href="incomerecord.php?jsid=837021.1424156929">收益记录</a></li>

                        <li> <a href="payrecord.php?jsid=837021.1424156929">收益提现</a></li>

                                            <li><a href="http://my.jjwxc.net/pay/transfer.php?jsid=837021.1424156929">站内转账</a></li>

                </ul>

            </li>

            <li>

                <a href="javascript:">【互动活动】</a>

                <ul>

                    <li><a href="subscribe_print.php?jsid=837021.1424156929">定制印刷</a></li>

                    <li><a href="readerKingTickets.php?jsid=837021.1424156929">霸王票</a></li>

                    <li><a href="yueshi_exchange.php?jsid=837021.1424156929">月石兑换</a></li>

                    <li><a href="http://my.jjwxc.net/sp/2013pinwen/index.php?jsid=837021.1424156929">拼文活动</a></li>

                    <li><a href="http://my.jjwxc.net/backend/forest.php?jsid=837021.1424156929" style="color: red;font-weight: bold">植树造林</a></li>

                    

                </ul>

            </li>		

            <li>

                <a href="javascript:" >【充值】</a>

                <ul>

                    <li><a href="/pay/pay.php?jsid=837021.1424156929">网银</a></li>

                    <li><a href="/pay/yeepay_zfb.php?jsid=837021.1424156929">支付宝</a></li>

                    <li><a href="/pay/phonepay.php?jsid=837021.1424156929">神州行充值卡</a></li>

                    <li><a href="/pay/ruyifu.php?jsid=837021.1424156929">联通充值卡</a></li>

                    <li><a href="/pay/ctpay.php?jsid=837021.1424156929">电信充值卡</a></li>

                    <li><a href="/pay/gamecard.php?jsid=837021.1424156929">游戏点卡</a></li>

                    <li><a href="/pay/remit_pay.php?jsid=837021.1424156929">邮局银行汇款</a></li>

                    <li><a href="/pay/vpay.php?jsid=837021.1424156929">固话/电话手机</a></li>

                    <li><a href="/pay/umpay.php?jsid=837021.1424156929">手机支付</a></li>

                    <li><a href="/pay/paypal.php?jsid=837021.1424156929">paypal海外充值</a></li>

                    <li><a href="drweb.php">充值活动</a>

                </ul>

            </li>

                            <li><a href="javascript:" style="color: red;font-weight: bold" >【邀您评审】</a>

                    <ul>

                        <li><a href="http://my.jjwxc.net/backend/examine_read_primary.php" target="_blank" style="color: red;font-weight: bold">邀您文章评审</a></li>

                        <li><a href="http://my.jjwxc.net/backend/comment_check.php" target="_blank" style="color: red;font-weight: bold">邀您评论评审</a></li>

                    </ul>

                </li>

                        </ul>

    </div> 

    <div style="clear:both"></div>

    <table width="984" border="0" align="center" cellpadding="0" cellspacing="0">

        <tr>

            <td id="sms_box" align="center">&nbsp;</td>

        </tr>

    </table>        <table width="984" border="0" cellpadding="5" cellspacing="1" bgcolor="#009900" align="center">

            <tr bgcolor="#eefaee">

                <td width="949" colspan="3" align="left" bgcolor="#eefaee">尊敬的　<font color="red">kom9ing@163.com (沐影霜) </font>您的晋江客户号:<font color="red">837021</font> </td>

            </tr>

            <tr bgcolor="#eefaee">

                <td colspan="3" align="center"><table width="828" border="0" align="left" bgcolor="#009900" cellpadding="0" cellspacing="0">

                                                <tr bgcolor="#eefaee">

                            <td align="left" nowrap>您的成功登陆总次数：538<img src="http://www.jjwxc.cn/passport/index/sid/837021_5d84e241ff5996e6042d0bb7041f3798" height="0" width="0" border="0" /></td>

                            <td align="left">&nbsp;</td>

                        </tr>

                        <tr bgcolor="#eefaee">

                            <td align="left" nowrap>您本次成功登陆时间：2015-02-17 15:08:48</td>

                            <td align="left">&nbsp;</td>

                        </tr>

                        <tr bgcolor="#eefaee">

                            <td align="left" nowrap>您最近成功登陆时间：2015-02-17 15:04:32</td>

                            <td align="left">如果发现此时间晚于您上次登陆时间，则说明有人曾用你的密码登陆成功，强烈建议修改密码。</td>

                        </tr>

                        <tr bgcolor="#eefaee">

                            <td align="left" nowrap>您最近失败登陆时间：2010-09-22 18:23:58</td>

                            <td align="left">如果发现此时间晚于您上次失败时间，则说明有人曾用错误密码登陆失败。</td>

                        </tr>

                        <tr bgcolor="#eefaee">

                            <td align="left" colspan="2" nowrap><b>账号安全信息变动提醒(保留最近一年的):</b></td>

                        </tr>

                                            </table></td>

            </tr>

        </table>

<br/><div id="footer">

    <p class="red"><a href="http://www.jjwxc.net/aboutus/" target="_blank"><font color="red">关于我们</font></a> - <a href="http://www.jjwxc.net/aboutus/#fragment-29" target="_blank"><font color="red">联系方式</font></a> - <a href="http://bbs.jjwxc.net/board.php?board=22&page=1" target="_blank"><font color="red">意见反馈</font></a> - <a href="http://help.jjwxc.net/user/more/24/0" target="_blank"><font color="red">读者导航</font></a> - <a href="http://help.jjwxc.net/user/more/23/0" target="_blank"><font color="red">作者导航</font></a> - <a href="http://www.jjwxc.net/invite.php" target="_blank"><font color="red">招纳贤才</font></a> - <a href="http://help.jjwxc.net/user/article/76" target="_blank"><font color="red">投稿说明</font></a> - <a href="http://www.jjwxc.net/jjwxcauthority.php" target="_blank"><font color="red">权利声明</font></a> - <a href="http://www.jjwxc.net/jjwxcad.php" target="_blank"><font color="red">广告服务</font></a> - <a href="http://www.jjwxc.net/friendly.php" target="_blank"><font color="red">友情链接</font></a> - <a href="http://help.jjwxc.net/user/more_index" target="_blank"><font color="red">常见问题</font></a></p>

    <p class="red"> Copyright By 晋江文学城 www.jjwxc.net All rights reserved</p>

    <p class="red">Processed in 0.05 second(s) 最后生成2015-02-17 15:08:49</p>

    <p class="red"><a href="http://www.miibeian.gov.cn/" target="_blank" rel="nofollow">京ICP证080637号</a> <a href="http://www.miibeian.gov.cn/" target="_blank" rel="nofollow">京ICP备12006214号-2</a><font color="#666666"> 新出网证(京)字206号 京公网安备11010502023476</font></p>

    <p class="red">本站全部作品（包括小说和书评）版权为原创作者所有 本网站仅为网友写作提供上传空间储存平台。本站所收录作品、互动话题、书库评论及本站所做之广告均属其个人行为</p>

    <p class="red">与本站立场无关。网站页面版权为晋江文学城所有，任何单位，个人未经授权不得转载、复制、分发，以及用作商业用途。</p>

    <p class="red">重要声明：请所有作者发布作品时严格遵守国家互联网信息管理办法规定。我们拒绝任何色情暴力小说，一经发现，立即删除违规作品，严重者将同时封掉作者账号。</p>

    <p class="red">请大家联合起来，共创和谐干净网络。</p>

</div>

<!-- google 部份后置加载的广告移到页脚 20140325 -->

<!-- Google Admanager BEGIN ，Must Put behind all googleADManager function-->

<script type="text/javascript" src="http://partner.googleadservices.com/gampad/google_service.js"></script>

<script type="text/javascript">JJ_ADS_GID = 'ca-pub-7602717919537096';

    GS_googleAddAdSenseService(JJ_ADS_GID);

    GS_googleEnableAllServices();</script>

<!-- Google Admanager END -->



<!-- Google Admanager BEGIN 部份后置加载的广告 晋江个性化处理 -->

<script type="text/javascript">JJ_ADS_POS = [];

    $("[id^='adp_']").each(function() {

        JJ_ADS_POS.push(this.id.replace(/adp_/, ''))

    });</script>

<script type="text/javascript">for (i in JJ_ADS_POS) {

        eval(GA_googleAddSlot(JJ_ADS_GID, JJ_ADS_POS[i]));

    }

    GA_googleFetchAds();</script>



<!-- Baidu Admanager BEGIN -->

<script type='text/javascript' src='http://drmcmm.baidu.com/js/m.js'></script>

<script type="text/javascript" src="http://www.jjwxc.net/scripts/check.js?var=20131224"></script>

<script type="text/javascript">JJ_BAIDU_ADS_POS = [];

    $("[id^='bdadp_']").each(function() {

        JJ_BAIDU_ADS_POS.push(this.id.replace(/bdadp_/, ''));

        $(this).attr('id', this.id.replace(/bdadp_/, 'adp_'))

    });</script>

<script type="text/javascript">for (i in JJ_BAIDU_ADS_POS) {

        eval(BAIDU_CLB_addSlot(JJ_BAIDU_ADS_POS[i]));

    }

    BAIDU_CLB_enableAllSlots();</script>





 <script type="text/javascript"> GA_googleAddAttr("url", "backend"); </script>



<!-- jjwxc_qz_db --><div class="adp_hidden" id="adp_h_jjwxc_qz_db" style="z-index: 2;"><script type="text/javascript">GA_googleFillSlot("jjwxc_qz_db");</script></div>
<!-- jjwxc_top_textlink_310_60 --><div class="adp_hidden" id="adp_h_jjwxc_top_textlink_310_60" style="width:310px;padding-top:10px"><script type="text/javascript">GA_googleFillSlot("jjwxc_top_textlink_310_60");</script></div>
<!-- jjwxc_payrecord_984_34 --><div class="adp_hidden" id="adp_h_jjwxc_payrecord_984_34"><script type="text/javascript">GA_googleFillSlot("jjwxc_payrecord_984_34");</script></div>
<script type="text/javascript">$('#hidden_adp').show();

    function show_google_ads() {

        $('div.adp_hidden').each(function() {

            var idp = $(this).attr('id').replace(/adp_h/, 'adp');

            var pos = $("#"+idp).offset();

            if (pos) {

                $(this).css({"left": pos.left+"px", "top": pos.top+"px"});

            }

        });

    }

    show_google_ads();

    $(window).scroll(function() {

        show_google_ads();

    })</script>

<!-- Google Admanager END -->

<script type="text/javascript">if (typeof (showTime)=='function') {

        showTime();

    }</script>



<div style="display:none;" class="cnzz">

    <script src='http://w.cnzz.com/c.php?id=30075907' language='JavaScript'></script>

    <script>

    var _czc = _czc||[];

    _czc.push(["_setAccount", "30075907"]);

    </script>

</div>



<!-- 隐藏广告位-->

<div style="display: none"><script>

    if (typeof (CNZZ_SLOT_RENDER)!="undefined") {

        CNZZ_SLOT_RENDER('261520');

        CNZZ_SLOT_RENDER('343535');

        CNZZ_SLOT_RENDER('343536');

            }

    </script>

</div>    </body>

</html>
>>> def extract_val(content):
    vals = []
    aelems = re.findall('<input type="button".*value="√通过"', content)
    print aelems
    for aelem in aelems:
        print aelem
        splits = aelem.split(' ')
        taelem = splits[3]
        print taelem
        matches = re.match('onclick="pass\((.*)\)"',taelem)
        val = matches.group(1)
        vals.append(val)
    return vals

>>> def find_result(content):
    aelems = re.findall('历史总评审字数.*</font>',content)
    return aelems

>>> url='http://my.jjwxc.net/backend/comment_check.php'
>>> op = opener.open(url)
>>> cont = op.read()
>>> print cont
<style type="text/css">
    .rows{
        background-color:red;
    }
</style>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<link href="/css/index.css" rel="stylesheet" type="text/css">
<script type="text/javascript">!window.jQuery&&document.write('<script src="http://static.jjwxc.net/scripts/jquery-1.8.0.min.js"><\/script>');</script>
<script type="text/javascript">
    //通过操作
    function pass(commentid, replyid, novelid, type) {
        $.get('comment_check.php?act=pass&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid, function(data) {
            if (data) {
                $('#'+commentid+'-'+replyid).remove();
                var selCheckboxObj = $("input[name='ids']");
                if (selCheckboxObj.length==0||type=='one') {
                    window.location.href = "http://my.jjwxc.net/backend/comment_check.php";
                }
            } else {
                alert('出现错误！');
            }
        })
    }

    //不通过操作
    function del(commentid, replyid, novelid) {
        $.get('comment_check.php?act=del&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid, function(data) {
            if (data) {
                $('#'+commentid+'-'+replyid).remove();
                var selCheckboxObj = $("input[name='ids']");
                if (selCheckboxObj.length==0||data) {
                    window.location.href = "http://my.jjwxc.net/backend/comment_check.php";
                }
            } else {
                alert('出现错误')
            }
        })
    }

    //批量通过
    function batchControll() {
        //首先获取页面所有勾选的复选框
        var selCheckboxObj = $("input[name='ids']:checked");
        var passvalue;
        for (var i = 0; i<selCheckboxObj.length; i++) {
            passvalue = selCheckboxObj[i].value.split("_");// 在每个"_"处进行分解。
            pass(passvalue[0], passvalue[1], passvalue[2], 'all');
        }

    }
    function rows(ob) {
//        ob.style.background = '#9ACD32';
        ob.style.background = '#eefaee';
    }
    function outrows(ob) {
        ob.style.background = '#eefaee';
    }
    function toggleselect(comment, replay) {
        var comments = comment+'-'+replay;
        if ($('#'+comments+' input').eq(0).attr('checked')=='checked') {
            $('#'+comments+' input').eq(0).attr('checked', false);
        } else {
            $('#'+comments+' input').eq(0).attr('checked', true);

        }
    }
    $(function() {
        var selCheckboxObj = $("input[name='ids']");
        if (selCheckboxObj.length==0) {
            window.location.href = "http://my.jjwxc.net/backend/comment_check.php";
        }
        $('#check').click(function() {
            if ($('#check').attr('checked')) {
                $(':checkbox:not(0)').attr('checked', true);
            } else {
                $(':checkbox:not(0)').attr('checked', false);
            }
        })
    })

</script>
<form name="frmLogList" method="post"  action="comment_check.php" >
    <table width="1024"  border="0" align="center" cellpadding="4" cellspacing="1" bgcolor="#009900" class="mouse" id="tb">
        <tr bgcolor="#FFF">
            <td colspan="2" align="left">
                <b>当日评审字数：<font color="red">0</font></b><br/><br/>
                <b>历史总评审字数：<font color="red">802336</font></b><br/><br/>                
                <span style="color:red"><b>【数据更新时间： 2015年02月17日 00:00:00】</b></span>
            </td>
        </tr>
        <tr bgcolor="#FFF">
            <td colspan="2" align="left">
                <font color="red">
                <b>审核不通过条件：</b><br/><br/>
                1、含有垃圾广告，比如：开发票，卖枪支，找小姐等等。 2、含有色情信息（有亲热描写）。3、含有联系方式，比如QQ，手机号码，邮箱等等 4、含有外站链接。</font>
            </td>

        </tr>
        <tr align="center"  bgcolor="#9FD59E">
            <td width="20">&nbsp;</td>
            <td width="680" align="center" style="font-size: 14px;">评论内容</td>
        </tr>
                    <tr align="right" bgcolor="#eefaee" id = "1968-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="1968_0_195424" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(1968,0)">
                        bluerobin：这孩子真是活跃，不过很可爱~~                    </div>
            <center>
                <span id='1968-0Recalculation'><input type="button" id ="1231968"  onclick="pass(1968,0,195424,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='1968-0Recalculationdel'><input type="button" id ="1231968" onclick="del(1968,0,195424)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "13572-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="13572_0_195343" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(13572,0)">
                        莫：赶快相认吧，全家团圆！                    </div>
            <center>
                <span id='13572-0Recalculation'><input type="button" id ="12313572"  onclick="pass(13572,0,195343,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='13572-0Recalculationdel'><input type="button" id ="12313572" onclick="del(13572,0,195343)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
            <tr  bgcolor="#eefaee"><td colspan="3" align="center"><a href="http://my.jjwxc.net/backend/comment_check.php">下一页</a></td></tr>        <tr bgcolor="#eefaee">
            <td colspan="2" align="center">
                <input type="button" name="buttondel" id = "buttondel" value="√批量通过" onclick="batchControll()" style="color:blue;"/>
            </td>

        </tr>
        <tr bgcolor="#eefaee">
            <td colspan="2" align="left">
                <font color="red">
                <b>审核不通过条件：</b><br/><br/>
                1、含有垃圾广告，比如：开发票，卖枪支，找小姐等等。 2、含有色情信息（有亲热描写）。3、含有联系方式，比如QQ，手机号码，邮箱等等 4、含有外站链接。</font><br/><br/> 
                <font color="blue">
                邀您评论评审奖励标准：每审核3000字(6000个字节)奖励2点晋江币，每周按照实际有效审核数据进行结算．结算后可在【我的余额】中查看。
                </font>
            </td>
        </tr>

    </table>
</form>
<div align = "center">
    <font color="red">运行总耗时：0.065937042236328 seconds  当前运行时间：2015-02-17 15:09:57</font>
</div>
>>> aelems = extract_val(cont)
['<input type="button" id ="1231968"  onclick="pass(1968,0,195424,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313572"  onclick="pass(13572,0,195343,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="1231968"  onclick="pass(1968,0,195424,'one')" value="√通过"
="1231968"

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    aelems = extract_val(cont)
  File "<pyshell#19>", line 11, in extract_val
    val = matches.group(1)
AttributeError: 'NoneType' object has no attribute 'group'
>>>  def extract_val(content):
    vals = []
    aelems = re.findall('<input type="button".*value="√通过"', content)
    print aelems
    for aelem in aelems:
        print aelem
        splits = aelem.split(' ')
        taelem = splits[5]
        print taelem
        matches = re.match('onclick="pass\((.*)\)"',taelem)
        val = matches.group(1)
        vals.append(val)
    return vals
  File "<pyshell#27>", line 1
    def extract_val(content):
    ^
IndentationError: unexpected indent
>>> def extract_val(content):
    vals = []
    aelems = re.findall('<input type="button".*value="√通过"', content)
    print aelems
    for aelem in aelems:
        print aelem
        splits = aelem.split(' ')
        taelem = splits[5]
        print taelem
        matches = re.match('onclick="pass\((.*)\)"',taelem)
        val = matches.group(1)
        vals.append(val)
    return vals

>>> aelems = extract_val(cont)
['<input type="button" id ="1231968"  onclick="pass(1968,0,195424,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313572"  onclick="pass(13572,0,195343,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="1231968"  onclick="pass(1968,0,195424,'one')" value="√通过"
onclick="pass(1968,0,195424,'one')"
<input type="button" id ="12313572"  onclick="pass(13572,0,195343,'one')" value="√通过"
onclick="pass(13572,0,195343,'one')"
>>> print aelems
["1968,0,195424,'one'", "13572,0,195343,'one'"]
>>> print find_result(cont)
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">802336</font>']
>>> for aelem in aelems:
	values = aelem.split(',')
	print values[0],' ',values[1],' ',values[2]
	commentid = values[0]
	replyid = values[1]
	novelid = values[2]
	url_read = url + '?act=pass&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid
	request2 = urllib2.Request(url_read, headers=headers)
	response_check = urllib2.urlopen(request2)
	print response_check.read()
	time.sleep(8.0)

1968   0   195424
1
13572   0   195343
1
>>> op = opener.open(url)
>>> print find_result(op.read())
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">802336</font>']
>>> print op.read()

>>> op = opener.open(url)
>>> cont = op.read()
>>> print cont
<style type="text/css">
    .rows{
        background-color:red;
    }
</style>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<link href="/css/index.css" rel="stylesheet" type="text/css">
<script type="text/javascript">!window.jQuery&&document.write('<script src="http://static.jjwxc.net/scripts/jquery-1.8.0.min.js"><\/script>');</script>
<script type="text/javascript">
    //通过操作
    function pass(commentid, replyid, novelid, type) {
        $.get('comment_check.php?act=pass&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid, function(data) {
            if (data) {
                $('#'+commentid+'-'+replyid).remove();
                var selCheckboxObj = $("input[name='ids']");
                if (selCheckboxObj.length==0||type=='one') {
                    window.location.href = "http://my.jjwxc.net/backend/comment_check.php";
                }
            } else {
                alert('出现错误！');
            }
        })
    }

    //不通过操作
    function del(commentid, replyid, novelid) {
        $.get('comment_check.php?act=del&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid, function(data) {
            if (data) {
                $('#'+commentid+'-'+replyid).remove();
                var selCheckboxObj = $("input[name='ids']");
                if (selCheckboxObj.length==0||data) {
                    window.location.href = "http://my.jjwxc.net/backend/comment_check.php";
                }
            } else {
                alert('出现错误')
            }
        })
    }

    //批量通过
    function batchControll() {
        //首先获取页面所有勾选的复选框
        var selCheckboxObj = $("input[name='ids']:checked");
        var passvalue;
        for (var i = 0; i<selCheckboxObj.length; i++) {
            passvalue = selCheckboxObj[i].value.split("_");// 在每个"_"处进行分解。
            pass(passvalue[0], passvalue[1], passvalue[2], 'all');
        }

    }
    function rows(ob) {
//        ob.style.background = '#9ACD32';
        ob.style.background = '#eefaee';
    }
    function outrows(ob) {
        ob.style.background = '#eefaee';
    }
    function toggleselect(comment, replay) {
        var comments = comment+'-'+replay;
        if ($('#'+comments+' input').eq(0).attr('checked')=='checked') {
            $('#'+comments+' input').eq(0).attr('checked', false);
        } else {
            $('#'+comments+' input').eq(0).attr('checked', true);

        }
    }
    $(function() {
        var selCheckboxObj = $("input[name='ids']");
        if (selCheckboxObj.length==0) {
            window.location.href = "http://my.jjwxc.net/backend/comment_check.php";
        }
        $('#check').click(function() {
            if ($('#check').attr('checked')) {
                $(':checkbox:not(0)').attr('checked', true);
            } else {
                $(':checkbox:not(0)').attr('checked', false);
            }
        })
    })

</script>
<form name="frmLogList" method="post"  action="comment_check.php" >
    <table width="1024"  border="0" align="center" cellpadding="4" cellspacing="1" bgcolor="#009900" class="mouse" id="tb">
        <tr bgcolor="#FFF">
            <td colspan="2" align="left">
                <b>当日评审字数：<font color="red">0</font></b><br/><br/>
                <b>历史总评审字数：<font color="red">802336</font></b><br/><br/>                
                <span style="color:red"><b>【数据更新时间： 2015年02月17日 00:00:00】</b></span>
            </td>
        </tr>
        <tr bgcolor="#FFF">
            <td colspan="2" align="left">
                <font color="red">
                <b>审核不通过条件：</b><br/><br/>
                1、含有垃圾广告，比如：开发票，卖枪支，找小姐等等。 2、含有色情信息（有亲热描写）。3、含有联系方式，比如QQ，手机号码，邮箱等等 4、含有外站链接。</font>
            </td>

        </tr>
        <tr align="center"  bgcolor="#9FD59E">
            <td width="20">&nbsp;</td>
            <td width="680" align="center" style="font-size: 14px;">评论内容</td>
        </tr>
                    <tr align="right" bgcolor="#eefaee" id = "167938-32996" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="167938_32996_2135677" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(167938,32996)">
                        墨仔：是的哈哈哈哈                    </div>
            <center>
                <span id='167938-32996Recalculation'><input type="button" id ="123167938"  onclick="pass(167938,32996,2135677,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='167938-32996Recalculationdel'><input type="button" id ="123167938" onclick="del(167938,32996,2135677)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "192452-44605" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="192452_44605_2278581" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(192452,44605)">
                        呜哈：<font style="background-color: yellow;font-weight: bold;">745038155</font>@qq.com<br>跪求～～～～                    </div>
            <center>
                <span id='192452-44605Recalculation'><input type="button" id ="123192452"  onclick="pass(192452,44605,2278581,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='192452-44605Recalculationdel'><input type="button" id ="123192452" onclick="del(192452,44605,2278581)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "17197-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="17197_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(17197,0)">
                        kuailede：决定不跟了，简直不可理喻。                    </div>
            <center>
                <span id='17197-0Recalculation'><input type="button" id ="12317197"  onclick="pass(17197,0,196136,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='17197-0Recalculationdel'><input type="button" id ="12317197" onclick="del(17197,0,196136)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "173344-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="173344_0_2266317" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(173344,0)">
                        青霖：小道君                    </div>
            <center>
                <span id='173344-0Recalculation'><input type="button" id ="123173344"  onclick="pass(173344,0,2266317,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='173344-0Recalculationdel'><input type="button" id ="123173344" onclick="del(173344,0,2266317)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "11948-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="11948_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(11948,0)">
                        晨：大人,偶坚决投小凌一票!!!!!!!<br>                    </div>
            <center>
                <span id='11948-0Recalculation'><input type="button" id ="12311948"  onclick="pass(11948,0,196136,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='11948-0Recalculationdel'><input type="button" id ="12311948" onclick="del(11948,0,196136)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16818-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16818_0_196949" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16818,0)">
                        rhea：难道传说中的花心九其实?....哎呀,怎么没了呢我那个心痒痒呀呵呵                    </div>
            <center>
                <span id='16818-0Recalculation'><input type="button" id ="12316818"  onclick="pass(16818,0,196949,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16818-0Recalculationdel'><input type="button" id ="12316818" onclick="del(16818,0,196949)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "176838-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="176838_0_2307154" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(176838,0)">
                        gun  and   鱿鱼：gun 啊<br>&lt;font color=#009900&gt;此评论发自晋江安卓手机APP客户端(http://m.jjwxc.net/download/android/)&lt;/font&gt;                    </div>
            <center>
                <span id='176838-0Recalculation'><input type="button" id ="123176838"  onclick="pass(176838,0,2307154,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='176838-0Recalculationdel'><input type="button" id ="123176838" onclick="del(176838,0,2307154)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "11682-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="11682_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(11682,0)">
                        大脸：小宝加油~~~                    </div>
            <center>
                <span id='11682-0Recalculation'><input type="button" id ="12311682"  onclick="pass(11682,0,196136,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='11682-0Recalculationdel'><input type="button" id ="12311682" onclick="del(11682,0,196136)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16771-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16771_0_196908" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16771,0)">
                        J：女主也太悬乎了吧里面的其他人整个就似群没脑子的人样牵着鼻子走                    </div>
            <center>
                <span id='16771-0Recalculation'><input type="button" id ="12316771"  onclick="pass(16771,0,196908,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16771-0Recalculationdel'><input type="button" id ="12316771" onclick="del(16771,0,196908)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "176829-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="176829_0_2307154" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(176829,0)">
                        深渊：啊啊啊，求表完结T_T<br>&lt;font color=#009900&gt;此评论发自晋江手机站(http://m.jjwxc.com/)&lt;/font&gt;                    </div>
            <center>
                <span id='176829-0Recalculation'><input type="button" id ="123176829"  onclick="pass(176829,0,2307154,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='176829-0Recalculationdel'><input type="button" id ="123176829" onclick="del(176829,0,2307154)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16736-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16736_0_196490" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16736,0)">
                        65：很棒!继续加油,等下文.                    </div>
            <center>
                <span id='16736-0Recalculation'><input type="button" id ="12316736"  onclick="pass(16736,0,196490,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16736-0Recalculationdel'><input type="button" id ="12316736" onclick="del(16736,0,196490)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "142959-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="142959_0_2317349" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(142959,0)">
                        lalal：下一话预感要虐了啊……怎么办                    </div>
            <center>
                <span id='142959-0Recalculation'><input type="button" id ="123142959"  onclick="pass(142959,0,2317349,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='142959-0Recalculationdel'><input type="button" id ="123142959" onclick="del(142959,0,2317349)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "7516-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="7516_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(7516,0)">
                        大脸：小宝加油啊~                    </div>
            <center>
                <span id='7516-0Recalculation'><input type="button" id ="1237516"  onclick="pass(7516,0,196136,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='7516-0Recalculationdel'><input type="button" id ="1237516" onclick="del(7516,0,196136)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "12961-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="12961_0_196029" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(12961,0)">
                        蓝水寒冰：支持天天总攻                    </div>
            <center>
                <span id='12961-0Recalculation'><input type="button" id ="12312961"  onclick="pass(12961,0,196029,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='12961-0Recalculationdel'><input type="button" id ="12312961" onclick="del(12961,0,196029)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "14717-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="14717_0_196312" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(14717,0)">
                        萍儿：我的橙子猪啊，如果是你的话给我把这更新起啊。                    </div>
            <center>
                <span id='14717-0Recalculation'><input type="button" id ="12314717"  onclick="pass(14717,0,196312,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='14717-0Recalculationdel'><input type="button" id ="12314717" onclick="del(14717,0,196312)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "15438-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="15438_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(15438,0)">
                        ww：大大不希望凌韵死啊！！！一点也不希望啊！！！<br>                    </div>
            <center>
                <span id='15438-0Recalculation'><input type="button" id ="12315438"  onclick="pass(15438,0,196136,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='15438-0Recalculationdel'><input type="button" id ="12315438" onclick="del(15438,0,196136)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "176933-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="176933_0_2307154" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(176933,0)">
                        路人甲：直播洗澡直播洗澡！！！<br>&lt;font color=#009900&gt;此评论发自晋江安卓手机APP客户端(http://m.jjwxc.net/download/android/)&lt;/font&gt;                    </div>
            <center>
                <span id='176933-0Recalculation'><input type="button" id ="123176933"  onclick="pass(176933,0,2307154,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='176933-0Recalculationdel'><input type="button" id ="123176933" onclick="del(176933,0,2307154)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "133181-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="133181_0_2264374" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(133181,0)">
                        可口：春节好。祝健康，快乐，幸福。<br>多多写文，咱们一起萌。                    </div>
            <center>
                <span id='133181-0Recalculation'><input type="button" id ="123133181"  onclick="pass(133181,0,2264374,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='133181-0Recalculationdel'><input type="button" id ="123133181" onclick="del(133181,0,2264374)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "17009-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="17009_0_196459" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(17009,0)">
                        s811fish：作者很勤快，不错！                    </div>
            <center>
                <span id='17009-0Recalculation'><input type="button" id ="12317009"  onclick="pass(17009,0,196459,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='17009-0Recalculationdel'><input type="button" id ="12317009" onclick="del(17009,0,196459)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16966-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16966_0_196654" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16966,0)">
                        xing：比&amp;lt;今天开始当魔王&gt;的还惨.可怜啊!!                    </div>
            <center>
                <span id='16966-0Recalculation'><input type="button" id ="12316966"  onclick="pass(16966,0,196654,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16966-0Recalculationdel'><input type="button" id ="12316966" onclick="del(16966,0,196654)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "250575-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="250575_0_2308233" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(250575,0)">
                        催更：等待中<br>&lt;font color=#009900&gt;此评论发自晋江手机站(http://m.jjwxc.com/)&lt;/font&gt;                    </div>
            <center>
                <span id='250575-0Recalculation'><input type="button" id ="123250575"  onclick="pass(250575,0,2308233,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='250575-0Recalculationdel'><input type="button" id ="123250575" onclick="del(250575,0,2308233)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "91814-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="91814_0_2323133" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(91814,0)">
                        穆瑾：小受竟然忘了⊙▽⊙预感以后会被攻因为这个粗掉很多次<br>&lt;font color=#009900&gt;此评论发自晋江手机站(http://m.jjwxc.com/)&lt;/font&gt;                    </div>
            <center>
                <span id='91814-0Recalculation'><input type="button" id ="12391814"  onclick="pass(91814,0,2323133,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='91814-0Recalculationdel'><input type="button" id ="12391814" onclick="del(91814,0,2323133)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "125176-42516" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="125176_42516_2043685" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(125176,42516)">
                        <font style="background-color: yellow;font-weight: bold;">16412503</font>：么么哒，我又回来重温了几遍，太好看惹?<br>&lt;font color=#009900&gt;此评论发自晋江安卓手机APP客户端(http://m.jjwxc.net/download/android/)&lt;/font&gt;                    </div>
            <center>
                <span id='125176-42516Recalculation'><input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='125176-42516Recalculationdel'><input type="button" id ="123125176" onclick="del(125176,42516,2043685)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "14659-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="14659_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(14659,0)">
                        ling：看到更新就高兴，看到大大好了更高兴!                    </div>
            <center>
                <span id='14659-0Recalculation'><input type="button" id ="12314659"  onclick="pass(14659,0,196136,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='14659-0Recalculationdel'><input type="button" id ="12314659" onclick="del(14659,0,196136)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "52678-38055" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="52678_38055_1914340" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(52678,38055)">
                        朱女：挺尸……                    </div>
            <center>
                <span id='52678-38055Recalculation'><input type="button" id ="12352678"  onclick="pass(52678,38055,1914340,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='52678-38055Recalculationdel'><input type="button" id ="12352678" onclick="del(52678,38055,1914340)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16757-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16757_0_196519" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16757,0)">
                        葵花籽：什么小屁孩                    </div>
            <center>
                <span id='16757-0Recalculation'><input type="button" id ="12316757"  onclick="pass(16757,0,196519,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16757-0Recalculationdel'><input type="button" id ="12316757" onclick="del(16757,0,196519)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "17201-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="17201_0_196838" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(17201,0)">
                        埃及猫咪：貌似大大的文都打不上分?试了好几个地方了,狂汗<br>其实看了不少大大的文才来打分实在是有点不好意思哦~~<br>偶很喜欢虐文,慕&amp;lt;第七夜&gt;之名而来,可惜被锁了.不知可否有重开之望...                    </div>
            <center>
                <span id='17201-0Recalculation'><input type="button" id ="12317201"  onclick="pass(17201,0,196838,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='17201-0Recalculationdel'><input type="button" id ="12317201" onclick="del(17201,0,196838)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "247769-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="247769_0_2186130" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(247769,0)">
                        路人甲：我怎么感觉竖起了对敌的flag呢←_←<br>&lt;font color=#009900&gt;此评论发自晋江手机站(http://wap.jjwxc.net/)&lt;/font&gt;                    </div>
            <center>
                <span id='247769-0Recalculation'><input type="button" id ="123247769"  onclick="pass(247769,0,2186130,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='247769-0Recalculationdel'><input type="button" id ="123247769" onclick="del(247769,0,2186130)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "13869-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="13869_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(13869,0)">
                        臭YA：小柳怎么样了.!?<br>为什么总是不见写他...<br>静雅好象好难选择呀...                    </div>
            <center>
                <span id='13869-0Recalculation'><input type="button" id ="12313869"  onclick="pass(13869,0,196136,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='13869-0Recalculationdel'><input type="button" id ="12313869" onclick="del(13869,0,196136)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16774-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16774_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16774,0)">
                        VV：上章自己说不把那男主弄4..现在还来这套..TMD.2B                    </div>
            <center>
                <span id='16774-0Recalculation'><input type="button" id ="12316774"  onclick="pass(16774,0,196136,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16774-0Recalculationdel'><input type="button" id ="12316774" onclick="del(16774,0,196136)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "11750-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="11750_0_196481" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(11750,0)">
                        呆~：支持!!加油!!                    </div>
            <center>
                <span id='11750-0Recalculation'><input type="button" id ="12311750"  onclick="pass(11750,0,196481,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='11750-0Recalculationdel'><input type="button" id ="12311750" onclick="del(11750,0,196481)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16890-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16890_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16890,0)">
                        牛牛：已经可以预见到以后有多虐了。。。。                    </div>
            <center>
                <span id='16890-0Recalculation'><input type="button" id ="12316890"  onclick="pass(16890,0,196136,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16890-0Recalculationdel'><input type="button" id ="12316890" onclick="del(16890,0,196136)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "128255-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="128255_0_2281167" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(128255,0)">
                        叶孤城：撒花<br>&lt;font color=#009900&gt;此评论发自晋江手机站(http://m.jjwxc.com/)&lt;/font&gt;                    </div>
            <center>
                <span id='128255-0Recalculation'><input type="button" id ="123128255"  onclick="pass(128255,0,2281167,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='128255-0Recalculationdel'><input type="button" id ="123128255" onclick="del(128255,0,2281167)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "7859-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="7859_0_196908" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(7859,0)">
                        风：越看越喜欢了,不懂有些大大为何非要让女主受伤害呢,那不是显得她身边的男主太无能了吗.                    </div>
            <center>
                <span id='7859-0Recalculation'><input type="button" id ="1237859"  onclick="pass(7859,0,196908,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='7859-0Recalculationdel'><input type="button" id ="1237859" onclick="del(7859,0,196908)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "7985-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="7985_0_196459" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(7985,0)">
                        00：在后宫不斗，那生活多平淡啊                    </div>
            <center>
                <span id='7985-0Recalculation'><input type="button" id ="1237985"  onclick="pass(7985,0,196459,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='7985-0Recalculationdel'><input type="button" id ="1237985" onclick="del(7985,0,196459)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "12607-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="12607_0_196908" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(12607,0)">
                        ：更新更新哦                    </div>
            <center>
                <span id='12607-0Recalculation'><input type="button" id ="12312607"  onclick="pass(12607,0,196908,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='12607-0Recalculationdel'><input type="button" id ="12312607" onclick="del(12607,0,196908)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "266260-42126" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="266260_42126_2230334" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(266260,42126)">
                        竹野 灯：哈哈哈哈，up主好好玩<br>&lt;font color=#009900&gt;此评论发自晋江手机站(http://wap.jjwxc.net/)&lt;/font&gt;                    </div>
            <center>
                <span id='266260-42126Recalculation'><input type="button" id ="123266260"  onclick="pass(266260,42126,2230334,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='266260-42126Recalculationdel'><input type="button" id ="123266260" onclick="del(266260,42126,2230334)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "129750-34985" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="129750_34985_2174576" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(129750,34985)">
                        画昔：是有关于赤司的脑洞，就是不知道选中二版本的还是疯狂吐槽版本的。ヽ(≧Д≦)ノ                    </div>
            <center>
                <span id='129750-34985Recalculation'><input type="button" id ="123129750"  onclick="pass(129750,34985,2174576,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='129750-34985Recalculationdel'><input type="button" id ="123129750" onclick="del(129750,34985,2174576)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "142777-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="142777_0_2317349" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(142777,0)">
                        lovelyz：开虐的节奏<br>&lt;font color=#009900&gt;此评论发自晋江手机站(http://m.jjwxc.com/)&lt;/font&gt;                    </div>
            <center>
                <span id='142777-0Recalculation'><input type="button" id ="123142777"  onclick="pass(142777,0,2317349,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='142777-0Recalculationdel'><input type="button" id ="123142777" onclick="del(142777,0,2317349)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16945-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16945_0_196957" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16945,0)">
                        123：这样的女主我喜欢,这才是现代过去的人呢.那些把穿越过去的女主写的懦弱无比的,真是让人越看越郁闷.                    </div>
            <center>
                <span id='16945-0Recalculation'><input type="button" id ="12316945"  onclick="pass(16945,0,196957,'one')" value="√通过" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16945-0Recalculationdel'><input type="button" id ="12316945" onclick="del(16945,0,196957)" value="×不通过" style="color:red;"></span>            </center>
            </td>
            </tr>
            <tr  bgcolor="#eefaee"><td colspan="3" align="center"><a href="http://my.jjwxc.net/backend/comment_check.php">下一页</a></td></tr>        <tr bgcolor="#eefaee">
            <td colspan="2" align="center">
                <input type="button" name="buttondel" id = "buttondel" value="√批量通过" onclick="batchControll()" style="color:blue;"/>
            </td>

        </tr>
        <tr bgcolor="#eefaee">
            <td colspan="2" align="left">
                <font color="red">
                <b>审核不通过条件：</b><br/><br/>
                1、含有垃圾广告，比如：开发票，卖枪支，找小姐等等。 2、含有色情信息（有亲热描写）。3、含有联系方式，比如QQ，手机号码，邮箱等等 4、含有外站链接。</font><br/><br/> 
                <font color="blue">
                邀您评论评审奖励标准：每审核3000字(6000个字节)奖励2点晋江币，每周按照实际有效审核数据进行结算．结算后可在【我的余额】中查看。
                </font>
            </td>
        </tr>

    </table>
</form>
<div align = "center">
    <font color="red">运行总耗时：0.036336183547974 seconds  当前运行时间：2015-02-17 15:17:09</font>
</div>
>>> print find_result(cont)
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">802336</font>']
>>> aelems = extract_val(cont)
['<input type="button" id ="123167938"  onclick="pass(167938,32996,2135677,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123192452"  onclick="pass(192452,44605,2278581,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317197"  onclick="pass(17197,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123173344"  onclick="pass(173344,0,2266317,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311948"  onclick="pass(11948,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316818"  onclick="pass(16818,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176838"  onclick="pass(176838,0,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311682"  onclick="pass(11682,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316771"  onclick="pass(16771,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176829"  onclick="pass(176829,0,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316736"  onclick="pass(16736,0,196490,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123142959"  onclick="pass(142959,0,2317349,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237516"  onclick="pass(7516,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312961"  onclick="pass(12961,0,196029,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314717"  onclick="pass(14717,0,196312,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315438"  onclick="pass(15438,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176933"  onclick="pass(176933,0,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123133181"  onclick="pass(133181,0,2264374,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317009"  onclick="pass(17009,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316966"  onclick="pass(16966,0,196654,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123250575"  onclick="pass(250575,0,2308233,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12391814"  onclick="pass(91814,0,2323133,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314659"  onclick="pass(14659,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12352678"  onclick="pass(52678,38055,1914340,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316757"  onclick="pass(16757,0,196519,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317201"  onclick="pass(17201,0,196838,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123247769"  onclick="pass(247769,0,2186130,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313869"  onclick="pass(13869,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316774"  onclick="pass(16774,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311750"  onclick="pass(11750,0,196481,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316890"  onclick="pass(16890,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123128255"  onclick="pass(128255,0,2281167,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237859"  onclick="pass(7859,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237985"  onclick="pass(7985,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312607"  onclick="pass(12607,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123266260"  onclick="pass(266260,42126,2230334,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123129750"  onclick="pass(129750,34985,2174576,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123142777"  onclick="pass(142777,0,2317349,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316945"  onclick="pass(16945,0,196957,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="123167938"  onclick="pass(167938,32996,2135677,'one')" value="√通过"
onclick="pass(167938,32996,2135677,'one')"
<input type="button" id ="123192452"  onclick="pass(192452,44605,2278581,'one')" value="√通过"
onclick="pass(192452,44605,2278581,'one')"
<input type="button" id ="12317197"  onclick="pass(17197,0,196136,'one')" value="√通过"
onclick="pass(17197,0,196136,'one')"
<input type="button" id ="123173344"  onclick="pass(173344,0,2266317,'one')" value="√通过"
onclick="pass(173344,0,2266317,'one')"
<input type="button" id ="12311948"  onclick="pass(11948,0,196136,'one')" value="√通过"
onclick="pass(11948,0,196136,'one')"
<input type="button" id ="12316818"  onclick="pass(16818,0,196949,'one')" value="√通过"
onclick="pass(16818,0,196949,'one')"
<input type="button" id ="123176838"  onclick="pass(176838,0,2307154,'one')" value="√通过"
onclick="pass(176838,0,2307154,'one')"
<input type="button" id ="12311682"  onclick="pass(11682,0,196136,'one')" value="√通过"
onclick="pass(11682,0,196136,'one')"
<input type="button" id ="12316771"  onclick="pass(16771,0,196908,'one')" value="√通过"
onclick="pass(16771,0,196908,'one')"
<input type="button" id ="123176829"  onclick="pass(176829,0,2307154,'one')" value="√通过"
onclick="pass(176829,0,2307154,'one')"
<input type="button" id ="12316736"  onclick="pass(16736,0,196490,'one')" value="√通过"
onclick="pass(16736,0,196490,'one')"
<input type="button" id ="123142959"  onclick="pass(142959,0,2317349,'one')" value="√通过"
onclick="pass(142959,0,2317349,'one')"
<input type="button" id ="1237516"  onclick="pass(7516,0,196136,'one')" value="√通过"
onclick="pass(7516,0,196136,'one')"
<input type="button" id ="12312961"  onclick="pass(12961,0,196029,'one')" value="√通过"
onclick="pass(12961,0,196029,'one')"
<input type="button" id ="12314717"  onclick="pass(14717,0,196312,'one')" value="√通过"
onclick="pass(14717,0,196312,'one')"
<input type="button" id ="12315438"  onclick="pass(15438,0,196136,'one')" value="√通过"
onclick="pass(15438,0,196136,'one')"
<input type="button" id ="123176933"  onclick="pass(176933,0,2307154,'one')" value="√通过"
onclick="pass(176933,0,2307154,'one')"
<input type="button" id ="123133181"  onclick="pass(133181,0,2264374,'one')" value="√通过"
onclick="pass(133181,0,2264374,'one')"
<input type="button" id ="12317009"  onclick="pass(17009,0,196459,'one')" value="√通过"
onclick="pass(17009,0,196459,'one')"
<input type="button" id ="12316966"  onclick="pass(16966,0,196654,'one')" value="√通过"
onclick="pass(16966,0,196654,'one')"
<input type="button" id ="123250575"  onclick="pass(250575,0,2308233,'one')" value="√通过"
onclick="pass(250575,0,2308233,'one')"
<input type="button" id ="12391814"  onclick="pass(91814,0,2323133,'one')" value="√通过"
onclick="pass(91814,0,2323133,'one')"
<input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,'one')" value="√通过"
onclick="pass(125176,42516,2043685,'one')"
<input type="button" id ="12314659"  onclick="pass(14659,0,196136,'one')" value="√通过"
onclick="pass(14659,0,196136,'one')"
<input type="button" id ="12352678"  onclick="pass(52678,38055,1914340,'one')" value="√通过"
onclick="pass(52678,38055,1914340,'one')"
<input type="button" id ="12316757"  onclick="pass(16757,0,196519,'one')" value="√通过"
onclick="pass(16757,0,196519,'one')"
<input type="button" id ="12317201"  onclick="pass(17201,0,196838,'one')" value="√通过"
onclick="pass(17201,0,196838,'one')"
<input type="button" id ="123247769"  onclick="pass(247769,0,2186130,'one')" value="√通过"
onclick="pass(247769,0,2186130,'one')"
<input type="button" id ="12313869"  onclick="pass(13869,0,196136,'one')" value="√通过"
onclick="pass(13869,0,196136,'one')"
<input type="button" id ="12316774"  onclick="pass(16774,0,196136,'one')" value="√通过"
onclick="pass(16774,0,196136,'one')"
<input type="button" id ="12311750"  onclick="pass(11750,0,196481,'one')" value="√通过"
onclick="pass(11750,0,196481,'one')"
<input type="button" id ="12316890"  onclick="pass(16890,0,196136,'one')" value="√通过"
onclick="pass(16890,0,196136,'one')"
<input type="button" id ="123128255"  onclick="pass(128255,0,2281167,'one')" value="√通过"
onclick="pass(128255,0,2281167,'one')"
<input type="button" id ="1237859"  onclick="pass(7859,0,196908,'one')" value="√通过"
onclick="pass(7859,0,196908,'one')"
<input type="button" id ="1237985"  onclick="pass(7985,0,196459,'one')" value="√通过"
onclick="pass(7985,0,196459,'one')"
<input type="button" id ="12312607"  onclick="pass(12607,0,196908,'one')" value="√通过"
onclick="pass(12607,0,196908,'one')"
<input type="button" id ="123266260"  onclick="pass(266260,42126,2230334,'one')" value="√通过"
onclick="pass(266260,42126,2230334,'one')"
<input type="button" id ="123129750"  onclick="pass(129750,34985,2174576,'one')" value="√通过"
onclick="pass(129750,34985,2174576,'one')"
<input type="button" id ="123142777"  onclick="pass(142777,0,2317349,'one')" value="√通过"
onclick="pass(142777,0,2317349,'one')"
<input type="button" id ="12316945"  onclick="pass(16945,0,196957,'one')" value="√通过"
onclick="pass(16945,0,196957,'one')"
>>> for i in range(10):
	op = opener.open(url)
	cont = op.read()
	aelems = extract_val(cont)
	print find_result(cont)
	for aelem in aelems:
		values = aelem.split(',')
		print values[0],' ',values[1],' ',values[2]
		commentid = values[0]
		replyid = values[1]
		novelid = values[2]
		url_read = url + '?act=pass&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid
		request2 = urllib2.Request(url_read, headers=headers)
		response_check = urllib2.urlopen(request2)
		print response_check.read()
	time.sleep(8.0)

	
['<input type="button" id ="123167938"  onclick="pass(167938,32996,2135677,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123192452"  onclick="pass(192452,44605,2278581,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317197"  onclick="pass(17197,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123173344"  onclick="pass(173344,0,2266317,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311948"  onclick="pass(11948,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316818"  onclick="pass(16818,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176838"  onclick="pass(176838,0,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311682"  onclick="pass(11682,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316771"  onclick="pass(16771,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176829"  onclick="pass(176829,0,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316736"  onclick="pass(16736,0,196490,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123142959"  onclick="pass(142959,0,2317349,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237516"  onclick="pass(7516,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312961"  onclick="pass(12961,0,196029,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314717"  onclick="pass(14717,0,196312,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315438"  onclick="pass(15438,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176933"  onclick="pass(176933,0,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123133181"  onclick="pass(133181,0,2264374,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317009"  onclick="pass(17009,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316966"  onclick="pass(16966,0,196654,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123250575"  onclick="pass(250575,0,2308233,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12391814"  onclick="pass(91814,0,2323133,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314659"  onclick="pass(14659,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12352678"  onclick="pass(52678,38055,1914340,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316757"  onclick="pass(16757,0,196519,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317201"  onclick="pass(17201,0,196838,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123247769"  onclick="pass(247769,0,2186130,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313869"  onclick="pass(13869,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316774"  onclick="pass(16774,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311750"  onclick="pass(11750,0,196481,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316890"  onclick="pass(16890,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123128255"  onclick="pass(128255,0,2281167,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237859"  onclick="pass(7859,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237985"  onclick="pass(7985,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312607"  onclick="pass(12607,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123266260"  onclick="pass(266260,42126,2230334,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123129750"  onclick="pass(129750,34985,2174576,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123142777"  onclick="pass(142777,0,2317349,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316945"  onclick="pass(16945,0,196957,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="123167938"  onclick="pass(167938,32996,2135677,'one')" value="√通过"
onclick="pass(167938,32996,2135677,'one')"
<input type="button" id ="123192452"  onclick="pass(192452,44605,2278581,'one')" value="√通过"
onclick="pass(192452,44605,2278581,'one')"
<input type="button" id ="12317197"  onclick="pass(17197,0,196136,'one')" value="√通过"
onclick="pass(17197,0,196136,'one')"
<input type="button" id ="123173344"  onclick="pass(173344,0,2266317,'one')" value="√通过"
onclick="pass(173344,0,2266317,'one')"
<input type="button" id ="12311948"  onclick="pass(11948,0,196136,'one')" value="√通过"
onclick="pass(11948,0,196136,'one')"
<input type="button" id ="12316818"  onclick="pass(16818,0,196949,'one')" value="√通过"
onclick="pass(16818,0,196949,'one')"
<input type="button" id ="123176838"  onclick="pass(176838,0,2307154,'one')" value="√通过"
onclick="pass(176838,0,2307154,'one')"
<input type="button" id ="12311682"  onclick="pass(11682,0,196136,'one')" value="√通过"
onclick="pass(11682,0,196136,'one')"
<input type="button" id ="12316771"  onclick="pass(16771,0,196908,'one')" value="√通过"
onclick="pass(16771,0,196908,'one')"
<input type="button" id ="123176829"  onclick="pass(176829,0,2307154,'one')" value="√通过"
onclick="pass(176829,0,2307154,'one')"
<input type="button" id ="12316736"  onclick="pass(16736,0,196490,'one')" value="√通过"
onclick="pass(16736,0,196490,'one')"
<input type="button" id ="123142959"  onclick="pass(142959,0,2317349,'one')" value="√通过"
onclick="pass(142959,0,2317349,'one')"
<input type="button" id ="1237516"  onclick="pass(7516,0,196136,'one')" value="√通过"
onclick="pass(7516,0,196136,'one')"
<input type="button" id ="12312961"  onclick="pass(12961,0,196029,'one')" value="√通过"
onclick="pass(12961,0,196029,'one')"
<input type="button" id ="12314717"  onclick="pass(14717,0,196312,'one')" value="√通过"
onclick="pass(14717,0,196312,'one')"
<input type="button" id ="12315438"  onclick="pass(15438,0,196136,'one')" value="√通过"
onclick="pass(15438,0,196136,'one')"
<input type="button" id ="123176933"  onclick="pass(176933,0,2307154,'one')" value="√通过"
onclick="pass(176933,0,2307154,'one')"
<input type="button" id ="123133181"  onclick="pass(133181,0,2264374,'one')" value="√通过"
onclick="pass(133181,0,2264374,'one')"
<input type="button" id ="12317009"  onclick="pass(17009,0,196459,'one')" value="√通过"
onclick="pass(17009,0,196459,'one')"
<input type="button" id ="12316966"  onclick="pass(16966,0,196654,'one')" value="√通过"
onclick="pass(16966,0,196654,'one')"
<input type="button" id ="123250575"  onclick="pass(250575,0,2308233,'one')" value="√通过"
onclick="pass(250575,0,2308233,'one')"
<input type="button" id ="12391814"  onclick="pass(91814,0,2323133,'one')" value="√通过"
onclick="pass(91814,0,2323133,'one')"
<input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,'one')" value="√通过"
onclick="pass(125176,42516,2043685,'one')"
<input type="button" id ="12314659"  onclick="pass(14659,0,196136,'one')" value="√通过"
onclick="pass(14659,0,196136,'one')"
<input type="button" id ="12352678"  onclick="pass(52678,38055,1914340,'one')" value="√通过"
onclick="pass(52678,38055,1914340,'one')"
<input type="button" id ="12316757"  onclick="pass(16757,0,196519,'one')" value="√通过"
onclick="pass(16757,0,196519,'one')"
<input type="button" id ="12317201"  onclick="pass(17201,0,196838,'one')" value="√通过"
onclick="pass(17201,0,196838,'one')"
<input type="button" id ="123247769"  onclick="pass(247769,0,2186130,'one')" value="√通过"
onclick="pass(247769,0,2186130,'one')"
<input type="button" id ="12313869"  onclick="pass(13869,0,196136,'one')" value="√通过"
onclick="pass(13869,0,196136,'one')"
<input type="button" id ="12316774"  onclick="pass(16774,0,196136,'one')" value="√通过"
onclick="pass(16774,0,196136,'one')"
<input type="button" id ="12311750"  onclick="pass(11750,0,196481,'one')" value="√通过"
onclick="pass(11750,0,196481,'one')"
<input type="button" id ="12316890"  onclick="pass(16890,0,196136,'one')" value="√通过"
onclick="pass(16890,0,196136,'one')"
<input type="button" id ="123128255"  onclick="pass(128255,0,2281167,'one')" value="√通过"
onclick="pass(128255,0,2281167,'one')"
<input type="button" id ="1237859"  onclick="pass(7859,0,196908,'one')" value="√通过"
onclick="pass(7859,0,196908,'one')"
<input type="button" id ="1237985"  onclick="pass(7985,0,196459,'one')" value="√通过"
onclick="pass(7985,0,196459,'one')"
<input type="button" id ="12312607"  onclick="pass(12607,0,196908,'one')" value="√通过"
onclick="pass(12607,0,196908,'one')"
<input type="button" id ="123266260"  onclick="pass(266260,42126,2230334,'one')" value="√通过"
onclick="pass(266260,42126,2230334,'one')"
<input type="button" id ="123129750"  onclick="pass(129750,34985,2174576,'one')" value="√通过"
onclick="pass(129750,34985,2174576,'one')"
<input type="button" id ="123142777"  onclick="pass(142777,0,2317349,'one')" value="√通过"
onclick="pass(142777,0,2317349,'one')"
<input type="button" id ="12316945"  onclick="pass(16945,0,196957,'one')" value="√通过"
onclick="pass(16945,0,196957,'one')"
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">802336</font>']
167938   32996   2135677
1
192452   44605   2278581
1
17197   0   196136
1
173344   0   2266317
1
11948   0   196136
1
16818   0   196949
1
176838   0   2307154
1
11682   0   196136
1
16771   0   196908
1
176829   0   2307154
1
16736   0   196490
1
142959   0   2317349
1
7516   0   196136
1
12961   0   196029
1
14717   0   196312
1
15438   0   196136
1
176933   0   2307154
1
133181   0   2264374
1
17009   0   196459
1
16966   0   196654
1
250575   0   2308233
1
91814   0   2323133
1
125176   42516   2043685
1
14659   0   196136
1
52678   38055   1914340
1
16757   0   196519
1
17201   0   196838
1
247769   0   2186130
1
13869   0   196136
1
16774   0   196136
1
11750   0   196481
1
16890   0   196136
1
128255   0   2281167
1
7859   0   196908
1
7985   0   196459
1
12607   0   196908
1
266260   42126   2230334
1
129750   34985   2174576
1
142777   0   2317349
1
16945   0   196957
1
['<input type="button" id ="12311963"  onclick="pass(11963,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123106976"  onclick="pass(106976,0,2322403,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316830"  onclick="pass(16830,0,196900,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123158785"  onclick="pass(158785,0,2294819,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237436"  onclick="pass(7436,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12388343"  onclick="pass(88343,0,1194650,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316124"  onclick="pass(16124,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12362234"  onclick="pass(62234,44637,1866123,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12383328"  onclick="pass(83328,0,2363778,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315221"  onclick="pass(15221,0,196742,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312837"  onclick="pass(12837,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1239304"  onclick="pass(9304,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237999"  onclick="pass(7999,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237403"  onclick="pass(7403,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12388534"  onclick="pass(88534,0,1194687,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123123773"  onclick="pass(123773,53687,2069151,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123188905"  onclick="pass(188905,0,2280358,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317105"  onclick="pass(17105,0,196253,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123109285"  onclick="pass(109285,0,2147636,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123113858"  onclick="pass(113858,34702,2252753,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311692"  onclick="pass(11692,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315265"  onclick="pass(15265,0,196162,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12387798"  onclick="pass(87798,0,2388248,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237673"  onclick="pass(7673,0,196162,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316974"  onclick="pass(16974,0,196162,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316480"  onclick="pass(16480,0,196893,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316829"  onclick="pass(16829,0,196519,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123205150"  onclick="pass(205150,0,2101336,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123115483"  onclick="pass(115483,0,1975072,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315382"  onclick="pass(15382,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123110985"  onclick="pass(110985,36027,2298596,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316237"  onclick="pass(16237,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176791"  onclick="pass(176791,47149,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316839"  onclick="pass(16839,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314831"  onclick="pass(14831,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311688"  onclick="pass(11688,0,196021,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12310896"  onclick="pass(10896,0,196886,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313276"  onclick="pass(13276,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123110989"  onclick="pass(110989,36031,2298596,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1239807"  onclick="pass(9807,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12395737"  onclick="pass(95737,0,2362362,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12378081"  onclick="pass(78081,0,1670047,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314130"  onclick="pass(14130,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316714"  onclick="pass(16714,0,196002,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316204"  onclick="pass(16204,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12310763"  onclick="pass(10763,0,196519,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12388521"  onclick="pass(88521,0,1194656,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12361359"  onclick="pass(61359,57154,1725511,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315324"  onclick="pass(15324,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314037"  onclick="pass(14037,0,196871,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123146137"  onclick="pass(146137,0,2305357,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123158696"  onclick="pass(158696,0,2294145,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316811"  onclick="pass(16811,0,196162,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="12311963"  onclick="pass(11963,0,196908,'one')" value="√通过"
onclick="pass(11963,0,196908,'one')"
<input type="button" id ="123106976"  onclick="pass(106976,0,2322403,'one')" value="√通过"
onclick="pass(106976,0,2322403,'one')"
<input type="button" id ="12316830"  onclick="pass(16830,0,196900,'one')" value="√通过"
onclick="pass(16830,0,196900,'one')"
<input type="button" id ="123158785"  onclick="pass(158785,0,2294819,'one')" value="√通过"
onclick="pass(158785,0,2294819,'one')"
<input type="button" id ="1237436"  onclick="pass(7436,0,196908,'one')" value="√通过"
onclick="pass(7436,0,196908,'one')"
<input type="button" id ="12388343"  onclick="pass(88343,0,1194650,'one')" value="√通过"
onclick="pass(88343,0,1194650,'one')"
<input type="button" id ="12316124"  onclick="pass(16124,0,196908,'one')" value="√通过"
onclick="pass(16124,0,196908,'one')"
<input type="button" id ="12362234"  onclick="pass(62234,44637,1866123,'one')" value="√通过"
onclick="pass(62234,44637,1866123,'one')"
<input type="button" id ="12383328"  onclick="pass(83328,0,2363778,'one')" value="√通过"
onclick="pass(83328,0,2363778,'one')"
<input type="button" id ="12315221"  onclick="pass(15221,0,196742,'one')" value="√通过"
onclick="pass(15221,0,196742,'one')"
<input type="button" id ="12312837"  onclick="pass(12837,0,196908,'one')" value="√通过"
onclick="pass(12837,0,196908,'one')"
<input type="button" id ="1239304"  onclick="pass(9304,0,196459,'one')" value="√通过"
onclick="pass(9304,0,196459,'one')"
<input type="button" id ="1237999"  onclick="pass(7999,0,196908,'one')" value="√通过"
onclick="pass(7999,0,196908,'one')"
<input type="button" id ="1237403"  onclick="pass(7403,0,196949,'one')" value="√通过"
onclick="pass(7403,0,196949,'one')"
<input type="button" id ="12388534"  onclick="pass(88534,0,1194687,'one')" value="√通过"
onclick="pass(88534,0,1194687,'one')"
<input type="button" id ="123123773"  onclick="pass(123773,53687,2069151,'one')" value="√通过"
onclick="pass(123773,53687,2069151,'one')"
<input type="button" id ="123188905"  onclick="pass(188905,0,2280358,'one')" value="√通过"
onclick="pass(188905,0,2280358,'one')"
<input type="button" id ="12317105"  onclick="pass(17105,0,196253,'one')" value="√通过"
onclick="pass(17105,0,196253,'one')"
<input type="button" id ="123109285"  onclick="pass(109285,0,2147636,'one')" value="√通过"
onclick="pass(109285,0,2147636,'one')"
<input type="button" id ="123113858"  onclick="pass(113858,34702,2252753,'one')" value="√通过"
onclick="pass(113858,34702,2252753,'one')"
<input type="button" id ="12311692"  onclick="pass(11692,0,196908,'one')" value="√通过"
onclick="pass(11692,0,196908,'one')"
<input type="button" id ="12315265"  onclick="pass(15265,0,196162,'one')" value="√通过"
onclick="pass(15265,0,196162,'one')"
<input type="button" id ="12387798"  onclick="pass(87798,0,2388248,'one')" value="√通过"
onclick="pass(87798,0,2388248,'one')"
<input type="button" id ="1237673"  onclick="pass(7673,0,196162,'one')" value="√通过"
onclick="pass(7673,0,196162,'one')"
<input type="button" id ="12316974"  onclick="pass(16974,0,196162,'one')" value="√通过"
onclick="pass(16974,0,196162,'one')"
<input type="button" id ="12316480"  onclick="pass(16480,0,196893,'one')" value="√通过"
onclick="pass(16480,0,196893,'one')"
<input type="button" id ="12316829"  onclick="pass(16829,0,196519,'one')" value="√通过"
onclick="pass(16829,0,196519,'one')"
<input type="button" id ="123205150"  onclick="pass(205150,0,2101336,'one')" value="√通过"
onclick="pass(205150,0,2101336,'one')"
<input type="button" id ="123115483"  onclick="pass(115483,0,1975072,'one')" value="√通过"
onclick="pass(115483,0,1975072,'one')"
<input type="button" id ="12315382"  onclick="pass(15382,0,196136,'one')" value="√通过"
onclick="pass(15382,0,196136,'one')"
<input type="button" id ="123110985"  onclick="pass(110985,36027,2298596,'one')" value="√通过"
onclick="pass(110985,36027,2298596,'one')"
<input type="button" id ="12316237"  onclick="pass(16237,0,196459,'one')" value="√通过"
onclick="pass(16237,0,196459,'one')"
<input type="button" id ="123176791"  onclick="pass(176791,47149,2307154,'one')" value="√通过"
onclick="pass(176791,47149,2307154,'one')"
<input type="button" id ="12316839"  onclick="pass(16839,0,196136,'one')" value="√通过"
onclick="pass(16839,0,196136,'one')"
<input type="button" id ="12314831"  onclick="pass(14831,0,196949,'one')" value="√通过"
onclick="pass(14831,0,196949,'one')"
<input type="button" id ="12311688"  onclick="pass(11688,0,196021,'one')" value="√通过"
onclick="pass(11688,0,196021,'one')"
<input type="button" id ="12310896"  onclick="pass(10896,0,196886,'one')" value="√通过"
onclick="pass(10896,0,196886,'one')"
<input type="button" id ="12313276"  onclick="pass(13276,0,196949,'one')" value="√通过"
onclick="pass(13276,0,196949,'one')"
<input type="button" id ="123110989"  onclick="pass(110989,36031,2298596,'one')" value="√通过"
onclick="pass(110989,36031,2298596,'one')"
<input type="button" id ="1239807"  onclick="pass(9807,0,196949,'one')" value="√通过"
onclick="pass(9807,0,196949,'one')"
<input type="button" id ="12395737"  onclick="pass(95737,0,2362362,'one')" value="√通过"
onclick="pass(95737,0,2362362,'one')"
<input type="button" id ="12378081"  onclick="pass(78081,0,1670047,'one')" value="√通过"
onclick="pass(78081,0,1670047,'one')"
<input type="button" id ="12314130"  onclick="pass(14130,0,196908,'one')" value="√通过"
onclick="pass(14130,0,196908,'one')"
<input type="button" id ="12316714"  onclick="pass(16714,0,196002,'one')" value="√通过"
onclick="pass(16714,0,196002,'one')"
<input type="button" id ="12316204"  onclick="pass(16204,0,196459,'one')" value="√通过"
onclick="pass(16204,0,196459,'one')"
<input type="button" id ="12310763"  onclick="pass(10763,0,196519,'one')" value="√通过"
onclick="pass(10763,0,196519,'one')"
<input type="button" id ="12388521"  onclick="pass(88521,0,1194656,'one')" value="√通过"
onclick="pass(88521,0,1194656,'one')"
<input type="button" id ="12361359"  onclick="pass(61359,57154,1725511,'one')" value="√通过"
onclick="pass(61359,57154,1725511,'one')"
<input type="button" id ="12315324"  onclick="pass(15324,0,196136,'one')" value="√通过"
onclick="pass(15324,0,196136,'one')"
<input type="button" id ="12314037"  onclick="pass(14037,0,196871,'one')" value="√通过"
onclick="pass(14037,0,196871,'one')"
<input type="button" id ="123146137"  onclick="pass(146137,0,2305357,'one')" value="√通过"
onclick="pass(146137,0,2305357,'one')"
<input type="button" id ="123158696"  onclick="pass(158696,0,2294145,'one')" value="√通过"
onclick="pass(158696,0,2294145,'one')"
<input type="button" id ="12316811"  onclick="pass(16811,0,196162,'one')" value="√通过"
onclick="pass(16811,0,196162,'one')"
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">803156</font>']
11963   0   196908
1
106976   0   2322403
1
16830   0   196900
1
158785   0   2294819
1
7436   0   196908
1
88343   0   1194650
1
16124   0   196908
1
62234   44637   1866123
1
83328   0   2363778
1
15221   0   196742
1
12837   0   196908
1
9304   0   196459
1
7999   0   196908
1
7403   0   196949
1
88534   0   1194687
1
123773   53687   2069151
1
188905   0   2280358
1
17105   0   196253
1
109285   0   2147636
1
113858   34702   2252753
1
11692   0   196908
1
15265   0   196162
1
87798   0   2388248
1
7673   0   196162
1
16974   0   196162
1
16480   0   196893
1
16829   0   196519
1
205150   0   2101336
1
115483   0   1975072
1
15382   0   196136
1
110985   36027   2298596
1
16237   0   196459
1
176791   47149   2307154
1
16839   0   196136
1
14831   0   196949
1
11688   0   196021
1
10896   0   196886
1
13276   0   196949
1
110989   36031   2298596
1
9807   0   196949
1
95737   0   2362362
1
78081   0   1670047
1
14130   0   196908
1
16714   0   196002
1
16204   0   196459
1
10763   0   196519
1
88521   0   1194656
1
61359   57154   1725511
1
15324   0   196136
1
14037   0   196871
1
146137   0   2305357
1
158696   0   2294145
1
16811   0   196162
1
['<input type="button" id ="12311873"  onclick="pass(11873,0,196617,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316545"  onclick="pass(16545,0,196162,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312388"  onclick="pass(12388,0,196519,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123162107"  onclick="pass(162107,0,2384689,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312920"  onclick="pass(12920,0,196162,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123167162"  onclick="pass(167162,48720,2368041,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317099"  onclick="pass(17099,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315110"  onclick="pass(15110,0,196351,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316757"  onclick="pass(16757,0,196519,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12390092"  onclick="pass(90092,0,2376218,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237023"  onclick="pass(7023,0,196861,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311864"  onclick="pass(11864,0,196341,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237765"  onclick="pass(7765,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315022"  onclick="pass(15022,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12399170"  onclick="pass(99170,0,1630010,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123136880"  onclick="pass(136880,27890,2387916,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123138613063"  onclick="pass(138613063,0,2295721,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311825"  onclick="pass(11825,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123135223"  onclick="pass(135223,0,2222974,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313162"  onclick="pass(13162,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314963"  onclick="pass(14963,0,196162,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313812"  onclick="pass(13812,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123103039"  onclick="pass(103039,0,2216191,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123220653"  onclick="pass(220653,0,2205648,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12396217"  onclick="pass(96217,0,2357853,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12364468"  onclick="pass(64468,0,1195298,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="12311873"  onclick="pass(11873,0,196617,'one')" value="√通过"
onclick="pass(11873,0,196617,'one')"
<input type="button" id ="12316545"  onclick="pass(16545,0,196162,'one')" value="√通过"
onclick="pass(16545,0,196162,'one')"
<input type="button" id ="12312388"  onclick="pass(12388,0,196519,'one')" value="√通过"
onclick="pass(12388,0,196519,'one')"
<input type="button" id ="123162107"  onclick="pass(162107,0,2384689,'one')" value="√通过"
onclick="pass(162107,0,2384689,'one')"
<input type="button" id ="12312920"  onclick="pass(12920,0,196162,'one')" value="√通过"
onclick="pass(12920,0,196162,'one')"
<input type="button" id ="123167162"  onclick="pass(167162,48720,2368041,'one')" value="√通过"
onclick="pass(167162,48720,2368041,'one')"
<input type="button" id ="12317099"  onclick="pass(17099,0,196136,'one')" value="√通过"
onclick="pass(17099,0,196136,'one')"
<input type="button" id ="12315110"  onclick="pass(15110,0,196351,'one')" value="√通过"
onclick="pass(15110,0,196351,'one')"
<input type="button" id ="12316757"  onclick="pass(16757,0,196519,'one')" value="√通过"
onclick="pass(16757,0,196519,'one')"
<input type="button" id ="12390092"  onclick="pass(90092,0,2376218,'one')" value="√通过"
onclick="pass(90092,0,2376218,'one')"
<input type="button" id ="1237023"  onclick="pass(7023,0,196861,'one')" value="√通过"
onclick="pass(7023,0,196861,'one')"
<input type="button" id ="12311864"  onclick="pass(11864,0,196341,'one')" value="√通过"
onclick="pass(11864,0,196341,'one')"
<input type="button" id ="1237765"  onclick="pass(7765,0,196908,'one')" value="√通过"
onclick="pass(7765,0,196908,'one')"
<input type="button" id ="12315022"  onclick="pass(15022,0,196908,'one')" value="√通过"
onclick="pass(15022,0,196908,'one')"
<input type="button" id ="12399170"  onclick="pass(99170,0,1630010,'one')" value="√通过"
onclick="pass(99170,0,1630010,'one')"
<input type="button" id ="123136880"  onclick="pass(136880,27890,2387916,'one')" value="√通过"
onclick="pass(136880,27890,2387916,'one')"
<input type="button" id ="123138613063"  onclick="pass(138613063,0,2295721,'one')" value="√通过"
onclick="pass(138613063,0,2295721,'one')"
<input type="button" id ="12311825"  onclick="pass(11825,0,196136,'one')" value="√通过"
onclick="pass(11825,0,196136,'one')"
<input type="button" id ="123135223"  onclick="pass(135223,0,2222974,'one')" value="√通过"
onclick="pass(135223,0,2222974,'one')"
<input type="button" id ="12313162"  onclick="pass(13162,0,196136,'one')" value="√通过"
onclick="pass(13162,0,196136,'one')"
<input type="button" id ="12314963"  onclick="pass(14963,0,196162,'one')" value="√通过"
onclick="pass(14963,0,196162,'one')"
<input type="button" id ="12313812"  onclick="pass(13812,0,196949,'one')" value="√通过"
onclick="pass(13812,0,196949,'one')"
<input type="button" id ="123103039"  onclick="pass(103039,0,2216191,'one')" value="√通过"
onclick="pass(103039,0,2216191,'one')"
<input type="button" id ="123220653"  onclick="pass(220653,0,2205648,'one')" value="√通过"
onclick="pass(220653,0,2205648,'one')"
<input type="button" id ="12396217"  onclick="pass(96217,0,2357853,'one')" value="√通过"
onclick="pass(96217,0,2357853,'one')"
<input type="button" id ="12364468"  onclick="pass(64468,0,1195298,'one')" value="√通过"
onclick="pass(64468,0,1195298,'one')"
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">804580</font>']
11873   0   196617
1
16545   0   196162
1
12388   0   196519
1
162107   0   2384689
1
12920   0   196162
1
167162   48720   2368041
1
17099   0   196136
1
15110   0   196351
1
16757   0   196519
1
90092   0   2376218
1
7023   0   196861
1
11864   0   196341
1
7765   0   196908
1
15022   0   196908
1
99170   0   1630010
1
136880   27890   2387916
1
138613063   0   2295721
1
11825   0   196136
1
135223   0   2222974
1
13162   0   196136
1
14963   0   196162
1
13812   0   196949
1
103039   0   2216191
1
220653   0   2205648
1
96217   0   2357853
1
64468   0   1195298
1
['<input type="button" id ="12313215"  onclick="pass(13215,0,196162,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317052"  onclick="pass(17052,0,196162,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314834"  onclick="pass(14834,0,196162,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123159562"  onclick="pass(159562,0,2311759,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314680"  onclick="pass(14680,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311682"  onclick="pass(11682,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123247673"  onclick="pass(247673,0,2186307,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316285"  onclick="pass(16285,0,196519,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12382829"  onclick="pass(82829,0,2361033,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313308"  onclick="pass(13308,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12341197"  onclick="pass(41197,0,1549768,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314525"  onclick="pass(14525,0,196367,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315336"  onclick="pass(15336,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12395703"  onclick="pass(95703,0,2362184,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123188671"  onclick="pass(188671,34624,2280389,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315325"  onclick="pass(15325,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123136906"  onclick="pass(136906,0,2143919,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123247485"  onclick="pass(247485,77247,2186626,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123714744"  onclick="pass(714744,0,2001817,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12365296"  onclick="pass(65296,0,1682792,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313314"  onclick="pass(13314,0,196714,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314431"  onclick="pass(14431,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12391777"  onclick="pass(91777,0,2323796,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123115465"  onclick="pass(115465,0,2312408,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123293107"  onclick="pass(293107,97242,2210912,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123126905"  onclick="pass(126905,0,2372068,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123167979"  onclick="pass(167979,0,2135590,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="12313215"  onclick="pass(13215,0,196162,'one')" value="√通过"
onclick="pass(13215,0,196162,'one')"
<input type="button" id ="12317052"  onclick="pass(17052,0,196162,'one')" value="√通过"
onclick="pass(17052,0,196162,'one')"
<input type="button" id ="12314834"  onclick="pass(14834,0,196162,'one')" value="√通过"
onclick="pass(14834,0,196162,'one')"
<input type="button" id ="123159562"  onclick="pass(159562,0,2311759,'one')" value="√通过"
onclick="pass(159562,0,2311759,'one')"
<input type="button" id ="12314680"  onclick="pass(14680,0,196949,'one')" value="√通过"
onclick="pass(14680,0,196949,'one')"
<input type="button" id ="12311682"  onclick="pass(11682,0,196136,'one')" value="√通过"
onclick="pass(11682,0,196136,'one')"
<input type="button" id ="123247673"  onclick="pass(247673,0,2186307,'one')" value="√通过"
onclick="pass(247673,0,2186307,'one')"
<input type="button" id ="12316285"  onclick="pass(16285,0,196519,'one')" value="√通过"
onclick="pass(16285,0,196519,'one')"
<input type="button" id ="12382829"  onclick="pass(82829,0,2361033,'one')" value="√通过"
onclick="pass(82829,0,2361033,'one')"
<input type="button" id ="12313308"  onclick="pass(13308,0,196949,'one')" value="√通过"
onclick="pass(13308,0,196949,'one')"
<input type="button" id ="12341197"  onclick="pass(41197,0,1549768,'one')" value="√通过"
onclick="pass(41197,0,1549768,'one')"
<input type="button" id ="12314525"  onclick="pass(14525,0,196367,'one')" value="√通过"
onclick="pass(14525,0,196367,'one')"
<input type="button" id ="12315336"  onclick="pass(15336,0,196136,'one')" value="√通过"
onclick="pass(15336,0,196136,'one')"
<input type="button" id ="12395703"  onclick="pass(95703,0,2362184,'one')" value="√通过"
onclick="pass(95703,0,2362184,'one')"
<input type="button" id ="123188671"  onclick="pass(188671,34624,2280389,'one')" value="√通过"
onclick="pass(188671,34624,2280389,'one')"
<input type="button" id ="12315325"  onclick="pass(15325,0,196136,'one')" value="√通过"
onclick="pass(15325,0,196136,'one')"
<input type="button" id ="123136906"  onclick="pass(136906,0,2143919,'one')" value="√通过"
onclick="pass(136906,0,2143919,'one')"
<input type="button" id ="123247485"  onclick="pass(247485,77247,2186626,'one')" value="√通过"
onclick="pass(247485,77247,2186626,'one')"
<input type="button" id ="123714744"  onclick="pass(714744,0,2001817,'one')" value="√通过"
onclick="pass(714744,0,2001817,'one')"
<input type="button" id ="12365296"  onclick="pass(65296,0,1682792,'one')" value="√通过"
onclick="pass(65296,0,1682792,'one')"
<input type="button" id ="12313314"  onclick="pass(13314,0,196714,'one')" value="√通过"
onclick="pass(13314,0,196714,'one')"
<input type="button" id ="12314431"  onclick="pass(14431,0,196949,'one')" value="√通过"
onclick="pass(14431,0,196949,'one')"
<input type="button" id ="12391777"  onclick="pass(91777,0,2323796,'one')" value="√通过"
onclick="pass(91777,0,2323796,'one')"
<input type="button" id ="123115465"  onclick="pass(115465,0,2312408,'one')" value="√通过"
onclick="pass(115465,0,2312408,'one')"
<input type="button" id ="123293107"  onclick="pass(293107,97242,2210912,'one')" value="√通过"
onclick="pass(293107,97242,2210912,'one')"
<input type="button" id ="123126905"  onclick="pass(126905,0,2372068,'one')" value="√通过"
onclick="pass(126905,0,2372068,'one')"
<input type="button" id ="123167979"  onclick="pass(167979,0,2135590,'one')" value="√通过"
onclick="pass(167979,0,2135590,'one')"
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">805127</font>']
13215   0   196162
1
17052   0   196162
1
14834   0   196162
1
159562   0   2311759
1
14680   0   196949
1
11682   0   196136
1
247673   0   2186307
1
16285   0   196519
1
82829   0   2361033
1
13308   0   196949
1
41197   0   1549768
1
14525   0   196367
1
15336   0   196136
1
95703   0   2362184
1
188671   34624   2280389
1
15325   0   196136
1
136906   0   2143919
1
247485   77247   2186626
1
714744   0   2001817
1
65296   0   1682792
1
13314   0   196714
1
14431   0   196949
1
91777   0   2323796
1
115465   0   2312408
1
293107   97242   2210912
1
126905   0   2372068
1
167979   0   2135590
1
['<input type="button" id ="123111083"  onclick="pass(111083,0,2075057,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123247582"  onclick="pass(247582,0,2186463,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123204930"  onclick="pass(204930,55782,2306660,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123120780"  onclick="pass(120780,0,2377397,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123148427"  onclick="pass(148427,0,2297063,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123135187"  onclick="pass(135187,0,2222846,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12360811"  onclick="pass(60811,0,195447,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311710"  onclick="pass(11710,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314839"  onclick="pass(14839,0,196475,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176711"  onclick="pass(176711,0,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1236819"  onclick="pass(6819,0,196253,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123122795"  onclick="pass(122795,0,2039432,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123247511"  onclick="pass(247511,77381,2186626,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315193"  onclick="pass(15193,0,196222,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="123111083"  onclick="pass(111083,0,2075057,'one')" value="√通过"
onclick="pass(111083,0,2075057,'one')"
<input type="button" id ="123247582"  onclick="pass(247582,0,2186463,'one')" value="√通过"
onclick="pass(247582,0,2186463,'one')"
<input type="button" id ="123204930"  onclick="pass(204930,55782,2306660,'one')" value="√通过"
onclick="pass(204930,55782,2306660,'one')"
<input type="button" id ="123120780"  onclick="pass(120780,0,2377397,'one')" value="√通过"
onclick="pass(120780,0,2377397,'one')"
<input type="button" id ="123148427"  onclick="pass(148427,0,2297063,'one')" value="√通过"
onclick="pass(148427,0,2297063,'one')"
<input type="button" id ="123135187"  onclick="pass(135187,0,2222846,'one')" value="√通过"
onclick="pass(135187,0,2222846,'one')"
<input type="button" id ="12360811"  onclick="pass(60811,0,195447,'one')" value="√通过"
onclick="pass(60811,0,195447,'one')"
<input type="button" id ="12311710"  onclick="pass(11710,0,196908,'one')" value="√通过"
onclick="pass(11710,0,196908,'one')"
<input type="button" id ="12314839"  onclick="pass(14839,0,196475,'one')" value="√通过"
onclick="pass(14839,0,196475,'one')"
<input type="button" id ="123176711"  onclick="pass(176711,0,2307154,'one')" value="√通过"
onclick="pass(176711,0,2307154,'one')"
<input type="button" id ="1236819"  onclick="pass(6819,0,196253,'one')" value="√通过"
onclick="pass(6819,0,196253,'one')"
<input type="button" id ="123122795"  onclick="pass(122795,0,2039432,'one')" value="√通过"
onclick="pass(122795,0,2039432,'one')"
<input type="button" id ="123247511"  onclick="pass(247511,77381,2186626,'one')" value="√通过"
onclick="pass(247511,77381,2186626,'one')"
<input type="button" id ="12315193"  onclick="pass(15193,0,196222,'one')" value="√通过"
onclick="pass(15193,0,196222,'one')"
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">806813</font>']
111083   0   2075057
1
247582   0   2186463
1
204930   55782   2306660
1
120780   0   2377397
1
148427   0   2297063
1
135187   0   2222846
1
60811   0   195447
1
11710   0   196908
1
14839   0   196475
1
176711   0   2307154
1
6819   0   196253
1
122795   0   2039432
1
247511   77381   2186626
1
15193   0   196222
1
['<input type="button" id ="123142708"  onclick="pass(142708,0,2317349,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12385981"  onclick="pass(85981,0,1574116,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314100"  onclick="pass(14100,0,196029,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123198619"  onclick="pass(198619,50580,2236954,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314564"  onclick="pass(14564,0,196029,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314979"  onclick="pass(14979,0,196399,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314637"  onclick="pass(14637,0,196351,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123171105"  onclick="pass(171105,36098,2272764,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312559"  onclick="pass(12559,0,196898,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237469"  onclick="pass(7469,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12361426"  onclick="pass(61426,0,1946641,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123247769"  onclick="pass(247769,0,2186130,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317173"  onclick="pass(17173,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123134882"  onclick="pass(134882,0,2203925,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12387525"  onclick="pass(87525,0,2365214,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12366345"  onclick="pass(66345,0,1195453,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314714"  onclick="pass(14714,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315407"  onclick="pass(15407,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1238905"  onclick="pass(8905,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176659"  onclick="pass(176659,35167,2347300,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313977"  onclick="pass(13977,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123106811"  onclick="pass(106811,14040,2322969,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123108976"  onclick="pass(108976,0,2319870,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312372"  onclick="pass(12372,0,196399,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316993"  onclick="pass(16993,0,196029,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12355883"  onclick="pass(55883,51319,1894923,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="123142708"  onclick="pass(142708,0,2317349,'one')" value="√通过"
onclick="pass(142708,0,2317349,'one')"
<input type="button" id ="12385981"  onclick="pass(85981,0,1574116,'one')" value="√通过"
onclick="pass(85981,0,1574116,'one')"
<input type="button" id ="12314100"  onclick="pass(14100,0,196029,'one')" value="√通过"
onclick="pass(14100,0,196029,'one')"
<input type="button" id ="123198619"  onclick="pass(198619,50580,2236954,'one')" value="√通过"
onclick="pass(198619,50580,2236954,'one')"
<input type="button" id ="12314564"  onclick="pass(14564,0,196029,'one')" value="√通过"
onclick="pass(14564,0,196029,'one')"
<input type="button" id ="12314979"  onclick="pass(14979,0,196399,'one')" value="√通过"
onclick="pass(14979,0,196399,'one')"
<input type="button" id ="12314637"  onclick="pass(14637,0,196351,'one')" value="√通过"
onclick="pass(14637,0,196351,'one')"
<input type="button" id ="123171105"  onclick="pass(171105,36098,2272764,'one')" value="√通过"
onclick="pass(171105,36098,2272764,'one')"
<input type="button" id ="12312559"  onclick="pass(12559,0,196898,'one')" value="√通过"
onclick="pass(12559,0,196898,'one')"
<input type="button" id ="1237469"  onclick="pass(7469,0,196949,'one')" value="√通过"
onclick="pass(7469,0,196949,'one')"
<input type="button" id ="12361426"  onclick="pass(61426,0,1946641,'one')" value="√通过"
onclick="pass(61426,0,1946641,'one')"
<input type="button" id ="123247769"  onclick="pass(247769,0,2186130,'one')" value="√通过"
onclick="pass(247769,0,2186130,'one')"
<input type="button" id ="12317173"  onclick="pass(17173,0,196949,'one')" value="√通过"
onclick="pass(17173,0,196949,'one')"
<input type="button" id ="123134882"  onclick="pass(134882,0,2203925,'one')" value="√通过"
onclick="pass(134882,0,2203925,'one')"
<input type="button" id ="12387525"  onclick="pass(87525,0,2365214,'one')" value="√通过"
onclick="pass(87525,0,2365214,'one')"
<input type="button" id ="12366345"  onclick="pass(66345,0,1195453,'one')" value="√通过"
onclick="pass(66345,0,1195453,'one')"
<input type="button" id ="12314714"  onclick="pass(14714,0,196136,'one')" value="√通过"
onclick="pass(14714,0,196136,'one')"
<input type="button" id ="12315407"  onclick="pass(15407,0,196136,'one')" value="√通过"
onclick="pass(15407,0,196136,'one')"
<input type="button" id ="1238905"  onclick="pass(8905,0,196136,'one')" value="√通过"
onclick="pass(8905,0,196136,'one')"
<input type="button" id ="123176659"  onclick="pass(176659,35167,2347300,'one')" value="√通过"
onclick="pass(176659,35167,2347300,'one')"
<input type="button" id ="12313977"  onclick="pass(13977,0,196949,'one')" value="√通过"
onclick="pass(13977,0,196949,'one')"
<input type="button" id ="123106811"  onclick="pass(106811,14040,2322969,'one')" value="√通过"
onclick="pass(106811,14040,2322969,'one')"
<input type="button" id ="123108976"  onclick="pass(108976,0,2319870,'one')" value="√通过"
onclick="pass(108976,0,2319870,'one')"
<input type="button" id ="12312372"  onclick="pass(12372,0,196399,'one')" value="√通过"
onclick="pass(12372,0,196399,'one')"
<input type="button" id ="12316993"  onclick="pass(16993,0,196029,'one')" value="√通过"
onclick="pass(16993,0,196029,'one')"
<input type="button" id ="12355883"  onclick="pass(55883,51319,1894923,'one')" value="√通过"
onclick="pass(55883,51319,1894923,'one')"
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">808365</font>']
142708   0   2317349
1
85981   0   1574116
1
14100   0   196029
1
198619   50580   2236954
1
14564   0   196029
1
14979   0   196399
1
14637   0   196351
1
171105   36098   2272764
1
12559   0   196898
1
7469   0   196949
1
61426   0   1946641
1
247769   0   2186130
1
17173   0   196949
1
134882   0   2203925
1
87525   0   2365214
1
66345   0   1195453
1
14714   0   196136
1
15407   0   196136
1
8905   0   196136
1
176659   35167   2347300
1
13977   0   196949
1
106811   14040   2322969
1
108976   0   2319870
1
12372   0   196399
1
16993   0   196029
1
55883   51319   1894923
1
['<input type="button" id ="12312646"  onclick="pass(12646,0,196475,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123124162"  onclick="pass(124162,0,2211410,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315152"  onclick="pass(15152,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12376664"  onclick="pass(76664,48498,1921020,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123184774"  onclick="pass(184774,0,2099758,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312796"  onclick="pass(12796,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312248"  onclick="pass(12248,0,196617,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123142777"  onclick="pass(142777,0,2317349,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123193784"  onclick="pass(193784,0,2246613,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313031"  onclick="pass(13031,0,196341,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123142940"  onclick="pass(142940,0,2317868,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312195"  onclick="pass(12195,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12362257"  onclick="pass(62257,0,1866123,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="12312646"  onclick="pass(12646,0,196475,'one')" value="√通过"
onclick="pass(12646,0,196475,'one')"
<input type="button" id ="123124162"  onclick="pass(124162,0,2211410,'one')" value="√通过"
onclick="pass(124162,0,2211410,'one')"
<input type="button" id ="12315152"  onclick="pass(15152,0,196908,'one')" value="√通过"
onclick="pass(15152,0,196908,'one')"
<input type="button" id ="12376664"  onclick="pass(76664,48498,1921020,'one')" value="√通过"
onclick="pass(76664,48498,1921020,'one')"
<input type="button" id ="123184774"  onclick="pass(184774,0,2099758,'one')" value="√通过"
onclick="pass(184774,0,2099758,'one')"
<input type="button" id ="12312796"  onclick="pass(12796,0,196949,'one')" value="√通过"
onclick="pass(12796,0,196949,'one')"
<input type="button" id ="12312248"  onclick="pass(12248,0,196617,'one')" value="√通过"
onclick="pass(12248,0,196617,'one')"
<input type="button" id ="123142777"  onclick="pass(142777,0,2317349,'one')" value="√通过"
onclick="pass(142777,0,2317349,'one')"
<input type="button" id ="123193784"  onclick="pass(193784,0,2246613,'one')" value="√通过"
onclick="pass(193784,0,2246613,'one')"
<input type="button" id ="12313031"  onclick="pass(13031,0,196341,'one')" value="√通过"
onclick="pass(13031,0,196341,'one')"
<input type="button" id ="123142940"  onclick="pass(142940,0,2317868,'one')" value="√通过"
onclick="pass(142940,0,2317868,'one')"
<input type="button" id ="12312195"  onclick="pass(12195,0,196949,'one')" value="√通过"
onclick="pass(12195,0,196949,'one')"
<input type="button" id ="12362257"  onclick="pass(62257,0,1866123,'one')" value="√通过"
onclick="pass(62257,0,1866123,'one')"
<input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,'one')" value="√通过"
onclick="pass(125176,42516,2043685,'one')"
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">808975</font>']
12646   0   196475
1
124162   0   2211410
1
15152   0   196908
1
76664   48498   1921020
1
184774   0   2099758
1
12796   0   196949
1
12248   0   196617
1
142777   0   2317349
1
193784   0   2246613
1
13031   0   196341
1
142940   0   2317868
1
12195   0   196949
1
62257   0   1866123
1
125176   42516   2043685
1
['<input type="button" id ="12312961"  onclick="pass(12961,0,196029,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1236179"  onclick="pass(6179,0,196228,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123250610"  onclick="pass(250610,0,2308235,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315049"  onclick="pass(15049,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312341"  onclick="pass(12341,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123112479"  onclick="pass(112479,27693,2366143,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313932"  onclick="pass(13932,0,196373,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237412"  onclick="pass(7412,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315213"  onclick="pass(15213,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12379924"  onclick="pass(79924,14568,2373399,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312745"  onclick="pass(12745,0,196957,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316755"  onclick="pass(16755,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123126872"  onclick="pass(126872,23637,2372269,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315520"  onclick="pass(15520,0,196714,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12394543"  onclick="pass(94543,22136,2337245,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315004"  onclick="pass(15004,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123109081"  onclick="pass(109081,0,2319574,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123115220"  onclick="pass(115220,21035,2310524,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316027"  onclick="pass(16027,0,196886,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237550"  onclick="pass(7550,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237310"  onclick="pass(7310,0,196909,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12364595"  onclick="pass(64595,0,626977,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123114190"  onclick="pass(114190,0,2252716,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237551"  onclick="pass(7551,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123224998"  onclick="pass(224998,39870,2299509,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12359801"  onclick="pass(59801,0,1928923,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237761"  onclick="pass(7761,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1236241"  onclick="pass(6241,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123160907"  onclick="pass(160907,0,2385018,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123167261"  onclick="pass(167261,0,2368078,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12375865"  onclick="pass(75865,18290,2360289,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="12312961"  onclick="pass(12961,0,196029,'one')" value="√通过"
onclick="pass(12961,0,196029,'one')"
<input type="button" id ="1236179"  onclick="pass(6179,0,196228,'one')" value="√通过"
onclick="pass(6179,0,196228,'one')"
<input type="button" id ="123250610"  onclick="pass(250610,0,2308235,'one')" value="√通过"
onclick="pass(250610,0,2308235,'one')"
<input type="button" id ="12315049"  onclick="pass(15049,0,196136,'one')" value="√通过"
onclick="pass(15049,0,196136,'one')"
<input type="button" id ="12312341"  onclick="pass(12341,0,196949,'one')" value="√通过"
onclick="pass(12341,0,196949,'one')"
<input type="button" id ="123112479"  onclick="pass(112479,27693,2366143,'one')" value="√通过"
onclick="pass(112479,27693,2366143,'one')"
<input type="button" id ="12313932"  onclick="pass(13932,0,196373,'one')" value="√通过"
onclick="pass(13932,0,196373,'one')"
<input type="button" id ="1237412"  onclick="pass(7412,0,196908,'one')" value="√通过"
onclick="pass(7412,0,196908,'one')"
<input type="button" id ="12315213"  onclick="pass(15213,0,196949,'one')" value="√通过"
onclick="pass(15213,0,196949,'one')"
<input type="button" id ="12379924"  onclick="pass(79924,14568,2373399,'one')" value="√通过"
onclick="pass(79924,14568,2373399,'one')"
<input type="button" id ="12312745"  onclick="pass(12745,0,196957,'one')" value="√通过"
onclick="pass(12745,0,196957,'one')"
<input type="button" id ="12316755"  onclick="pass(16755,0,196136,'one')" value="√通过"
onclick="pass(16755,0,196136,'one')"
<input type="button" id ="123126872"  onclick="pass(126872,23637,2372269,'one')" value="√通过"
onclick="pass(126872,23637,2372269,'one')"
<input type="button" id ="12315520"  onclick="pass(15520,0,196714,'one')" value="√通过"
onclick="pass(15520,0,196714,'one')"
<input type="button" id ="12394543"  onclick="pass(94543,22136,2337245,'one')" value="√通过"
onclick="pass(94543,22136,2337245,'one')"
<input type="button" id ="12315004"  onclick="pass(15004,0,196949,'one')" value="√通过"
onclick="pass(15004,0,196949,'one')"
<input type="button" id ="123109081"  onclick="pass(109081,0,2319574,'one')" value="√通过"
onclick="pass(109081,0,2319574,'one')"
<input type="button" id ="123115220"  onclick="pass(115220,21035,2310524,'one')" value="√通过"
onclick="pass(115220,21035,2310524,'one')"
<input type="button" id ="12316027"  onclick="pass(16027,0,196886,'one')" value="√通过"
onclick="pass(16027,0,196886,'one')"
<input type="button" id ="1237550"  onclick="pass(7550,0,196908,'one')" value="√通过"
onclick="pass(7550,0,196908,'one')"
<input type="button" id ="1237310"  onclick="pass(7310,0,196909,'one')" value="√通过"
onclick="pass(7310,0,196909,'one')"
<input type="button" id ="12364595"  onclick="pass(64595,0,626977,'one')" value="√通过"
onclick="pass(64595,0,626977,'one')"
<input type="button" id ="123114190"  onclick="pass(114190,0,2252716,'one')" value="√通过"
onclick="pass(114190,0,2252716,'one')"
<input type="button" id ="1237551"  onclick="pass(7551,0,196459,'one')" value="√通过"
onclick="pass(7551,0,196459,'one')"
<input type="button" id ="123224998"  onclick="pass(224998,39870,2299509,'one')" value="√通过"
onclick="pass(224998,39870,2299509,'one')"
<input type="button" id ="12359801"  onclick="pass(59801,0,1928923,'one')" value="√通过"
onclick="pass(59801,0,1928923,'one')"
<input type="button" id ="1237761"  onclick="pass(7761,0,196908,'one')" value="√通过"
onclick="pass(7761,0,196908,'one')"
<input type="button" id ="1236241"  onclick="pass(6241,0,196136,'one')" value="√通过"
onclick="pass(6241,0,196136,'one')"
<input type="button" id ="123160907"  onclick="pass(160907,0,2385018,'one')" value="√通过"
onclick="pass(160907,0,2385018,'one')"
<input type="button" id ="123167261"  onclick="pass(167261,0,2368078,'one')" value="√通过"
onclick="pass(167261,0,2368078,'one')"
<input type="button" id ="12375865"  onclick="pass(75865,18290,2360289,'one')" value="√通过"
onclick="pass(75865,18290,2360289,'one')"
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">809470</font>']
12961   0   196029
1
6179   0   196228
1
250610   0   2308235
1
15049   0   196136
1
12341   0   196949
1
112479   27693   2366143
1
13932   0   196373
1
7412   0   196908
1
15213   0   196949
1
79924   14568   2373399
1
12745   0   196957
1
16755   0   196136
1
126872   23637   2372269
1
15520   0   196714
1
94543   22136   2337245
1
15004   0   196949
1
109081   0   2319574
1
115220   21035   2310524
1
16027   0   196886
1
7550   0   196908
1
7310   0   196909
1
64595   0   626977
1
114190   0   2252716
1
7551   0   196459
1
224998   39870   2299509
1
59801   0   1928923
1
7761   0   196908
1
6241   0   196136
1
160907   0   2385018
1
167261   0   2368078
1
75865   18290   2360289
1
['<input type="button" id ="12312821"  onclick="pass(12821,0,196568,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313204"  onclick="pass(13204,0,196029,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314186"  onclick="pass(14186,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123141474"  onclick="pass(141474,0,2168548,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311565"  onclick="pass(11565,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317022"  onclick="pass(17022,0,196617,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237451"  onclick="pass(7451,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123159678"  onclick="pass(159678,0,2311060,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123160938"  onclick="pass(160938,0,2385572,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="12312821"  onclick="pass(12821,0,196568,'one')" value="√通过"
onclick="pass(12821,0,196568,'one')"
<input type="button" id ="12313204"  onclick="pass(13204,0,196029,'one')" value="√通过"
onclick="pass(13204,0,196029,'one')"
<input type="button" id ="12314186"  onclick="pass(14186,0,196949,'one')" value="√通过"
onclick="pass(14186,0,196949,'one')"
<input type="button" id ="123141474"  onclick="pass(141474,0,2168548,'one')" value="√通过"
onclick="pass(141474,0,2168548,'one')"
<input type="button" id ="12311565"  onclick="pass(11565,0,196136,'one')" value="√通过"
onclick="pass(11565,0,196136,'one')"
<input type="button" id ="12317022"  onclick="pass(17022,0,196617,'one')" value="√通过"
onclick="pass(17022,0,196617,'one')"
<input type="button" id ="1237451"  onclick="pass(7451,0,196459,'one')" value="√通过"
onclick="pass(7451,0,196459,'one')"
<input type="button" id ="123159678"  onclick="pass(159678,0,2311060,'one')" value="√通过"
onclick="pass(159678,0,2311060,'one')"
<input type="button" id ="123160938"  onclick="pass(160938,0,2385572,'one')" value="√通过"
onclick="pass(160938,0,2385572,'one')"
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">810469</font>']
12821   0   196568
1
13204   0   196029
1
14186   0   196949
1
141474   0   2168548
1
11565   0   196136
1
17022   0   196617
1
7451   0   196459
1
159678   0   2311060
1
160938   0   2385572
1
['<input type="button" id ="12312248"  onclick="pass(12248,0,196617,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313314"  onclick="pass(13314,0,196714,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12394648"  onclick="pass(94648,0,2337210,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312663"  onclick="pass(12663,0,196351,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312915"  onclick="pass(12915,0,196886,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315556"  onclick="pass(15556,0,196706,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123157370"  onclick="pass(157370,36367,2314023,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12389920"  onclick="pass(89920,12179,2376218,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314979"  onclick="pass(14979,0,196399,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="12312248"  onclick="pass(12248,0,196617,'one')" value="√通过"
onclick="pass(12248,0,196617,'one')"
<input type="button" id ="12313314"  onclick="pass(13314,0,196714,'one')" value="√通过"
onclick="pass(13314,0,196714,'one')"
<input type="button" id ="12394648"  onclick="pass(94648,0,2337210,'one')" value="√通过"
onclick="pass(94648,0,2337210,'one')"
<input type="button" id ="12312663"  onclick="pass(12663,0,196351,'one')" value="√通过"
onclick="pass(12663,0,196351,'one')"
<input type="button" id ="12312915"  onclick="pass(12915,0,196886,'one')" value="√通过"
onclick="pass(12915,0,196886,'one')"
<input type="button" id ="12315556"  onclick="pass(15556,0,196706,'one')" value="√通过"
onclick="pass(15556,0,196706,'one')"
<input type="button" id ="123157370"  onclick="pass(157370,36367,2314023,'one')" value="√通过"
onclick="pass(157370,36367,2314023,'one')"
<input type="button" id ="12389920"  onclick="pass(89920,12179,2376218,'one')" value="√通过"
onclick="pass(89920,12179,2376218,'one')"
<input type="button" id ="12314979"  onclick="pass(14979,0,196399,'one')" value="√通过"
onclick="pass(14979,0,196399,'one')"
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">810707</font>']
12248   0   196617
1
13314   0   196714
1
94648   0   2337210
1
12663   0   196351
1
12915   0   196886
1
15556   0   196706
1
157370   36367   2314023
1
89920   12179   2376218
1
14979   0   196399
1
>>> op = opener.open(url)
>>> cont = op.read()
>>> print find_result(cont)
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">810782</font>']
>>> 
