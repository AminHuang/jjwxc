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

        <title>������ѧ��[��½��Ϣ]</title>

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

            // �������������ʾ

            $.ajax({

                type: "get",

                async: true, //ͬ���첽 trueΪ�첽(Ĭ��),falseΪͬ��

                url: "http://s8.static.jjwxc.net/public_notice.php", //ʵ���Ϸ���ʱ�����ĵ�ַΪ: test.php?callbackfun=jsonpCallback&id=10

                cache: true, //Ĭ��ֵfalse falseʱ���������&_=�����

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

            var type = 1;//����Ʒ����

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

    function getCursortPosition(ctrl) {//��ȡ���λ�ú���

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

            <noscript>�������������������javascript���޷�����ʹ�ñ���վ���ܣ�<a href="http://help.jjwxc.net/user/article/136" target="_blank"><font color="blue">��ο��˷������¿���javascript</font></a></noscript>

        </div>

    </div>

    <script>checkLogin();</script>

    <!--�������ʾ��Ϣ��-->

    <div class="blockUI blockMsg" id ="examine_num" style="z-index: 1002; position: absolute; height:45px; width:140px; top: 35px; left: 820px; text-align: center; color: rgb(0, 0, 0);  background-color:#FFFFF7;border:1px solid #FFCC00;display: none;line-height:15px">

        <a href="#" style="float: right;margin-right: 8px" id="examine_num_close">�ر�</a><br/>

        <div id ="examine_num_content"></div>

    </div>

</div>

<!--��վͷ������-->

<!--js�����жϣ�����ǰ��foot_opt.php�еı�ǩ��������-->

<p id="checkJs" style="text-align:center"></p>

<!--logo ������-->

<div id="sitehead" style="position:relative; z-index:2;line-height: 22px;">

    <div class="logo"><a href="http://www.jjwxc.net/" rel="nofollow"><img src="http://static.jjwxc.net/images/channel_2010/logo.gif" width="120" height="120" alt="������ѧ��logo" title="������ѧ��" /></a></div>

    <div class="nav1">

        <div class="fl" style="width:371px;">

            <div class="link1"><a href="http://www.jjwxc.net/fenzhan/yq/" class="a1"></a><a href="http://www.jjwxc.net/fenzhan/yc/" class="a2"></a><a href="http://www.jjwxc.net/fenzhan/noyq/" class="a3"></a><a href="http://www.jjwxc.net/fenzhan/ys/" class="a4"></a></div>

            <div class="link2">

                <a href="http://www.jjwxc.net/fenzhan/by/" target="_blank">����Ŀ�</a><a href="http://www.jjwxc.net/fenzhan/bq/" target="_blank">����Ӱ��</a><a href="http://www.jjwxc.net/jjgame/" target="_blank" >��Ϸ����</a><a href="http://bbs.jjwxc.net" target="_blank">��̳</a><a href="http://www.jjwxc.net/sp/JJ-app-download/" onclick="_czc.push(['_trackEvent', 'WWW��ҳ', '���', '�ֻ�Ƶ��']);" target="_blank"><font style="color:red;font-weight:700">�ֻ���</font></a><a onclick="trans(0);

                        return false;" id="S2TLink" href="#">�����</a>



            </div>

        </div>

        <!--ȫվͨ������banner���-->

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

                    <div class="title"><a href="http://www.jjwxc.net/bookbase_slave.php">��Ʒ��<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?endstr=true&orderstr=1">�����Ʒ</a></li>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?booktype=sp">פվ��Ʒ</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe></li>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?booktype=vip">VIP��Ʒ</a></li>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?booktype=package">�����/����</a></li>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?booktype=scriptures">�����Ŀ�</a></li>

                        <li><a href="http://www.jjwxc.net/bookbase_slave.php?booktype=free">����Ŀ�</a></li>

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

                    <div class="title"><a href="http://www.jjwxc.net/topten.php">���а�<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=1">���������</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=1&t=1">���ƴ���ͬ�˰�</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=3">�½����߰�</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=5">�¶����а�</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=4">�������а�</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=6">�������а�</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=7">�ܷ����а�</a></li>

                        <li><a href="http://www.jjwxc.net/topten.php?orderstr=8">�������а�</a></li>

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

                    <div class="title"><a href="http://www.jjwxc.net/channel/comment.html">����Ƶ��<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/comment.php?orderstr=1">��������</a></li>

                        <li><a href="http://www.jjwxc.net/comment.php?orderstr=2">�������</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:45px;"></iframe></li>

                        <li><a href="http://www.jjwxc.net/spcomment.php">��������</a></li>

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

                    <div class="title"><a href="http://www.jjwxc.net/authorlist.php">����ר��<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/authorlist.php">��ĸ����</a></li>

                        <li><a href="http://www.jjwxc.net/scorelist.php">��������</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe></li>

                        <li><a href="http://help.jjwxc.net/user/more/23/0">д������</a></li>

                        <li><a href="http://www.jjwxc.net/starshow.php">��������</a></li>

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

                    <div class="title"><a href="http://www.jjwxc.net/fenzhan/bq/">����ר��<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/fenzhan/bq/">��������</a></li>

                        <li><a href="http://www.jjwxc.net/fenzhan/bq/">����ǩԼ</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:35px;"></iframe></li>

                        <li><a href="http://www.jjwxc.cn/zhuanlan/index/zhuanlantype/yuanchuang">ͼ������</a></li>

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

                    <div class="title"><a href="http://www.jjwxc.net/aboutus/#fragment-33">���Ż<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://www.jjwxc.net/onebook.php?novelid=494708">��������</a></li>

                        <li><a href="http://www.jjwxc.net/aboutus/#fragment-33">��վ�</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:45px;"></iframe></li>

                        <li><a href="http://www.jjwxc.net/aboutus/#fragment-33">ý�屨��</a></li>

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

                    <div class="title"><a href="http://my.jjwxc.net/pay/paycenter.php"><font color="red">��ֵ</font><img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://my.jjwxc.net/pay/paycenter.php">��ݳ�ֵ</a></li>

                        <li><a href="http://my.jjwxc.net/pay/tutorial.php">��ֵ����</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:45px;"></iframe></li>

                        <li><a href="http://www.jjwxc.net/fenzhan/yq/action_center.html">���¿�����</a></li>

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

                    <div class="title"><a href="http://my.jjwxc.net/backend/auto.php">����Ͷ��<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://help.jjwxc.net/user/article/49">���ı���</a></li>

                        <li><a href="http://my.jjwxc.net/backend/auto.php?act=3">������ɱ</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe></li>

                        <li><a href="http://my.jjwxc.net/backend/auto.php?act=4">ɾ������</a></li>

                        <li><a href="http://www.jjwxc.net/report_center.php">�������</a></li>

                        <li><a href="http://my.jjwxc.net/backend/auto.php?act=6">Ͷ������</a></li>

                        <li><a href="http://my.jjwxc.net/backend/auto.php?act=7">�޸���Ȩ</a></li>

                        <li><a href="http://my.jjwxc.net/backend/auto.php?act=8">�����������</a></li>

                        <li><a href="http://help.jjwxc.net/user/password">��������</a></li>

                        <li><a href="http://bbs.jjwxc.net/board.php?board=22&page=1">������鲾</a></li>

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

                    <div class="title"><a href="http://my.jjwxc.net/login.php">ע��/��¼<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://my.jjwxc.net/register/index.html" rel="nofollow">�û�ע��</a></li>

                        <li><a href="http://my.jjwxc.net/login.php">��½����</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe></li>

                        <li><a href="http://my.jjwxc.net/backend/logout.php" title="�˳���¼״̬">�˳���½</a></li>

                        <li><a href="http://help.jjwxc.net/user/password">��������</a></li>

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

                    <div class="title"><a href="http://help.jjwxc.net/user/index">����<img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul>

                        <li><a href="http://help.jjwxc.net/user/index">��������</a></li>

                        <li><a href="http://help.jjwxc.net/user/contact">�ͷ�����</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:20px;"></iframe></li>

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

                    <div class="title"><a href="http://game.jjwxc.net"><font color="red">��Ϸ</font><img src="http://static.jjwxc.net/images/channel_2010/navli.jpg" /></a></div>

                    <ul id="jjgames">

                        <li>

                            <a style="width:110px" href="http://ktpd.jjqj.net/" target="_blank">��������ٵ�2

                                <img src="http://static.jjwxc.net/images/channel_2010/new.gif" width="22px" />   

                            </a>    

                        </li>

                        <li>

                            <a style="width:110px" href="http://jjhgll.175wan.com/" target="_blank">����������

                            </a>    

                        </li>

                        <!--                        <li>

                                                    <a style="width:110px" href="http://jjzsxy.3737.com/" target="_blank">����������Ե

                                                    </a>    

                                                </li>-->

                        <li><a style="width:110px" href="http://xxd.jjqj.net/" target="_blank">����������</a>    

                        </li>

                        <li><a style="width:110px" href="http://jjwxc.tgm.9917.com/" target="_blank">�����ƹ���</a>

                        </li>

<!--                        <li><a href="http://jjwxc.zcl.2g.cn/" target="_blank">�����ܲ���</a><iframe src="about:blank" style="filter:'progid:DXImageTransform.Microsoft.Alpha(style=0,opacity=0)'; position:absolute; visibility:inherit; top:0px; left:0px; width:110px; z-index:-1; height:65px;"></iframe>

                        </li>-->

                        <li><a style="width:110px" href="http://jjwxc.aoshitang.com/gcld" target="_blank">���������ӵ�

                            </a>    

                        </li>



                        <li><a style="width:110px" href="http://jjwxc.9917.com/servers_yyzq.html?wait=alert">������˾�



                            </a>    

                        </li>

                        <li><a style="width:110px" href="http://jjwxc.aoshitang.com/">����������˵

                            </a>    

                        </li>

                        <li><a style="width:110px" href="http://jjwxc.9917.com/">������͢��</a>

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



                <a href="http://www.jjwxc.net/fenzhan/yq/dp.html">��ƪ</a>

                <a href="http://www.jjwxc.net/fenzhan/dm/ys.html">ͬ������С˵</a>

                <a href="http://www.jjwxc.net/fenzhan/dm/tr.html">ͬ�����鶯��</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/kh.html">�ƻ���������</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/wx.html">�������</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/chy.html">�Ŵ���Խ</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/qc.html">��������</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/bgx.html">�����ഺ</a>

                <a href="http://www.jjwxc.net/fenzhan/yq/bgg.html">�Ŵ�����</a>

            </div>

            <div class="search">

                <a class="limitFree" href="http://www.jjwxc.net/sp/novelfree/" target="_blank" style="float:left"><img width="51" style="margin-left: 40px;" src="http://static.jjwxc.net/images/Channel/xmyd.gif" ></a>

                <div class="search_right">

                    <form  method="get" action="http://www.jjwxc.net/bookbase.php" target="_top"  id="formright">

                        <input type="hidden" name="s_typeid" value="1" />

                        <select name="fw" id="fwfw" class="input2">

                            <option value="0">-��Χ-</option>

                                                                                        <option value="1" >ȫվ</option>

                                                                    <option value="2" >�����</option>

                                                                    <option value="3" >VIP��</option>

                                                            </select>

                        <select name="ycx" id="ycyc" class="input2" style="width:73px">

                            <option value="0">-ԭ����-</option>

                                                                                        <option value="1" >ԭ��</option>

                                                                    <option value="2" >ͬ��</option>

                                                            </select>

                        <select name="xx" id="xxxx" class="input2">

                            <option value="0">-����-</option>

                                                                                        <option value="1" >����</option>

                                                                    <option value="2" >����</option>

                                                                    <option value="3" >�ٺ�</option>

                                                                    <option value="4" >Ů��</option>

                                                                    <option value="5" >��CP</option>

                                                            </select>

                        <select name="sd" id="sdsd" class="input2">

                            <option value="0">-ʱ��-</option>

                                                                                        <option value="1" >�����ִ�</option>

                                                                    <option value="2" >��ɫ����</option>

                                                                    <option value="4" >�ܿ���ʷ</option>

                                                                    <option value="5" >����δ��</option>

                                                            </select>

                        <select name="lx" id="lxlx" class="input2">

                            <option value="0">-����-</option>

                                                                                        <option value="1" >����</option>

                                                                    <option value="2" >����</option>

                                                                    <option value="3" >���</option>

                                                                    <option value="4" >����</option>

                                                                    <option value="5" >����</option>

                                                                    <option value="6" >����</option>

                                                                    <option value="7" >�ƻ�</option>

                                                                    <option value="8" >ͯ��</option>

                                                                    <option value="9" >�ֲ�</option>

                                                                    <option value="10" >��̽</option>

                                                                    <option value="11" >����</option>

                                                                    <option value="12" >Ӱ��</option>

                                                                    <option value="13" >С˵</option>

                                                                    <option value="14" >����</option>

                                                                    <option value="15" >����</option>

                                                                    <option value="16" >����</option>

                                                            </select>

                        <select name="fg" id="fgfg" class="input2">

                            <option value="0">-���-</option>

                                                                                        <option value="1" >����</option>

                                                                    <option value="2" >����</option>

                                                                    <option value="3" >����</option>

                                                                    <option value="4" >��Ц</option>

                                                                    <option value="5" >����</option>

                                                            </select>

                        <select name="bq" id="ss_tags" class="input2" style="width: 71px;"><!--ԭ�������� id="s_tags" ������js�ļ���ԭ��������ø�id�ᵼ�����������ܶ�ܶ��ǩ�����ң�����޸ĵ���-->

                            <option value="-1">-��ǩ-</option>

                            <!--��ǩ��ΪAjax��ȡ���� main.120724_.js ��-->

                        </select>

                        <input name="submit" type="submit" onclick="_czc.push(['_trackEvent', 'WWW��ҳ', '���', '�����ѯ']);" class="searchbutton input3" id="submit" value="��ѯ" />

                    </form>

                </div>

                <div class="search_left">

                    <form name="form8" method="get" action="http://www.jjwxc.net/search.php" target=_blank id="formleft">

                                                    <input name = "kw" id = "autoComplete" autocomplete = "off" type = "text" onfocus = "if (this.value!='')

                                            this.value = '';

                                        $(this).css('color', 'black');" style = "width: 110px;color:#B2B2B2;" value = "������ؼ���">

                                   



                        <div id="showNovelTro"></div>

                        <select name="t" class="input2" id="tj">

                            <option value="1" selected>��Ʒ</option>

                            <option value="2">����</option>

                            <option value="4">����</option>

                            <option value="5">���</option>

                            <option value="6">�����ؼ���</option>

                        </select>

                        <input name="submit" type="submit" onclick="_czc.push(['_trackEvent', 'WWW��ҳ', '���', '�ؼ��ֲ�ѯ']);" value="��ѯ" class="searchbutton input3" />

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

    <!--logo ����������-->                

</head>

<!--281948-->

<meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>

<link rel="stylesheet" type="text/css" href="http://static.jjwxc.net/scripts/jquerycssmenu/jquerycssmenu.css" />

<script type="text/javascript" src="http://static.jjwxc.net/scripts/jquerycssmenu/jquerycssmenu.js?var=20130115"></script>

<script type="text/javascript">

    // --- ��ʾ����

    var alert_blockUI = function(message) {

        $.blockUI('<div align="center"><div style="float:right"><img src="http://static.jjwxc.net/images/close.gif" width="12" height="12" style="cursor:pointer" onClick="$.unblockUI()"/></div><b>'+message+'</b><br><br><br><br><input type="button" value="ȷ ��" onClick="$.unblockUI()"/></div>', {

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

                    html += '<tr><td bgcolor="#ffffb0">��<b>��������ĵ�VIP���¸����������</b>��</td></tr>';

                    html += '<tr><td bgcolor="#ffffcc">'+json.message_vip['body']+'</td></tr>';

                    html += '</table><div style="height: 12px"></div>';

                }



                $.each(json.message_sms, function(index, value) {

                    if (value['smstype']==0||value['smstype']==4) {

                        bgcolors[0] = '#FF6633';

                        bgcolors[1] = '#FFFFB0';

                        bgcolors[2] = '#FFFFCC';

                        smssubject = '<b>'+value['smssubject']+'</b>��<font color="#999999">��'+value['smsdate']+'����</font><a id="sms_'+value['smsid']+'" onclick="smsclick('+value['smsid']+', 1)" style="cursor:pointer;">�����Ĺرա�</a>';

                    } else if (value['smstype']==1||value['smstype']==3) {

                        bgcolors[0] = '#CCCCCC';

                        bgcolors[1] = '#D8E3F4';

                        bgcolors[2] = '#FFFFFF';

                        smssubject = '<b>'+value['smssubject']+'</b>��<font color="#999999">��'+value['smsdate']+'����</font><a id="sms_'+value['smsid']+'" onclick="smsclick('+value['smsid']+', 1)" style="cursor:pointer;">�����Ĺرա�</a>';

                    } else if (value['smstype']==2) {

                        smssubject = '��'+value['sendname']+'�� <font color="#999999">��</font> '+value['smsdate']+' <font color="#999999">���Ÿ�����</font>��'+value['smssubject']+'������<a id="sms_'+value['smsid']+'" onclick="smsclick('+value['smsid']+', 2)" style="cursor:pointer;">��<b>���Ĺر�</b>��</a>';

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



                        if (confirm('ȷ���Ѿ��յ�������Ʒ����')) {

                            $.blockUI('<img src="http://static.jjwxc.net/images/loading.gif">  <strong>���Ժ�...</strong>');

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

                        var message = '&nbsp;&nbsp;�����յ���ӡˢƷ��ĥ�����ڴ��ϴ�ĥ����Ƭ(��Ƭ���ݰ���ӡˢƷĥ��λ�Ϳ�ݵ���),�Թ�ӡˢ���˶�,�����ؼġ�<br>���ϴ���Ƭ���󣬿������ϴ���<br>�ϴ�ͼƬ��ʽΪJPG����С��2M���ڣ���1��';

                        $.blockUI('<div align="center"><div style="float:right"><img src="http://static.jjwxc.net/images/close.gif" width="12" height="12" style="cursor:pointer" onClick="$.unblockUI()"/></div><br><br><b>'+message+'</b><br><br><br><input type="button" value="����ϴ�ͼƬ" class="pic" id="'+order_id+'"/>&nbsp;&nbsp;&nbsp;&nbsp;<input type="button" value="��  ��" onClick="$.unblockUI()"/></div>', {width: '330px', height: '200px', cursor: 'default'});

                        $('.pic').each(function() {

                            new AjaxUpload('#'+order_id, {

                                action: 'subscribe_print1.php?action=delayupload',

                                onSubmit: function(file, ext) {

                                    if (ext&&/(jpg){1}$/i.test(ext)) {

                                        $.blockUI('<img src="http://static.jjwxc.net/images/loading.gif">  <strong>���Ժ�...</strong>');

                                        this.setData({

                                            'id': order_id

                                        });

                                    } else {

                                        alert_blockUI('�ļ���ʽ����ֻ֧���ϴ�jpg�ı���ʽ');

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

            $("#sms_"+id).html("<img src=\"http://static.jjwxc.net/images/loading.gif\" width=\"16\" height=\"16\"> <font color=\"red\">���Ժ�</font>");

            $.post("sms.php", {smsid: id, smstype: smstype});

            $("#"+id).animate({opacity: 'hide'}, "slow");

            var total = parseInt($('#sms_total').html());

            if (total-1<=0) {

                $('#sms').html('������<span id="sms_total"></span>');

            } else {

                total = total-1;

                $('#sms_total').html(total);

            }

        } else {

            $("#vip_message1").html("<img src=\"http://static.jjwxc.net/images/loading.gif\" width=\"16\" height=\"16\"> <font color=\"red\">���Ժ�</font>");

            $.post("sms.php", {smsid: id, smstype: smstype});

            $("#vip_message").animate({opacity: 'hide'}, "slow");

        }

    }

</script>

<body>

    <div id="myjquerymenu" class="jquerycssmenu">

        <ul>

                        <li>

                <a href="javascript:">���ҵĽ�����</a>

                <ul>

                    <li><a href="logininfo.php?jsid=837021.1424156929">��ȫ��Ϣ</a></li>

                    <li><a href="userinfo.php?jsid=837021.1424156929">������Ϣ</a></li>

                    <li><a href="sms.php?jsid=837021.1424156929">վ�ڶ���</a></li>

                </ul>

            </li>

            <li>

                <a href="javascript:">�����顿</a>

                <ul>

                    <li><a href="favorite.php?jsid=837021.1424156929">�ղ��б�</a></li>

                    <li><a href="commentshistory.php?jsid=837021.1424156929">�ҷ���������</a></li>

                    <li><a href="vip_services.php?jsid=837021.1424156929">vip����</a></li>

                                     

                </ul>

            </li>       

            <script type="text/javascript">

                function demo() {

                    if (confirm('ֻ��Ҫ�������²���Ҫ��Ϊ���ߣ���ȷ��Ҫ������'))

                        location.href = ('http://my.jjwxc.net/registeauthor.php?jsid=837021.1424156929');

                }

            </script>

            <!--string(6) "281948"
 -->

            <li>

                <a href="javascript:">��д����</a>

                                    <ul>

                        <li><a href="publish.php?jsid=837021.1424156929">��������</a></li>

                        <li><a href="oneauthor_login.php?jsid=837021.1424156929">���¾���</a></li>

                        <li><a href="series.php?jsid=837021.1424156929">����ϵ��</a></li>

                        <li><a href="setcolumn.php?jsid=837021.1424156929">����ר��</a></li>

                        <li><a href="novelcomment.php?jsid=837021.1424156929">���յ�������</a></li>

                        <li><a href="goodnovelrecommend.php?jsid=837021.1424156929">��������</a></li>

                        <li><a href="contract.php?jsid=837021.1424156929"><b>-��ҪǩԼ-</b></a></li>

                    </ul>

                

            </li>	

            <li>

                <a href="javascript:">��ǩԼ����</a>

                <ul>

                    <li><a href="#">�����</a></li>

                                            <li><a href="vipnovel.php?jsid=837021.1424156929">�Լ���v</a></li>

                                            

                    <li><a href="complaint.php?jsid=837021.1424156929">����Ͷ��</a></li>

                                            <li><a href="novel_free_vip.php?jsid=837021.1424156929" style="color:red;font-weight:bold;">��ʱ���</a></li>

                        

                </ul>

            </li>

            <li>

                <a href="javascript:">������</a>

                <ul>

                    <li> <a href="bankbook.php?jsid=837021.1424156929">�ҵ����</a></li>

                    <li><a href="sendpointlist.php?jsid=837021.1424156929">���ּ�¼</a></li>

                    <li><a href="consumerecord.php?jsid=837021.1424156929">���Ѽ�¼</a></li>

                                            <li><a href="incomerecord.php?jsid=837021.1424156929">�����¼</a></li>

                        <li> <a href="payrecord.php?jsid=837021.1424156929">��������</a></li>

                                            <li><a href="http://my.jjwxc.net/pay/transfer.php?jsid=837021.1424156929">վ��ת��</a></li>

                </ul>

            </li>

            <li>

                <a href="javascript:">���������</a>

                <ul>

                    <li><a href="subscribe_print.php?jsid=837021.1424156929">����ӡˢ</a></li>

                    <li><a href="readerKingTickets.php?jsid=837021.1424156929">����Ʊ</a></li>

                    <li><a href="yueshi_exchange.php?jsid=837021.1424156929">��ʯ�һ�</a></li>

                    <li><a href="http://my.jjwxc.net/sp/2013pinwen/index.php?jsid=837021.1424156929">ƴ�Ļ</a></li>

                    <li><a href="http://my.jjwxc.net/backend/forest.php?jsid=837021.1424156929" style="color: red;font-weight: bold">ֲ������</a></li>

                    

                </ul>

            </li>		

            <li>

                <a href="javascript:" >����ֵ��</a>

                <ul>

                    <li><a href="/pay/pay.php?jsid=837021.1424156929">����</a></li>

                    <li><a href="/pay/yeepay_zfb.php?jsid=837021.1424156929">֧����</a></li>

                    <li><a href="/pay/phonepay.php?jsid=837021.1424156929">�����г�ֵ��</a></li>

                    <li><a href="/pay/ruyifu.php?jsid=837021.1424156929">��ͨ��ֵ��</a></li>

                    <li><a href="/pay/ctpay.php?jsid=837021.1424156929">���ų�ֵ��</a></li>

                    <li><a href="/pay/gamecard.php?jsid=837021.1424156929">��Ϸ�㿨</a></li>

                    <li><a href="/pay/remit_pay.php?jsid=837021.1424156929">�ʾ����л��</a></li>

                    <li><a href="/pay/vpay.php?jsid=837021.1424156929">�̻�/�绰�ֻ�</a></li>

                    <li><a href="/pay/umpay.php?jsid=837021.1424156929">�ֻ�֧��</a></li>

                    <li><a href="/pay/paypal.php?jsid=837021.1424156929">paypal�����ֵ</a></li>

                    <li><a href="drweb.php">��ֵ�</a>

                </ul>

            </li>

                            <li><a href="javascript:" style="color: red;font-weight: bold" >����������</a>

                    <ul>

                        <li><a href="http://my.jjwxc.net/backend/examine_read_primary.php" target="_blank" style="color: red;font-weight: bold">������������</a></li>

                        <li><a href="http://my.jjwxc.net/backend/comment_check.php" target="_blank" style="color: red;font-weight: bold">������������</a></li>

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

                <td width="949" colspan="3" align="left" bgcolor="#eefaee">�𾴵ġ�<font color="red">kom9ing@163.com (��Ӱ˪) </font>���Ľ����ͻ���:<font color="red">837021</font> </td>

            </tr>

            <tr bgcolor="#eefaee">

                <td colspan="3" align="center"><table width="828" border="0" align="left" bgcolor="#009900" cellpadding="0" cellspacing="0">

                                                <tr bgcolor="#eefaee">

                            <td align="left" nowrap>���ĳɹ���½�ܴ�����538<img src="http://www.jjwxc.cn/passport/index/sid/837021_5d84e241ff5996e6042d0bb7041f3798" height="0" width="0" border="0" /></td>

                            <td align="left">&nbsp;</td>

                        </tr>

                        <tr bgcolor="#eefaee">

                            <td align="left" nowrap>�����γɹ���½ʱ�䣺2015-02-17 15:08:48</td>

                            <td align="left">&nbsp;</td>

                        </tr>

                        <tr bgcolor="#eefaee">

                            <td align="left" nowrap>������ɹ���½ʱ�䣺2015-02-17 15:04:32</td>

                            <td align="left">������ִ�ʱ���������ϴε�½ʱ�䣬��˵������������������½�ɹ���ǿ�ҽ����޸����롣</td>

                        </tr>

                        <tr bgcolor="#eefaee">

                            <td align="left" nowrap>�����ʧ�ܵ�½ʱ�䣺2010-09-22 18:23:58</td>

                            <td align="left">������ִ�ʱ���������ϴ�ʧ��ʱ�䣬��˵���������ô��������½ʧ�ܡ�</td>

                        </tr>

                        <tr bgcolor="#eefaee">

                            <td align="left" colspan="2" nowrap><b>�˺Ű�ȫ��Ϣ�䶯����(�������һ���):</b></td>

                        </tr>

                                            </table></td>

            </tr>

        </table>

<br/><div id="footer">

    <p class="red"><a href="http://www.jjwxc.net/aboutus/" target="_blank"><font color="red">��������</font></a> - <a href="http://www.jjwxc.net/aboutus/#fragment-29" target="_blank"><font color="red">��ϵ��ʽ</font></a> - <a href="http://bbs.jjwxc.net/board.php?board=22&page=1" target="_blank"><font color="red">�������</font></a> - <a href="http://help.jjwxc.net/user/more/24/0" target="_blank"><font color="red">���ߵ���</font></a> - <a href="http://help.jjwxc.net/user/more/23/0" target="_blank"><font color="red">���ߵ���</font></a> - <a href="http://www.jjwxc.net/invite.php" target="_blank"><font color="red">�����Ͳ�</font></a> - <a href="http://help.jjwxc.net/user/article/76" target="_blank"><font color="red">Ͷ��˵��</font></a> - <a href="http://www.jjwxc.net/jjwxcauthority.php" target="_blank"><font color="red">Ȩ������</font></a> - <a href="http://www.jjwxc.net/jjwxcad.php" target="_blank"><font color="red">������</font></a> - <a href="http://www.jjwxc.net/friendly.php" target="_blank"><font color="red">��������</font></a> - <a href="http://help.jjwxc.net/user/more_index" target="_blank"><font color="red">��������</font></a></p>

    <p class="red"> Copyright By ������ѧ�� www.jjwxc.net All rights reserved</p>

    <p class="red">Processed in 0.05 second(s) �������2015-02-17 15:08:49</p>

    <p class="red"><a href="http://www.miibeian.gov.cn/" target="_blank" rel="nofollow">��ICP֤080637��</a> <a href="http://www.miibeian.gov.cn/" target="_blank" rel="nofollow">��ICP��12006214��-2</a><font color="#666666"> �³���֤(��)��206�� ����������11010502023476</font></p>

    <p class="red">��վȫ����Ʒ������С˵����������ȨΪԭ���������� ����վ��Ϊ����д���ṩ�ϴ��ռ䴢��ƽ̨����վ����¼��Ʒ���������⡢������ۼ���վ����֮�������������Ϊ</p>

    <p class="red">�뱾վ�����޹ء���վҳ���ȨΪ������ѧ�����У��κε�λ������δ����Ȩ����ת�ء����ơ��ַ����Լ�������ҵ��;��</p>

    <p class="red">��Ҫ���������������߷�����Ʒʱ�ϸ����ع��һ�������Ϣ����취�涨�����Ǿܾ��κ�ɫ�鱩��С˵��һ�����֣�����ɾ��Υ����Ʒ�������߽�ͬʱ��������˺š�</p>

    <p class="red">��������������������г�ɾ����硣</p>

</div>

<!-- google ���ݺ��ü��صĹ���Ƶ�ҳ�� 20140325 -->

<!-- Google Admanager BEGIN ��Must Put behind all googleADManager function-->

<script type="text/javascript" src="http://partner.googleadservices.com/gampad/google_service.js"></script>

<script type="text/javascript">JJ_ADS_GID = 'ca-pub-7602717919537096';

    GS_googleAddAdSenseService(JJ_ADS_GID);

    GS_googleEnableAllServices();</script>

<!-- Google Admanager END -->



<!-- Google Admanager BEGIN ���ݺ��ü��صĹ�� �������Ի����� -->

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



<!-- ���ع��λ-->

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
    aelems = re.findall('<input type="button".*value="��ͨ��"', content)
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
    aelems = re.findall('��ʷ����������.*</font>',content)
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
    //ͨ������
    function pass(commentid, replyid, novelid, type) {
        $.get('comment_check.php?act=pass&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid, function(data) {
            if (data) {
                $('#'+commentid+'-'+replyid).remove();
                var selCheckboxObj = $("input[name='ids']");
                if (selCheckboxObj.length==0||type=='one') {
                    window.location.href = "http://my.jjwxc.net/backend/comment_check.php";
                }
            } else {
                alert('���ִ���');
            }
        })
    }

    //��ͨ������
    function del(commentid, replyid, novelid) {
        $.get('comment_check.php?act=del&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid, function(data) {
            if (data) {
                $('#'+commentid+'-'+replyid).remove();
                var selCheckboxObj = $("input[name='ids']");
                if (selCheckboxObj.length==0||data) {
                    window.location.href = "http://my.jjwxc.net/backend/comment_check.php";
                }
            } else {
                alert('���ִ���')
            }
        })
    }

    //����ͨ��
    function batchControll() {
        //���Ȼ�ȡҳ�����й�ѡ�ĸ�ѡ��
        var selCheckboxObj = $("input[name='ids']:checked");
        var passvalue;
        for (var i = 0; i<selCheckboxObj.length; i++) {
            passvalue = selCheckboxObj[i].value.split("_");// ��ÿ��"_"�����зֽ⡣
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
                <b>��������������<font color="red">0</font></b><br/><br/>
                <b>��ʷ������������<font color="red">802336</font></b><br/><br/>                
                <span style="color:red"><b>�����ݸ���ʱ�䣺 2015��02��17�� 00:00:00��</b></span>
            </td>
        </tr>
        <tr bgcolor="#FFF">
            <td colspan="2" align="left">
                <font color="red">
                <b>��˲�ͨ��������</b><br/><br/>
                1������������棬���磺����Ʊ����ǹ֧����С��ȵȡ� 2������ɫ����Ϣ����������д����3��������ϵ��ʽ������QQ���ֻ����룬����ȵ� 4��������վ���ӡ�</font>
            </td>

        </tr>
        <tr align="center"  bgcolor="#9FD59E">
            <td width="20">&nbsp;</td>
            <td width="680" align="center" style="font-size: 14px;">��������</td>
        </tr>
                    <tr align="right" bgcolor="#eefaee" id = "1968-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="1968_0_195424" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(1968,0)">
                        bluerobin���⺢�����ǻ�Ծ�������ܿɰ�~~                    </div>
            <center>
                <span id='1968-0Recalculation'><input type="button" id ="1231968"  onclick="pass(1968,0,195424,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='1968-0Recalculationdel'><input type="button" id ="1231968" onclick="del(1968,0,195424)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "13572-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="13572_0_195343" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(13572,0)">
                        Ī���Ͽ����ϰɣ�ȫ����Բ��                    </div>
            <center>
                <span id='13572-0Recalculation'><input type="button" id ="12313572"  onclick="pass(13572,0,195343,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='13572-0Recalculationdel'><input type="button" id ="12313572" onclick="del(13572,0,195343)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
            <tr  bgcolor="#eefaee"><td colspan="3" align="center"><a href="http://my.jjwxc.net/backend/comment_check.php">��һҳ</a></td></tr>        <tr bgcolor="#eefaee">
            <td colspan="2" align="center">
                <input type="button" name="buttondel" id = "buttondel" value="������ͨ��" onclick="batchControll()" style="color:blue;"/>
            </td>

        </tr>
        <tr bgcolor="#eefaee">
            <td colspan="2" align="left">
                <font color="red">
                <b>��˲�ͨ��������</b><br/><br/>
                1������������棬���磺����Ʊ����ǹ֧����С��ȵȡ� 2������ɫ����Ϣ����������д����3��������ϵ��ʽ������QQ���ֻ����룬����ȵ� 4��������վ���ӡ�</font><br/><br/> 
                <font color="blue">
                ����������������׼��ÿ���3000��(6000���ֽ�)����2������ң�ÿ�ܰ���ʵ����Ч������ݽ��н��㣮�������ڡ��ҵ����в鿴��
                </font>
            </td>
        </tr>

    </table>
</form>
<div align = "center">
    <font color="red">�����ܺ�ʱ��0.065937042236328 seconds  ��ǰ����ʱ�䣺2015-02-17 15:09:57</font>
</div>
>>> aelems = extract_val(cont)
['<input type="button" id ="1231968"  onclick="pass(1968,0,195424,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313572"  onclick="pass(13572,0,195343,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="1231968"  onclick="pass(1968,0,195424,'one')" value="��ͨ��"
="1231968"

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    aelems = extract_val(cont)
  File "<pyshell#19>", line 11, in extract_val
    val = matches.group(1)
AttributeError: 'NoneType' object has no attribute 'group'
>>>  def extract_val(content):
    vals = []
    aelems = re.findall('<input type="button".*value="��ͨ��"', content)
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
    aelems = re.findall('<input type="button".*value="��ͨ��"', content)
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
<input type="button" id ="1231968"  onclick="pass(1968,0,195424,'one')" value="��ͨ��"
onclick="pass(1968,0,195424,'one')"
<input type="button" id ="12313572"  onclick="pass(13572,0,195343,'one')" value="��ͨ��"
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
    //ͨ������
    function pass(commentid, replyid, novelid, type) {
        $.get('comment_check.php?act=pass&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid, function(data) {
            if (data) {
                $('#'+commentid+'-'+replyid).remove();
                var selCheckboxObj = $("input[name='ids']");
                if (selCheckboxObj.length==0||type=='one') {
                    window.location.href = "http://my.jjwxc.net/backend/comment_check.php";
                }
            } else {
                alert('���ִ���');
            }
        })
    }

    //��ͨ������
    function del(commentid, replyid, novelid) {
        $.get('comment_check.php?act=del&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid, function(data) {
            if (data) {
                $('#'+commentid+'-'+replyid).remove();
                var selCheckboxObj = $("input[name='ids']");
                if (selCheckboxObj.length==0||data) {
                    window.location.href = "http://my.jjwxc.net/backend/comment_check.php";
                }
            } else {
                alert('���ִ���')
            }
        })
    }

    //����ͨ��
    function batchControll() {
        //���Ȼ�ȡҳ�����й�ѡ�ĸ�ѡ��
        var selCheckboxObj = $("input[name='ids']:checked");
        var passvalue;
        for (var i = 0; i<selCheckboxObj.length; i++) {
            passvalue = selCheckboxObj[i].value.split("_");// ��ÿ��"_"�����зֽ⡣
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
                <b>��������������<font color="red">0</font></b><br/><br/>
                <b>��ʷ������������<font color="red">802336</font></b><br/><br/>                
                <span style="color:red"><b>�����ݸ���ʱ�䣺 2015��02��17�� 00:00:00��</b></span>
            </td>
        </tr>
        <tr bgcolor="#FFF">
            <td colspan="2" align="left">
                <font color="red">
                <b>��˲�ͨ��������</b><br/><br/>
                1������������棬���磺����Ʊ����ǹ֧����С��ȵȡ� 2������ɫ����Ϣ����������д����3��������ϵ��ʽ������QQ���ֻ����룬����ȵ� 4��������վ���ӡ�</font>
            </td>

        </tr>
        <tr align="center"  bgcolor="#9FD59E">
            <td width="20">&nbsp;</td>
            <td width="680" align="center" style="font-size: 14px;">��������</td>
        </tr>
                    <tr align="right" bgcolor="#eefaee" id = "167938-32996" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="167938_32996_2135677" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(167938,32996)">
                        ī�У��ǵĹ�������                    </div>
            <center>
                <span id='167938-32996Recalculation'><input type="button" id ="123167938"  onclick="pass(167938,32996,2135677,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='167938-32996Recalculationdel'><input type="button" id ="123167938" onclick="del(167938,32996,2135677)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "192452-44605" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="192452_44605_2278581" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(192452,44605)">
                        �ع���<font style="background-color: yellow;font-weight: bold;">745038155</font>@qq.com<br>���󡫡�����                    </div>
            <center>
                <span id='192452-44605Recalculation'><input type="button" id ="123192452"  onclick="pass(192452,44605,2278581,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='192452-44605Recalculationdel'><input type="button" id ="123192452" onclick="del(192452,44605,2278581)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "17197-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="17197_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(17197,0)">
                        kuailede�����������ˣ���ֱ����������                    </div>
            <center>
                <span id='17197-0Recalculation'><input type="button" id ="12317197"  onclick="pass(17197,0,196136,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='17197-0Recalculationdel'><input type="button" id ="12317197" onclick="del(17197,0,196136)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "173344-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="173344_0_2266317" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(173344,0)">
                        ���أ�С����                    </div>
            <center>
                <span id='173344-0Recalculation'><input type="button" id ="123173344"  onclick="pass(173344,0,2266317,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='173344-0Recalculationdel'><input type="button" id ="123173344" onclick="del(173344,0,2266317)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "11948-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="11948_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(11948,0)">
                        ��������,ż���ͶС��һƱ!!!!!!!<br>                    </div>
            <center>
                <span id='11948-0Recalculation'><input type="button" id ="12311948"  onclick="pass(11948,0,196136,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='11948-0Recalculationdel'><input type="button" id ="12311948" onclick="del(11948,0,196136)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16818-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16818_0_196949" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16818,0)">
                        rhea���ѵ���˵�еĻ��ľ���ʵ?....��ѽ,��ôû�������Ǹ�������ѽ�Ǻ�                    </div>
            <center>
                <span id='16818-0Recalculation'><input type="button" id ="12316818"  onclick="pass(16818,0,196949,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16818-0Recalculationdel'><input type="button" id ="12316818" onclick="del(16818,0,196949)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "176838-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="176838_0_2307154" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(176838,0)">
                        gun  and   ���㣺gun ��<br>&lt;font color=#009900&gt;�����۷��Խ�����׿�ֻ�APP�ͻ���(http://m.jjwxc.net/download/android/)&lt;/font&gt;                    </div>
            <center>
                <span id='176838-0Recalculation'><input type="button" id ="123176838"  onclick="pass(176838,0,2307154,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='176838-0Recalculationdel'><input type="button" id ="123176838" onclick="del(176838,0,2307154)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "11682-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="11682_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(11682,0)">
                        ������С������~~~                    </div>
            <center>
                <span id='11682-0Recalculation'><input type="button" id ="12311682"  onclick="pass(11682,0,196136,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='11682-0Recalculationdel'><input type="button" id ="12311682" onclick="del(11682,0,196136)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16771-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16771_0_196908" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16771,0)">
                        J��Ů��Ҳ̫�����˰��������������������Ⱥû���ӵ�����ǣ�ű�����                    </div>
            <center>
                <span id='16771-0Recalculation'><input type="button" id ="12316771"  onclick="pass(16771,0,196908,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16771-0Recalculationdel'><input type="button" id ="12316771" onclick="del(16771,0,196908)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "176829-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="176829_0_2307154" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(176829,0)">
                        ��Ԩ����������������T_T<br>&lt;font color=#009900&gt;�����۷��Խ����ֻ�վ(http://m.jjwxc.com/)&lt;/font&gt;                    </div>
            <center>
                <span id='176829-0Recalculation'><input type="button" id ="123176829"  onclick="pass(176829,0,2307154,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='176829-0Recalculationdel'><input type="button" id ="123176829" onclick="del(176829,0,2307154)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16736-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16736_0_196490" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16736,0)">
                        65���ܰ�!��������,������.                    </div>
            <center>
                <span id='16736-0Recalculation'><input type="button" id ="12316736"  onclick="pass(16736,0,196490,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16736-0Recalculationdel'><input type="button" id ="12316736" onclick="del(16736,0,196490)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "142959-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="142959_0_2317349" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(142959,0)">
                        lalal����һ��Ԥ��ҪŰ�˰�������ô��                    </div>
            <center>
                <span id='142959-0Recalculation'><input type="button" id ="123142959"  onclick="pass(142959,0,2317349,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='142959-0Recalculationdel'><input type="button" id ="123142959" onclick="del(142959,0,2317349)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "7516-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="7516_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(7516,0)">
                        ������С�����Ͱ�~                    </div>
            <center>
                <span id='7516-0Recalculation'><input type="button" id ="1237516"  onclick="pass(7516,0,196136,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='7516-0Recalculationdel'><input type="button" id ="1237516" onclick="del(7516,0,196136)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "12961-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="12961_0_196029" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(12961,0)">
                        ��ˮ������֧�������ܹ�                    </div>
            <center>
                <span id='12961-0Recalculation'><input type="button" id ="12312961"  onclick="pass(12961,0,196029,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='12961-0Recalculationdel'><input type="button" id ="12312961" onclick="del(12961,0,196029)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "14717-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="14717_0_196312" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(14717,0)">
                        Ƽ�����ҵĳ��������������Ļ����Ұ�������𰡡�                    </div>
            <center>
                <span id='14717-0Recalculation'><input type="button" id ="12314717"  onclick="pass(14717,0,196312,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='14717-0Recalculationdel'><input type="button" id ="12314717" onclick="del(14717,0,196312)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "15438-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="15438_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(15438,0)">
                        ww�����ϣ����������������һ��Ҳ��ϣ����������<br>                    </div>
            <center>
                <span id='15438-0Recalculation'><input type="button" id ="12315438"  onclick="pass(15438,0,196136,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='15438-0Recalculationdel'><input type="button" id ="12315438" onclick="del(15438,0,196136)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "176933-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="176933_0_2307154" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(176933,0)">
                        ·�˼ף�ֱ��ϴ��ֱ��ϴ�裡����<br>&lt;font color=#009900&gt;�����۷��Խ�����׿�ֻ�APP�ͻ���(http://m.jjwxc.net/download/android/)&lt;/font&gt;                    </div>
            <center>
                <span id='176933-0Recalculation'><input type="button" id ="123176933"  onclick="pass(176933,0,2307154,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='176933-0Recalculationdel'><input type="button" id ="123176933" onclick="del(176933,0,2307154)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "133181-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="133181_0_2264374" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(133181,0)">
                        �ɿڣ����ںá�ף���������֣��Ҹ���<br>���д�ģ�����һ���ȡ�                    </div>
            <center>
                <span id='133181-0Recalculation'><input type="button" id ="123133181"  onclick="pass(133181,0,2264374,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='133181-0Recalculationdel'><input type="button" id ="123133181" onclick="del(133181,0,2264374)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "17009-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="17009_0_196459" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(17009,0)">
                        s811fish�����ߺ��ڿ죬����                    </div>
            <center>
                <span id='17009-0Recalculation'><input type="button" id ="12317009"  onclick="pass(17009,0,196459,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='17009-0Recalculationdel'><input type="button" id ="12317009" onclick="del(17009,0,196459)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16966-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16966_0_196654" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16966,0)">
                        xing����&amp;lt;���쿪ʼ��ħ��&gt;�Ļ���.������!!                    </div>
            <center>
                <span id='16966-0Recalculation'><input type="button" id ="12316966"  onclick="pass(16966,0,196654,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16966-0Recalculationdel'><input type="button" id ="12316966" onclick="del(16966,0,196654)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "250575-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="250575_0_2308233" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(250575,0)">
                        �߸����ȴ���<br>&lt;font color=#009900&gt;�����۷��Խ����ֻ�վ(http://m.jjwxc.com/)&lt;/font&gt;                    </div>
            <center>
                <span id='250575-0Recalculation'><input type="button" id ="123250575"  onclick="pass(250575,0,2308233,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='250575-0Recalculationdel'><input type="button" id ="123250575" onclick="del(250575,0,2308233)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "91814-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="91814_0_2323133" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(91814,0)">
                        ��誣�С�ܾ�Ȼ���ˡѨ���Ԥ���Ժ�ᱻ����Ϊ����ֵ��ܶ��<br>&lt;font color=#009900&gt;�����۷��Խ����ֻ�վ(http://m.jjwxc.com/)&lt;/font&gt;                    </div>
            <center>
                <span id='91814-0Recalculation'><input type="button" id ="12391814"  onclick="pass(91814,0,2323133,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='91814-0Recalculationdel'><input type="button" id ="12391814" onclick="del(91814,0,2323133)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "125176-42516" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="125176_42516_2043685" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(125176,42516)">
                        <font style="background-color: yellow;font-weight: bold;">16412503</font>��ôô�գ����ֻ��������˼��飬̫�ÿ���?<br>&lt;font color=#009900&gt;�����۷��Խ�����׿�ֻ�APP�ͻ���(http://m.jjwxc.net/download/android/)&lt;/font&gt;                    </div>
            <center>
                <span id='125176-42516Recalculation'><input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='125176-42516Recalculationdel'><input type="button" id ="123125176" onclick="del(125176,42516,2043685)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "14659-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="14659_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(14659,0)">
                        ling���������¾͸��ˣ����������˸�����!                    </div>
            <center>
                <span id='14659-0Recalculation'><input type="button" id ="12314659"  onclick="pass(14659,0,196136,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='14659-0Recalculationdel'><input type="button" id ="12314659" onclick="del(14659,0,196136)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "52678-38055" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="52678_38055_1914340" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(52678,38055)">
                        ��Ů��ͦʬ����                    </div>
            <center>
                <span id='52678-38055Recalculation'><input type="button" id ="12352678"  onclick="pass(52678,38055,1914340,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='52678-38055Recalculationdel'><input type="button" id ="12352678" onclick="del(52678,38055,1914340)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16757-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16757_0_196519" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16757,0)">
                        �����ѣ�ʲôСƨ��                    </div>
            <center>
                <span id='16757-0Recalculation'><input type="button" id ="12316757"  onclick="pass(16757,0,196519,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16757-0Recalculationdel'><input type="button" id ="12316757" onclick="del(16757,0,196519)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "17201-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="17201_0_196838" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(17201,0)">
                        ����è�䣺ò�ƴ����Ķ����Ϸ�?���˺ü����ط���,��<br>��ʵ���˲��ٴ����Ĳ������ʵ�����е㲻����˼Ŷ~~<br>ż��ϲ��Ű��,Ľ&amp;lt;����ҹ&gt;֮������,��ϧ������.��֪�ɷ����ؿ�֮��...                    </div>
            <center>
                <span id='17201-0Recalculation'><input type="button" id ="12317201"  onclick="pass(17201,0,196838,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='17201-0Recalculationdel'><input type="button" id ="12317201" onclick="del(17201,0,196838)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "247769-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="247769_0_2186130" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(247769,0)">
                        ·�˼ף�����ô�о������˶Եе�flag�ء�_��<br>&lt;font color=#009900&gt;�����۷��Խ����ֻ�վ(http://wap.jjwxc.net/)&lt;/font&gt;                    </div>
            <center>
                <span id='247769-0Recalculation'><input type="button" id ="123247769"  onclick="pass(247769,0,2186130,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='247769-0Recalculationdel'><input type="button" id ="123247769" onclick="del(247769,0,2186130)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "13869-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="13869_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(13869,0)">
                        ��YA��С����ô����.!?<br>Ϊʲô���ǲ���д��...<br>���ź������ѡ��ѽ...                    </div>
            <center>
                <span id='13869-0Recalculation'><input type="button" id ="12313869"  onclick="pass(13869,0,196136,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='13869-0Recalculationdel'><input type="button" id ="12313869" onclick="del(13869,0,196136)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16774-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16774_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16774,0)">
                        VV�������Լ�˵����������Ū4..���ڻ�������..TMD.2B                    </div>
            <center>
                <span id='16774-0Recalculation'><input type="button" id ="12316774"  onclick="pass(16774,0,196136,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16774-0Recalculationdel'><input type="button" id ="12316774" onclick="del(16774,0,196136)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "11750-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="11750_0_196481" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(11750,0)">
                        ��~��֧��!!����!!                    </div>
            <center>
                <span id='11750-0Recalculation'><input type="button" id ="12311750"  onclick="pass(11750,0,196481,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='11750-0Recalculationdel'><input type="button" id ="12311750" onclick="del(11750,0,196481)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16890-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16890_0_196136" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16890,0)">
                        ţţ���Ѿ�����Ԥ�����Ժ��ж�Ű�ˡ�������                    </div>
            <center>
                <span id='16890-0Recalculation'><input type="button" id ="12316890"  onclick="pass(16890,0,196136,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16890-0Recalculationdel'><input type="button" id ="12316890" onclick="del(16890,0,196136)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "128255-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="128255_0_2281167" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(128255,0)">
                        Ҷ�³ǣ�����<br>&lt;font color=#009900&gt;�����۷��Խ����ֻ�վ(http://m.jjwxc.com/)&lt;/font&gt;                    </div>
            <center>
                <span id='128255-0Recalculation'><input type="button" id ="123128255"  onclick="pass(128255,0,2281167,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='128255-0Recalculationdel'><input type="button" id ="123128255" onclick="del(128255,0,2281167)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "7859-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="7859_0_196908" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(7859,0)">
                        �磺Խ��Խϲ����,������Щ���Ϊ�η�Ҫ��Ů�����˺���,�ǲ����Ե�����ߵ�����̫��������.                    </div>
            <center>
                <span id='7859-0Recalculation'><input type="button" id ="1237859"  onclick="pass(7859,0,196908,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='7859-0Recalculationdel'><input type="button" id ="1237859" onclick="del(7859,0,196908)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "7985-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="7985_0_196459" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(7985,0)">
                        00���ں󹬲������������ƽ����                    </div>
            <center>
                <span id='7985-0Recalculation'><input type="button" id ="1237985"  onclick="pass(7985,0,196459,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='7985-0Recalculationdel'><input type="button" id ="1237985" onclick="del(7985,0,196459)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "12607-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="12607_0_196908" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(12607,0)">
                        �����¸���Ŷ                    </div>
            <center>
                <span id='12607-0Recalculation'><input type="button" id ="12312607"  onclick="pass(12607,0,196908,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='12607-0Recalculationdel'><input type="button" id ="12312607" onclick="del(12607,0,196908)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "266260-42126" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="266260_42126_2230334" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(266260,42126)">
                        ��Ұ �ƣ�����������up���ú���<br>&lt;font color=#009900&gt;�����۷��Խ����ֻ�վ(http://wap.jjwxc.net/)&lt;/font&gt;                    </div>
            <center>
                <span id='266260-42126Recalculation'><input type="button" id ="123266260"  onclick="pass(266260,42126,2230334,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='266260-42126Recalculationdel'><input type="button" id ="123266260" onclick="del(266260,42126,2230334)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "129750-34985" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="129750_34985_2174576" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(129750,34985)">
                        ���������й��ڳ�˾���Զ������ǲ�֪��ѡ�ж��汾�Ļ��Ƿ���²۰汾�ġ��c(�R���Q)��                    </div>
            <center>
                <span id='129750-34985Recalculation'><input type="button" id ="123129750"  onclick="pass(129750,34985,2174576,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='129750-34985Recalculationdel'><input type="button" id ="123129750" onclick="del(129750,34985,2174576)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "142777-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="142777_0_2317349" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(142777,0)">
                        lovelyz����Ű�Ľ���<br>&lt;font color=#009900&gt;�����۷��Խ����ֻ�վ(http://m.jjwxc.com/)&lt;/font&gt;                    </div>
            <center>
                <span id='142777-0Recalculation'><input type="button" id ="123142777"  onclick="pass(142777,0,2317349,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='142777-0Recalculationdel'><input type="button" id ="123142777" onclick="del(142777,0,2317349)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
                        <tr align="right" bgcolor="#eefaee" id = "16945-0" class="" onMouseMove ="rows(this)" onMouseOut="outrows(this)">
                <td align="center">
                    <input name="ids" type="checkbox" id="logids" value="16945_0_196957" />
                </td>
                <td align="left" style="width:500px;word-break:break-all;word-wrap:break-word;font-size:14px;line-height:1.8em;"><div onclick="toggleselect(16945,0)">
                        123��������Ů����ϲ��,������ִ���ȥ������.��Щ�Ѵ�Խ��ȥ��Ů��д��ų���ޱȵ�,��������Խ��Խ����.                    </div>
            <center>
                <span id='16945-0Recalculation'><input type="button" id ="12316945"  onclick="pass(16945,0,196957,'one')" value="��ͨ��" style="color:blue;"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span id='16945-0Recalculationdel'><input type="button" id ="12316945" onclick="del(16945,0,196957)" value="����ͨ��" style="color:red;"></span>            </center>
            </td>
            </tr>
            <tr  bgcolor="#eefaee"><td colspan="3" align="center"><a href="http://my.jjwxc.net/backend/comment_check.php">��һҳ</a></td></tr>        <tr bgcolor="#eefaee">
            <td colspan="2" align="center">
                <input type="button" name="buttondel" id = "buttondel" value="������ͨ��" onclick="batchControll()" style="color:blue;"/>
            </td>

        </tr>
        <tr bgcolor="#eefaee">
            <td colspan="2" align="left">
                <font color="red">
                <b>��˲�ͨ��������</b><br/><br/>
                1������������棬���磺����Ʊ����ǹ֧����С��ȵȡ� 2������ɫ����Ϣ����������д����3��������ϵ��ʽ������QQ���ֻ����룬����ȵ� 4��������վ���ӡ�</font><br/><br/> 
                <font color="blue">
                ����������������׼��ÿ���3000��(6000���ֽ�)����2������ң�ÿ�ܰ���ʵ����Ч������ݽ��н��㣮�������ڡ��ҵ����в鿴��
                </font>
            </td>
        </tr>

    </table>
</form>
<div align = "center">
    <font color="red">�����ܺ�ʱ��0.036336183547974 seconds  ��ǰ����ʱ�䣺2015-02-17 15:17:09</font>
</div>
>>> print find_result(cont)
['\xc0\xfa\xca\xb7\xd7\xdc\xc6\xc0\xc9\xf3\xd7\xd6\xca\xfd\xa3\xba<font color="red">802336</font>']
>>> aelems = extract_val(cont)
['<input type="button" id ="123167938"  onclick="pass(167938,32996,2135677,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123192452"  onclick="pass(192452,44605,2278581,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317197"  onclick="pass(17197,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123173344"  onclick="pass(173344,0,2266317,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311948"  onclick="pass(11948,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316818"  onclick="pass(16818,0,196949,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176838"  onclick="pass(176838,0,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311682"  onclick="pass(11682,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316771"  onclick="pass(16771,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176829"  onclick="pass(176829,0,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316736"  onclick="pass(16736,0,196490,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123142959"  onclick="pass(142959,0,2317349,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237516"  onclick="pass(7516,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312961"  onclick="pass(12961,0,196029,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314717"  onclick="pass(14717,0,196312,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12315438"  onclick="pass(15438,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123176933"  onclick="pass(176933,0,2307154,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123133181"  onclick="pass(133181,0,2264374,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317009"  onclick="pass(17009,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316966"  onclick="pass(16966,0,196654,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123250575"  onclick="pass(250575,0,2308233,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12391814"  onclick="pass(91814,0,2323133,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12314659"  onclick="pass(14659,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12352678"  onclick="pass(52678,38055,1914340,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316757"  onclick="pass(16757,0,196519,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12317201"  onclick="pass(17201,0,196838,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123247769"  onclick="pass(247769,0,2186130,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12313869"  onclick="pass(13869,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316774"  onclick="pass(16774,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12311750"  onclick="pass(11750,0,196481,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316890"  onclick="pass(16890,0,196136,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123128255"  onclick="pass(128255,0,2281167,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237859"  onclick="pass(7859,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="1237985"  onclick="pass(7985,0,196459,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12312607"  onclick="pass(12607,0,196908,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123266260"  onclick="pass(266260,42126,2230334,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123129750"  onclick="pass(129750,34985,2174576,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="123142777"  onclick="pass(142777,0,2317349,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"', '<input type="button" id ="12316945"  onclick="pass(16945,0,196957,\'one\')" value="\xa1\xcc\xcd\xa8\xb9\xfd"']
<input type="button" id ="123167938"  onclick="pass(167938,32996,2135677,'one')" value="��ͨ��"
onclick="pass(167938,32996,2135677,'one')"
<input type="button" id ="123192452"  onclick="pass(192452,44605,2278581,'one')" value="��ͨ��"
onclick="pass(192452,44605,2278581,'one')"
<input type="button" id ="12317197"  onclick="pass(17197,0,196136,'one')" value="��ͨ��"
onclick="pass(17197,0,196136,'one')"
<input type="button" id ="123173344"  onclick="pass(173344,0,2266317,'one')" value="��ͨ��"
onclick="pass(173344,0,2266317,'one')"
<input type="button" id ="12311948"  onclick="pass(11948,0,196136,'one')" value="��ͨ��"
onclick="pass(11948,0,196136,'one')"
<input type="button" id ="12316818"  onclick="pass(16818,0,196949,'one')" value="��ͨ��"
onclick="pass(16818,0,196949,'one')"
<input type="button" id ="123176838"  onclick="pass(176838,0,2307154,'one')" value="��ͨ��"
onclick="pass(176838,0,2307154,'one')"
<input type="button" id ="12311682"  onclick="pass(11682,0,196136,'one')" value="��ͨ��"
onclick="pass(11682,0,196136,'one')"
<input type="button" id ="12316771"  onclick="pass(16771,0,196908,'one')" value="��ͨ��"
onclick="pass(16771,0,196908,'one')"
<input type="button" id ="123176829"  onclick="pass(176829,0,2307154,'one')" value="��ͨ��"
onclick="pass(176829,0,2307154,'one')"
<input type="button" id ="12316736"  onclick="pass(16736,0,196490,'one')" value="��ͨ��"
onclick="pass(16736,0,196490,'one')"
<input type="button" id ="123142959"  onclick="pass(142959,0,2317349,'one')" value="��ͨ��"
onclick="pass(142959,0,2317349,'one')"
<input type="button" id ="1237516"  onclick="pass(7516,0,196136,'one')" value="��ͨ��"
onclick="pass(7516,0,196136,'one')"
<input type="button" id ="12312961"  onclick="pass(12961,0,196029,'one')" value="��ͨ��"
onclick="pass(12961,0,196029,'one')"
<input type="button" id ="12314717"  onclick="pass(14717,0,196312,'one')" value="��ͨ��"
onclick="pass(14717,0,196312,'one')"
<input type="button" id ="12315438"  onclick="pass(15438,0,196136,'one')" value="��ͨ��"
onclick="pass(15438,0,196136,'one')"
<input type="button" id ="123176933"  onclick="pass(176933,0,2307154,'one')" value="��ͨ��"
onclick="pass(176933,0,2307154,'one')"
<input type="button" id ="123133181"  onclick="pass(133181,0,2264374,'one')" value="��ͨ��"
onclick="pass(133181,0,2264374,'one')"
<input type="button" id ="12317009"  onclick="pass(17009,0,196459,'one')" value="��ͨ��"
onclick="pass(17009,0,196459,'one')"
<input type="button" id ="12316966"  onclick="pass(16966,0,196654,'one')" value="��ͨ��"
onclick="pass(16966,0,196654,'one')"
<input type="button" id ="123250575"  onclick="pass(250575,0,2308233,'one')" value="��ͨ��"
onclick="pass(250575,0,2308233,'one')"
<input type="button" id ="12391814"  onclick="pass(91814,0,2323133,'one')" value="��ͨ��"
onclick="pass(91814,0,2323133,'one')"
<input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,'one')" value="��ͨ��"
onclick="pass(125176,42516,2043685,'one')"
<input type="button" id ="12314659"  onclick="pass(14659,0,196136,'one')" value="��ͨ��"
onclick="pass(14659,0,196136,'one')"
<input type="button" id ="12352678"  onclick="pass(52678,38055,1914340,'one')" value="��ͨ��"
onclick="pass(52678,38055,1914340,'one')"
<input type="button" id ="12316757"  onclick="pass(16757,0,196519,'one')" value="��ͨ��"
onclick="pass(16757,0,196519,'one')"
<input type="button" id ="12317201"  onclick="pass(17201,0,196838,'one')" value="��ͨ��"
onclick="pass(17201,0,196838,'one')"
<input type="button" id ="123247769"  onclick="pass(247769,0,2186130,'one')" value="��ͨ��"
onclick="pass(247769,0,2186130,'one')"
<input type="button" id ="12313869"  onclick="pass(13869,0,196136,'one')" value="��ͨ��"
onclick="pass(13869,0,196136,'one')"
<input type="button" id ="12316774"  onclick="pass(16774,0,196136,'one')" value="��ͨ��"
onclick="pass(16774,0,196136,'one')"
<input type="button" id ="12311750"  onclick="pass(11750,0,196481,'one')" value="��ͨ��"
onclick="pass(11750,0,196481,'one')"
<input type="button" id ="12316890"  onclick="pass(16890,0,196136,'one')" value="��ͨ��"
onclick="pass(16890,0,196136,'one')"
<input type="button" id ="123128255"  onclick="pass(128255,0,2281167,'one')" value="��ͨ��"
onclick="pass(128255,0,2281167,'one')"
<input type="button" id ="1237859"  onclick="pass(7859,0,196908,'one')" value="��ͨ��"
onclick="pass(7859,0,196908,'one')"
<input type="button" id ="1237985"  onclick="pass(7985,0,196459,'one')" value="��ͨ��"
onclick="pass(7985,0,196459,'one')"
<input type="button" id ="12312607"  onclick="pass(12607,0,196908,'one')" value="��ͨ��"
onclick="pass(12607,0,196908,'one')"
<input type="button" id ="123266260"  onclick="pass(266260,42126,2230334,'one')" value="��ͨ��"
onclick="pass(266260,42126,2230334,'one')"
<input type="button" id ="123129750"  onclick="pass(129750,34985,2174576,'one')" value="��ͨ��"
onclick="pass(129750,34985,2174576,'one')"
<input type="button" id ="123142777"  onclick="pass(142777,0,2317349,'one')" value="��ͨ��"
onclick="pass(142777,0,2317349,'one')"
<input type="button" id ="12316945"  onclick="pass(16945,0,196957,'one')" value="��ͨ��"
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
<input type="button" id ="123167938"  onclick="pass(167938,32996,2135677,'one')" value="��ͨ��"
onclick="pass(167938,32996,2135677,'one')"
<input type="button" id ="123192452"  onclick="pass(192452,44605,2278581,'one')" value="��ͨ��"
onclick="pass(192452,44605,2278581,'one')"
<input type="button" id ="12317197"  onclick="pass(17197,0,196136,'one')" value="��ͨ��"
onclick="pass(17197,0,196136,'one')"
<input type="button" id ="123173344"  onclick="pass(173344,0,2266317,'one')" value="��ͨ��"
onclick="pass(173344,0,2266317,'one')"
<input type="button" id ="12311948"  onclick="pass(11948,0,196136,'one')" value="��ͨ��"
onclick="pass(11948,0,196136,'one')"
<input type="button" id ="12316818"  onclick="pass(16818,0,196949,'one')" value="��ͨ��"
onclick="pass(16818,0,196949,'one')"
<input type="button" id ="123176838"  onclick="pass(176838,0,2307154,'one')" value="��ͨ��"
onclick="pass(176838,0,2307154,'one')"
<input type="button" id ="12311682"  onclick="pass(11682,0,196136,'one')" value="��ͨ��"
onclick="pass(11682,0,196136,'one')"
<input type="button" id ="12316771"  onclick="pass(16771,0,196908,'one')" value="��ͨ��"
onclick="pass(16771,0,196908,'one')"
<input type="button" id ="123176829"  onclick="pass(176829,0,2307154,'one')" value="��ͨ��"
onclick="pass(176829,0,2307154,'one')"
<input type="button" id ="12316736"  onclick="pass(16736,0,196490,'one')" value="��ͨ��"
onclick="pass(16736,0,196490,'one')"
<input type="button" id ="123142959"  onclick="pass(142959,0,2317349,'one')" value="��ͨ��"
onclick="pass(142959,0,2317349,'one')"
<input type="button" id ="1237516"  onclick="pass(7516,0,196136,'one')" value="��ͨ��"
onclick="pass(7516,0,196136,'one')"
<input type="button" id ="12312961"  onclick="pass(12961,0,196029,'one')" value="��ͨ��"
onclick="pass(12961,0,196029,'one')"
<input type="button" id ="12314717"  onclick="pass(14717,0,196312,'one')" value="��ͨ��"
onclick="pass(14717,0,196312,'one')"
<input type="button" id ="12315438"  onclick="pass(15438,0,196136,'one')" value="��ͨ��"
onclick="pass(15438,0,196136,'one')"
<input type="button" id ="123176933"  onclick="pass(176933,0,2307154,'one')" value="��ͨ��"
onclick="pass(176933,0,2307154,'one')"
<input type="button" id ="123133181"  onclick="pass(133181,0,2264374,'one')" value="��ͨ��"
onclick="pass(133181,0,2264374,'one')"
<input type="button" id ="12317009"  onclick="pass(17009,0,196459,'one')" value="��ͨ��"
onclick="pass(17009,0,196459,'one')"
<input type="button" id ="12316966"  onclick="pass(16966,0,196654,'one')" value="��ͨ��"
onclick="pass(16966,0,196654,'one')"
<input type="button" id ="123250575"  onclick="pass(250575,0,2308233,'one')" value="��ͨ��"
onclick="pass(250575,0,2308233,'one')"
<input type="button" id ="12391814"  onclick="pass(91814,0,2323133,'one')" value="��ͨ��"
onclick="pass(91814,0,2323133,'one')"
<input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,'one')" value="��ͨ��"
onclick="pass(125176,42516,2043685,'one')"
<input type="button" id ="12314659"  onclick="pass(14659,0,196136,'one')" value="��ͨ��"
onclick="pass(14659,0,196136,'one')"
<input type="button" id ="12352678"  onclick="pass(52678,38055,1914340,'one')" value="��ͨ��"
onclick="pass(52678,38055,1914340,'one')"
<input type="button" id ="12316757"  onclick="pass(16757,0,196519,'one')" value="��ͨ��"
onclick="pass(16757,0,196519,'one')"
<input type="button" id ="12317201"  onclick="pass(17201,0,196838,'one')" value="��ͨ��"
onclick="pass(17201,0,196838,'one')"
<input type="button" id ="123247769"  onclick="pass(247769,0,2186130,'one')" value="��ͨ��"
onclick="pass(247769,0,2186130,'one')"
<input type="button" id ="12313869"  onclick="pass(13869,0,196136,'one')" value="��ͨ��"
onclick="pass(13869,0,196136,'one')"
<input type="button" id ="12316774"  onclick="pass(16774,0,196136,'one')" value="��ͨ��"
onclick="pass(16774,0,196136,'one')"
<input type="button" id ="12311750"  onclick="pass(11750,0,196481,'one')" value="��ͨ��"
onclick="pass(11750,0,196481,'one')"
<input type="button" id ="12316890"  onclick="pass(16890,0,196136,'one')" value="��ͨ��"
onclick="pass(16890,0,196136,'one')"
<input type="button" id ="123128255"  onclick="pass(128255,0,2281167,'one')" value="��ͨ��"
onclick="pass(128255,0,2281167,'one')"
<input type="button" id ="1237859"  onclick="pass(7859,0,196908,'one')" value="��ͨ��"
onclick="pass(7859,0,196908,'one')"
<input type="button" id ="1237985"  onclick="pass(7985,0,196459,'one')" value="��ͨ��"
onclick="pass(7985,0,196459,'one')"
<input type="button" id ="12312607"  onclick="pass(12607,0,196908,'one')" value="��ͨ��"
onclick="pass(12607,0,196908,'one')"
<input type="button" id ="123266260"  onclick="pass(266260,42126,2230334,'one')" value="��ͨ��"
onclick="pass(266260,42126,2230334,'one')"
<input type="button" id ="123129750"  onclick="pass(129750,34985,2174576,'one')" value="��ͨ��"
onclick="pass(129750,34985,2174576,'one')"
<input type="button" id ="123142777"  onclick="pass(142777,0,2317349,'one')" value="��ͨ��"
onclick="pass(142777,0,2317349,'one')"
<input type="button" id ="12316945"  onclick="pass(16945,0,196957,'one')" value="��ͨ��"
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
<input type="button" id ="12311963"  onclick="pass(11963,0,196908,'one')" value="��ͨ��"
onclick="pass(11963,0,196908,'one')"
<input type="button" id ="123106976"  onclick="pass(106976,0,2322403,'one')" value="��ͨ��"
onclick="pass(106976,0,2322403,'one')"
<input type="button" id ="12316830"  onclick="pass(16830,0,196900,'one')" value="��ͨ��"
onclick="pass(16830,0,196900,'one')"
<input type="button" id ="123158785"  onclick="pass(158785,0,2294819,'one')" value="��ͨ��"
onclick="pass(158785,0,2294819,'one')"
<input type="button" id ="1237436"  onclick="pass(7436,0,196908,'one')" value="��ͨ��"
onclick="pass(7436,0,196908,'one')"
<input type="button" id ="12388343"  onclick="pass(88343,0,1194650,'one')" value="��ͨ��"
onclick="pass(88343,0,1194650,'one')"
<input type="button" id ="12316124"  onclick="pass(16124,0,196908,'one')" value="��ͨ��"
onclick="pass(16124,0,196908,'one')"
<input type="button" id ="12362234"  onclick="pass(62234,44637,1866123,'one')" value="��ͨ��"
onclick="pass(62234,44637,1866123,'one')"
<input type="button" id ="12383328"  onclick="pass(83328,0,2363778,'one')" value="��ͨ��"
onclick="pass(83328,0,2363778,'one')"
<input type="button" id ="12315221"  onclick="pass(15221,0,196742,'one')" value="��ͨ��"
onclick="pass(15221,0,196742,'one')"
<input type="button" id ="12312837"  onclick="pass(12837,0,196908,'one')" value="��ͨ��"
onclick="pass(12837,0,196908,'one')"
<input type="button" id ="1239304"  onclick="pass(9304,0,196459,'one')" value="��ͨ��"
onclick="pass(9304,0,196459,'one')"
<input type="button" id ="1237999"  onclick="pass(7999,0,196908,'one')" value="��ͨ��"
onclick="pass(7999,0,196908,'one')"
<input type="button" id ="1237403"  onclick="pass(7403,0,196949,'one')" value="��ͨ��"
onclick="pass(7403,0,196949,'one')"
<input type="button" id ="12388534"  onclick="pass(88534,0,1194687,'one')" value="��ͨ��"
onclick="pass(88534,0,1194687,'one')"
<input type="button" id ="123123773"  onclick="pass(123773,53687,2069151,'one')" value="��ͨ��"
onclick="pass(123773,53687,2069151,'one')"
<input type="button" id ="123188905"  onclick="pass(188905,0,2280358,'one')" value="��ͨ��"
onclick="pass(188905,0,2280358,'one')"
<input type="button" id ="12317105"  onclick="pass(17105,0,196253,'one')" value="��ͨ��"
onclick="pass(17105,0,196253,'one')"
<input type="button" id ="123109285"  onclick="pass(109285,0,2147636,'one')" value="��ͨ��"
onclick="pass(109285,0,2147636,'one')"
<input type="button" id ="123113858"  onclick="pass(113858,34702,2252753,'one')" value="��ͨ��"
onclick="pass(113858,34702,2252753,'one')"
<input type="button" id ="12311692"  onclick="pass(11692,0,196908,'one')" value="��ͨ��"
onclick="pass(11692,0,196908,'one')"
<input type="button" id ="12315265"  onclick="pass(15265,0,196162,'one')" value="��ͨ��"
onclick="pass(15265,0,196162,'one')"
<input type="button" id ="12387798"  onclick="pass(87798,0,2388248,'one')" value="��ͨ��"
onclick="pass(87798,0,2388248,'one')"
<input type="button" id ="1237673"  onclick="pass(7673,0,196162,'one')" value="��ͨ��"
onclick="pass(7673,0,196162,'one')"
<input type="button" id ="12316974"  onclick="pass(16974,0,196162,'one')" value="��ͨ��"
onclick="pass(16974,0,196162,'one')"
<input type="button" id ="12316480"  onclick="pass(16480,0,196893,'one')" value="��ͨ��"
onclick="pass(16480,0,196893,'one')"
<input type="button" id ="12316829"  onclick="pass(16829,0,196519,'one')" value="��ͨ��"
onclick="pass(16829,0,196519,'one')"
<input type="button" id ="123205150"  onclick="pass(205150,0,2101336,'one')" value="��ͨ��"
onclick="pass(205150,0,2101336,'one')"
<input type="button" id ="123115483"  onclick="pass(115483,0,1975072,'one')" value="��ͨ��"
onclick="pass(115483,0,1975072,'one')"
<input type="button" id ="12315382"  onclick="pass(15382,0,196136,'one')" value="��ͨ��"
onclick="pass(15382,0,196136,'one')"
<input type="button" id ="123110985"  onclick="pass(110985,36027,2298596,'one')" value="��ͨ��"
onclick="pass(110985,36027,2298596,'one')"
<input type="button" id ="12316237"  onclick="pass(16237,0,196459,'one')" value="��ͨ��"
onclick="pass(16237,0,196459,'one')"
<input type="button" id ="123176791"  onclick="pass(176791,47149,2307154,'one')" value="��ͨ��"
onclick="pass(176791,47149,2307154,'one')"
<input type="button" id ="12316839"  onclick="pass(16839,0,196136,'one')" value="��ͨ��"
onclick="pass(16839,0,196136,'one')"
<input type="button" id ="12314831"  onclick="pass(14831,0,196949,'one')" value="��ͨ��"
onclick="pass(14831,0,196949,'one')"
<input type="button" id ="12311688"  onclick="pass(11688,0,196021,'one')" value="��ͨ��"
onclick="pass(11688,0,196021,'one')"
<input type="button" id ="12310896"  onclick="pass(10896,0,196886,'one')" value="��ͨ��"
onclick="pass(10896,0,196886,'one')"
<input type="button" id ="12313276"  onclick="pass(13276,0,196949,'one')" value="��ͨ��"
onclick="pass(13276,0,196949,'one')"
<input type="button" id ="123110989"  onclick="pass(110989,36031,2298596,'one')" value="��ͨ��"
onclick="pass(110989,36031,2298596,'one')"
<input type="button" id ="1239807"  onclick="pass(9807,0,196949,'one')" value="��ͨ��"
onclick="pass(9807,0,196949,'one')"
<input type="button" id ="12395737"  onclick="pass(95737,0,2362362,'one')" value="��ͨ��"
onclick="pass(95737,0,2362362,'one')"
<input type="button" id ="12378081"  onclick="pass(78081,0,1670047,'one')" value="��ͨ��"
onclick="pass(78081,0,1670047,'one')"
<input type="button" id ="12314130"  onclick="pass(14130,0,196908,'one')" value="��ͨ��"
onclick="pass(14130,0,196908,'one')"
<input type="button" id ="12316714"  onclick="pass(16714,0,196002,'one')" value="��ͨ��"
onclick="pass(16714,0,196002,'one')"
<input type="button" id ="12316204"  onclick="pass(16204,0,196459,'one')" value="��ͨ��"
onclick="pass(16204,0,196459,'one')"
<input type="button" id ="12310763"  onclick="pass(10763,0,196519,'one')" value="��ͨ��"
onclick="pass(10763,0,196519,'one')"
<input type="button" id ="12388521"  onclick="pass(88521,0,1194656,'one')" value="��ͨ��"
onclick="pass(88521,0,1194656,'one')"
<input type="button" id ="12361359"  onclick="pass(61359,57154,1725511,'one')" value="��ͨ��"
onclick="pass(61359,57154,1725511,'one')"
<input type="button" id ="12315324"  onclick="pass(15324,0,196136,'one')" value="��ͨ��"
onclick="pass(15324,0,196136,'one')"
<input type="button" id ="12314037"  onclick="pass(14037,0,196871,'one')" value="��ͨ��"
onclick="pass(14037,0,196871,'one')"
<input type="button" id ="123146137"  onclick="pass(146137,0,2305357,'one')" value="��ͨ��"
onclick="pass(146137,0,2305357,'one')"
<input type="button" id ="123158696"  onclick="pass(158696,0,2294145,'one')" value="��ͨ��"
onclick="pass(158696,0,2294145,'one')"
<input type="button" id ="12316811"  onclick="pass(16811,0,196162,'one')" value="��ͨ��"
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
<input type="button" id ="12311873"  onclick="pass(11873,0,196617,'one')" value="��ͨ��"
onclick="pass(11873,0,196617,'one')"
<input type="button" id ="12316545"  onclick="pass(16545,0,196162,'one')" value="��ͨ��"
onclick="pass(16545,0,196162,'one')"
<input type="button" id ="12312388"  onclick="pass(12388,0,196519,'one')" value="��ͨ��"
onclick="pass(12388,0,196519,'one')"
<input type="button" id ="123162107"  onclick="pass(162107,0,2384689,'one')" value="��ͨ��"
onclick="pass(162107,0,2384689,'one')"
<input type="button" id ="12312920"  onclick="pass(12920,0,196162,'one')" value="��ͨ��"
onclick="pass(12920,0,196162,'one')"
<input type="button" id ="123167162"  onclick="pass(167162,48720,2368041,'one')" value="��ͨ��"
onclick="pass(167162,48720,2368041,'one')"
<input type="button" id ="12317099"  onclick="pass(17099,0,196136,'one')" value="��ͨ��"
onclick="pass(17099,0,196136,'one')"
<input type="button" id ="12315110"  onclick="pass(15110,0,196351,'one')" value="��ͨ��"
onclick="pass(15110,0,196351,'one')"
<input type="button" id ="12316757"  onclick="pass(16757,0,196519,'one')" value="��ͨ��"
onclick="pass(16757,0,196519,'one')"
<input type="button" id ="12390092"  onclick="pass(90092,0,2376218,'one')" value="��ͨ��"
onclick="pass(90092,0,2376218,'one')"
<input type="button" id ="1237023"  onclick="pass(7023,0,196861,'one')" value="��ͨ��"
onclick="pass(7023,0,196861,'one')"
<input type="button" id ="12311864"  onclick="pass(11864,0,196341,'one')" value="��ͨ��"
onclick="pass(11864,0,196341,'one')"
<input type="button" id ="1237765"  onclick="pass(7765,0,196908,'one')" value="��ͨ��"
onclick="pass(7765,0,196908,'one')"
<input type="button" id ="12315022"  onclick="pass(15022,0,196908,'one')" value="��ͨ��"
onclick="pass(15022,0,196908,'one')"
<input type="button" id ="12399170"  onclick="pass(99170,0,1630010,'one')" value="��ͨ��"
onclick="pass(99170,0,1630010,'one')"
<input type="button" id ="123136880"  onclick="pass(136880,27890,2387916,'one')" value="��ͨ��"
onclick="pass(136880,27890,2387916,'one')"
<input type="button" id ="123138613063"  onclick="pass(138613063,0,2295721,'one')" value="��ͨ��"
onclick="pass(138613063,0,2295721,'one')"
<input type="button" id ="12311825"  onclick="pass(11825,0,196136,'one')" value="��ͨ��"
onclick="pass(11825,0,196136,'one')"
<input type="button" id ="123135223"  onclick="pass(135223,0,2222974,'one')" value="��ͨ��"
onclick="pass(135223,0,2222974,'one')"
<input type="button" id ="12313162"  onclick="pass(13162,0,196136,'one')" value="��ͨ��"
onclick="pass(13162,0,196136,'one')"
<input type="button" id ="12314963"  onclick="pass(14963,0,196162,'one')" value="��ͨ��"
onclick="pass(14963,0,196162,'one')"
<input type="button" id ="12313812"  onclick="pass(13812,0,196949,'one')" value="��ͨ��"
onclick="pass(13812,0,196949,'one')"
<input type="button" id ="123103039"  onclick="pass(103039,0,2216191,'one')" value="��ͨ��"
onclick="pass(103039,0,2216191,'one')"
<input type="button" id ="123220653"  onclick="pass(220653,0,2205648,'one')" value="��ͨ��"
onclick="pass(220653,0,2205648,'one')"
<input type="button" id ="12396217"  onclick="pass(96217,0,2357853,'one')" value="��ͨ��"
onclick="pass(96217,0,2357853,'one')"
<input type="button" id ="12364468"  onclick="pass(64468,0,1195298,'one')" value="��ͨ��"
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
<input type="button" id ="12313215"  onclick="pass(13215,0,196162,'one')" value="��ͨ��"
onclick="pass(13215,0,196162,'one')"
<input type="button" id ="12317052"  onclick="pass(17052,0,196162,'one')" value="��ͨ��"
onclick="pass(17052,0,196162,'one')"
<input type="button" id ="12314834"  onclick="pass(14834,0,196162,'one')" value="��ͨ��"
onclick="pass(14834,0,196162,'one')"
<input type="button" id ="123159562"  onclick="pass(159562,0,2311759,'one')" value="��ͨ��"
onclick="pass(159562,0,2311759,'one')"
<input type="button" id ="12314680"  onclick="pass(14680,0,196949,'one')" value="��ͨ��"
onclick="pass(14680,0,196949,'one')"
<input type="button" id ="12311682"  onclick="pass(11682,0,196136,'one')" value="��ͨ��"
onclick="pass(11682,0,196136,'one')"
<input type="button" id ="123247673"  onclick="pass(247673,0,2186307,'one')" value="��ͨ��"
onclick="pass(247673,0,2186307,'one')"
<input type="button" id ="12316285"  onclick="pass(16285,0,196519,'one')" value="��ͨ��"
onclick="pass(16285,0,196519,'one')"
<input type="button" id ="12382829"  onclick="pass(82829,0,2361033,'one')" value="��ͨ��"
onclick="pass(82829,0,2361033,'one')"
<input type="button" id ="12313308"  onclick="pass(13308,0,196949,'one')" value="��ͨ��"
onclick="pass(13308,0,196949,'one')"
<input type="button" id ="12341197"  onclick="pass(41197,0,1549768,'one')" value="��ͨ��"
onclick="pass(41197,0,1549768,'one')"
<input type="button" id ="12314525"  onclick="pass(14525,0,196367,'one')" value="��ͨ��"
onclick="pass(14525,0,196367,'one')"
<input type="button" id ="12315336"  onclick="pass(15336,0,196136,'one')" value="��ͨ��"
onclick="pass(15336,0,196136,'one')"
<input type="button" id ="12395703"  onclick="pass(95703,0,2362184,'one')" value="��ͨ��"
onclick="pass(95703,0,2362184,'one')"
<input type="button" id ="123188671"  onclick="pass(188671,34624,2280389,'one')" value="��ͨ��"
onclick="pass(188671,34624,2280389,'one')"
<input type="button" id ="12315325"  onclick="pass(15325,0,196136,'one')" value="��ͨ��"
onclick="pass(15325,0,196136,'one')"
<input type="button" id ="123136906"  onclick="pass(136906,0,2143919,'one')" value="��ͨ��"
onclick="pass(136906,0,2143919,'one')"
<input type="button" id ="123247485"  onclick="pass(247485,77247,2186626,'one')" value="��ͨ��"
onclick="pass(247485,77247,2186626,'one')"
<input type="button" id ="123714744"  onclick="pass(714744,0,2001817,'one')" value="��ͨ��"
onclick="pass(714744,0,2001817,'one')"
<input type="button" id ="12365296"  onclick="pass(65296,0,1682792,'one')" value="��ͨ��"
onclick="pass(65296,0,1682792,'one')"
<input type="button" id ="12313314"  onclick="pass(13314,0,196714,'one')" value="��ͨ��"
onclick="pass(13314,0,196714,'one')"
<input type="button" id ="12314431"  onclick="pass(14431,0,196949,'one')" value="��ͨ��"
onclick="pass(14431,0,196949,'one')"
<input type="button" id ="12391777"  onclick="pass(91777,0,2323796,'one')" value="��ͨ��"
onclick="pass(91777,0,2323796,'one')"
<input type="button" id ="123115465"  onclick="pass(115465,0,2312408,'one')" value="��ͨ��"
onclick="pass(115465,0,2312408,'one')"
<input type="button" id ="123293107"  onclick="pass(293107,97242,2210912,'one')" value="��ͨ��"
onclick="pass(293107,97242,2210912,'one')"
<input type="button" id ="123126905"  onclick="pass(126905,0,2372068,'one')" value="��ͨ��"
onclick="pass(126905,0,2372068,'one')"
<input type="button" id ="123167979"  onclick="pass(167979,0,2135590,'one')" value="��ͨ��"
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
<input type="button" id ="123111083"  onclick="pass(111083,0,2075057,'one')" value="��ͨ��"
onclick="pass(111083,0,2075057,'one')"
<input type="button" id ="123247582"  onclick="pass(247582,0,2186463,'one')" value="��ͨ��"
onclick="pass(247582,0,2186463,'one')"
<input type="button" id ="123204930"  onclick="pass(204930,55782,2306660,'one')" value="��ͨ��"
onclick="pass(204930,55782,2306660,'one')"
<input type="button" id ="123120780"  onclick="pass(120780,0,2377397,'one')" value="��ͨ��"
onclick="pass(120780,0,2377397,'one')"
<input type="button" id ="123148427"  onclick="pass(148427,0,2297063,'one')" value="��ͨ��"
onclick="pass(148427,0,2297063,'one')"
<input type="button" id ="123135187"  onclick="pass(135187,0,2222846,'one')" value="��ͨ��"
onclick="pass(135187,0,2222846,'one')"
<input type="button" id ="12360811"  onclick="pass(60811,0,195447,'one')" value="��ͨ��"
onclick="pass(60811,0,195447,'one')"
<input type="button" id ="12311710"  onclick="pass(11710,0,196908,'one')" value="��ͨ��"
onclick="pass(11710,0,196908,'one')"
<input type="button" id ="12314839"  onclick="pass(14839,0,196475,'one')" value="��ͨ��"
onclick="pass(14839,0,196475,'one')"
<input type="button" id ="123176711"  onclick="pass(176711,0,2307154,'one')" value="��ͨ��"
onclick="pass(176711,0,2307154,'one')"
<input type="button" id ="1236819"  onclick="pass(6819,0,196253,'one')" value="��ͨ��"
onclick="pass(6819,0,196253,'one')"
<input type="button" id ="123122795"  onclick="pass(122795,0,2039432,'one')" value="��ͨ��"
onclick="pass(122795,0,2039432,'one')"
<input type="button" id ="123247511"  onclick="pass(247511,77381,2186626,'one')" value="��ͨ��"
onclick="pass(247511,77381,2186626,'one')"
<input type="button" id ="12315193"  onclick="pass(15193,0,196222,'one')" value="��ͨ��"
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
<input type="button" id ="123142708"  onclick="pass(142708,0,2317349,'one')" value="��ͨ��"
onclick="pass(142708,0,2317349,'one')"
<input type="button" id ="12385981"  onclick="pass(85981,0,1574116,'one')" value="��ͨ��"
onclick="pass(85981,0,1574116,'one')"
<input type="button" id ="12314100"  onclick="pass(14100,0,196029,'one')" value="��ͨ��"
onclick="pass(14100,0,196029,'one')"
<input type="button" id ="123198619"  onclick="pass(198619,50580,2236954,'one')" value="��ͨ��"
onclick="pass(198619,50580,2236954,'one')"
<input type="button" id ="12314564"  onclick="pass(14564,0,196029,'one')" value="��ͨ��"
onclick="pass(14564,0,196029,'one')"
<input type="button" id ="12314979"  onclick="pass(14979,0,196399,'one')" value="��ͨ��"
onclick="pass(14979,0,196399,'one')"
<input type="button" id ="12314637"  onclick="pass(14637,0,196351,'one')" value="��ͨ��"
onclick="pass(14637,0,196351,'one')"
<input type="button" id ="123171105"  onclick="pass(171105,36098,2272764,'one')" value="��ͨ��"
onclick="pass(171105,36098,2272764,'one')"
<input type="button" id ="12312559"  onclick="pass(12559,0,196898,'one')" value="��ͨ��"
onclick="pass(12559,0,196898,'one')"
<input type="button" id ="1237469"  onclick="pass(7469,0,196949,'one')" value="��ͨ��"
onclick="pass(7469,0,196949,'one')"
<input type="button" id ="12361426"  onclick="pass(61426,0,1946641,'one')" value="��ͨ��"
onclick="pass(61426,0,1946641,'one')"
<input type="button" id ="123247769"  onclick="pass(247769,0,2186130,'one')" value="��ͨ��"
onclick="pass(247769,0,2186130,'one')"
<input type="button" id ="12317173"  onclick="pass(17173,0,196949,'one')" value="��ͨ��"
onclick="pass(17173,0,196949,'one')"
<input type="button" id ="123134882"  onclick="pass(134882,0,2203925,'one')" value="��ͨ��"
onclick="pass(134882,0,2203925,'one')"
<input type="button" id ="12387525"  onclick="pass(87525,0,2365214,'one')" value="��ͨ��"
onclick="pass(87525,0,2365214,'one')"
<input type="button" id ="12366345"  onclick="pass(66345,0,1195453,'one')" value="��ͨ��"
onclick="pass(66345,0,1195453,'one')"
<input type="button" id ="12314714"  onclick="pass(14714,0,196136,'one')" value="��ͨ��"
onclick="pass(14714,0,196136,'one')"
<input type="button" id ="12315407"  onclick="pass(15407,0,196136,'one')" value="��ͨ��"
onclick="pass(15407,0,196136,'one')"
<input type="button" id ="1238905"  onclick="pass(8905,0,196136,'one')" value="��ͨ��"
onclick="pass(8905,0,196136,'one')"
<input type="button" id ="123176659"  onclick="pass(176659,35167,2347300,'one')" value="��ͨ��"
onclick="pass(176659,35167,2347300,'one')"
<input type="button" id ="12313977"  onclick="pass(13977,0,196949,'one')" value="��ͨ��"
onclick="pass(13977,0,196949,'one')"
<input type="button" id ="123106811"  onclick="pass(106811,14040,2322969,'one')" value="��ͨ��"
onclick="pass(106811,14040,2322969,'one')"
<input type="button" id ="123108976"  onclick="pass(108976,0,2319870,'one')" value="��ͨ��"
onclick="pass(108976,0,2319870,'one')"
<input type="button" id ="12312372"  onclick="pass(12372,0,196399,'one')" value="��ͨ��"
onclick="pass(12372,0,196399,'one')"
<input type="button" id ="12316993"  onclick="pass(16993,0,196029,'one')" value="��ͨ��"
onclick="pass(16993,0,196029,'one')"
<input type="button" id ="12355883"  onclick="pass(55883,51319,1894923,'one')" value="��ͨ��"
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
<input type="button" id ="12312646"  onclick="pass(12646,0,196475,'one')" value="��ͨ��"
onclick="pass(12646,0,196475,'one')"
<input type="button" id ="123124162"  onclick="pass(124162,0,2211410,'one')" value="��ͨ��"
onclick="pass(124162,0,2211410,'one')"
<input type="button" id ="12315152"  onclick="pass(15152,0,196908,'one')" value="��ͨ��"
onclick="pass(15152,0,196908,'one')"
<input type="button" id ="12376664"  onclick="pass(76664,48498,1921020,'one')" value="��ͨ��"
onclick="pass(76664,48498,1921020,'one')"
<input type="button" id ="123184774"  onclick="pass(184774,0,2099758,'one')" value="��ͨ��"
onclick="pass(184774,0,2099758,'one')"
<input type="button" id ="12312796"  onclick="pass(12796,0,196949,'one')" value="��ͨ��"
onclick="pass(12796,0,196949,'one')"
<input type="button" id ="12312248"  onclick="pass(12248,0,196617,'one')" value="��ͨ��"
onclick="pass(12248,0,196617,'one')"
<input type="button" id ="123142777"  onclick="pass(142777,0,2317349,'one')" value="��ͨ��"
onclick="pass(142777,0,2317349,'one')"
<input type="button" id ="123193784"  onclick="pass(193784,0,2246613,'one')" value="��ͨ��"
onclick="pass(193784,0,2246613,'one')"
<input type="button" id ="12313031"  onclick="pass(13031,0,196341,'one')" value="��ͨ��"
onclick="pass(13031,0,196341,'one')"
<input type="button" id ="123142940"  onclick="pass(142940,0,2317868,'one')" value="��ͨ��"
onclick="pass(142940,0,2317868,'one')"
<input type="button" id ="12312195"  onclick="pass(12195,0,196949,'one')" value="��ͨ��"
onclick="pass(12195,0,196949,'one')"
<input type="button" id ="12362257"  onclick="pass(62257,0,1866123,'one')" value="��ͨ��"
onclick="pass(62257,0,1866123,'one')"
<input type="button" id ="123125176"  onclick="pass(125176,42516,2043685,'one')" value="��ͨ��"
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
<input type="button" id ="12312961"  onclick="pass(12961,0,196029,'one')" value="��ͨ��"
onclick="pass(12961,0,196029,'one')"
<input type="button" id ="1236179"  onclick="pass(6179,0,196228,'one')" value="��ͨ��"
onclick="pass(6179,0,196228,'one')"
<input type="button" id ="123250610"  onclick="pass(250610,0,2308235,'one')" value="��ͨ��"
onclick="pass(250610,0,2308235,'one')"
<input type="button" id ="12315049"  onclick="pass(15049,0,196136,'one')" value="��ͨ��"
onclick="pass(15049,0,196136,'one')"
<input type="button" id ="12312341"  onclick="pass(12341,0,196949,'one')" value="��ͨ��"
onclick="pass(12341,0,196949,'one')"
<input type="button" id ="123112479"  onclick="pass(112479,27693,2366143,'one')" value="��ͨ��"
onclick="pass(112479,27693,2366143,'one')"
<input type="button" id ="12313932"  onclick="pass(13932,0,196373,'one')" value="��ͨ��"
onclick="pass(13932,0,196373,'one')"
<input type="button" id ="1237412"  onclick="pass(7412,0,196908,'one')" value="��ͨ��"
onclick="pass(7412,0,196908,'one')"
<input type="button" id ="12315213"  onclick="pass(15213,0,196949,'one')" value="��ͨ��"
onclick="pass(15213,0,196949,'one')"
<input type="button" id ="12379924"  onclick="pass(79924,14568,2373399,'one')" value="��ͨ��"
onclick="pass(79924,14568,2373399,'one')"
<input type="button" id ="12312745"  onclick="pass(12745,0,196957,'one')" value="��ͨ��"
onclick="pass(12745,0,196957,'one')"
<input type="button" id ="12316755"  onclick="pass(16755,0,196136,'one')" value="��ͨ��"
onclick="pass(16755,0,196136,'one')"
<input type="button" id ="123126872"  onclick="pass(126872,23637,2372269,'one')" value="��ͨ��"
onclick="pass(126872,23637,2372269,'one')"
<input type="button" id ="12315520"  onclick="pass(15520,0,196714,'one')" value="��ͨ��"
onclick="pass(15520,0,196714,'one')"
<input type="button" id ="12394543"  onclick="pass(94543,22136,2337245,'one')" value="��ͨ��"
onclick="pass(94543,22136,2337245,'one')"
<input type="button" id ="12315004"  onclick="pass(15004,0,196949,'one')" value="��ͨ��"
onclick="pass(15004,0,196949,'one')"
<input type="button" id ="123109081"  onclick="pass(109081,0,2319574,'one')" value="��ͨ��"
onclick="pass(109081,0,2319574,'one')"
<input type="button" id ="123115220"  onclick="pass(115220,21035,2310524,'one')" value="��ͨ��"
onclick="pass(115220,21035,2310524,'one')"
<input type="button" id ="12316027"  onclick="pass(16027,0,196886,'one')" value="��ͨ��"
onclick="pass(16027,0,196886,'one')"
<input type="button" id ="1237550"  onclick="pass(7550,0,196908,'one')" value="��ͨ��"
onclick="pass(7550,0,196908,'one')"
<input type="button" id ="1237310"  onclick="pass(7310,0,196909,'one')" value="��ͨ��"
onclick="pass(7310,0,196909,'one')"
<input type="button" id ="12364595"  onclick="pass(64595,0,626977,'one')" value="��ͨ��"
onclick="pass(64595,0,626977,'one')"
<input type="button" id ="123114190"  onclick="pass(114190,0,2252716,'one')" value="��ͨ��"
onclick="pass(114190,0,2252716,'one')"
<input type="button" id ="1237551"  onclick="pass(7551,0,196459,'one')" value="��ͨ��"
onclick="pass(7551,0,196459,'one')"
<input type="button" id ="123224998"  onclick="pass(224998,39870,2299509,'one')" value="��ͨ��"
onclick="pass(224998,39870,2299509,'one')"
<input type="button" id ="12359801"  onclick="pass(59801,0,1928923,'one')" value="��ͨ��"
onclick="pass(59801,0,1928923,'one')"
<input type="button" id ="1237761"  onclick="pass(7761,0,196908,'one')" value="��ͨ��"
onclick="pass(7761,0,196908,'one')"
<input type="button" id ="1236241"  onclick="pass(6241,0,196136,'one')" value="��ͨ��"
onclick="pass(6241,0,196136,'one')"
<input type="button" id ="123160907"  onclick="pass(160907,0,2385018,'one')" value="��ͨ��"
onclick="pass(160907,0,2385018,'one')"
<input type="button" id ="123167261"  onclick="pass(167261,0,2368078,'one')" value="��ͨ��"
onclick="pass(167261,0,2368078,'one')"
<input type="button" id ="12375865"  onclick="pass(75865,18290,2360289,'one')" value="��ͨ��"
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
<input type="button" id ="12312821"  onclick="pass(12821,0,196568,'one')" value="��ͨ��"
onclick="pass(12821,0,196568,'one')"
<input type="button" id ="12313204"  onclick="pass(13204,0,196029,'one')" value="��ͨ��"
onclick="pass(13204,0,196029,'one')"
<input type="button" id ="12314186"  onclick="pass(14186,0,196949,'one')" value="��ͨ��"
onclick="pass(14186,0,196949,'one')"
<input type="button" id ="123141474"  onclick="pass(141474,0,2168548,'one')" value="��ͨ��"
onclick="pass(141474,0,2168548,'one')"
<input type="button" id ="12311565"  onclick="pass(11565,0,196136,'one')" value="��ͨ��"
onclick="pass(11565,0,196136,'one')"
<input type="button" id ="12317022"  onclick="pass(17022,0,196617,'one')" value="��ͨ��"
onclick="pass(17022,0,196617,'one')"
<input type="button" id ="1237451"  onclick="pass(7451,0,196459,'one')" value="��ͨ��"
onclick="pass(7451,0,196459,'one')"
<input type="button" id ="123159678"  onclick="pass(159678,0,2311060,'one')" value="��ͨ��"
onclick="pass(159678,0,2311060,'one')"
<input type="button" id ="123160938"  onclick="pass(160938,0,2385572,'one')" value="��ͨ��"
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
<input type="button" id ="12312248"  onclick="pass(12248,0,196617,'one')" value="��ͨ��"
onclick="pass(12248,0,196617,'one')"
<input type="button" id ="12313314"  onclick="pass(13314,0,196714,'one')" value="��ͨ��"
onclick="pass(13314,0,196714,'one')"
<input type="button" id ="12394648"  onclick="pass(94648,0,2337210,'one')" value="��ͨ��"
onclick="pass(94648,0,2337210,'one')"
<input type="button" id ="12312663"  onclick="pass(12663,0,196351,'one')" value="��ͨ��"
onclick="pass(12663,0,196351,'one')"
<input type="button" id ="12312915"  onclick="pass(12915,0,196886,'one')" value="��ͨ��"
onclick="pass(12915,0,196886,'one')"
<input type="button" id ="12315556"  onclick="pass(15556,0,196706,'one')" value="��ͨ��"
onclick="pass(15556,0,196706,'one')"
<input type="button" id ="123157370"  onclick="pass(157370,36367,2314023,'one')" value="��ͨ��"
onclick="pass(157370,36367,2314023,'one')"
<input type="button" id ="12389920"  onclick="pass(89920,12179,2376218,'one')" value="��ͨ��"
onclick="pass(89920,12179,2376218,'one')"
<input type="button" id ="12314979"  onclick="pass(14979,0,196399,'one')" value="��ͨ��"
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
