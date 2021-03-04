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
                        '<small>' + DateToCustomFormat(post.date_published) + '</small>' +
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

function DateToCustomFormat(dateStr) {
    const date = new Date(dateStr)
    const months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    const days = [
        'Sun',
        'Mon',
        'Tue',
        'Wed',
        'Thu',
        'Fri',
        'Sat'
    ]
    return `${days[date.getDay()]}, ${date.getDate()} ${months[date.getMonth()]} ${date.getFullYear()}, ${date.getHours()}:${date.getMinutes()}`
}