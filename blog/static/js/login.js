function login() {
    var username=$(" #username").val()
    var password=$(" #password").val()
    var data={
        'username':username,
        'password':password
    }
    $.ajax({
        type:'POST',
        url:'/administrator/admin_login',
        dataType:'json',//希望服务器返回json格式的数据
        data:data,
        success:function(data){
                if (data.result==1)
                    {
                        window.location.href="http://127.0.0.1:5000/admin/";
                    }
                else
                    {
                        alert("账号或密码错误！")
                     }
         }
        });

    }

