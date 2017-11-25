from .transcript_day import *



def test():
    parsed = TranscriptDay(EXAMPLE_DATA)
    print(parsed)

    assert parsed.room_id == 11540
    assert parsed.room_name == "Charcoal HQ"

    assert parsed.first_day == datetime.date(2013, 11, 16)
    assert parsed.previous_day == datetime.date(2017, 11, 16)
    assert parsed.next_day == datetime.date(2017, 11, 18)
    assert parsed.last_day == datetime.date(2017, 11, 22)

    assert parsed.messages[0].id == 41197805
    assert parsed.messages[0].parent_message_id is None
    assert parsed.messages[0].owner_user_id == 205533
    assert parsed.messages[0].owner_user_name == "Videonauth"

    assert len(parsed.messages) == 61


EXAMPLE_DATA = r'''


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" >
<head>
    <title>Charcoal HQ - 2017-11-17 (page 2 of 4)</title>
    <link rel="shortcut icon" href="//cdn.sstatic.net/stackexchange/img/favicon.ico?v=da"><link rel="apple-touch-icon" href="//cdn.sstatic.net/stackexchange/img/apple-touch-icon.png?v=da"><link rel="search" type="application/opensearchdescription+xml" title="Chat for chat.stackexchange.com" href="/opensearch.xml">    
    <link rel="canonical" href="/transcript/11540/2017/11/17/1-2" />
                        <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    
    <script type="text/javascript" src="//cdn-chat.sstatic.net/chat/Js/master-chat.js?v=f1e5ed9ea207"></script>
    <link rel="stylesheet" href="//cdn-chat.sstatic.net/chat/css/chat.stackexchange.com.css?v=7d154b0411cf">  
    
<script type="text/javascript">
    function IMAGE(f) { return ("//cdn-chat.sstatic.net/chat/img/" + f); }
</script>
    <script type="text/javascript">
        $(function() {
            initTranscript(true,
                1251, true,
                true, 11540,
                true);
            popupDismisser();
        });
    </script>
    
</head>
    
<body id="transcript-body">
    <div id="container">
    <div id="main">
      <a href="/transcript/11540/2013/11/16" class="button noprint" title="2013-11-16">&laquo; first day (1461 days earlier)</a>&nbsp;
<a href="/transcript/11540/2017/11/16" class="button noprint" rel="prev" title="2017-11-16">&larr; previous day</a>&nbsp;
<link rel="prev" title="2017-11-16" href="/transcript/11540/2017/11/16" />
<a href="/transcript/11540/2017/11/18" class="button noprint" rel="next" title="2017-11-18">next day &rarr;</a>&nbsp;
<link rel="next" title="2017-11-18" href="/transcript/11540/2017/11/18" />
<a href="/transcript/11540/2017/11/22" class="button noprint" title="2017-11-22"> last day (5 days later) &raquo;</a>&nbsp;
<div class="clear-both"></div>
      <div class="clear-both"></div><div class="pager"><a href="/transcript/11540/2017/11/17/0-1"><span class="page-numbers">00:00 - 01:00</span></a><span class="page-numbers current">01:00 - 02:00</span><a href="/transcript/11540/2017/11/17/2-13"><span class="page-numbers">02:00 - 13:00</span></a><a href="/transcript/11540/2017/11/17/13-24"><span class="page-numbers">13:00 - 00:00</span></a></div><div class="clear-both"></div>
      <br/>
      <div id="transcript">

<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
             <div class="timestamp">1:00 AM</div>

        
        
            <div class="message" id="message-41197805">
                <a name="41197805" href="/transcript/11540?m=41197805#41197805"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    <div class="onebox ob-image"><a rel="nofollow noopener noreferrer" href="//i.stack.imgur.com/mdGKA.jpg"><img src="//i.stack.imgur.com/mdGKA.jpg" class="user-image" alt="user image" /></a></div>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41197807">
                <a name="41197807" href="/transcript/11540?m=41197807#41197807"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    and this :)                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-137388">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/Ma6sp.jpg?s=16&g=1" alt="QPaysTaxes" />
            </div>
        
        <div class="username"><a href="/users/137388/qpaystaxes" title="QPaysTaxes">QPaysTaxes</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41197831">
                <a name="41197831" href="/transcript/11540?m=41197831#41197831"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    Mhm                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-120914">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/WyV1l.png?s=16&g=1" alt="SmokeDetector" />
            </div>
        
        <div class="username"><a href="/users/120914/smokedetector" title="SmokeDetector">SmokeDetector</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41197902">
                <a name="41197902" href="/transcript/11540?m=41197902#41197902"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    Merged SmokeDetector <a href="https://github.com/Charcoal-SE/SmokeDetector/pull/1236" rel="nofollow noopener noreferrer">#1236</a>.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-167070">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/AYXNm.png?s=16&g=1" alt="quartata" />
            </div>
        
        <div class="username"><a href="/users/167070/quartata" title="quartata">quartata</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41197912">
                <a name="41197912" href="/transcript/11540?m=41197912#41197912"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    sorry for the delay                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-120914">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/WyV1l.png?s=16&g=1" alt="SmokeDetector" />
            </div>
        
        <div class="username"><a href="/users/120914/smokedetector" title="SmokeDetector">SmokeDetector</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41197915">
                <a name="41197915" href="/transcript/11540?m=41197915#41197915"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    <a href="https://codecov.io/gh/Charcoal-SE/SmokeDetector/compare/8c1cd7633587085fff94743dcc9096c646c7344a...afbbeba682ba4094d33c8d9dd2a522b2d713b665" rel="nofollow noopener noreferrer">CI</a> on <a href="https://github.com/Charcoal-SE/SmokeDetector/commit/afbbeba" rel="nofollow noopener noreferrer"><code>afbbeba</code></a> succeeded. Message contains &#39;autopull&#39;, pulling...                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41197923">
                <a name="41197923" href="/transcript/11540?m=41197923#41197923"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//github.com/Charcoal-SE/SmokeDetector" rel="nofollow noopener noreferrer">SmokeDetector</a> ] SmokeDetector started at <a href="//github.com/Charcoal-SE/SmokeDetector/commit/6ad928a" rel="nofollow noopener noreferrer">rev 6ad928a (metasmoke: <i>Merge pull request #1236 from Charcoal-SE/auto-blacklist-1510879822.8478458</i>)</a> (running on Henders/EC2)                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41197925">
                <a name="41197925" href="/transcript/11540?m=41197925#41197925"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    Restart: API quota is 18014.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41197984">
                <a name="41197984" href="/transcript/11540?m=41197984#41197984"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//goo.gl/eLDYqh" rel="nofollow noopener noreferrer">SmokeDetector</a> | <a href="//m.erwaysoftware.com/posts/by-url?url=//askubuntu.com/a/977247" rel="nofollow noopener noreferrer">MS</a> ] Potentially bad keyword in answer, blacklisted user: <a href="//askubuntu.com/a/977247">viewer for X.509 certificate</a> by <a href="//askubuntu.com/users/760491">vite11</a> on <code>askubuntu.com</code>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198028">
                <a name="41198028" href="/transcript/11540?m=41198028#41198028"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//goo.gl/eLDYqh" rel="nofollow noopener noreferrer">SmokeDetector</a> | <a href="//m.erwaysoftware.com/posts/by-url?url=//es.stackoverflow.com/questions/118122" rel="nofollow noopener noreferrer">MS</a> ] Mostly dots in body: <a href="//es.stackoverflow.com/questions/118122">Por qu&#233; el organo varonil se llama pene?</a> by <a href="//es.stackoverflow.com/users/66574">Escroto Y Pene Gratis</a> on <code>es.stackoverflow.com</code>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-137388">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/Ma6sp.jpg?s=16&g=1" alt="QPaysTaxes" />
            </div>
        
        <div class="username"><a href="/users/137388/qpaystaxes" title="QPaysTaxes">QPaysTaxes</a></div>

    </div></div>
    <div class="messages">
        
             <div class="timestamp">1:15 AM</div>

        
        
            <div class="message" id="message-41198159">
                <a name="41198159" href="/transcript/11540?m=41198159#41198159"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    sd k                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198165">
                <a name="41198165" href="/transcript/11540?m=41198165#41198165"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    sd - k                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-120914">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/WyV1l.png?s=16&g=1" alt="SmokeDetector" />
            </div>
        
        <div class="username"><a href="/users/120914/smokedetector" title="SmokeDetector">SmokeDetector</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198166">
                <a name="41198166" href="/transcript/11540?m=41198166#41198166"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    Conflicting feedback across revisions: <a href="//metasmoke.erwaysoftware.com/post/93853" rel="nofollow noopener noreferrer">current</a>, <a href="//metasmoke.erwaysoftware.com/post/93852" rel="nofollow noopener noreferrer">#1</a>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198171">
                <a name="41198171" href="/transcript/11540?m=41198171#41198171"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    tpu by QPaysTaxes on <a href="//askubuntu.com/a/977247">viewer for X.509 certificate</a> &#91;<a href="http://metasmoke.erwaysoftware.com/post/93852" rel="nofollow noopener noreferrer">MS</a>]                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198235">
                <a name="41198235" href="/transcript/11540?m=41198235#41198235"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//goo.gl/eLDYqh" rel="nofollow noopener noreferrer">SmokeDetector</a> | <a href="//m.erwaysoftware.com/posts/by-url?url=//es.stackoverflow.com/a/118124" rel="nofollow noopener noreferrer">MS</a> ] Blacklisted user: <a href="//es.stackoverflow.com/a/118124">Como mandar un registro de una celda DataGridView a un textbox de otro formulario?</a> by <a href="//es.stackoverflow.com/users/66574">Escroto Y Pene Gratis</a> on <code>es.stackoverflow.com</code>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198237">
                <a name="41198237" href="/transcript/11540?m=41198237#41198237"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//goo.gl/eLDYqh" rel="nofollow noopener noreferrer">SmokeDetector</a> | <a href="//m.erwaysoftware.com/posts/by-url?url=//es.stackoverflow.com/a/118127" rel="nofollow noopener noreferrer">MS</a> ] Blacklisted user: <a href="//es.stackoverflow.com/a/118127">Como mandar un registro de una celda DataGridView a un textbox de otro formulario?</a> by <a href="//es.stackoverflow.com/users/66574">Escroto Y Pene Gratis</a> on <code>es.stackoverflow.com</code>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198240">
                <a name="41198240" href="/transcript/11540?m=41198240#41198240"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//goo.gl/eLDYqh" rel="nofollow noopener noreferrer">SmokeDetector</a> | <a href="//m.erwaysoftware.com/posts/by-url?url=//es.stackoverflow.com/questions/118125" rel="nofollow noopener noreferrer">MS</a> ] Blacklisted user: <a href="//es.stackoverflow.com/questions/118125">&#191;C&#243;mo puedo hacer este c&#243;digo funcional para mi website-blog de tecnolog&#237;a?</a> by <a href="//es.stackoverflow.com/users/66574">Escroto Y Pene Gratis</a> on <code>es.stackoverflow.com</code>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198242">
                <a name="41198242" href="/transcript/11540?m=41198242#41198242"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//goo.gl/eLDYqh" rel="nofollow noopener noreferrer">SmokeDetector</a> | <a href="//m.erwaysoftware.com/posts/by-url?url=//es.stackoverflow.com/questions/118122" rel="nofollow noopener noreferrer">MS</a> ] Blacklisted user: <a href="//es.stackoverflow.com/questions/118122">Por que el organo varonil se le denomina pene</a> by <a href="//es.stackoverflow.com/users/66574">Escroto Y Pene Gratis</a> on <code>es.stackoverflow.com</code>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-155243">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/fY1pd.jpg?s=16&g=1" alt="Nisse Engstr&#246;m" />
            </div>
        
        <div class="username"><a href="/users/155243/nisse-engstrom" title="Nisse Engstr&#246;m">Nisse Engstr&#246;m</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198272">
                <a name="41198272" href="/transcript/11540?m=41198272#41198272"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198242#41198242"> </a> 

                <div class="content">
                    @SmokeDetector tpu-                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198287">
                <a name="41198287" href="/transcript/11540?m=41198287#41198287"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198240#41198240"> </a> 

                <div class="content">
                    @SmokeDetector tpu-                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198300">
                <a name="41198300" href="/transcript/11540?m=41198300#41198300"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198237#41198237"> </a> 

                <div class="content">
                    @SmokeDetector tpu-                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198304">
                <a name="41198304" href="/transcript/11540?m=41198304#41198304"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    question: can anyone in here do: <code>!!&#47;repor t &lt;link&gt;</code> when a case linke above happens?                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-155243">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/fY1pd.jpg?s=16&g=1" alt="Nisse Engstr&#246;m" />
            </div>
        
        <div class="username"><a href="/users/155243/nisse-engstrom" title="Nisse Engstr&#246;m">Nisse Engstr&#246;m</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198305">
                <a name="41198305" href="/transcript/11540?m=41198305#41198305"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198235#41198235"> </a> 

                <div class="content">
                    @SmokeDetector tpu-                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198345">
                <a name="41198345" href="/transcript/11540?m=41198345#41198345"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198304#41198304"> </a> 

                <div class="content">
                    @Videonauth You need to be a <a href="https://charcoal-se.org/smokey/Commands#privileged-commands" rel="nofollow noopener noreferrer">privileged user</a>.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-120914">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/WyV1l.png?s=16&g=1" alt="SmokeDetector" />
            </div>
        
        <div class="username"><a href="/users/120914/smokedetector" title="SmokeDetector">SmokeDetector</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198349">
                <a name="41198349" href="/transcript/11540?m=41198349#41198349"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    Conflicting feedback across revisions: <a href="//metasmoke.erwaysoftware.com/post/93848" rel="nofollow noopener noreferrer">current</a>, <a href="//metasmoke.erwaysoftware.com/post/93847" rel="nofollow noopener noreferrer">#1</a>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
             <div class="timestamp">1:28 AM</div>

        
        
            <div class="message" id="message-41198350">
                <a name="41198350" href="/transcript/11540?m=41198350#41198350"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    ah ok :)                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-155243">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/fY1pd.jpg?s=16&g=1" alt="Nisse Engstr&#246;m" />
            </div>
        
        <div class="username"><a href="/users/155243/nisse-engstrom" title="Nisse Engstr&#246;m">Nisse Engstr&#246;m</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198423">
                <a name="41198423" href="/transcript/11540?m=41198423#41198423"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198350#41198350"> </a> 

                <div class="content">
                    @Videonauth There&#39;s a <a href="https://charcoal-se.org/pings/mods" rel="nofollow noopener noreferrer">list of mods to ping</a> when things get out of hand.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198457">
                <a name="41198457" href="/transcript/11540?m=41198457#41198457"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    oh yes i know a few i would ping then otherwise i drop you guys here a line if i stumble on a missed one                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-155243">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/fY1pd.jpg?s=16&g=1" alt="Nisse Engstr&#246;m" />
            </div>
        
        <div class="username"><a href="/users/155243/nisse-engstrom" title="Nisse Engstr&#246;m">Nisse Engstr&#246;m</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198542">
                <a name="41198542" href="/transcript/11540?m=41198542#41198542"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198457#41198457"> </a> 

                <div class="content">
                    @Videonauth Do you understand Spanish?                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198550">
                <a name="41198550" href="/transcript/11540?m=41198550#41198550"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    nope only english and german (native)                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-155243">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/fY1pd.jpg?s=16&g=1" alt="Nisse Engstr&#246;m" />
            </div>
        
        <div class="username"><a href="/users/155243/nisse-engstrom" title="Nisse Engstr&#246;m">Nisse Engstr&#246;m</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198594">
                <a name="41198594" href="/transcript/11540?m=41198594#41198594"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    I have no idea what <a href="https://es.stackoverflow.com/a/118124/">this</a> means. It should probably be reported, but I don&#39;t know. It sort of looks like Italian though.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198607">
                <a name="41198607" href="/transcript/11540?m=41198607#41198607"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    No wait, it&#39;s already caught above.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
             <div class="timestamp">1:45 AM</div>

        
        
            <div class="message" id="message-41198629">
                <a name="41198629" href="/transcript/11540?m=41198629#41198629"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                     <span class="deleted">(removed)</span>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198635">
                <a name="41198635" href="/transcript/11540?m=41198635#41198635"><span style="display:inline-block;" class="action-link edits"><span class="img"> </span></span></a>

                

                <div class="content">
                    use google translate, cant let this stand here :) at least not without getting a time out for naughtyness                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-137388">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/Ma6sp.jpg?s=16&g=1" alt="QPaysTaxes" />
            </div>
        
        <div class="username"><a href="/users/137388/qpaystaxes" title="QPaysTaxes">QPaysTaxes</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198641">
                <a name="41198641" href="/transcript/11540?m=41198641#41198641"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198594#41198594"> </a> 

                <div class="content">
                    @NisseEngström It&#39;s spam.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-155243">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/fY1pd.jpg?s=16&g=1" alt="Nisse Engstr&#246;m" />
            </div>
        
        <div class="username"><a href="/users/155243/nisse-engstrom" title="Nisse Engstr&#246;m">Nisse Engstr&#246;m</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198709">
                <a name="41198709" href="/transcript/11540?m=41198709#41198709"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198635#41198635"> </a> 

                <div class="content">
                    @Videonauth Google Translate didn&#39;t work on that one.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198714">
                <a name="41198714" href="/transcript/11540?m=41198714#41198714"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198641#41198641"> </a> 

                <div class="content">
                    @QPaysTaxes Thanks.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198715">
                <a name="41198715" href="/transcript/11540?m=41198715#41198715"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    it did                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198719">
                <a name="41198719" href="/transcript/11540?m=41198719#41198719"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    dont know if you can see deleted messages                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-155243">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/fY1pd.jpg?s=16&g=1" alt="Nisse Engstr&#246;m" />
            </div>
        
        <div class="username"><a href="/users/155243/nisse-engstrom" title="Nisse Engstr&#246;m">Nisse Engstr&#246;m</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198731">
                <a name="41198731" href="/transcript/11540?m=41198731#41198731"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198719#41198719"> </a> 

                <div class="content">
                    @Videonauth Nope.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198769">
                <a name="41198769" href="/transcript/11540?m=41198769#41198769"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    its spanish, autodetection did work to english: will post it in a few seconds againhere for short please dont flagbann me                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198776">
                <a name="41198776" href="/transcript/11540?m=41198776#41198776"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                     <span class="deleted">(removed)</span>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198787">
                <a name="41198787" href="/transcript/11540?m=41198787#41198787"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    seen?                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-155243">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/fY1pd.jpg?s=16&g=1" alt="Nisse Engstr&#246;m" />
            </div>
        
        <div class="username"><a href="/users/155243/nisse-engstrom" title="Nisse Engstr&#246;m">Nisse Engstr&#246;m</a></div>

    </div></div>
    <div class="messages">
        
             <div class="timestamp">1:54 AM</div>

        
        
            <div class="message" id="message-41198799">
                <a name="41198799" href="/transcript/11540?m=41198799#41198799"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198787#41198787"> </a> 

                <div class="content">
                    @Videonauth Yes, but that&#39;s not the one I linked to.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198835">
                <a name="41198835" href="/transcript/11540?m=41198835#41198835"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    ah the one above mhmmm yes doesnt work                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-137388">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/Ma6sp.jpg?s=16&g=1" alt="QPaysTaxes" />
            </div>
        
        <div class="username"><a href="/users/137388/qpaystaxes" title="QPaysTaxes">QPaysTaxes</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198853">
                <a name="41198853" href="/transcript/11540?m=41198853#41198853"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198769#41198769"> </a> 

                <div class="content">
                    @Videonauth No one here flag-bans people.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198854">
                <a name="41198854" href="/transcript/11540?m=41198854#41198854"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    You get flag banned if you flag too many things that get declined by mods.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198858">
                <a name="41198858" href="/transcript/11540?m=41198858#41198858"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    its gibberish tho talking about a garden party at an uncles place                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-137388">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/Ma6sp.jpg?s=16&g=1" alt="QPaysTaxes" />
            </div>
        
        <div class="username"><a href="/users/137388/qpaystaxes" title="QPaysTaxes">QPaysTaxes</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198860">
                <a name="41198860" href="/transcript/11540?m=41198860#41198860"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    Gibberish is a perfectly good reason to red-flag.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198864">
                <a name="41198864" href="/transcript/11540?m=41198864#41198864"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    Whether you flag as spam or r/a doesn&#39;t really matter.                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198869">
                <a name="41198869" href="/transcript/11540?m=41198869#41198869"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    got it translated via leo.org                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-155243">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/fY1pd.jpg?s=16&g=1" alt="Nisse Engstr&#246;m" />
            </div>
        
        <div class="username"><a href="/users/155243/nisse-engstrom" title="Nisse Engstr&#246;m">Nisse Engstr&#246;m</a></div>

    </div></div>
    <div class="messages">
        
             <div class="timestamp">1:58 AM</div>

        
        
            <div class="message" id="message-41198872">
                <a name="41198872" href="/transcript/11540?m=41198872#41198872"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    !!/report <a href="https://es.stackoverflow.com/a/118116/" rel="nofollow noopener noreferrer">es.stackoverflow.com/a/118116</a> <a href="https://es.stackoverflow.com/a/118114/" rel="nofollow noopener noreferrer">es.stackoverflow.com/a/118114</a> <a href="https://es.stackoverflow.com/a/118120/" rel="nofollow noopener noreferrer">es.stackoverflow.com/a/118120</a> <a href="https://es.stackoverflow.com/a/118119/" rel="nofollow noopener noreferrer">es.stackoverflow.com/a/118119</a>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-120914">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/WyV1l.png?s=16&g=1" alt="SmokeDetector" />
            </div>
        
        <div class="username"><a href="/users/120914/smokedetector" title="SmokeDetector">SmokeDetector</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198873">
                <a name="41198873" href="/transcript/11540?m=41198873#41198873"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//goo.gl/eLDYqh" rel="nofollow noopener noreferrer">SmokeDetector</a> | <a href="//m.erwaysoftware.com/posts/by-url?url=//es.stackoverflow.com/a/118116" rel="nofollow noopener noreferrer">MS</a> ] Manually reported answer (batch report: post 1 out of 4): <a href="//es.stackoverflow.com/a/118116">No logro entender porque me da este error ArrayIndexOutOfBoundsException: 6</a> by <a href="//es.stackoverflow.com/users/66574">Escroto Y Pene Gratis</a> on <code>es.stackoverflow.com</code>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198876">
                <a name="41198876" href="/transcript/11540?m=41198876#41198876"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//goo.gl/eLDYqh" rel="nofollow noopener noreferrer">SmokeDetector</a> | <a href="//m.erwaysoftware.com/posts/by-url?url=//es.stackoverflow.com/a/118114" rel="nofollow noopener noreferrer">MS</a> ] Manually reported answer (batch report: post 2 out of 4): <a href="//es.stackoverflow.com/a/118114">Asignar valores a un combobox html con JSOUP</a> by <a href="//es.stackoverflow.com/users/66574">Escroto Y Pene Gratis</a> on <code>es.stackoverflow.com</code>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-137388">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/Ma6sp.jpg?s=16&g=1" alt="QPaysTaxes" />
            </div>
        
        <div class="username"><a href="/users/137388/qpaystaxes" title="QPaysTaxes">QPaysTaxes</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198880">
                <a name="41198880" href="/transcript/11540?m=41198880#41198880"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198873#41198873"> </a> 

                <div class="content">
                    @SmokeDetector k                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-120914">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/WyV1l.png?s=16&g=1" alt="SmokeDetector" />
            </div>
        
        <div class="username"><a href="/users/120914/smokedetector" title="SmokeDetector">SmokeDetector</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198879">
                <a name="41198879" href="/transcript/11540?m=41198879#41198879"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//goo.gl/eLDYqh" rel="nofollow noopener noreferrer">SmokeDetector</a> | <a href="//m.erwaysoftware.com/posts/by-url?url=//es.stackoverflow.com/a/118120" rel="nofollow noopener noreferrer">MS</a> ] Manually reported answer (batch report: post 3 out of 4): <a href="//es.stackoverflow.com/a/118120">Crystal Reports Arroja &quot;E_NOINTERFACE&quot; cuando reporte.SetDataSource(ds);</a> by <a href="//es.stackoverflow.com/users/66574">Escroto Y Pene Gratis</a> on <code>es.stackoverflow.com</code>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198882">
                <a name="41198882" href="/transcript/11540?m=41198882#41198882"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                

                <div class="content">
                    [ <a href="//goo.gl/eLDYqh" rel="nofollow noopener noreferrer">SmokeDetector</a> | <a href="//m.erwaysoftware.com/posts/by-url?url=//es.stackoverflow.com/a/118119" rel="nofollow noopener noreferrer">MS</a> ] Manually reported answer (batch report: post 4 out of 4): <a href="//es.stackoverflow.com/a/118119">Descargar archivos desde la terminal de Mac</a> by <a href="//es.stackoverflow.com/users/66574">Escroto Y Pene Gratis</a> on <code>es.stackoverflow.com</code>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-137388">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/Ma6sp.jpg?s=16&g=1" alt="QPaysTaxes" />
            </div>
        
        <div class="username"><a href="/users/137388/qpaystaxes" title="QPaysTaxes">QPaysTaxes</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198884">
                <a name="41198884" href="/transcript/11540?m=41198884#41198884"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198876#41198876"> </a> 

                <div class="content">
                    @SmokeDetector k                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-205533">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/idNpq.jpg?s=16&g=1" alt="Videonauth" />
            </div>
        
        <div class="username"><a href="/users/205533/videonauth" title="Videonauth">Videonauth</a></div>

    </div></div>
    <div class="messages">
        
            <div class="message" id="message-41198888">
                <a name="41198888" href="/transcript/11540?m=41198888#41198888"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198853#41198853"> </a> 

                <div class="content">
                    @QPaysTaxes well i posted the translation of that other spanish post which was not really PG friendly <i>coughs coughs</i>                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>


<div class="monologue user-137388">
    <div class="signature"><div class="tiny-signature">
        
            <div class="avatar avatar-16">
                <img width="16" height="16" src="https://i.stack.imgur.com/Ma6sp.jpg?s=16&g=1" alt="QPaysTaxes" />
            </div>
        
        <div class="username"><a href="/users/137388/qpaystaxes" title="QPaysTaxes">QPaysTaxes</a></div>

    </div></div>
    <div class="messages">
        
             <div class="timestamp">1:59 AM</div>

        
        
            <div class="message" id="message-41198889">
                <a name="41198889" href="/transcript/11540?m=41198889#41198889"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198879#41198879"> </a> 

                <div class="content">
                    @SmokeDetector k                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
            <div class="message" id="message-41198893">
                <a name="41198893" href="/transcript/11540?m=41198893#41198893"><span style="display:inline-block;" class="action-link"><span class="img"> </span></span></a>

                 <a class="reply-info" href="/transcript/11540?m=41198882#41198882"> </a> 

                <div class="content">
                    @SmokeDetector k                      
                </div>
                <span class="flash">
                    
                </span>
            </div>
        
    
    </div>
    <div class="clear-both" style="height:0">&nbsp;</div> 
</div>
</div>
      <div class="clear-both"></div><div class="pager"><a href="/transcript/11540/2017/11/17/0-1"><span class="page-numbers">00:00 - 01:00</span></a><span class="page-numbers current">01:00 - 02:00</span><a href="/transcript/11540/2017/11/17/2-13"><span class="page-numbers">02:00 - 13:00</span></a><a href="/transcript/11540/2017/11/17/13-24"><span class="page-numbers">13:00 - 00:00</span></a></div><div class="clear-both"></div>
      <br/>
      <a href="/transcript/11540/2013/11/16" class="button noprint" title="2013-11-16">&laquo; first day (1461 days earlier)</a>&nbsp;
<a href="/transcript/11540/2017/11/16" class="button noprint" rel="prev" title="2017-11-16">&larr; previous day</a>&nbsp;
<link rel="prev" title="2017-11-16" href="/transcript/11540/2017/11/16" />
<a href="/transcript/11540/2017/11/18" class="button noprint" rel="next" title="2017-11-18">next day &rarr;</a>&nbsp;
<link rel="next" title="2017-11-18" href="/transcript/11540/2017/11/18" />
<a href="/transcript/11540/2017/11/22" class="button noprint" title="2017-11-22"> last day (5 days later) &raquo;</a>&nbsp;
<div class="clear-both"></div>
    <div id="sidebar">
    <div id="sidebar-content">
    <div id="info">
        <form method="get" action="/search">
            <input type="text" id="searchbox" name="q"/>
            <input type="hidden" name="room" value="11540" />
        </form>
        

        <div style="padding-top:3px;"><a href="/" class="button">all rooms</a></div>

        <br clear=left />

        <h2>Transcript for</h2>

        
        <a class="calendar-small-link" href="/transcript/11540/2017/11/16">
            <div class="icon" title="2017-11-16"><div class="calendar-small"><span class="weekday-small">Nov</span>16</div></div>
        </a>
        <div class="icon" title="2017-11-17"><div class="calendar"><span class="weekday">Nov</span>17</div></div>
        
        <a class="calendar-small-link" href="/transcript/11540/2017/11/18">
            <div class="icon" title="2017-11-18"><div class="calendar-small"><span class="weekday-small">Nov</span>18</div></div>
        </a>
        
        <br clear=left />
        
        <div class="room-mini"><div class="room-mini-header"><h3><span class="room-name"><a rel="noreferrer noopener" href="/rooms/11540/charcoal-hq">Charcoal HQ</a></span></h3><div title="Where diamonds are made, smoke is detected, and we break things by developing on production. 76,000 true positives and counting. [Recursive] oneboxes are awesome. Handy links: http://charcoal-se.org, https://github.com/Charcoal-SE, http://charcoal-se.org/blaze/" class="room-mini-description">Where diamonds are made, smoke is detected, and we break thing...<a href="http://charcoal-se.org" rel="nofollow noopener noreferrer"></a><a href="https://github.com/Charcoal-SE" rel="nofollow noopener noreferrer"></a><a href="http://charcoal-se.org/blaze/" rel="nofollow noopener noreferrer"></a></div></div><div class="room-current-user-count" title="current users"><a rel="noopener noreferrer" href="/rooms/info/11540/charcoal-hq">33</a></div><div class="room-message-count" title="messages in the last 2h"><a rel="noopener noreferrer" href="/transcript/11540">75</a></div><div class="mspark" style="height:25px;width:205px">
<div class="mspbar" style="width:8px;height:6px;left:0px;"></div><div class="mspbar" style="width:8px;height:7px;left:8px;"></div><div class="mspbar" style="width:8px;height:9px;left:16px;"></div><div class="mspbar" style="width:8px;height:9px;left:24px;"></div><div class="mspbar" style="width:8px;height:16px;left:32px;"></div><div class="mspbar" style="width:8px;height:20px;left:40px;"></div><div class="mspbar" style="width:8px;height:21px;left:48px;"></div><div class="mspbar" style="width:8px;height:25px;left:56px;"></div><div class="mspbar" style="width:8px;height:21px;left:64px;"></div><div class="mspbar" style="width:8px;height:25px;left:72px;"></div><div class="mspbar" style="width:8px;height:20px;left:80px;"></div><div class="mspbar" style="width:8px;height:20px;left:88px;"></div><div class="mspbar" style="width:8px;height:17px;left:96px;"></div><div class="mspbar" style="width:8px;height:13px;left:104px;"></div><div class="mspbar" style="width:8px;height:10px;left:112px;"></div><div class="mspbar" style="width:8px;height:9px;left:120px;"></div><div class="mspbar" style="width:8px;height:13px;left:128px;"></div><div class="mspbar" style="width:8px;height:12px;left:136px;"></div><div class="mspbar" style="width:8px;height:17px;left:144px;"></div><div class="mspbar" style="width:8px;height:15px;left:152px;"></div><div class="mspbar" style="width:8px;height:12px;left:160px;"></div><div class="mspbar" style="width:8px;height:9px;left:168px;"></div><div class="mspbar" style="width:8px;height:7px;left:176px;"></div><div class="mspbar" style="width:8px;height:4px;left:184px;"></div><div class="mspbar now" style="height:25px;left:166px;"></div></div>
<div class="clear-both"></div></div>
        <div><a rel="noopener noreferrer" class="tag" href="http://stackexchange.com/tags/best-bad-practices/info">best-bad-practices</a> <a rel="noopener noreferrer" class="tag" href="http://stackexchange.com/tags/dev-on-prod/info">dev-on-prod</a> <a rel="noopener noreferrer" class="tag" href="http://stackexchange.com/tags/panic-driven-development/info">panic-driven-development</a> <a rel="noopener noreferrer" class="tag" href="http://stackexchange.com/tags/plastic-knives/info">plastic-knives</a></div>
        <br class="clear-both" />
        <div class="noprint">
            <div id="transcript-links">
                <a id="join-room" href="/rooms/11540/charcoal-hq" class="button">join this room</a><br />
                <a href="/rooms/info/11540/charcoal-hq" class="button">about this room</a><br />
                
                    <a class="button" href="#" id="bookmark-button">bookmark a conversation</a><br />
                
            </div>
            
            <br />
            <div class="mspark" style="height:300px;width:200px">
<div class="mspbar" style="height:12px;width:57px;top:0px;"></div><div class="msplab" style="top:0px;">00:00</div><div class="mspbar" style="height:12px;width:182px;top:12px;"></div><div class="mspbar" style="height:12px;width:54px;top:24px;"></div><div class="mspbar" style="height:12px;width:12px;top:36px;"></div><div class="mspbar" style="height:12px;width:131px;top:48px;"></div><div class="mspbar" style="height:12px;width:110px;top:60px;"></div><div class="mspbar" style="height:12px;width:161px;top:72px;"></div><div class="msplab" style="top:72px;">06:00</div><div class="mspbar" style="height:12px;width:99px;top:84px;"></div><div class="mspbar" style="height:12px;width:113px;top:96px;"></div><div class="mspbar" style="height:12px;width:200px;top:108px;"></div><div class="mspbar" style="height:12px;width:99px;top:120px;"></div><div class="mspbar" style="height:12px;width:110px;top:132px;"></div><div class="mspbar" style="height:12px;width:90px;top:144px;"></div><div class="msplab" style="top:144px;">12:00</div><div class="mspbar" style="height:12px;width:191px;top:156px;"></div><div class="mspbar" style="height:12px;width:18px;top:168px;"></div><div class="mspbar" style="height:12px;width:15px;top:180px;"></div><div class="mspbar" style="height:12px;width:6px;top:192px;"></div><div class="mspbar" style="height:12px;width:75px;top:204px;"></div><div class="mspbar" style="height:12px;width:90px;top:216px;"></div><div class="msplab" style="top:216px;">18:00</div><div class="mspbar" style="height:12px;width:45px;top:228px;"></div><div class="mspbar" style="height:12px;width:57px;top:240px;"></div><div class="mspbar" style="height:12px;width:36px;top:252px;"></div><div class="mspbar" style="height:12px;width:54px;top:264px;"></div><div class="mspbar" style="height:12px;width:27px;top:276px;"></div><a href="/transcript/11540/2017/11/17/0-1"><div class="msparea" style="top:0px;width:200px;height:12px" title="19 messages"></div></a><a href="/transcript/11540/2017/11/17/1-2"><div class="msparea now" style="top:12px;width:200px;height:12px" title="61 messages"></div></a><a href="/transcript/11540/2017/11/17/2-13"><div class="msparea" style="top:24px;width:200px;height:132px" title="395 messages"></div></a><a href="/transcript/11540/2017/11/17/13-24"><div class="msparea" style="top:156px;width:200px;height:132px" title="205 messages"></div></a></div>

            <div class="msg-small">
                all times are UTC
            </div>
            
            <br />
        </div>
        <br /><br /><div id="transcript-logo"><a rel="noreferrer noopener" href="http://stackexchange.com" title="The Stack Exchange Network"><img style="max-width:150px" src="//cdn-chat.sstatic.net/chat/img/se-logo-white.png?v=da" alt="The Stack Exchange Network"/></a>
    </div>
<br class="clear-both" /><br />
<div id="copyright">
    site design / logo &copy; 2017 Stack Exchange Inc; <a rel="noopener noreferrer" href="http://stackexchange.com/legal">legal</a>
    <br /><br />
    <a href="#" class="mobile-on">mobile</a>
</div>

    </div>
    </div>    
    </div> 
    </div> 
    
    </div> <input id="fkey" name="fkey" type="hidden" value="64f0ae1fdde80a7b92d9281473795fde" />
</body>
</html>'''
