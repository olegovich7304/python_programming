var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        // Находим родительский пост
        var post = e.target.closest('.one-post');
        // Переключаем класс folded у поста
        post.classList.toggle('folded');
        // Меняем текст кнопки в зависимости от состояния
        e.target.textContent = post.classList.contains('folded') ? 'развернуть' : 'свернуть';
    });
}