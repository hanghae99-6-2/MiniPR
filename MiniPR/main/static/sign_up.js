// 회원 가입 클라이언트
function sign_up() {
    let username = $("#input-username").val()
    let password = $("#input-password").val()
    let password2 = $("#input-password2").val()
    console.log(username, password, password2)


    if ($("#help-id").hasClass("is-danger")) {                    //아이디 중복 확인에서 막히면
        alert("아이디를 다시 확인해주세요.")
        return;
    } else if (!$("#help-id").hasClass("is-success")) {           //아이디 중복 확인을 통과하면
        alert("아이디 중복확인을 해주세요.")
        return;
    }

    if (password == "") {                           //비밀번호 입력 했는지 검사
        $("#help-password").text("비밀번호를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-password").focus()
        return;
    } else if (!is_password(password)) {                //정규식 검사
        $("#help-password").text("비밀번호의 형식을 확인해주세요. 영문과 숫자 필수 포함, 특수문자(!@#$%^&*) 사용가능 8-20자").removeClass("is-safe").addClass("is-danger")
        $("#input-password").focus()
        return
    } else {
        $("#help-password").text("사용할 수 있는 비밀번호입니다.").removeClass("is-danger").addClass("is-success")
    }
    if (password2 == "") {                                          //패스워드 확인 입력 했는지 검사
        $("#help-password2").text("비밀번호를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-password2").focus()
        return;
    } else if (password2 != password) {                             //패스워드 1과 같은지 검사
        $("#help-password2").text("비밀번호가 일치하지 않습니다.").removeClass("is-safe").addClass("is-danger")
        $("#input-password2").focus()
        return;
    } else {
        $("#help-password2").text("비밀번호가 일치합니다.").removeClass("is-danger").addClass("is-success")
    }                                       //통과한다면 서버로 POST
    $.ajax({
        type: "POST",
        url: "/sign_up/save",
        data: {
            username_give: username,
            password_give: password
        },
        success: function (response) {
            alert("회원가입을 축하드립니다!")
            window.location.replace("/login")
        }
    });

}

//jQuery toggleClass()
function toggle_sign_up() {
    $("#sign-up-box").toggleClass("is-hidden")
    $("#div-sign-in-or-up").toggleClass("is-hidden")
    $("#btn-check-dup").toggleClass("is-hidden")
    $("#help-id").toggleClass("is-hidden")
    $("#help-password").toggleClass("is-hidden")
    $("#help-password2").toggleClass("is-hidden")
}

//아이디, 패스워드 정규표현식
function is_nickname(asValue) {
    var regExp = /^(?=.*[a-zA-Z])[-a-zA-Z0-9_.]{2,10}$/;
    return regExp.test(asValue);
}

function is_password(asValue) {
    //()안에 내용은 필수 포함//'\d'는 숫자를 의미함//
    var regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;
    return regExp.test(asValue);
}

//아이디 중복확인 클라이언트
function check_dup() {
    let username = $("#input-username").val()
    console.log(username)
    if (username == "") {                //중복 확인 버튼을 눌렀는데 아무 것도 입력 하지 않았을 때
        $("#help-id").text("아이디를 입력해주세요.").removeClass("is-safe").addClass("is-danger") //help-id에 텍스트 입력
        $("#input-username").focus()
        return;
    }
    if (!is_nickname(username)) {                 //중복 확인 버튼을 눌렀는데 형식이 맞지 않았을 때
        $("#help-id").text("아이디의 형식을 확인해주세요. 영문과 숫자, 일부 특수문자(._-) 사용 가능. 2-10자 길이").removeClass("is-safe").addClass("is-danger")
        $("#input-username").focus()
        return;
    }
    $("#help-id").addClass("is-loading")                     //정상적으로 중복 확인 버튼을 눌렀을 때
    $.ajax({
        type: "POST",
        url: "/sign_up/check_dup",
        data: {
            username_give: username
        },
        success: function (response) {

            if (response["exists"]) {
                $("#help-id").text("이미 존재하는 아이디입니다.").removeClass("is-safe").addClass("is-danger")
                $("#input-username").focus()
            } else {
                $("#help-id").text("사용할 수 있는 아이디입니다.").removeClass("is-danger").addClass("is-success")          //중복 확인 버튼을 정상적으로 통과 해야만 회원가입이 //
            }                                                                                                           //이루어 져야 하므로  .addClass("is-success") 추가//
            $("#help-id").removeClass("is-loading")

        }
    });
}

//아이디 중복확인 클라이언트
function check_dup_id() {
    let username = $("#input-username").val()
    console.log(username)
    if (username == "") {                //중복 확인 버튼을 눌렀는데 아무 것도 입력 하지 않았을 때
        $("#help-id").text("아이디를 입력해주세요.").removeClass("is-safe").addClass("is-danger") //help-id에 텍스트 입력
        $("#input-username").focus()
        return;
    }
    if (!is_nickname(username)) {                 //중복 확인 버튼을 눌렀는데 형식이 맞지 않았을 때
        $("#help-id").text("아이디의 형식을 확인해주세요. 영문과 숫자, 일부 특수문자(._-) 사용 가능. 2-10자 길이").removeClass("is-safe").addClass("is-danger")
        $("#input-username").focus()
        return;
    }
    $("#help-id").addClass("is-loading")                     //정상적으로 중복 확인 버튼을 눌렀을 때
    $.ajax({
        type: "POST",
        url: "/sign_up/check_dup_id",
        data: {
            username_give: username
        },
        success: function (response) {

            if (response["exists"]) {
                $("#help-id").text("이미 존재하는 아이디입니다.").removeClass("is-safe").addClass("is-danger")
                $("#input-username").focus()
            } else {
                $("#help-id").text("사용할 수 있는 아이디입니다.").removeClass("is-danger").addClass("is-success")          //중복 확인 버튼을 정상적으로 통과 해야만 회원가입이 //
            }                                                                                                           //이루어 져야 하므로  .addClass("is-success") 추가//
            $("#help-id").removeClass("is-loading")

        }
    });
}

//이메일 중복확인 클라이언트
function check_dup_email() {
    let email = $("#input-email").val()
    console.log(email)
    if (email == "") {                //중복 확인 버튼을 눌렀는데 아무 것도 입력 하지 않았을 때
        $("#help-email").text("이메일을 입력해주세요.").removeClass("is-safe").addClass("is-danger") //help-email에 텍스트 입력
        $("#input-email").focus()
        return;
    }
    if (!is_email(email)) {                 //중복 확인 버튼을 눌렀는데 형식이 맞지 않았을 때
        $("#help-email").text("이메일의 형식을 확인해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-email").focus()
        return;
    }
    $("#help-email").addClass("is-loading")                     //정상적으로 중복 확인 버튼을 눌렀을 때
    $.ajax({
        type: "POST",
        url: "/sign_up/check_dup_email",
        data: {
            email_give: email
        },
        success: function (response) {

            if (response["exists"]) {
                $("#help-email").text("이미 존재하는 이메일입니다.").removeClass("is-safe").addClass("is-danger")
                $("#input-email").focus()
            } else {
                $("#help-email").text("사용할 수 있는 이메일입니다.").removeClass("is-danger").addClass("is-success")          //중복 확인 버튼을 정상적으로 통과 해야만 회원가입이 //
            }                                                                                                           //이루어 져야 하므로  .addClass("is-success") 추가//
            $("#help-email").removeClass("is-loading")

        }
    });
}