const questions = [
    {
        question: "هل تعتبر الرسالة التي تطلب منك كلمة المرور آمنة؟",
        options: ["نعم", "لا"],
        answer: "لا"
    },
    {
        question: "إذا استلمت رسالة من جهة تدعي أنها البنك وتطلب بياناتك، ما الذي تفعله؟",
        options: ["أرسل المعلومات المطلوبة", "اتصل بالبنك للتحقق"],
        answer: "اتصل بالبنك للتحقق"
    }
];

function loadQuiz() {
    const quizContainer = document.getElementById("quiz-container");
    questions.forEach((q, index) => {
        const questionDiv = document.createElement("div");
        questionDiv.classList.add("question");
        questionDiv.innerHTML = `
            <h3>${index + 1}. ${q.question}</h3>
            ${q.options.map((option, i) => `
                <label>
                    <input type="radio" name="question${index}" value="${option}">
                    ${option}
                </label><br>
            `).join('')}
        `;
        quizContainer.appendChild(questionDiv);
    });
}

function submitQuiz() {
    let score = 0;
    questions.forEach((q, index) => {
        const answer = document.querySelector(`input[name="question${index}"]:checked`);
        if (answer && answer.value === q.answer) {
            score++;
        }
    });
    document.getElementById("result").innerText = `نتيجتك: ${score} من ${questions.length}`;
}

loadQuiz();
