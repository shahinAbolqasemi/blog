$('.modal-body form.input-group').submit(function (event) {
    event.preventDefault()
    const $myModal = $("#searchModal")
    const $inputText = $myModal.find('.modal-body .input-group input:text')
    $.ajax({
        accepts: {
            "json": 'application/json'
        },
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/search',
        data: {'search': $inputText.val()},
    })
        .done(function (data, status, resp) {
            let $postsList = $myModal.find('.modal-body .list-group')
            $postsList.html('')
            if (data) {
                data.forEach(function (post) {
                    const $postItemHtml = $('<li class="list-group-item list-group-item-action">' +
                        '<div class="d-flex w-100 justify-content-between">' +
                        '<a href="" class="text-decoration-none"><h5 class="mb-1">' + post.title + '</h5></a>' +
                        '<small>' + post.date_published + '</small>' +
                        '</div>' +
                        '<small class="mb-1">' + post.description + '</small>' +
                        '</li>')
                    $postsList.append($postItemHtml)
                })
            }
        })
        .fail(function (msg) {
            console.log(msg)
        });
});