import json, os, textwrap

BASE = "/root/.openclaw/workspace/projects/ai-nontechnical-course/site/lessons"

def generate_lesson(lesson_id, title, phase, duration, content):
    slug = lesson_id.replace('.', '-')
    path = f"{BASE}/{slug}"
    os.makedirs(path, exist_ok=True)
    
    # Extract prev/next
    prev_link = "../../catalog.html"
    next_link = "../../catalog.html"
    
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
  .model-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 16px; margin: 8px 0; }}
  .model-card h4 {{ margin: 0 0 8px; color: var(--accent); }}
  .model-card .pros {{ color: var(--success); font-size: 0.9rem; }}
  .model-card .cons {{ color: var(--warning); font-size: 0.9rem; }}
  .comparison {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0; }}
  .comparison-box {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 16px; }}
  .comparison-box h4 {{ margin: 0 0 12px; }}
  .cloud {{ border-left: 4px solid var(--accent2); }}
  .onprem {{ border-left: 4px solid var(--success); }}
  .risk-matrix {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin: 16px 0; }}
  .risk-item {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 12px; text-align: center; }}
  .risk-high {{ color: var(--danger); }}
  .risk-medium {{ color: var(--warning); }}
  .risk-low {{ color: var(--success); }}
  .tier {{ display: flex; align-items: center; gap: 16px; padding: 12px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; margin: 8px 0; }}
  .tier-price {{ font-size: 1.5rem; font-weight: 700; color: var(--accent); min-width: 100px; }}
  .tier-desc {{ color: var(--muted); font-size: 0.9rem; }}
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
    <a href="{prev_link}" class="nav-btn">← К каталогу</a>
    <a href="{next_link}" class="nav-btn primary">Каталог →</a>
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

# Phase 1: Tools Mastery
lessons = [
    ("1.1", "Промпт-инжиниринг для менеджера", "🛠️ ФАЗА 1 · ВЛАДЕНИЕ ИНСТРУМЕНТАМИ", "45 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>"Сделай красиво" — худший промпт. Плохой промпт = 5 итераций = потерянный день. Хороший промпт = результат с первого раза.</p>
    <div class="card card-accent">
      <strong>После этого урока:</strong>
      <ul>
        <li>Пишете промпты, которые дают результат с 1-2 попытки</li>
        <li>Используете формулу: Роль + Контекст + Задача + Формат</li>
        <li>Экономите 3-5 часов в неделю на рутинных запросах</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>📚 Формула идеального промпта</h2>
    <div class="card card-success">
      <h3>RCOF: Role + Context + Objective + Format</h3>
      <div class="example">
        <div class="example-label">✅ ХОРОШИЙ ПРОМПТ</div>
        <p><strong>Роль:</strong> Ты — менеджер по закупкам с 10-летним опытом в FMCG.</p>
        <p><strong>Контекст:</strong> Мы пересматриваем контракт с поставщиком сахара. Текущие условия: цена 45 руб/кг, отсрочка 30 дней, мин. партия 10 тонн.</p>
        <p><strong>Задача:</strong> Предложи 5 аргументов для переговоров о снижении цены на 10%.</p>
        <p><strong>Формат:</strong> Таблица: Аргумент | Обоснование | Риск для нас | Риск для поставщика.</p>
      </div>
      <div class="example">
        <div class="example-label">❌ ПЛОХОЙ ПРОМПТ</div>
        <p>"Как снизить цену у поставщика?"</p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Шаблоны для типовых задач</h2>
    <div class="card">
      <h3>Анализ документа</h3>
      <pre style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px; overflow-x: auto;">
"Проанализируй [ДОКУМЕНТ].

Роль: Ты — [СПЕЦИАЛИСТ] с опытом в [ОТРАСЛЬ].
Задача: Найди [N] рисковых моментов.
Формат: Таблица с колонками: Риск | Уровень | Рекомендация.
Ограничение: Не более [N] пунктов, только критичные."
      </pre>
    </div>
    <div class="card">
      <h3>Сравнение вариантов</h3>
      <pre style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px; overflow-x: auto;">
"Сравни варианты А и Б для [СИТУАЦИЯ].

Критерии:
- Стоимость (включая скрытые)
- Сроки внедрения
- Риски
- Масштабируемость

Формат: Таблица + рекомендация с обоснованием."
      </pre>
    </div>
  </div>

  <div class="section">
    <h2>👨‍💻 Как поставить задачу разработчику</h2>
    <div class="card card-success">
      <pre style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px; overflow-x: auto;">
"Нужно создать библиотеку промптов для отдела [НАЗВАНИЕ].

Требования:
- 20 шаблонов под типовые задачи
- Валидация: результат проверяется [КЕМ]
- Версионирование: как обновлять шаблоны
- Интеграция: где хранить (Notion / Confluence / Git)

Дайте демо на 3 шаблонах за [N] дней."
      </pre>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Промпт дает результат с 1-2 попыток?</li>
      <li>Формат ответа предсказуем и удобен?</li>
      <li>Контекст (роль, ограничения) достаточен?</li>
      <li>Есть библиотека шаблонов для команды?</li>
      <li>Новичок может использовать без объяснений?</li>
    </ul>
  </div>

  <div class="section">
    <h2>📝 Проверка понимания</h2>
    <div class="card card-accent">
      <p><strong>Вопрос 1:</strong> Какая формула для хорошего промпта?</p>
      <p><em>Ответ: RCOF — Role + Context + Objective + Format.</em></p>
    </div>
    <div class="card card-accent">
      <p><strong>Вопрос 2:</strong> Почему "сделай красиво" — плохой промпт?</p>
      <p><em>Ответ: Нет контекста, роли, формата. Результат непредсказуем.</em></p>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Хороший промпт = чёткая роль + контекст + конкретная задача + желаемый формат. Используйте шаблоны, не пишите с нуля каждый раз. Экономия: 3-5 часов в неделю.</p>
    </div>
  </div>'''),

    ("1.2", "Структурированный вывод: JSON, таблицы, чеклисты", "🛠️ ФАЗА 1 · ВЛАДЕНИЕ ИНСТРУМЕНТАМИ", "40 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>AI может выдавать результат в любом формате. Но если не указать — получите "стену текста", которую невозможно скопировать в Excel.</p>
    <div class="card card-accent">
      <strong>После этого урока:</strong>
      <ul>
        <li>Получаете данные в нужном формате (JSON, CSV, таблица)</li>
        <li>Автоматизируете перенос в Excel / Sheets / BI</li>
        <li>Создаёте чеклисты для проверки работы AI</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>📚 Форматы вывода</h2>
    <div class="card">
      <h3>Таблица (Markdown)</h3>
      <div class="example">
        <div class="example-label">✅ ПРОМПТ</div>
        <p>"Проанализируй 3 поставщика. Выведи результат в таблице: Поставщик | Цена | Сроки | Риск | Рекомендация."</p>
      </div>
    </div>
    <div class="card">
      <h3>JSON (для автоматизации)</h3>
      <div class="example">
        <div class="example-label">✅ ПРОМПТ</div>
        <p>"Выведи результат в JSON: {"supplier": "", "price": 0, "delivery_days": 0, "risk": "", "recommend": true/false}"</p>
      </div>
    </div>
    <div class="card">
      <h3>Чеклист</h3>
      <div class="example">
        <div class="example-label">✅ ПРОМПТ</div>
        <p>"Проверь договор на риски. Выведи чеклист: [ ] пункт риска — [ ] уровень — [ ] рекомендация."</p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Интерактив: калькулятор формата</h2>
    <div class="calc-box">
      <label>Задача:<select id="task" onchange="formatCalc()">
        <option value="table">Сравнение вариантов</option>
        <option value="json">Интеграция с системой</option>
        <option value="checklist">Проверка документа</option>
        <option value="text">Объяснение / отчёт</option>
      </select></label>
      <div class="calc-result" id="formatResult" style="margin-top: 16px;">
        <div id="formatRec">Рекомендация появится здесь</div>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>👨‍💻 Как поставить задачу разработчику</h2>
    <div class="card card-success">
      <pre style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px; overflow-x: auto;">
"Нужно стандартизировать вывод AI для отдела [НАЗВАНИЕ].

Требования:
- Формат: [JSON/CSV/Таблица]
- Валидация: структура проверяется автоматически
- Примеры: 5 корректных и 3 некорректных вывода
- Документация: как редактировать формат

Дайте API-спецификацию или шаблон."
      </pre>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Формат стабилен (10 запросов — одинаковая структура)?</li>
      <li>Можно скопировать в Excel без ручной правки?</li>
      <li>Есть примеры для каждого сценария?</li>
      <li>Новичек понимает формат без объяснений?</li>
    </ul>
  </div>

  <div class="section">
    <h2>📝 Проверка понимания</h2>
    <div class="card card-accent">
      <p><strong>Вопрос 1:</strong> Какой формат выбрать для интеграции с 1С?</p>
      <p><em>Ответ: JSON — структурированный, машиночитаемый.</em></p>
    </div>
    <div class="card card-accent">
      <p><strong>Вопрос 2:</strong> Почему "стена текста" — плохо?</p>
      <p><em>Ответ: Невозможно автоматизировать, легко пропустить важное.</em></p>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Указывайте формат вывода в каждом промпте. Таблица для сравнений, JSON для интеграций, чеклист для проверок. Это экономит 50% времени на обработке результатов.</p>
    </div>
  </div>

<script>
function formatCalc() {
  const task = document.getElementById('task').value;
  const result = document.getElementById('formatRec');
  const formats = {
    'table': 'Таблица (Markdown) — легко копировать в Excel',
    'json': 'JSON — для API-интеграций и автоматизации',
    'checklist': 'Чеклист — для проверки и аудита',
    'text': 'Простой текст — для объяснений и отчётов'
  };
  result.textContent = formats[task] || 'Выберите задачу';
}
formatCalc();
</script>'''),
]

for lesson in lessons:
    generate_lesson(*lesson)

print("\nPhase 1 (2/5) created. Continuing...")
