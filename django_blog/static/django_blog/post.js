$('.like-bar a').click(function (e) {
    $icon = $(this).find('i').toggleClass('fas text-danger')
    let likeCount = $(this).parent().find('p')
    if ($icon.hasClass('fas')) {
        likeCount.html(parseInt(likeCount.text()) + 1)
    } else {
        likeCount.html(parseInt(likeCount.text()) - 1)
    }
})
