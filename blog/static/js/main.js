/* 
    {% comment %} //creating an instance of the HTTP request object 
    var xmlHttp = new XMLHttpRequest();

    //specify the method and the url
    xmlHttp.open("GET", "http://127.0.0.1:8000/api/{{post.id}}/", false)
    
    xmlHttp.send(null);

    var json_obj = JSON.parse(xmlHttp.responseText)

    console.log(json_obj);

    var card_element = document.getElementById('content');
    var comment_cnt = document.getElementById('comment_count');

    card_element.innerHTML = "";
    comment_cnt.innerHTML = "{{number_of_commments}}";
    for (i=0; i<json_obj.length; i++)
    {                   
        card_element.innerHTML += "<div class='media d-block d-md-flex mt-3'><img style='width:100px;' class='d-flex mb-3 mx-auto' src='https://mdbootstrap.com/img/Photos/Avatars/img (30).jpg' alt='Generic placeholder image'><div class='media-body text-center text-md-left ml-md-3 ml-0'><h5 class='mt-0 font-weight-bold'>" + json_obj[i].author + "</h5><p>" + json_obj[i].body + "</p></div><p class='blockquote-footer'>" + json_obj[i].created_on + "</p></div>";
        //console.log(json_obj[i].author);
        //console.log(json_obj[i].body);
        //console.log(json_obj[i].created_on);
    } {% endcomment %}
*/