$(document).ready(function () {
    comment_container();
    data_post();    
})

function comment_container(){
    document.getElementById("comment_container").style.overflowY = "auto";
}

function index_post() {
    index = $('#db_index').text();
    
    $.ajax({
        type: "POST",
        url: "/community/comment_post",
        data: {index_give : index},
        success: function (response) {
        }
    });
}

function comment_post() {
    let comment_input = $('#comment_give').val();

    $.ajax({
        type: "POST",
        url: "/community/comment_post",
        data: {comment_give : comment_input},
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    });
}

function data_post(){

    $.ajax({
            type: "GET" ,
            url: "/community/post",
            data: {},
            success: function(response) {
                let temp_html =``

                let card = response['data_page']
                console.log(card)

                for(let i = 0 ; i < card.length ; i++){
                    let name = card[i]['comment']['username']
                    let email = card[i]['email']
                    let now = card[i]['now']
                    let comment = card[i]['comment']
                    let temp_html = `<article class="media">
                                            <div class="media-content">
                                                <div class="content">
                                                    <p>
                                                        <strong>${name}</strong> <small>${email}</small> <small>${now}</small>
                                                        <br>
                                                        ${comment}
                                                    </p>
                                                </div>
                                                <nav class="level is-mobile">
                                                    <div class="level-left">
                                                        <a class="level-item">
                                                            <span class="icon is-small"><i class="fas fa-reply"></i></span>
                                                        </a>
                                                        <a class="level-item">
                                                            <span class="icon is-small"><i class="fas fa-retweet"></i></span>
                                                        </a>
                                                        <a class="level-item">
                                                            <span class="icon is-small"><i class="fas fa-heart"></i></span>
                                                        </a>
                                                    </div>
                                                </nav>
                                            </div>
                                            <div class="media-right">
                                                <button class="delete"></button>
                                            </div>
                                        </article>
                                        `
                $('#comment_container').append(temp_html)
                }
        }
    });
}

