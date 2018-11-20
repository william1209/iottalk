
var xx=320,yy=240;

$(function () {
    csmapi.set_endpoint ('http://140.113.199.186:9999');
    var profile = {
        'dm_name': 'IOT1016',
        'idf_list': [],
        'odf_list': [IOT1016],
    }
    
    


    var r = 255 ;
    var g = 255;
    var b = 0;
    var lum = 100;

    function draw () {
        var rr = Math.floor((r * lum) / 100);
        var gg = Math.floor((g * lum) / 100);
        var bb = Math.floor((b * lum) / 100);
        $('.bulb-top, .bulb-middle-1, .bulb-middle-2, .bulb-middle-3, .bulb-bottom, .night').css(
            {'background': 'rgb('+ rr +', '+ gg +', '+ bb +')'}
        );
    }

    function IOT1016 (data) {
        lum = data[0]
        if(data!=0){
            xx = xx+data[1];
            yy = yy+data[2];
            console.log(xx+" "+yy);
            if(xx<0) xx=0;
            if(xx>640) xx=640;
            if(yy<0) yy=0;
            if(yy>480) yy=480;
        }
        //draw();
    }

    // function IOT1016 (data) {
    //     r = data[0];
    //     g = data[1];
    //     b = data[2];
    //     //draw();
    // }

    function ida_init () {
        $('font')[0].innerText = profile.d_name;
        draw();
    }

    var ida = {
        'ida_init': ida_init,
    };

    dai(profile, ida);
});
