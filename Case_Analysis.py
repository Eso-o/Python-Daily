#自己设计
import streamlit as st
import pandas as pd
import numpy as np
from pyecharts.charts import Bar
import streamlit_echarts
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import random as rd
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode
def data_form():
        rd.seed(520)
        sum1=0
        sum2=0
        sum3=0
        Numbers1=[]
        Numbers2=[]
        porpo1=[]
        porpo2=[]
        porpo3=[]
        for blo in range(17):
            a=rd.randint(0,5000)
            Numbers1.append(a)
        for blt in range(17):
            b=rd.randint(0,10000)
            Numbers1.append(b)
        for blr in range(17):
            c=rd.randint(0,2000)
            Numbers2.append(c)
        for blf in range(17):
            d=rd.randint(0,500)
            Numbers2.append(d)
        Numbers3=[x+y for x,y in zip(Numbers1,Numbers2)]
        #生成各段的比例
        for j in Numbers1:
            sum1+=j
        for k in Numbers1:
            porp1=k/sum1
            porpo1.append(porp1)
        for j in Numbers2:
            sum2+=j
        for k in Numbers2:
            porp2=k/sum2
            porpo2.append(porp2) 
        for j in Numbers3:
            sum3+=j
        for k in Numbers3:
            porp3=k/sum3
            porpo3.append(porp3)  
        Province = ['内蒙古','广西','西藏','宁夏','新疆','北京','陕西','甘肃','青海','天津','上海','重庆','河北','山西','辽宁','吉林','黑龙江','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','海南',\
                    '四川','贵州','云南','台湾','香港','澳门']
        return Province,Numbers1,Numbers2,Numbers3,porpo1,porpo2,porpo3
def bar_run():
    bar = Bar()
    bar.add_xaxis(Province)
    bar.add_yaxis("Mild Patients",Numbers1,itemstyle_opts=opts.ItemStyleOpts(color="#5D7DB3"))
    bar.add_yaxis("Critical Patients",Numbers2,itemstyle_opts=opts.ItemStyleOpts(color="#464879"))
    bar.add_yaxis("All Patients",Numbers3,itemstyle_opts=opts.ItemStyleOpts(color="#B6CAD7"))
    bar.set_series_opts(
        #是否显示标签
        label_opts = opts.LabelOpts(is_show = False)
        ,markpoint_opts = opts.MarkPointOpts(data = [opts.MarkPointItem(type_ = "max",name = "max")
                                                    ,opts.MarkPointItem(name = "min",type_ = "min")]
                                            )
        ,markline_opts = opts.MarkLineOpts(data = [opts.MarkLineItem(name = "average",type_ = "average")]))
    #全局配置设置
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Histogram", subtitle="Number of patients by province"))
    return streamlit_echarts.st_pyecharts(bar)
def pie_run():
    # 数据设置
    pie = Pie(init_opts=opts.InitOpts(width='1700px', height='720px')) 
    pie.add(
        "",
        [list(z) for z in zip(Province,porpo1)],
        center=["20%", "30%"],  # 位置
        radius=[0, 80],   # 每个饼图内外圈的大小
    )
    pie.add(
        "",
        [list(z) for z in zip(Province,porpo2)],
        center=["60%", "30%"],
        radius=[0, 80],
    )
    pie.add(
        "",
        [list(z) for z in zip(Province,porpo3)],
        center=["40%", "70%"],
        radius=[0, 80],
    )
    pie.set_series_opts(
        #是否显示标签
        label_opts=opts.LabelOpts(is_show=False,
                                formatter=JsCode(
                                    "function(x){return Number(x.data.percent*100).toFixed()+'%'}"
                                )),
        markpoint_opts = opts.MarkPointOpts(data = [opts.MarkPointItem(type_ = "max",name = "max")
                                                    ,opts.MarkPointItem(name = "min",type_ = "min")]))
    pie.set_global_opts(
        title_opts = opts.TitleOpts(title = "Pie",subtitle="Proportion of patients by province"),
        legend_opts = opts.LegendOpts(pos_top = "5%",pos_left = "80%",orient="vertical"))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    return streamlit_echarts.st_pyecharts(pie)
np.random.seed(520)
show_part=st.sidebar.selectbox("Select a part",("Distribution Of Cases","Regional Relevance","Individual Analysis"))
st.title("**Case Analysis**")
if show_part=="Distribution Of Cases":
    df = pd.DataFrame(
    np.random.randn(1000, 2)*30+[45,80],
    columns=['lat', 'lon'])
    agree=st.checkbox("Show the raw data")
    if agree:
        st.write(df)
    st.divider()
    st.caption("This map bellow precisely illustrates the distribution of the cases")
    st.map(df)
    st.write('''Every point refer to an patient's address.
So according to the density of the point, we could estimate the infectivity of the disease''')
    with st.expander("Show source code"):
        code = '''
    df = pd.DataFrame(
    np.random.rand(10000, 2)*61+[73.5, 0],
    columns=['lat', 'lon'])
    agree=st.checkbox("Show the raw data")
    if agree:
        st.write(df)
    st.divider()
    st.caption("This map bellow precisely illustrates the distribution of the cases")
    st.map(df)
    st.text(''Every point refer to an patient's address.
    So according to the density of the point, we could estimate the infectivity of the disease'')
    with st.expander("Show source code"):
        st.code(code,language='python')'''
        st.code(code,language='python')
elif show_part=="Regional Relevance":   
    Province,Numbers1,Numbers2,Numbers3,porpo1,porpo2,porpo3=data_form() 
    show_chart=st.sidebar.selectbox("Select a chart",("Bar", "Pie"))
    if  show_chart=="Bar":
        bar_run()
    else :
        pie_run()
    agree=st.checkbox("Show the raw data")
    if agree:
        coli1,coli2=st.columns(2)
        with coli1:
            st.subheader("The Raw Data Of The Bar")
            bar_data=dict(zip(Province,Numbers1))
            Bar_data=pd.DataFrame.from_dict(bar_data,orient='index')       
            st.write(Bar_data)
        with coli2:
            st.subheader("The Raw Data Of The Pie")
            pie_data=dict(zip(Province,porpo1))
            Pie_data=pd.DataFrame.from_dict(pie_data,orient='index')
            st.write(Pie_data)
    with st.expander("Show source code"):
        code = '''
def data_form():
    rd.seed(520)
    sum1=0
    Numbers1=[]
    porpo1=[]
    for i in range(34):
        a=rd.randint(0,10000)
        Numbers1.append(a)
    for j in Numbers1:
        sum1+=j
    for k in Numbers1:
        porpo1o1=k/sum1
        porpo1.append(porpo1o1)   
    Province = ['北京','天津','上海','重庆','河北','山西','辽宁','吉林','黑龙江','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','海南',\
                '四川','贵州','云南','陕西','甘肃','青海','台湾','内蒙古','广西','西藏','宁夏','新疆','香港','澳门']
    return Province,Numbers1,porpo1
def bar_run():
    bar = Bar()
    bar.add_xaxis(Province)
    bar.add_yaxis('',Numbers1)
    bar.set_series_opts(
        #是否显示标签
        label_opts = opts.LabelOpts(is_show = False)
        ,markpoint_opts = opts.MarkPointOpts(data = [opts.MarkPointItem(type_ = "max",name = "max")
                                                    ,opts.MarkPointItem(name = "min",type_ = "min")]
                                            )
        ,markline_opts = opts.MarkLineOpts(data = [opts.MarkLineItem(name = "average",type_ = "average")]))
    #全局配置设置
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Histogram", subtitle="Number of patients by province"))
    return streamlit_echarts.st_pyecharts(bar)
def pie_run():
    # 数据设置
    pie = Pie(init_opts=opts.InitOpts(width='1700px', height='720px')) 
    pie.add("",[list(z) for z in zip(Province,porpo1)],radius = ["40%","75%"])    # 设置圆环的粗细和大小
    pie.set_series_opts
    pie.set_series_opts(
        #是否显示标签
        label_opts=opts.LabelOpts(is_show=False,
                                formatter=JsCode(
                                    "function(x){return Number(x.data.percent*100).toFixed()+'%'}"
                                )),
        markpoint_opts = opts.MarkPointOpts(data = [opts.MarkPointItem(type_ = "max",name = "max")
                                                    ,opts.MarkPointItem(name = "min",type_ = "min")]))
    pie.set_global_opts(
        title_opts = opts.TitleOpts(title = "Pie",subtitle="Proportion of patients by province"),
        legend_opts = opts.LegendOpts(pos_top = "5%",pos_left = "80%",orient="vertical"))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    return streamlit_echarts.st_pyecharts(pie)
Province,Numbers1,porpo1=data_form() 
bar_run()
st.divider()  
pie_run()
agree=st.checkbox("Show the raw data")
if agree:
    coli1,coli2=st.columns(2)
    with coli1:
        st.subheader("The Raw Data Of The Bar")
        bar_data=dict(zip(Province,Numbers1))
        Bar_data=pd.DataFrame.from_dict(bar_data,orient='index')       
        st.write(Bar_data)
    with coli2:
        st.subheader("The Raw Data Of The Pie")
        pie_data=dict(zip(Province,porpo1))
        Pie_data=pd.DataFrame.from_dict(pie_data,orient='index')
        st.write(Pie_data)'''
        st.code(code,language='python')
else:
    weight = st.slider('How much do you weigh? :neutral_face:',0.0,200.0,60.0)
    high = st.slider('How tall are you? :neutral_face:',0.0,2.50,1.70)
    BMI=weight/(high*high)
    pressure=st.number_input("What's your systolic blood pressure? :neutral_face:")
    blood_glucose=st.number_input("What's your fasting blood glucose? :neutral_face:")

    # 比较输入值和目标值
    if weight< 0 or high< 0 or pressure < 0 or blood_glucose < 0:
        result  ="Please input valid data"
        result2 ="Please input valid data"
        result3 ="Please input valid data"
    else:
        if  0< BMI < 18.5:
            result = "Your BMI data shows that you are **:orange[underweight]** :worried:"
        elif BMI>= 35:
            result = "Your BMI data shows that you are severely **:red[severe obese]** :disappointed_relieved:"
        elif 30 <= BMI < 35:
            result = "Your BMI data shows that you are **:orange[obese]** :disappointed:"
        elif 25 <= BMI < 30:
            result = "Your BMI data shows that you are **:orange[overweight]** :persevere:"
        elif 18.5 <= BMI < 25:
            result = "Your BMI data shows that you are **:blue[healthy]** :yum:"

        if pressure < 90:
            result2 = "Your systolic blood pressure data shows that you are currently suffering from **:orange[high blood pressure]** :disappointed:"
        elif BMI > 140:
            result2 = "Your systolic blood pressure data shows that you are currently suffering from **:orange[low blood pressure]** :disappointed:"
        else:
            result2 = "Your systolic blood pressure data shows that you are now in **:blue[the normal range]** :blush:"

        if  blood_glucose>= 10.11:
            result3 = "Your fasting blood glucose data indicates that you may now have **:red[severe diabetes]** :disappointed_relieved:"
        elif 3.9 <= blood_glucose < 6.1:
            result3 = "Your fasting blood glucose data shows that your blood glucose level is in **:blue[the normal range]** :blush: "
        elif 7.0 <= blood_glucose < 8.4:
            result3 = "Your fasting blood glucose data indicates that you may now have **:orange[mild diabetes]** :disappointed_relieved:"
        elif 8.4 <= blood_glucose <= 10.1:
            result3 = "Your fasting blood glucose data indicates that you may now have **:orange[moderate diabetes]** :disappointed:"
        else:
            result3 = "Your fasting blood glucose data shows that your blood glucose level is in **:orange[a less normal range]** :sweat_smile:"

    #根据上述数据判断就诊等级与迫切程度
    if result3 == "Your fasting blood glucose data indicates that you may now have **:red[severe diabetes]** :disappointed_relieved:"\
        and result2 == "Your systolic blood pressure data shows that you are currently suffering from **:orange[high blood pressure]** :disappointed:"\
        and result == "Your BMI data shows that you are severely **:red[severe obese]** :isappointed_relieved:":
        result4 = "You now need to go to a Grade II and above hospital in time :exclamation:"
    else:
        result4 = "You can choose to go to Grade II and below hospitals in your free time for daily physical examination :flushed:"
    st.divider()

    # 显示结果
    st.write(result)
    st.write(result2)
    st.write(result3)
    st.write(result4)
    st.divider()
    with st.expander("Show source code"):
        code = '''
weight = st.slider('How much do you weigh? :neutral_face:',0.0,200.0,50.0)
high = st.slider('How tall are you? :neutral_face:',0.0,2.50,1.70)
BMI=weight/(high*high)
pressure=st.number_input("What's your systolic blood pressure? :neutral_face:")
blood_glucose=st.number_input("What's your fasting blood glucose? :neutral_face:")

# 比较输入值和目标值
if weight< 0 or high< 0 or pressure < 0 or blood_glucose < 0:
    result  ="Please input valid data"
    result2 ="Please input valid data"
    result3 ="Please input valid data"
else:
    if  0< BMI < 18.5:
        result = "Your BMI data shows that you are **:orange[underweight]** :worried:"
    elif BMI>= 35:
        result = "Your BMI data shows that you are severely **:red[severe obese]** :disappointed_relieved:"
    elif 30 <= BMI < 35:
        result = "Your BMI data shows that you are **:orange[obese]** :disappointed:"
    elif 25 <= BMI < 30:
        result = "Your BMI data shows that you are **:orange[overweight]** :persevere:"
    elif 18.5 <= BMI < 25:
        result = "Your BMI data shows that you are **:blue[healthy]** :yum:"

    if pressure < 90:
        result2 = "Your systolic blood pressure data shows that you are currently suffering from **:orange[high blood pressure]** :disappointed:"
    elif BMI > 140:
        result2 = "Your systolic blood pressure data shows that you are currently suffering from **:orange[low blood pressure]** :disappointed:"
    else:
        result2 = "Your systolic blood pressure data shows that you are now in **:blue[the normal range]** :blush:"

    if  blood_glucose>= 10.11:
        result3 = "Your fasting blood glucose data indicates that you may now have **:red[severe diabetes]** :isappointed_relieved:"
    elif 3.9 <= blood_glucose < 6.1:
        result3 = "Your fasting blood glucose data shows that your blood glucose level is in **:blue[the normal range]** :blush: "
    elif 7.0 <= blood_glucose < 8.4:
        result3 = "Your fasting blood glucose data indicates that you may now have **:orange[mild diabetes]** :disappointed_relieved:"
    elif 8.4 <= blood_glucose <= 10.1:
        result3 = "Your fasting blood glucose data indicates that you may now have **:orange[moderate diabetes]** :disappointed:"
    else:
        result3 = "Your fasting blood glucose data shows that your blood glucose level is in **:orange[a less normal range]** :sweat_smile:"

#根据上述数据判断就诊等级与迫切程度
if result3 == "Your fasting blood glucose data indicates that you may now have **:red[severe diabetes]** :disappointed_relieved:"\
    and result2 == "Your systolic blood pressure data shows that you are currently suffering from **:orange[high blood pressure]** :disappointed:"\
    and result == "Your BMI data shows that you are severely **:red[severe obese]** :isappointed_relieved:":
    result4 = "You now need to go to a Grade II and above hospital in time :exclamation:"
else:
    result4 = "You can choose to go to Grade II and below hospitals in your free time for daily physical examination :flushed:"
st.divider()

# 显示结果
st.write(result)
st.write(result2)
st.write(result3)
st.write(result4)
st.divider()'''
        st.code(code,language='python')
