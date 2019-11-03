add_answer = document.querySelector('#add-answer')
add_answer.addEventListener('click', event => {
    event.preventDefault()
    add_answer.style.display = 'none';
    document.getElementById('answer-form').style.display = 'block';
})

question_star = document.querySelector('.question-favorite')
question_star.addEventListener('click', event => {
    fetch(`/AnswerQuest/question/${question_star.dataset.questionpk}/starred/`, {
        method: 'POST',
    })
    if (question_star.textContent == '☆') {
        question_star.textContent = '★'
    } else {
        question_star.textContent = '☆'
    }
})

delete_question = document.querySelector('.delete_question')
delete_question.addEventListener('click', event => {
    if (!confirm('Are you sure you want to delete this question? This is permanent')) {
        event.preventDefault()
    }
})
