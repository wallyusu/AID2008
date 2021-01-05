(function() { 
var fs = document.createElement("script"); 
fs.src = "//fe.faisys.com/jssdk_1_1/js/hawkEye.min.js?v=202011271721"; 
fs.id = "faiHawkEye"; 
window.FAI_HAWK_EYE = {}; 
window.FAI_HAWK_EYE.jssdk_report_url = "//report.fkw.com/js/report"; 
window.FAI_HAWK_EYE.jssdk_appid = 3010; 
window.FAI_HAWK_EYE.fai_is_oem = 0; 
window.FAI_HAWK_EYE.fai_aid = 26015186; 
window.FAI_HAWK_EYE.fai_bs_aid = 26015186; 
window.FAI_HAWK_EYE.fai_bs_id = 0; 
window.FAI_HAWK_EYE.fai_bs_wid = 0; 
window.FAI_HAWK_EYE.fai_web_name = "site-2"; 
var s = document.getElementsByTagName("script")[0]; 
s.parentNode.insertBefore(fs, s);
})()