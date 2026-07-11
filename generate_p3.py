import json, os, textwrap

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
  .comparison-box h4 {{ margin: 0 0 12px; }}
  .tier {{ display: flex; align-items: center; gap: 16px; padding: 12px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; margin: 8px 0; }}
  .tier-price {{ font-size: 1.5rem; font-weight: 700; color: var(--accent); min-width: 100px; }}
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
    <div class="meta">⏱️ {duration} · 🎯 Без кода · ✅ Квиз в конце</div>
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

# Phase 3: Automation
lessons_p3 = [
    ("3.1", "No-code автоматизация: Make, n8n, Zapier", "⚡ ФАЗА 3 · АВТОМАТИЗАЦИЯ", "45 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p><span class="highlight">70% рутинных задач</span> можно автоматизировать без программирования. Создаёте "цепочки" в визуальном редакторе: "Если письмо от поставщика → извлеки цену → сравни с прошлой → отправь уведомление, если выросла > 10%".</p>
  </div>

  <div class="section">
    <h2>📚 Сравнение платформ</h2>
    <div class="comparison">
      <div class="comparison-box">
        <h4>🟠 Make (Integromat)</h4>
        <p style="color: var(--success);">✅ Визуальный drag-and-drop, 1000+ интеграций, сложные условия</p>
        <p style="color: var(--warning);">⚠️ От $9/мес, сложнее в освоении чем Zapier</p>
      </div>
      <div class="comparison-box">
        <h4>🔵 n8n</h4>
        <p style="color: var(--success);">✅ Open-source, self-hosted, бесплатно, мощные функции</p>
        <p style="color: var(--warning);">⚠️ Требует сервера для self-hosted, круче кривая обучения</p>
      </div>
      <div class="comparison-box">
        <h4>🟢 Zapier</h4>
        <p style="color: var(--success);">✅ Самый простой, 5000+ интеграций, отличная документация</p>
        <p style="color: var(--warning);">⚠️ Дороже ($20/мес), ограничения на бесплатном плане</p>
      </div>
      <div class="comparison-box">
        <h4>🟣 Microsoft Power Automate</h4>
        <p style="color: var(--success);">✅ Интеграция с Office 365, корпоративная поддержка</p>
        <p style="color: var(--warning);">⚠️ Требует лицензии, привязка к Microsoft</p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Пример автоматизации: сравнение цен поставщиков</h2>
    <div class="card card-success">
      <h3>Сценарий (Make/n8n)</h3>
      <ol>
        <li><strong>Триггер:</strong> Новое письмо от поставщика (Gmail / Outlook)</li>
        <li><strong>AI-шаг:</strong> Извлечь цену, товар, сроки из письма (ChatGPT API)</li>
        <li><strong>Проверка:</strong> Сравнить с прошлой ценой в Google Sheets / Excel</li>
        <li><strong>Условие:</strong> Если цена выросла > 10% → уведомление в Slack / Telegram</li>
        <li><strong>Действие:</strong> Записать новую цену в таблицу</li>
      </ol>
      <p><strong>Результат:</strong> Вы узнаёте о росте цен за 5 минут, а не через 3 дня.</p>
    </div>
  </div>

  <div class="section">
    <h2>👨‍💻 Как поставить задачу разработчику</h2>
    <div class="card card-success">
      <pre style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px;">
"Нужно автоматизировать процесс: [ОПИСАНИЕ].

Текущий процесс:
- [ШАГ 1] → [ШАГ 2] → [ШАГ 3]
- Время: [N] минут/раз
- Частота: [N] раз/день

Требования:
- Платформа: [Make / n8n / Zapier / Power Automate]
- Интеграции: [Gmail / Slack / 1C / Bitrix]
- AI-шаги: [извлечение данных / анализ / генерация]
- Уведомления: [Email / Slack / Telegram]
- Обработка ошибок: если AI не справился → человек

Прошу сделать POC за [N] дней."
      </pre>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Автоматизация работает без сбоев 7 дней подряд?</li>
      <li>Обработка ошибок: если AI не справился → уведомление человеку?</li>
      <li>Можно отключить автоматизацию за 1 клик (экстренный стоп)?</li>
      <li>Есть лог (кто, когда, что произошло)?</li>
      <li>Экономия времени > 50%?</li>
    </ul>
  </div>

  <div class="section">
    <h2>📝 Проверка понимания</h2>
    <div class="card card-accent">
      <p><strong>Вопрос 1:</strong> Какая платформа бесплатна для self-hosted?</p>
      <p><em>Ответ: n8n (open-source, ставится на свой сервер).</em></p>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</strong></h3>
      <p>No-code автоматизация (Make, n8n, Zapier) позволяет создавать бизнес-процессы без программирования. Стартуйте с простых сценариев, проверяйте 7 дней, потом усложняйте. ROI: 5-20 часов в месяц на сценарий.</p>
    </div>
  </div>'''),

    ("3.2", "Интеграция AI в процессы: чеклисты и шаблоны", "⚡ ФАЗА 3 · АВТОМАТИЗАЦИЯ", "40 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>AI — это не замена сотруднику, а <strong>усилитель</strong>. Ключевое слово — интеграция. Не "заменим менеджера на AI", а "менеджер + AI = в 3 раза быстрее".</p>
  </div>

  <div class="section">
    <h2>📚 Модели интеграции AI</h2>
    <div class="card">
      <h3>1. AI-ассистент (Copilot)</h3>
      <p>AI работает <strong>рядом</strong> с сотрудником. Предлагает варианты, но решение принимает человек.</p>
      <p><strong>Пример:</strong> AI предлагает 3 варианта ответа клиенту, менеджер выбирает и редактирует.</p>
    </div>
    <div class="card">
      <h3>2. AI-автоматизация (Autopilot)</h3>
      <p>AI выполняет задачу <strong>автоматически</strong>, человек только проверяет критичные случаи.</p>
      <p><strong>Пример:</strong> AI проверяет 100 договоров на риски, юрист проверяет только помеченные "высокий риск".</p>
    </div>
    <div class="card">
      <h3>3. AI-агент (Agent)</h3>
      <p>AI выполняет задачу <strong>целиком</strong>, но с "человеком в цикле" для одобрения.</p>
      <p><strong>Пример:</strong> AI готовит заказ поставщику, но отправляет только после approve менеджера.</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Чеклист интеграции AI</h2>
    <div class="card card-success">
      <ul class="checklist">
        <li>Задача повторяется > 3 раз в неделю?</li>
        <li>Есть чёткие правила (можно описать алгоритм)?</li>
        <li>Результат можно проверить (не требует экспертизы)?</li>
        <li>Ошибка AI не критична (можно исправить)?</li>
        <li>Есть человек, который проверит результат?</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Сотрудники используют AI > 80% случаев?</li>
      <li>Время задачи сократилось > 50%?</li>
      <li>Ошибок AI < 5%? (проверяется по выборке)</li>
      <li>Есть процесс обратной связи (сотрудник может пожаловаться)?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>AI = усилитель, не замена. Начинайте с Copilot (помощник), переходите к Autopilot (автоматизация) только после проверки. Всегда оставляйте "человека в цикле" для критичных решений.</p>
    </div>
  </div>'''),

    ("3.3", "Простые агенты без кода", "⚡ ФАЗА 3 · АВТОМАТИЗАЦИЯ", "45 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p><strong>AI-агент</strong> = программа, которая сама выполняет задачи, используя AI. Без кода — через визуальные конструкторы.</p>
  </div>

  <div class="section">
    <h2>📚 Что такое агент (простыми словами)</h2>
    <div class="example">
      <div class="example-label">💡 АНАЛОГИЯ</div>
      <p><strong>Агент = виртуальный стажёр с инструкцией.</strong> Вы даёте ему задачу: "Каждое утро проверяй почту, находи письма от поставщиков, извлекай цены, сравнивай с прошлой, если выросла > 10% — пиши мне в Telegram". Агент делает это сам.</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Платформы для создания агентов без кода</h2>
    <div class="card">
      <ul>
        <li><strong>Relevance AI</strong> — визуальный конструктор агентов, интеграции с 50+ сервисами</li>
        <li><strong>MindStudio</strong> — no-code агенты для бизнеса, шаблоны под задачи</li>
        <li><strong>AgentGPT (локальный)</strong> — open-source, ставится на сервер, данные не уходят в облако</li>
        <li><strong>Dify</strong> — open-source, удобный интерфейс, self-hosted</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Пример: агент для закупок</h2>
    <div class="card card-success">
      <h3>Задача агента:</h3>
      <ol>
        <li>Каждое утро в 9:00 проверять email на письма от поставщиков</li>
        <li>Извлекать: товар, цена, сроки, условия</li>
        <li>Сравнивать с текущими ценами в таблице</li>
        <li>Если цена выросла > 10% → отправить уведомление в Telegram + email</li>
        <li>Если цена снизилась > 5% → предложить пересмотр контракта</li>
        <li>В 18:00 отправлять сводку за день в Slack</li>
      </ol>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Агент работает стабильно 7 дней без сбоев?</li>
      <li>Уведомления приходят вовремя?</li>
      <li>Ошибки < 5%? (проверьте 20 случаев)</li>
      <li>Можно остановить/изменить за 5 минут?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>AI-агенты без кода — это реальность. Relevance AI, MindStudio, Dify позволяют создавать автономных помощников за часы, а не месяцы. Начните с одного простого агента, проверьте 1 неделю, потом добавляйте сложность.</p>
    </div>
  </div>'''),

    ("3.4", "Мониторинг и качество: как проверить результат", "⚡ ФАЗА 3 · АВТОМАТИЗАЦИЯ", "40 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>AI ошибается. Без мониторинга ошибка может стоить миллионы. Нужно <strong>измерять качество</strong> и <strong>улучшать процесс</strong>.</p>
  </div>

  <div class="section">
    <h2>📚 Метрики качества AI</h2>
    <div class="card">
      <table>
        <thead>
          <tr><th>Метрика</th><th>Что измеряет</th><th>Целевое значение</th></tr>
        </thead>
        <tbody>
          <tr><td>Accuracy (точность)</td><td>% правильных ответов</td><td>> 90%</td></tr>
          <tr><td>Hallucination rate</td><td>% выдуманных фактов</td><td>< 2%</td></tr>
          <tr><td>Response time</td><td>Время ответа</td><td>< 5 сек</td></tr>
          <tr><td>User satisfaction</td><td>Оценка пользователей</td><td>> 4.0 / 5</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Практика: проверка качества (без кода)</h2>
    <div class="card card-success">
      <h3>Метод "Золотой набор"</h3>
      <ol>
        <li>Создайте набор из 50-100 реальных запросов с <strong>известными правильными ответами</strong></li>
        <li>Прогоните через AI каждую неделю</li>
        <li>Сравните ответы AI с правильными</li>
        <li>Считайте точность: (правильные / всего) × 100%</li>
      </ol>
    </div>
    
    <div class="card card-success">
      <h3>Метод "Выборочный контроль"</h3>
      <ol>
        <li>Каждую неделю выбирайте 10 случайных ответов AI</li>
        <li>Проверяйте экспертом (юрист, аналитик, менеджер)</li>
        <li>Записывайте ошибки в таблицу: Тип | Частота | Критичность</li>
        <li>Раз в месяц анализируйте: какие ошибки повторяются → исправляйте промпт</li>
      </ol>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Точность > 90%? (проверьте золотой набор)</li>
      <li>Галлюцинации < 2%? (проверьте 100 ответов)</li>
      <li>Время ответа < 5 секунд?</li>
      <li>Пользователи довольны (> 4.0 / 5)?</li>
      <li>Есть процесс улучшения промптов по ошибкам?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Без мониторинга AI — это рулетка. Измеряйте точность, галлюцинации, время, удовлетворённость. Используйте "золотой набор" и выборочный контроль. Улучшайте промпты по ошибкам. Качество AI — это не "настроил и забыл", а непрерывный процесс.</p>
    </div>
  </div>'''),
]

for lesson in lessons_p3:
    generate_lesson(*lesson)

print("\nPhase 3 done!")
