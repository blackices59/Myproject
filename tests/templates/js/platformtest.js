$.get("/getProvince/", function (data) {
    for(var i = 0; i < data.provinces.length; i++){
        // # 循环遍历接收的含有所有省的列表
        $new = $("<option value="+data.provinces[i][0]+">"+data.provinces[i][1]+"</option>");
        // # 将该省份添加到前端的下拉列表中
        $("#province").append($new);
    }
});
// 由于要实现联动效果，所以当选择的省份发生改变，要将之前选择的市、县的下拉列表全部清空，再重新添加
$("#province").change(function () {
    $("#city").empty().append('<option value="">请选择城市</option>');
    $("#district").empty().append('<option value="">请选择区/县</option>');
    $.ajax({
        url: "/getCity/",
        type:'get',
        data:{
            "city_id":$(this).val()
        }
    }).done(function (data) {
        // # 将选择的当前省份的所有市循环添加到下拉列表中
        for(var i = 0;i < data.cities.length; i++){
            $new = $("<option value="+data.cities[i][0]+">"+data.cities[i][1]+"</option>");
            $("#city").append($new);
        }
    });
});
$("#city").change(function () {
    // # 同理，当选择的市发生改变时，清空之前选择的县
    $("#district").empty().append('<option value="">请选择区/县</option>');
    $.ajax({
        url:'/getDistrict/',
        type:'get',
        data:{
            "district_id":$(this).val()
        }
    }).done(function (data) {
        // # 重新循环添加当前市的所有县
        for(var i = 0;i < data.district.length; i++){
            $new = $("<option value="+data.district[i][0]+">"+data.district[i][1]+"</option>");
            $("#district").append($new);
        }
    });
});