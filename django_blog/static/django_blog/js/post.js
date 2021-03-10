$('.like-bar a').click(function (e) {
    $icon = $(this).find('i').toggleClass('fas text-danger')
    let likeCount = $(this).parent().find('p')
    if ($icon.hasClass('fas')) {
        likeCount.html(parseInt(likeCount.text()) + 1)
    } else {
        likeCount.html(parseInt(likeCount.text()) - 1)
    }
})

$('#commentForm').submit(function (event) {
    event.preventDefault()
    const postId = $(this).attr('data-post-id')
    const commentText = $(this).find('textarea.form-control')
    const csrf = $(this).find('input[name=csrfmiddlewaretoken]')
    const $submitBtn = $(this).find('button:submit')
    $.ajax({
        accepts: {
            "json": 'application/json'
        },
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/comment/add',
        data: {
            "csrfmiddlewaretoken": csrf.val(),
            "text": commentText.val(),
            "post": postId
        },
    })
        .done(function () {
            commentText.val('')
            $submitBtn.attr('disabled', true)
        })
        .fail(function () {

        })
})
