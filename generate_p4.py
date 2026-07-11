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

# Phase 4: Agents
lessons_p4 = [
    ("4.1", "Что такое AI-агент: простыми словами", "🤖 ФАЗА 4 · АГЕНТЫ И ОРКЕСТРАЦИЯ", "35 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p><strong>AI-агент</strong> = автономный помощник, который сам ставит подзадачи, выполняет их и сообщает о результатах. Не просто отвечает на вопросы — а <strong>решает задачи от начала до конца</strong>.</p>
  </div>

  <div class="section">
    <h2>📚 Агент vs Chatbot</h2>
    <div class="comparison">
      <div class="comparison-box">
        <h4>🤖 Chatbot (чат-бот)</h4>
        <ul>
          <li>Отвечает на вопросы</li>
          <li>Ждёт команду пользователя</li>
          <li>Одно действие = один ответ</li>
          <li>Пример: "Сколько стоит доставка?"</li>
        </ul>
      </div>
      <div class="comparison-box">
        <h4>🎯 Agent (агент)</h4>
        <ul>
          <li>Выполняет задачи самостоятельно</li>
          <li>Ставит подзадачи и решает их</li>
          <li>Много шагов без участия человека</li>
          <li>Пример: "Подготовь заказ поставщику на основе остатков и продаж"</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Как работает агент (5 шагов)</h2>
    <div class="card card-success">
      <ol>
        <li><strong>Понимание задачи:</strong> "Подготовить заказ поставщику"</li>
        <li><strong>Декомпозиция:</strong> Проверить остатки → Посмотреть продажи за месяц → Рассчитать потребность → Сформировать заказ → Проверить бюджет</li>
        <li><strong>Выполнение:</strong> Агент запрашивает данные из 1С, Excel, email</li>
        <li><strong>Проверка:</strong> Сверка с правилами (мин. партия, бюджет, сроки)</li>
        <li><strong>Результат:</strong> Готовый заказ + обоснование + уведомление менеджеру</li>
      </ol>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист: готов ли ваш процесс к агенту?</h2>
    <ul class="checklist">
      <li>Задача повторяется > 5 раз в неделю?</li>
      <li>Есть чёткий алгоритм (можно записать шаги)?</li>
      <li>Данные доступны в цифровом виде (1С, Excel, CRM)?</li>
      <li>Решение можно проверить (не требует интуиции)?</li>
      <li>Ошибка не критична (можно исправить за 10 минут)?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Агент = автономный исполнитель задач. Отличие от чат-бота: сам ставит подзадачи, сам выполняет, сам проверяет. Начинайте с простых процессов, где есть чёткий алгоритм и данные в цифре.</p>
    </div>
  </div>'''),

    ("4.2", "Мультиагентные системы: когда нужны несколько агентов", "🤖 ФАЗА 4 · АГЕНТЫ И ОРКЕСТРАЦИЯ", "40 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>Сложные задачи требуют разных экспертиз. Один агент — аналитик, второй — юрист, третий — коммуникатор. Вместе они решают задачу, которую один агент не осилит.</p>
  </div>

  <div class="section">
    <h2>📚 Пример: закупка с тремя агентами</h2>
    <div class="card card-success">
      <h3>Агент 1: Аналитик</h3>
      <p>Задача: Анализировать остатки, продажи, прогноз спроса. Выход: рекомендуемый заказ.</p>
      <h3>Агент 2: Юрист</h3>
      <p>Задача: Проверять договор с поставщиком на риски. Выход: список рисков + рекомендации.</p>
      <h3>Агент 3: Коммуникатор</h3>
      <p>Задача: Формировать письмо поставщику с заказом. Выход: готовое письмо.</p>
      <hr style="border-color: var(--border);">
      <p><strong>Оркестратор:</strong> Запускает агентов по очереди, передаёт результаты между ними, проверяет согласованность.</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Когда нужны мультиагенты</h2>
    <div class="card card-success">
      <ul>
        <li><strong>Сложные процессы:</strong> > 5 шагов, разные типы работы (анализ + проверка + коммуникация)</li>
        <li><strong>Масштаб:</strong> > 1000 документов/запросов в день — один агент не справится</li>
        <li><strong>Качество:</strong> нужна "вторая пара глаз" — проверка одним агентом работы другого</li>
      </ul>
    </div>
    <div class="card card-warning">
      <strong>⚠️ Не нужны мультиагенты:</strong> Для простых задач (< 3 шагов) — проще один агент или автоматизация.
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Мультиагенты нужны для сложных процессов с разными экспертизами. Аналитик + юрист + коммуникатор = полноценный процесс закупки. Но для простых задач достаточно одного агента. Не усложняйте без необходимости.</p>
    </div>
  </div>'''),

    ("4.3", "Человек в цикле: approve, reject, доработка", "🤖 ФАЗА 4 · АГЕНТЫ И ОРКЕСТРАЦИЯ", "40 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>AI не может нести ответственность. <strong>"Человек в цикле" (Human-in-the-loop, HITL)</strong> = обязательная проверка человеком для критичных решений.</p>
  </div>

  <div class="section">
    <h2>📚 Три уровня контроля</h2>
    <div class="card">
      <h3>1. Approve (одобрить)</h3>
      <p>AI предлагает решение → человек нажимает "✅ Одобрить" или "❌ Отклонить".</p>
      <p><strong>Пример:</strong> AI сформировал заказ на 500 000 руб. Менеджер проверяет и одобряет.</p>
    </div>
    <div class="card">
      <h3>2. Reject (отклонить с причиной)</h3>
      <p>AI предлагает решение → человек отклоняет и указывает причину → AI учится на ошибке.</p>
      <p><strong>Пример:</strong> AI предложил поставщика с рейтингом 3.5 — менеджер отклоняет: "рейтинг должен быть > 4.0".</p>
    </div>
    <div class="card">
      <h3>3. Доработка (редактировать)</h3>
      <p>AI предлагает черновик → человек редактирует → AI запоминает правки.</p>
      <p><strong>Пример:</strong> AI написал письмо поставщику → менеджер добавил срочность → AI запоминает, что в письмах нужно указывать срочность.</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Матрица: когда нужен человек</h2>
    <div class="card">
      <table>
        <thead>
          <tr><th>Действие</th><th>Автоматизация</th><th>HITL</th></tr>
        </thead>
        <tbody>
          <tr><td>Сбор данных</td><td>✅ Авто</td><td>—</td></tr>
          <tr><td>Анализ рисков</td><td>✅ Авто</td><td>—</td></tr>
          <tr><td>Подписание договора</td><td>—</td><td>✅ Approve</td></tr>
          <tr><td>Отправка заказа</td><td>—</td><td>✅ Approve</td></tr>
          <tr><td>Изменение цены > 10%</td><td>—</td><td>✅ Approve</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>"Человек в цикле" — не слабость, а сила. AI собирает данные и анализирует, человек принимает критичные решения. Это даёт скорость + контроль. Начинайте с HITL для всех критичных действий, постепенно расширяйте автоматизацию.</p>
    </div>
  </div>'''),

    ("4.4", "MCP: интеграция с корпоративными системами", "🤖 ФАЗА 4 · АГЕНТЫ И ОРКЕСТРАЦИЯ", "45 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>AI без доступа к данным — как автомобиль без топлива. <strong>MCP (Model Context Protocol)</strong> = стандарт, который позволяет AI подключаться к 1С, CRM, ERP и другим системам.</p>
  </div>

  <div class="section">
    <h2>📚 MCP простыми словами</h2>
    <div class="example">
      <div class="example-label">💡 АНАЛОГИЯ</div>
      <p>MCP = <strong>универсальный адаптер</strong>, как USB-C для телефона. Раньше каждый телефон нужен был свой зарядник. Теперь один кабель подходит ко всем. MCP — это "USB-C" для AI и корпоративных систем.</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Что можно подключить через MCP</h2>
    <div class="card"
      <ul>
        <li><strong>1С / Битрикс / МойСклад</strong> — остатки, цены, контрагенты</li>
        <li><strong>SAP / Oracle ERP</strong> — производство, логистика, финансы</li>
        <li><strong>CRM (Salesforce, HubSpot, amoCRM)</strong> — клиенты, сделки, история</li>
        <li><strong>Базы данных (PostgreSQL, MySQL)</strong> — произвольные запросы</li>
        <li><strong>API сервисов (Dadata, СБИС, Такском)</strong> — проверка контрагентов, налогов</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>👨‍💻 Как поставить задачу разработчику</h2>
    <div class="card card-success">
      <pre style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px;">
"Нужно подключить AI к [СИСТЕМА] через MCP.

Требования:
- Система: [1С / SAP / CRM]
- Данные: [остатки / цены / клиенты]
- Операции: [чтение / запись / оба]
- Безопасность: [роли, ограничения доступа]
- Логирование: кто, когда, что запрашивал

Прошу:
1. Оценить трудоёмкость
2. Предложить архитектуру
3. Сделать POC на 1 операции
4. Описать процесс добавления новых систем"
      </pre>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>AI получает актуальные данные (не кэшированные)?</li>
      <li>Права доступа соответствуют ролям пользователя?</li>
      <li>Все запросы логируются (кто, когда, что запрашивал)?</li>
      <li>Есть fallback, если система недоступна?</li>
      <li>Можно добавить новую систему за < 1 дня?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>MCP = универсальный адаптер для AI. Позволяет подключаться к 1С, ERP, CRM без кастомной разработки для каждой системы. Экономия на интеграциях: 50-70%.</p>
    </div>
  </div>'''),
]

for lesson in lessons_p4:
    generate_lesson(*lesson)

print("\nPhase 4 done!")
