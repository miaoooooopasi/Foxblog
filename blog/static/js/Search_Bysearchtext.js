$(document).ready(function(){
  $("#button_search").click(function(){
      var baseUrl = 'http://127.0.0.1:5000/home/search'
      var text=$("#search_text").val()
      var finalUrl = baseUrl + '?text='+ text
      alert("值为: " + $("#search_text").val());
      alert(":"+finalUrl)
      window.location.href=finalUrl
      //window.location.href="https://www.baidu.com"
  });
});