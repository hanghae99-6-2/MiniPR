<!doctype html>
<html lang="en">
    <head>
        <!-- Webpage Title -->
        <title>login | 차좀타볼카 </title>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <!-- Bulma CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css">
        <!-- Font Awesome CSS -->
        <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link href="https://fonts.googleapis.com/css2?family=Hahmlet:wght@500&display=swap" rel="stylesheet">

        <!-- JS -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.js"></script>

        <style>
            * {
                font-family: 'Hahmlet', serif;
            }


            body {
                height: 100vh;
                background-image: linear-gradient(0deg, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("https://cphoto.asiae.co.kr/listimglink/9/2022030713315569250_1646627515.jpg");
                background-repeat: no-repeat;
                background-size: cover;
            }

            .button.is-sparta {
                background-color: royalblue;
                border-color: transparent;
                color: #fff !important;
            }

            .button.is-sparta.is-outlined {
                background-color: transparent;
                border-color: royalblue;
                color: royalblue !important;
            }


        </style>

        <script>
            function sign_in() {
                let username = $("#input-username").val()              // id값을 읽어옴.
                let password = $("#input-password").val()              // pw값을 읽어옴.

                if (username == "") {
                    $("#help-id-login").text("아이디를 입력해주세요.")     // 아이디의 값들이 빈 값인지 아닌지 검사. -> ""(아이디 창이 비어 있으면) text를 보여줌.
                    $("#input-username").focus()
                    return;
                } else {
                    $("#help-id-login").text("")
                }

                if (password == "") {
                    $("#help-password-login").text("비밀번호를 입력해주세요.")   // 비밀번호의 값들이 빈 값인지 아닌지 검사. -> ""(pw 창이 비어 있으면) text를 보여줌.
                    $("#input-password").focus()
                    return;
                } else {
                    $("#help-password-login").text("")
                }
                $.ajax({
                    type: "POST",
                    url: "/login",
                    data: {
                        username_give: username,
                        password_give: password
                    },
                    success: function (response) {
                        if (response['result'] == 'success') {                         // 검증을 통과했다면 서버는 토큰을 발행해줌. 토큰에는 검증받는 사람의 아이디, 접속 유효 시간이 포함되어 있음.
                            $.cookie('mytoken', response['token'], {path: '/'});       //토큰을 받아서 브라우저에 쿠키를 저장! 쿠키에는 key value 형태로 값을 저장! 요청을 받을 때마다 쿠키가 계속 딸려감.
                            window.location.replace("/main")
                        } else {
                            alert(response['msg'])
                        }
                    }
                });
            }
        </script>

    </head>
    <body>
    <section class="section">
        <div class="container">
            <div class="box" style="min-width: 480px; max-width: 600px; margin: 20vh 0 30vh 90vh;">
                <article class="media">
                    <div class="media-content">
                        <div class="content">
                            <div class="field has-addons">
                                <div class="control has-icons-left" style="width:100%">
                                    <input id="input-username" class="input" type="text" placeholder="아이디">
                                    <span class="icon is-small is-left"><i class="fa fa-user"></i></span>
                                </div>
                                <div id="btn-check-dup" class="control">
                                </div>
                            </div>

                            <div class="field">
                                <div class="control has-icons-left">
                                    <input id="input-password" class="input" type="password" placeholder="비밀번호">
                                    <span class="icon is-small is-left"><i class="fa fa-lock"></i></span>
                                </div>
                            </div>


                        </div>
                        <div id="div-sign-in-or-up" class="has-text-centered">
                            <nav class="level is-mobile">
                                <button class="level-item button is-sparta" onclick="sign_in()">
                                    로그인
                                </button>
                            </nav>
                            <hr>
                            <h4 class="mb-3">아직 회원이 아니시라구요? </h4>
                            <nav class="level is-mobile">

                                <button class="level-item button is-sparta is-outlined">
                                    회원가입하기
                                </button>
                            </nav>
                        </div>
                    </div>
                </article>
            </div>
        </div>
    </section>
    </body>
</html>
