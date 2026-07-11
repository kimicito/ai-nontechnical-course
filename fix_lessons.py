
import os, re, glob

BASE = '/root/.openclaw/workspace/projects/ai-nontechnical-course/site/lessons'

# 1. Fix all lesson files: remove time, update footer, update logo, fix quiz
for root, dirs, files in os.walk(BASE):
    for f in files:
        if f == 'index.html':
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
            
            # Remove ⏱️ XX minutes from meta
            content = re.sub(r'⏱️\s*\d+.*?·\s*', '', content)
            # Also handle variations without the dot
            content = re.sub(r'⏱️\s*\d+.*?минут\s*', '', content)
            
            # Update footer text
            content = content.replace('AI для Нетехнических Специалистов', 'AI для не ИТ-специалистов')
            content = content.replace('AI для Менеджеров', 'AI для не ИТ-специалистов')
            
            # Fix logo in header
            content = content.replace('🧠 AI для Менеджеров', '🧠 AI для не ИТ-специалистов')
            
            # Fix quiz: allow retry on wrong answer
            # Replace old quiz handler with new one that allows retry
            old_quiz = '''function checkAnswer(element, isCorrect) {
  const card = element.closest('.card');
  const options = card.querySelectorAll('.quiz-option');
  const resultDiv = card.querySelector('.result');
  
  options.forEach(opt => {
    opt.style.pointerEvents = 'none';
    if (opt === element) {
      opt.classList.add(isCorrect ? 'correct' : 'wrong');
    }
  });'''
            
            new_quiz = '''function checkAnswer(element, isCorrect) {
  const card = element.closest('.card');
  const options = card.querySelectorAll('.quiz-option');
  const resultDiv = card.querySelector('.result');
  
  if (isCorrect) {
    options.forEach(opt => {
      opt.style.pointerEvents = 'none';
      if (opt === element) opt.classList.add('correct');
      else opt.classList.add('disabled');
    });'''
            
            if old_quiz in content:
                content = content.replace(old_quiz, new_quiz)
                # Also update result text for wrong answer
                content = content.replace(
                    'resultDiv.innerHTML = \'<strong>❌ Не совсем.</strong> Подумайте ещё раз.\';',
                    "resultDiv.innerHTML = '<strong>⚠️ Не совсем. Попробуйте другой вариант.</strong>';"
                )
                # Add warning background for wrong answer
                content = content.replace(
                    "resultDiv.style.background = 'rgba(239,68,68,0.1)';\n    resultDiv.style.border = '1px solid var(--danger)';",
                    "resultDiv.style.background = 'rgba(245,158,11,0.1)';\n    resultDiv.style.border = '1px solid var(--warning)';"
                )
            
            # Add .disabled CSS if not present
            if '.disabled' not in content:
                content = content.replace(
                    '.quiz-option.wrong { border-color: var(--danger); background: rgba(239,68,68,0.1); }',
                    '.quiz-option.wrong { border-color: var(--danger); background: rgba(239,68,68,0.1); }\n  .quiz-option.disabled { opacity: 0.5; pointer-events: none; }'
                )
            
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(content)

print('All lessons updated!')
