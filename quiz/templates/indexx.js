let questions = JSON.parse(localStorage.getItem('questions')) || [];
let score = 0;

function displayQuiz() {
    const quizDiv = document.getElementById('quiz');
    questions.forEach((q, index) => {
        const div = document.createElement('div');
        div.classList.add('question');
        const questionText = document.createElement('p');
        questionText.textContent = `${index + 1}. ${q.question}`;
        div.appendChild(questionText);

        if (q.type === 'mcq') {
            q.options.forEach((option, optIndex) => {
                const label = document.createElement('label');
                label.textContent = option;
                const input = document.createElement('input');
                input.type = 'radio';
                input.name = `question${index}`;
                input.value = optIndex + 1;
                input.addEventListener('change', () => checkAnswer(index, optIndex + 1));
                div.appendChild(input);
                div.appendChild(label);
                div.appendChild(document.createElement('br'));
            });
        } else {
            const input = document.createElement('input');
            input.type = 'number';
            input.addEventListener('input', (e) => checkAnswer(index, parseInt(e.target.value)));
            div.appendChild(input);
        }
        quizDiv.appendChild(div);
    });
}

function checkAnswer(questionIndex, selectedAnswer) {
    const question = questions[questionIndex];
    if (question.type === 'mcq' && question.correctAnswer === selectedAnswer) {
        score++;
    } else if (question.type === 'numeric' && question.correctAnswer === selectedAnswer) {
        score++;
    }
    document.getElementById('score').textContent = score;
}

displayQuiz();
