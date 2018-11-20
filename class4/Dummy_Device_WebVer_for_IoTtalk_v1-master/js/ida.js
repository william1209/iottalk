 $(function () {
     csmapi.set_endpoint('http://140.113.199.186:9999');
     var profile = {
         'dm_name': 'test75',
         'idf_list': [Dummy_Sensor],
         'odf_list': [test75],
     };

     function Dummy_Sensor() {
         return Math.random();
     }

     function test75(data) {
         if (data[0] != 0) $('.ODF_value')[0].innerText = data[0];
         else $('.ODF_value')[0].innerText = " ";

     }

     /*******************************************************************/
     function ida_init() {}
     var ida = {
         'ida_init': ida_init,
     };
     dai(profile, ida);
 });