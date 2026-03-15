var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var post = e.target.closest('.one-post'); // находим родительский пост
        post.classList.toggle('folded');           // переключаем класс свёрнутости
        // меняем текст кнопки в зависимости от состояния
        e.target.textContent = post.classList.contains('folded') ? 'развернуть' : 'свернуть';
    });
}