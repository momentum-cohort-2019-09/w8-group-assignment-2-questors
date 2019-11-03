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

for (let answer_star of document.querySelectorAll('.answer-favorite')) {
    answer_star.addEventListener('click', event => {
        fetch(`/AnswerQuest/answer/${answer_star.dataset.answerpk}/starred/`, {
            method: 'POST',
        })
        if (answer_star.textContent == '☆') {
            answer_star.textContent = '★'
        } else {
            answer_star.textContent = '☆'
        }
    }
    )
}

let all_correct_buttons = document.querySelectorAll('.correct-answer')
for (let correct_button of all_correct_buttons) {
    correct_button.addEventListener('click', event => {
        fetch(`/AnswerQuest/answer/${correct_button.dataset.answerpk}/correct/`, {
            method: 'POST',
        })
        correct_button.parentElement.querySelector('.correct-answer').style.display = 'none'
        correct_button.parentElement.querySelector('.first-correct-mark').style.display = 'inline-block'

    })
}
