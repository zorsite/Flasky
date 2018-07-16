//使用jquery的ajax方法执行异步 HTTP (Ajax) 请求。
$(document).ready(function () {//等待jquery全部加载完毕
    htmlobj = $.ajax({
        url: "/getData",//要访问的地址
        type: "get",//请求方式
        dataType: "json",//预期服务器返回的数据类型
        contentType: "application/json",//发送信息至服务器时内容编码类型
        success: function (res) {//当请求成功之后调用，传入返回后的数据
            showChart('firstchart', res);//调用showChart函数
        },
        error: function (xhr, err, exception) {
            console.log(err);
            //$("#msg").html(err);
        }
    });
});

function showChart(divId, res) {//定义showChart函数,有两个参数，参数1是存放图表的divid，参数2是图标的数据
    var myChart = echarts.init(document.getElementById(divId));//对传递过来的divId参数进行图表初始化，并赋值给myChart变量。
    option = {//设置图表各参数
        animation: false,
        title:{text:'右臂翻转力量',textStyle:{fontSize:12}},
        tooltip:{},
        legend:{show:true, right: 10,top:20,right:40,orient: 'vertical',textStyle:{fontSize:12},data:[{name:'右手',icon:'line'}]},
        //图例一定要等于series中的某个name
        xAxis:{min:0,max:5,type: 'value'},
        yAxis:{min:0},
        series:[{name:'右手',type:'line',smooth: true,data:res}]
    };
    myChart.setOption(option);//myChart图标对象根据定义好的option进行设置
}