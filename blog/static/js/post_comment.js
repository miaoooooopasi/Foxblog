function post_comment(){

      var easy_id = $("#easy_id").val()
      var comment = $("#comment").val()
      //var email = $("#email").val()
      alert(comment);
      alert(easy_id)


      var data={
        'comment':comment,
    }

    $.ajax({
        type:'POST',
        url:'/home/postcoment',
        dataType:'json',//希望服务器返回json格式的数据
        data:data,
        success:function(data){
                if (data.type='ok')
                    {
                        alert('提交评论成功!')
                        window.location.href="http://127.0.0.1:5000/home/easy/"+easy_id;
                    }
                else if (data.type='erro') 
                    {
                        alert("提交评论失败！")
                     }
         },
         error:function() {
             alert("Ajax方法失败error");
         }
        });

    }

