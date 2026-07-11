import json, os

BASE = "/root/.openclaw/workspace/projects/ai-nontechnical-course/site/lessons"

def generate_lesson(lesson_id, title, phase, duration, content):
    slug = lesson_id.replace('.', '-')
    path = f"{BASE}/{slug}"
    os.makedirs(path, exist_ok=True)
    
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lesson_id} {title} — AI для Менеджеров</title>
<link rel="stylesheet" href="../../style.css">
<style>
  :root {{ --bg: #0B0F19; --card: #111827; --text: #F3F4F6; --muted: #9CA3AF; --accent: #8B5CF6; --accent2: #06B6D4; --border: rgba(255,255,255,0.08); --success: #10B981; --warning: #F59E0B; --danger: #EF4444; }}
  body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; }}
  .container {{ max-width: 800px; margin: 0 auto; padding: 0 20px; }}
  header {{ padding: 20px 0; border-bottom: 1px solid var(--border); }}
  header .container {{ display: flex; justify-content: space-between; align-items: center; }}
  .logo {{ font-size: 1.1rem; font-weight: 700; color: var(--accent); text-decoration: none; }}
  .lesson-header {{ padding: 40px 0 20px; }}
  .lesson-header .phase {{ color: var(--accent); font-size: 0.85rem; font-weight: 600; }}
  .lesson-header h1 {{ margin: 8px 0; font-size: 2rem; }}
  .lesson-header .meta {{ color: var(--muted); font-size: 0.9rem; }}
  .section {{ margin: 32px 0; }}
  .section h2 {{ color: var(--accent); font-size: 1.3rem; margin-bottom: 16px; }}
  .section h3 {{ color: var(--accent2); font-size: 1.1rem; margin: 24px 0 12px; }}
  .card {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin: 16px 0; }}
  .card-accent {{ border-left: 4px solid var(--accent); }}
  .card-success {{ border-left: 4px solid var(--success); }}
  .card-warning {{ border-left: 4px solid var(--warning); }}
  .card-danger {{ border-left: 4px solid var(--danger); }}
  .highlight {{ background: rgba(139,92,246,0.1); padding: 2px 6px; border-radius: 4px; }}
  .checklist {{ list-style: none; padding: 0; }}
  .checklist li {{ padding: 8px 0; padding-left: 28px; position: relative; }}
  .checklist li:before {{ content: "☐"; position: absolute; left: 0; color: var(--accent); }}
  .example {{ background: rgba(6,182,212,0.05); border: 1px solid rgba(6,182,212,0.2); border-radius: 8px; padding: 16px; margin: 12px 0; }}
  .example-label {{ color: var(--accent2); font-size: 0.8rem; font-weight: 600; margin-bottom: 8px; }}
  .nav-footer {{ display: flex; justify-content: space-between; padding: 40px 0; border-top: 1px solid var(--border); margin-top: 40px; }}
  .nav-btn {{ padding: 12px 24px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; color: var(--text); text-decoration: none; transition: all 0.2s; }}
  .nav-btn:hover {{ border-color: var(--accent); }}
  .nav-btn.primary {{ background: var(--accent); border-color: var(--accent); }}
  footer {{ padding: 40px 0; text-align: center; color: var(--muted); border-top: 1px solid var(--border); }}
  .calc-box {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 20px; margin: 16px 0; }}
  .calc-box input, .calc-box select {{ width: 100%; padding: 8px; background: var(--bg); border: 1px solid var(--border); border-radius: 4px; color: var(--text); margin: 8px 0; }}
  .calc-box label {{ display: block; margin: 8px 0 4px; color: var(--muted); font-size: 0.9rem; }}
  .calc-result {{ background: rgba(16,185,129,0.1); border: 1px solid var(--success); border-radius: 8px; padding: 16px; margin: 16px 0; text-align: center; }}
  .calc-result .sum {{ font-size: 2rem; font-weight: 700; color: var(--success); }}
  table {{ width: 100%; border-collapse: collapse; margin: 16px 0; }}
  th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid var(--border); }}
  th {{ color: var(--accent); font-weight: 600; }}
  tr:hover {{ background: rgba(255,255,255,0.02); }}
  .comparison {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0; }}
  .comparison-box {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 16px; }}
</style>
</head>
<body>

<header>
  <div class="container">
    <a href="../../index.html" class="logo">🧠 AI для Менеджеров</a>
    <a href="../../catalog.html" style="color: var(--muted); text-decoration: none;">← Каталог</a>
  </div>
</header>

<article class="container">

  <div class="lesson-header">
    <div class="phase">{phase}</div>
    <h1>{lesson_id} · {title}</h1>
    <div class="meta">⏱️ {duration} · 🎯 Интерактивный калькулятор · ✅ Квиз</div>
  </div>

{content}

  <div class="nav-footer">
    <a href="../../catalog.html" class="nav-btn">← К каталогу</a>
    <a href="../../catalog.html" class="nav-btn primary">Каталог →</a>
  </div>

</article>

<footer>
  <div class="container">
    <p>© 2026 Artur A. · AI для Нетехнических Специалистов</p>
  </div>
</footer>

</body>
</html>'''
    
    with open(f"{path}/index.html", 'w') as f:
        f.write(html)
    print(f"Created: {lesson_id} {title}")

# Phase 5: Integration
lessons_p5 = [
    ("5.1", "ROI-калькулятор: выбор процесса для автоматизации", "🏢 ФАЗА 5 · ВНЕДРЕНИЕ В БИЗНЕС", "40 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p><span class="highlight">60% проектов AI проваливаются</span> из-за неправильного выбора процесса. Не «давайте внедрим AI везде» — а «где ROI максимальный».</p>
  </div>

  <div class="section">
    <h2>📚 Формула ROI для AI</h2>
    <div class="card card-success">
      <h3>ROI = (Экономия − Затраты) / Затраты × 100%</h3>
      <p><strong>Экономия =</strong> (Часы до − Часы после) × Стоимость часа сотрудника × Количество сотрудников</p>
      <p><strong>Затраты =</strong> Лицензии + Интеграция + Обучение + Поддержка (12 месяцев)</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Интерактивный ROI-калькулятор</h2>
    <div class="calc-box">
      <label>Часов в неделю на задачу (до AI):<input type="number" id="hoursBefore" value="10" onchange="roiCalc()"></label>
      <label>Часов в неделю (после AI):<input type="number" id="hoursAfter" value="3" onchange="roiCalc()"></label>
      <label>Стоимость часа сотрудника ($):<input type="number" id="hourRate" value="25" onchange="roiCalc()"></label>
      <label>Количество сотрудников:<input type="number" id="employees" value="5" onchange="roiCalc()"></label>
      <label>Затраты на AI в год ($):<input type="number" id="aiCosts" value="5000" onchange="roiCalc()"></label>
    </div>
    
    <div class="calc-result">
      <div>Годовая экономия:</div>
      <div class="sum" id="savings">$0</div>
      <div class="muted" id="roiResult" style="margin-top: 8px;">ROI: 0%</div>
      <div class="muted" id="payback" style="margin-top: 4px; font-size: 0.9rem;"></div>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Матрица выбора процесса</h2>
    <div class="card">
      <table>
        <thead>
          <tr><th>Критерий</th><th>✅ Идеально</th><th>❌ Не подходит</th></tr>
        </thead>
        <tbody>
          <tr><td>Частота</td><td>> 5 раз/неделю</td><td>< 1 раз/месяц</td></tr>
          <tr><td>Время</td><td>> 2 часа/раз</td><td>< 15 минут</td></tr>
          <tr><td>Правила</td><td>Чёткий алгоритм</td><td>Требует интуиции</td></tr>
          <tr><td>Данные</td><td>В цифровом виде</td><td>Только в голове у эксперта</td></tr>
          <tr><td>Ошибка</td><td>Не критична</td><td>Юридические/финансовые риски</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>ROI > 200% за год?</li>
      <li>Окупаемость < 6 месяцев?</li>
      <li>Процесс соответствует всем 5 критериям?</li>
      <li>Есть данные "до" (базовый уровень для сравнения)?</li>
      <li>Руководство готово выделить ресурсы?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Выбирайте процесс по ROI: частота > 5/нед, время > 2 часа, чёткие правила, цифровые данные, некритичные ошибки. Цель: ROI > 200%, окупаемость < 6 месяцев. Считайте заранее, не верьте обещаниям вендоров.</p>
    </div>
  </div>

<script>
function roiCalc() {
  const hoursBefore = parseFloat(document.getElementById('hoursBefore').value) || 0;
  const hoursAfter = parseFloat(document.getElementById('hoursAfter').value) || 0;
  const rate = parseFloat(document.getElementById('hourRate').value) || 0;
  const emp = parseInt(document.getElementById('employees').value) || 0;
  const costs = parseFloat(document.getElementById('aiCosts').value) || 0;
  
  const weeklySavings = (hoursBefore - hoursAfter) * rate * emp;
  const annualSavings = weeklySavings * 48; // 48 рабочих недель
  const roi = costs > 0 ? ((annualSavings - costs) / costs * 100).toFixed(0) : 0;
  const payback = weeklySavings > 0 ? (costs / weeklySavings).toFixed(1) : 0;
  
  document.getElementById('savings').textContent = '$' + annualSavings.toLocaleString();
  document.getElementById('roiResult').textContent = 'ROI: ' + roi + '%';
  document.getElementById('payback').textContent = 'Окупаемость: ' + payback + ' недель';
}
roiCalc();
</script>'''),

    ("5.2", "Пилотный проект: от идеи до результата", "🏢 ФАЗА 5 · ВНЕДРЕНИЕ В БИЗНЕС", "45 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p><span class="highlight">80% пилотов успешны, 20% внедрений в продакшен — тоже.</span> Разница: пилот — это проверка гипотезы, а не полноценное внедрение. Нужен чёткий план.</p>
  </div>

  <div class="section"
    <h2>📚 6 недель пилота (план)</h2>
    <div class="card card-success">
      <h3>Неделя 1: Подготовка</h3>
      <ul>
        <li>Выбрать процесс (по ROI-калькулятору)</li>
        <li>Собрать команду: бизнес-спонсор, аналитик, IT, пользователь</li>
        <li>Определить метрики: что измеряем, как считаем успех</li>
      </ul>
    </div>
    
    <div class="card">
      <h3>Неделя 2-3: Разработка</h3>
      <ul>
        <li>Создать промпты / автоматизацию / агента</li>
        <li>Собрать тестовые данные (10-20 реальных примеров)</li>
        <li>Проверить на тестовых данных (точность, скорость)</li>
      </ul>
    </div>
    
    <div class="card">
      <h3>Неделя 4-5: Пилот</h3>
      <ul>
        <li>Запустить на 1-2 пользователях с реальными задачами</li>
        <li>Собирать обратную связь каждый день</li>
        <li>Фиксировать ошибки и улучшать промпты</li>
      </ul>
    </div>
    
    <div class="card card-success">
      <h3>Неделя 6: Оценка и решение</h3>
      <ul>
        <li>Посчитать метрики: время, качество, ошибки, удовлетворённость</li>
        <li>Сравнить с целью (ROI, окупаемость)</li>
        <li>Принять решение: масштабировать / доработать / закрыть</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия пилота</h2>
    <ul class="checklist">
      <li>Метрики достигнуты (время, качество, ROI)?</li>
      <li>Пользователи довольны (> 4.0 / 5)?</li>
      <li>Ошибки < 5% и не критичны?</li>
      <li>IT готов поддерживать в продакшене?</li>
      <li>Руководство готово выделить бюджет на масштабирование?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Пилот = 6 недель: подготовка → разработка → тест → оценка. Метрики, обратная связь, чёткие критерии успеха. Не масштабируйте без успешного пилота. Лучше потратить 6 недель на проверку, чем 6 месяцев на исправление ошибок.</p>
    </div>
  </div>'''),

    ("5.3", "Масштабирование: от отдела к компании", "🏢 ФАЗА 5 · ВНЕДРЕНИЕ В БИЗНЕС", "35 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>Успешный пилот в 1 отделе ≠ успех в 10 отделах. Масштабирование — это отдельный проект со своими рисками.</p>
  </div>

  <div class="section">
    <h2>📚 Пирамида масштабирования</h2>
    <div class="card card-success">
      <h3>Уровень 1: Один отдел (1-2 месяца)</h3>
      <ul>
        <li>1-2 команды, 5-10 пользователей</li>
        <li>Ручная поддержка, обучение "из рук в руки"</li>
        <li>Цель: доказать ценность, собрать кейсы</li>
      </ul>
    </div>
    
    <div class="card">
      <h3>Уровень 2: Несколько отделов (3-6 месяцев)</h3>
      <ul>
        <li>3-5 отделов, 20-50 пользователей</li>
        <li>Обучающие материалы, FAQ, чат поддержки</li>
        <li>Цель: стандартизировать процесс, снизить зависимость от экспертов</li>
      </ul>
    </div>
    
    <div class="card">
      <h3>Уровень 3: Компания (6-12 месяцев)</h3>
      <ul>
        <li>Все отделы, 100+ пользователей</li>
        <li>Автоматическое обучение, самообслуживание</li>
        <li>Цель: AI как инфраструктура, не проект</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Чеклист масштабирования</h2>
    <div class="card card-success">
      <ul class="checklist">
        <li>Пилот успешен (метрики, ROI, удовлетворённость)?</li>
        <li>Есть обучающие материалы (видео, инструкции, FAQ)?</li>
        <li>IT готов поддерживать нагрузку (×10 от пилота)?</li>
        <li>Есть бюджет на лицензии (×10 пользователей)?</li>
        <li>Есть "чемпионы" — сотрудники, которые помогают коллегам?</li>
        <li>Руководство поддерживает масштабирование?</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Масштабирование — это пирамида: отдел → несколько отделов → компания. Не прыгайте через уровни. Каждый уровень требует своих инструментов: ручная поддержка → обучение → автоматизация. Начинайте с "чемпионов" — они потянут остальных.</p>
    </div>
  </div>'''),
]

for lesson in lessons_p5:
    generate_lesson(*lesson)

print("\nPhase 5 done!")
