<?xml version="1.0"?>
<flowgorithm fileversion="3.0">
    <attributes>
        <attribute name="name" value="huy"/>
        <attribute name="authors" value="HP"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-02-28 08:53:12 AM"/>
        <attribute name="created" value="SFA7REVTS1RPUC1DQU5OM1JROzIwMjUtMDItMjg7MDg6MDE6NDMgQU07MjUwMw=="/>
        <attribute name="edited" value="SFA7REVTS1RPUC1DQU5OM1JROzIwMjUtMDItMjg7MDg6NTM6MTIgQU07MTsyNjE0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="d" type="Real" array="False" size=""/>
            <declare name="h" type="Real" array="False" size=""/>
            <declare name="s" type="Real" array="False" size=""/>
            <output expression="&quot;Vui l&#242;ng nh&#7853;p &#273;&#7897; d&#224;i c&#7841;nh &#273;&#225;y:&quot;" newline="True"/>
            <input variable="d"/>
            <output expression="&quot;vui l&#242;ng nh&#7853;p &#273;&#7891; d&#224;i chi&#7873;u cao:&quot;" newline="True"/>
            <input variable="h"/>
            <assign variable="s" expression="(d*h)/2"/>
            <output expression="&quot;di&#7879;n t&#237;ch c&#7911;a tam giac l&#224;: &quot;&amp;s" newline="True"/>
        </body>
    </function>
</flowgorithm>
