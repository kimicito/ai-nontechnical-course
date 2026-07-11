import os, sys

BASE = "/root/.openclaw/workspace/projects/ai-nontechnical-course/site/lessons"

TEMPLATE = '''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<title>{lesson_id} {title} — AI для Менеджеров</title>
<link rel="stylesheet" href="../../style.css">
<style>
  :root {{ --bg: #0B0F19; --card: #111827; --text: #F3F4F6; --muted: #9CA3AF; --accent: #8B5CF6; --accent2: #06B6D4; --border: rgba(255,255,255,0.08); --success: #10B981; --warning: #F59E0B; --danger: #EF4444; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; overflow-x: hidden; }}
  .container {{ max-width: 800px; margin: 0 auto; padding: 0 16px; }}
  header {{ padding: 16px 0; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: var(--bg); z-index: 100; }}
  header .container {{ display: flex; justify-content: space-between; align-items: center; }}
  .logo {{ font-size: 1.1rem; font-weight: 700; color: var(--accent); text-decoration: none; white-space: nowrap; }}
  .lesson-header {{ padding: 32px 0 16px; }}
  .lesson-header .phase {{ color: var(--accent); font-size: 0.85rem; font-weight: 600; }}
  .lesson-header h1 {{ margin: 8px 0; font-size: 1.8rem; line-height: 1.25; word-break: break-word; }}
  .lesson-header .meta {{ color: var(--muted); font-size: 0.9rem; }}
  .section {{ margin: 28px 0; }}
  .section h2 {{ color: var(--accent); font-size: 1.2rem; margin-bottom: 12px; }}
  .section h3 {{ color: var(--accent2); font-size: 1.05rem; margin: 20px 0 10px; }}
  .card {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; margin: 14px 0; }}
  .card-accent {{ border-left: 4px solid var(--accent); }}
  .card-success {{ border-left: 4px solid var(--success); }}
  .card-warning {{ border-left: 4px solid var(--warning); }}
  .card-danger {{ border-left: 4px solid var(--danger); }}
  .highlight {{ background: rgba(139,92,246,0.1); padding: 2px 6px; border-radius: 4px; }}
  .checklist {{ list-style: none; padding: 0; }}
  .checklist li {{ padding: 8px 0; padding-left: 28px; position: relative; }}
  .checklist li:before {{ content: "☐"; position: absolute; left: 0; color: var(--accent); }}
  .example {{ background: rgba(6,182,212,0.05); border: 1px solid rgba(6,182,212,0.2); border-radius: 8px; padding: 14px; margin: 12px 0; }}
  .example-label {{ color: var(--accent2); font-size: 0.75rem; font-weight: 600; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }}
  .nav-footer {{ display: flex; justify-content: space-between; padding: 32px 0; border-top: 1px solid var(--border); margin-top: 32px; flex-wrap: wrap; gap: 8px; }}
  .nav-btn {{ padding: 10px 20px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; color: var(--text); text-decoration: none; transition: all 0.2s; font-size: 0.9rem; }}
  .nav-btn:hover {{ border-color: var(--accent); }}
  .nav-btn.primary {{ background: var(--accent); border-color: var(--accent); color: white; }}
  footer {{ padding: 32px 16px; text-align: center; color: var(--muted); border-top: 1px solid var(--border); }}
  .calc-box {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 16px; margin: 14px 0; }}
  .calc-box input, .calc-box select {{ width: 100%; padding: 8px; background: var(--bg); border: 1px solid var(--border); border-radius: 4px; color: var(--text); margin: 6px 0; font-size: 1rem; }}
  .calc-box label {{ display: block; margin: 8px 0 4px; color: var(--muted); font-size: 0.9rem; }}
  .calc-result {{ background: rgba(16,185,129,0.1); border: 1px solid var(--success); border-radius: 8px; padding: 16px; margin: 14px 0; text-align: center; }}
  .calc-result .sum {{ font-size: 1.8rem; font-weight: 700; color: var(--success); }}
  table {{ width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 0.9rem; }}
  th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid var(--border); }}
  th {{ color: var(--accent); font-weight: 600; }}
  tr:hover {{ background: rgba(255,255,255,0.02); }}
  .comparison {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin: 14px 0; }}
  .comparison-box {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 14px; }}
  .comparison-box h4 {{ margin: 0 0 10px; font-size: 0.95rem; }}
  .tier {{ display: flex; align-items: center; gap: 14px; padding: 10px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; margin: 8px 0; flex-wrap: wrap; }}
  .tier-price {{ font-size: 1.3rem; font-weight: 700; color: var(--accent); min-width: 80px; }}
  pre {{ background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.85rem; line-height: 1.5; }}
  ul, ol {{ padding-left: 20px; }}
  li {{ margin: 4px 0; }}
  hr {{ border: 0; border-top: 1px solid var(--border); margin: 16px 0; }}
  
  @media (max-width: 768px) {{
    .lesson-header h1 {{ font-size: 1.4rem; }}
    .comparison {{ grid-template-columns: 1fr; }}
    .nav-footer {{ flex-direction: column; }}
    .nav-btn {{ width: 100%; text-align: center; }}
    table {{ font-size: 0.8rem; }}
    th, td {{ padding: 6px; }}
  }}
</style>
</head>
<body>

<header>
  <div class="container">
    <a href="../../index.html" class="logo">🧠 AI для Менеджеров</a>
    <a href="../../catalog.html" style="color: var(--muted); text-decoration: none; font-size: 0.9rem;">← Каталог</a>
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

def generate_lesson(lesson_id, title, phase, duration, content):
    slug = lesson_id.replace('.', '-')
    path = os.path.join(BASE, slug)
    os.makedirs(path, exist_ok=True)
    
    html = TEMPLATE.format(
        lesson_id=lesson_id,
        title=title,
        phase=phase,
        duration=duration,
        content=content
    )
    
    with open(os.path.join(path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created: {lesson_id} {title}")

# Phase 1 lessons
lessons_p1 = [
    ("1.1", "Промпт-инжиниринг для менеджера: писать ТЗ, а не \"сделай красиво\"", "🛠️ УРОВЕНЬ 1 · ВЛАДЕНИЕ ИНСТРУМЕНТАМИ", "45 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p><span class="highlight">80% результатов AI зависит от промпта.</span> Плохой промпт = плохой ответ. Хороший промпт = экономия 2-3 часа в день на каждого сотрудника.</p>
  </div>

  <div class="section">
    <h2>📚 Формула хорошего промпта: RCOF</h2>
    <div class="card card-success">
      <p><strong>R — Role (Роль):</strong> Кто ты? "Ты опытный закупщик с 10-летним стажем"</p>
      <p><strong>C — Context (Контекст):</strong> Что происходит? "Мы выбираем поставщика упаковки для пищевой продукции"</p>
      <p><strong>O — Objective (Цель):</strong> Что нужно получить? "Сравни 3 предложения и рекомендуй лучшее"</p>
      <p><strong>F — Format (Формат):</strong> В каком виде? "Таблица: Критерий | Поставщик 1 | Поставщик 2 | Поставщик 3 | Победитель"</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Пример: промпт для сравнения поставщиков</h2>
    <div class="example">
      <div class="example-label">💡 Пример хорошего промпта</div>
      <pre>Ты — опытный закупщик FMCG с 10-летним стажем.
Мы выбираем поставщика картонной упаковки для печенья.
Получили 3 предложения во вложениях.

Задача: сравни предложения по критериям и рекомендуй лучшее.

Критерии:
1. Цена за единицу (включая доставку)
2. Минимальный заказ
3. Срок изготовления
4. Условия оплаты
5. Рейтинг/репутация (если есть данные)

Формат: таблица сравнения + однозначная рекомендация с обоснованием.

Ограничения: если срок > 14 дней — отметь как риск.</pre>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист качества промпта</h2>
    <ul class="checklist">
      <li>Указана роль? (кто отвечает)</li>
      <li>Дан контекст? (что происходит)</li>
      <li>Определена цель? (что нужно получить)</li>
      <li>Задан формат? (таблица, список, текст)</li>
      <li>Есть ограничения? (что исключить)</li>
      <li>Проверьте результат: он соответствует запросу?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Промпт = ТЗ для AI. Используйте формулу RCOF: Роль, Контекст, Цель, Формат. Чем конкретнее — тем лучше результат. Не пишите "сделай красиво", пишите "сделай таблицу сравнения по 5 критериям".</p>
    </div>
  </div>'''),

    ("1.2", "Структурированный вывод: JSON, таблицы, чеклисты", "🛠️ УРОВЕНЬ 1 · ВЛАДЕНИЕ ИНСТРУМЕНТАМИ", "40 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>AI может выдавать ответы в <strong>любом формате</strong>: таблица, JSON, чеклист, CSV. Это позволяет копировать результат в Excel, 1С или CRM за 1 клик.</p>
  </div>

  <div class="section">
    <h2>📚 Форматы вывода</h2>
    <div class="comparison">
      <div class="comparison-box">
        <h4>📊 Таблица</h4>
        <p>Для сравнения, анализа, отчётов. Легко копировать в Excel.</p>
      </div>
      <div class="comparison-box">
        <h4>📋 JSON</h4>
        <p>Для программистов и автоматизации. AI выдаёт данные в структурированном виде.</p>
      </div>
      <div class="comparison-box">
        <h4>☑️ Чеклист</h4>
        <p>Для проверки, аудита, контроля качества. Понятно всем.</p>
      </div>
      <div class="comparison-box">
        <h4>📝 Markdown</h4>
        <p>Для документации, инструкций, статей. Читается везде.</p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Пример: запрос таблицы сравнения</h2>
    <div class="example">
      <div class="example-label">💡 Пример промпта</div>
      <pre>Ты — финансовый аналитик.
Проанализируй 3 инвестиционных проекта (данные ниже).

Выведи результат в формате таблицы:
| Проект | ROI | Срок окупаемости | Риск | Рекомендация |

После таблицы — краткое обоснование рекомендации.</pre>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Формат соответствует запросу? (таблица / JSON / чеклист)</li>
      <li>Все поля заполнены? (нет пропусков)</li>
      <li>Данные корректны? (проверьте 2-3 случайные ячейки)</li>
      <li>Можно скопировать в Excel / 1С / CRM?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Указывайте формат в промпте. Таблица для сравнения, JSON для автоматизации, чеклист для проверки. Это экономит 5-10 минут на форматирование каждый раз.</p>
    </div>
  </div>'''),

    ("1.3", "Цепочки запросов: от простого к сложному", "🛠️ УРОВЕНЬ 1 · ВЛАДЕНИЕ ИНСТРУМЕНТАМИ", "45 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>Сложные задачи нельзя решить одним промптом. <strong>Цепочка запросов</strong> = разбиение задачи на шаги, где каждый следующий использует результат предыдущего.</p>
  </div>

  <div class="section">
    <h2>📚 Пример цепочки: анализ рынка</h2>
    <div class="card card-success">
      <h3>Шаг 1: Сбор информации</h3>
      <p>"Найди 5 крупнейших поставщиков [товара] в [регионе]. Для каждого: название, сайт, контакт, рейтинг."</p>
      <h3>Шаг 2: Структурирование</h3>
      <p>"Преобразуй результат в таблицу: Поставщик | Сайт | Телефон | Рейтинг | Примечания"</p>
      <h3>Шаг 3: Анализ</h3>
      <p>"Проанализируй таблицу: какие риски? Кто лидер? Что проверить дополнительно?"</p>
      <h3>Шаг 4: Рекомендация</h3>
      <p>"На основе анализа — рекомендуй 2 поставщика для первого контакта. Обоснуй."</p>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист: когда использовать цепочки</h2>
    <ul class="checklist">
      <li>Задача требует > 3 действий?</li>
      <li>Каждый шаг зависит от предыдущего?</li>
      <li>Нужен промежуточный результат для проверки?</li>
      <li>Один промпт даёт слишком длинный/сложный ответ?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Сложные задачи разбивайте на цепочку: сбор → структурирование → анализ → рекомендация. Проверяйте результат каждого шага. Это даёт качество, которого невозможно достичь одним промптом.</p>
    </div>
  </div>'''),

    ("1.4", "Работа с документами: анализ, суммаризация, сравнение", "🛠️ УРОВЕНЬ 1 · ВЛАДЕНИЕ ИНСТРУМЕНТАМИ", "50 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p><span class="highlight">Менеджер читает 2-3 часа документов в день.</span> AI сокращает это до 15 минут: анализирует, суммирует, сравнивает, находит риски.</p>
  </div>

  <div class="section">
    <h2>📚 3 типа задач с документами</h2>
    <div class="card card-success">
      <h3>1. Суммаризация (сжатие)</h3>
      <p>"Перескажи договор в 5 пунктах: что покупаем, за сколько, сроки, риски, штрафы."</p>
      <p><strong>Экономия:</strong> 30 мин → 2 минуты</p>
    </div>
    <div class="card card-success">
      <h3>2. Сравнение</h3>
      <p>"Сравни 2 договора: где лучшие условия оплаты, доставки, гарантии? Выдели различия."</p>
      <p><strong>Экономия:</strong> 1 час → 5 минут</p>
    </div>
    <div class="card card-success">
      <h3>3. Анализ рисков</h3>
      <p>"Проверь договор на риски: неустойка, форс-мажор, расторжение, споры. Оцени каждый риск по шкале 1-5."</p>
      <p><strong>Экономия:</strong> 2 часа → 10 минут</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Практика: промпт для анализа договора</h2>
    <div class="example">
      <div class="example-label">💡 Пример промпта</div>
      <pre>Ты — юрист с 15-летним стажем в корпоративном праве.
Проанализируй приложенный договор поставки.

Задачи:
1. Выдели ключевые условия (цена, сроки, объём, оплата)
2. Найди риски для покупателя (неустойка, качество, просрочка)
3. Оцени каждый риск: Высокий / Средний / Низкий
4. Дай рекомендации по минимизации рисков

Формат: таблица рисков + рекомендации</pre>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Все ключевые пункты договора учтены?</li>
      <li>Риски оценены корректно? (проверьте 2-3 пункта)</li>
      <li>Рекомендации применимы? (можно реализовать)</li>
      <li>Формат удобен для передачи коллегам?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>AI анализирует документы за минуты: суммирует, сравнивает, находит риски. Но всегда проверяйте критичные выводы. AI — помощник, не замена юристу. Экономия: 2-3 часа в день.</p>
    </div>
  </div>'''),

    ("1.5", "Практика: автоматизируй свою первую задачу", "🛠️ УРОВЕНЬ 1 · ВЛАДЕНИЕ ИНСТРУМЕНТАМИ", "60 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>Теория без практики бесполезна. Выберите <strong>одну реальную задачу</strong> из вашей работы и автоматизируйте её с помощью AI за 1 час.</p>
  </div>

  <div class="section">
    <h2>📚 Выбор задачи для автоматизации</h2>
    <div class="card card-success">
      <p><strong>Идеальная задача:</strong></p>
      <ul>
        <li>Повторяется > 3 раз в неделю</li>
        <li>Занимает > 20 минут каждый раз</li>
        <li>Есть чёткий алгоритм (можно описать шаги)</li>
        <li>Не требует критичных решений (безопасно ошибиться)</li>
      </ul>
    </div>
    <div class="example">
      <div class="example-label">💡 Примеры задач</div>
      <ul>
        <li>"Создавай еженедельный отчёт о продажах из CSV"</li>
        <li>"Проверяй 10 писем поставщиков на изменения цен"</li>
        <li>"Формируй сводку новостей по отрасли"</li>
        <li>"Анализируй 5 отзывов клиентов и выделяй тренды"</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Алгоритм автоматизации</h2>
    <div class="card card-success">
      <ol>
        <li><strong>Опишите задачу:</strong> Что делаете, зачем, как часто</li>
        <li><strong>Напишите промпт:</strong> RCOF (Роль, Контекст, Цель, Формат)</li>
        <li><strong>Проверьте на 3 примерах:</strong> Работает? Корректно?</li>
        <li><strong>Запишите процесс:</strong> Шаги, промпт, примеры</li>
        <li><strong>Поделитесь с коллегами:</strong> Покажите, как экономите время</li>
      </ol>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Лучший способ научиться — сделать. Выберите одну задачу, напишите промпт, проверьте на 3 примерах, запишите процесс. Экономия 2-3 часа в неделю — реальность, а не теория.</p>
    </div>
  </div>'''),
]

for lesson in lessons_p1:
    generate_lesson(*lesson)

print("\nPhase 1 done!")
