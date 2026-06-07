// Global state
let sessionId = null;
let currentQuestionIndex = 0;
let totalQuestions = 0;

// API base URL
const API_BASE = '/api';

// Screen switching
function showScreen(screenName) {
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });
    document.getElementById(screenName).classList.add('active');
}

// Start Interview
async function startInterview() {
    try {
        showLoadingState(true);
        const response = await fetch(`${API_BASE}/interview/start`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        
        if (!response.ok) throw new Error('Failed to start interview');
        
        const data = await response.json();
        sessionId = data.session_id;
        totalQuestions = data.total_questions;
        currentQuestionIndex = 0;
        
        showScreen('interviewScreen');
        await loadQuestion();
        showLoadingState(false);
    } catch (error) {
        console.error('Error starting interview:', error);
        alert('Failed to start interview. Please try again.');
        showLoadingState(false);
    }
}

// Load Question
async function loadQuestion() {
    try {
        const response = await fetch(`${API_BASE}/interview/${sessionId}/question`);
        if (!response.ok) throw new Error('Failed to load question');
        
        const data = await response.json();
        
        if (data.completed) {
            await getFeedback();
            return;
        }
        
        document.getElementById('questionText').textContent = data.question;
        document.getElementById('questionCount').textContent = `Question ${data.question_number} of ${totalQuestions}`;
        document.getElementById('answerText').value = '';
        
        // Update progress bar
        const progress = (data.question_number / totalQuestions) * 100;
        document.getElementById('progressFill').style.width = progress + '%';
    } catch (error) {
        console.error('Error loading question:', error);
        alert('Failed to load question. Please try again.');
    }
}

// Submit Answer
async function submitAnswer() {
    const answer = document.getElementById('answerText').value.trim();
    
    if (!answer) {
        alert('Please enter an answer before submitting.');
        return;
    }
    
    if (answer.length < 10) {
        alert('Please provide a more detailed answer (at least 10 characters).');
        return;
    }
    
    try {
        showLoadingState(true);
        
        const question = document.getElementById('questionText').textContent;
        const response = await fetch(`${API_BASE}/interview/${sessionId}/evaluate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                question: question,
                answer: answer
            })
        });
        
        if (!response.ok) throw new Error('Failed to evaluate answer');
        
        const data = await response.json();
        
        // Display evaluation
        document.getElementById('evaluationText').innerHTML = `
            <h4>Evaluation</h4>
            <p>${data.evaluation.replace(/\n/g, '<br>')}</p>
        `;
        
        document.getElementById('followupText').innerHTML = `
            <h4>Follow-up Question</h4>
            <p>${data.followup_question.replace(/\n/g, '<br>')}</p>
        `;
        
        showScreen('evaluationScreen');
        showLoadingState(false);
    } catch (error) {
        console.error('Error evaluating answer:', error);
        alert('Failed to evaluate answer. Please try again.');
        showLoadingState(false);
    }
}

// Next Question
async function nextQuestion() {
    try {
        showLoadingState(true);
        await loadQuestion();
        showScreen('interviewScreen');
        showLoadingState(false);
    } catch (error) {
        console.error('Error loading next question:', error);
        alert('Failed to load next question. Please try again.');
        showLoadingState(false);
    }
}

// Get Feedback
async function getFeedback() {
    try {
        showLoadingState(true);
        
        const response = await fetch(`${API_BASE}/interview/${sessionId}/feedback`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        
        if (!response.ok) throw new Error('Failed to get feedback');
        
        const data = await response.json();
        
        // Display feedback
        document.getElementById('finalScore').textContent = data.total_score;
        document.getElementById('feedbackText').innerHTML = `
            <p>${data.feedback.replace(/\n/g, '<br>')}</p>
        `;
        
        showScreen('feedbackScreen');
        showLoadingState(false);
    } catch (error) {
        console.error('Error getting feedback:', error);
        alert('Failed to get feedback. Please try again.');
        showLoadingState(false);
    }
}

// Download Report
function downloadReport() {
    const score = document.getElementById('finalScore').textContent;
    const feedback = document.getElementById('feedbackText').innerText;
    
    const content = `
AI INTERVIEW AGENT - FEEDBACK REPORT
=====================================

Session ID: ${sessionId}
Final Score: ${score}

FEEDBACK:
${feedback}

Generated: ${new Date().toLocaleString()}
    `;
    
    const element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(content));
    element.setAttribute('download', `interview_report_${sessionId}.txt`);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

// Restart Interview
function restartInterview() {
    sessionId = null;
    currentQuestionIndex = 0;
    totalQuestions = 0;
    showScreen('startScreen');
}

// Cancel Interview
function cancelInterview() {
    if (confirm('Are you sure you want to cancel the interview?')) {
        restartInterview();
    }
}

// Loading state
function showLoadingState(isLoading) {
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(btn => {
        if (isLoading) {
            btn.classList.add('loading');
            btn.disabled = true;
        } else {
            btn.classList.remove('loading');
            btn.disabled = false;
        }
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('AI Interview Agent loaded successfully');
});
