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
  .model-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 16px; margin: 8px 0; }}
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

# All remaining lessons
all_lessons = [
    # Phase 1 remainder
    ("1.3", "Цепочки запросов: от простого к сложному", "🛠️ ФАЗА 1 · ВЛАДЕНИЕ ИНСТРУМЕНТАМИ", "45 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>Один сложный запрос = риск галлюцинации. 5 простых запросов = точный результат. Разбивайте задачу на шаги.</p>
    <div class="card card-accent">
      <strong>После этого урока:</strong>
      <ul>
        <li>Разбиваете сложные задачи на цепочки простых</li>
        <li>Используете выход одного запроса как вход следующего</li>
        <li>Создаёте шаблоны цепочек для типовых задач</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>📚 Пример цепочки: анализ договора</h2>
    <div class="card card-success">
      <p><strong>Шаг 1:</strong> "Суммаризируй договор в 5 пунктов"</p>
      <p><strong>Шаг 2:</strong> "Найди рисковые пункты в каждом из 5 пунктов"</p>
      <p><strong>Шаг 3:</strong> "Предложи альтернативную формулировку для каждого риска"</p>
      <p><strong>Шаг 4:</strong> "Составь чеклист для юриста на основе рисков"</p>
    </div>
    <div class="card card-warning">
      <strong>⚠️ Антипаттерн:</strong> "Проанализируй договор, найди риски, предложи альтернативы и сделай чеклист для юриста" — слишком много за один раз.
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Шаблоны цепочек</h2>
    <div class="card">
      <h3>Цепочка "Сравнение поставщиков"</h3>
      <ol>
        <li>"Извлеки из предложения: цена, сроки, условия оплаты"</li>
        <li>"Сравни 3 поставщика по критериям: цена, сроки, гарантия"</li>
        <li>"Оцени риски каждого варианта"</li>
        <li>"Дай финальную рекомендацию с обоснованием"</li>
      </ol>
    </div>
    <div class="card">
      <h3>Цепочка "Подготовка отчёта"</h3>
      <ol>
        <li>"Собери данные из [ИСТОЧНИКИ]"</li>
        <li>"Сгруппируй по категориям"</li>
        <li>"Выдели ключевые тренды"</li>
        <li>"Сформулируй рекомендации для руководства"</li>
      </ol>
    </div>
  </div>

  <div class="section">
    <h2>👨‍💻 Как поставить задачу разработчику</h2>
    <div class="card card-success">
      <pre style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px;">
"Нужно автоматизировать цепочку запросов для [ЗАДАЧА].

Шаги:
1. [ВХОД] → [ПРОМПТ] → [ВЫХОД]
2. [ВЫХОД шага 1] → [ПРОМПТ] → [ВЫХОД]
3. ...

Требования:
- Промежуточные результаты сохраняются
- Можно пропустить шаг или вернуться
- Есть точка проверки человеком
- Общее время < 2 минут"
      </pre>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Каждый шаг выполняется за 1 запрос?</li>
      <li>Есть проверка между критичными шагами?</li>
      <li>Общее время цепочки < 5 минут?</li>
      <li>Результат предсказуем при одинаковом входе?</li>
    </ul>
  </div>

  <div class="section">
    <h2>📝 Проверка понимания</h2>
    <div class="card card-accent">
      <p><strong>Вопрос 1:</strong> Почему цепочка лучше одного сложного запроса?</p>
      <p><em>Ответ: Проще контролировать, меньше риск ошибки, можно проверить промежуточные результаты.</em></p>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Разбивайте сложные задачи на 3-5 простых шагов. Каждый шаг — один промпт. Проверяйте промежуточные результаты. Это снижает ошибки на 70%.</p>
    </div>
  </div>'''),
    
    ("1.4", "Работа с документами: анализ, суммаризация, сравнение", "🛠️ ФАЗА 1 · ВЛАДЕНИЕ ИНСТРУМЕНТАМИ", "50 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>Менеджер тратит <span class="highlight">2-3 часа в день</span> на чтение документов. AI может сделать это за 5 минут — с чеклистом для проверки.</p>
  </div>

  <div class="section">
    <h2>📚 Три типа работы с документами</h2>
    
    <div class="card">
      <h3>1. Суммаризация ("Изложи короче")</h3>
      <div class="example">
        <div class="example-label">✅ ПРОМПТ</div>
        <p>"Суммаризируй договор в 5 пунктов: суть сделки, обязательства сторон, сроки, неустойка, условия расторжения."</p>
      </div>
    </div>
    
    <div class="card">
      <h3>2. Анализ ("Найди риски")</h3>
      <div class="example">
        <div class="example-label">✅ ПРОМПТ</div>
        <p>"Проанализируй договор. Найди риски для нашей компании. Для каждого риска: уровень (низкий/средний/высокий), рекомендация по смягчению."</p>
      </div>
    </div>
    
    <div class="card">
      <h3>3. Сравнение ("Сравни А и Б")</h3>
      <div class="example">
        <div class="example-label">✅ ПРОМПТ</div>
        <p>"Сравни приложение 1 и приложение 2 к договору. Выдели расхождения. Таблица: Параметр | Приложение 1 | Приложение 2 | Расхождение | Критичность."</p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Практика: загрузка документа</h2>
    <div class="card card-success">
      <h3>Как загрузить документ в AI (без кода)</h3>
      <ul>
        <li><strong>ChatGPT Plus:</strong> Прикрепите файл (PDF, Word, Excel) — AI прочитает автоматически</li>
        <li><strong>Claude:</strong> Прикрепите файл или вставьте текст (до 100K слов)</li>
        <li><strong>Kimi:</strong> Прикрепите файл (до 2M токенов — ~500 страниц)</li>
      </ul>
    </div>
    
    <div class="card card-warning">
      <strong>⚠️ Ограничение:</strong> Не загружайте конфиденциальные документы в облачные AI. Используйте on-premise (OpenWebUI) для договоров, цен, стратегий.
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Суммаризация не потеряла ключевые пункты? (проверьте по оригиналу)</li>
      <li>Риски реальные, не выдуманные?</li>
      <li>Сравнение нашло все расхождения?</li>
      <li>Юрист / эксперт проверил критичные выводы?</li>
    </ul>
  </div>

  <div class="section">
    <h2>📝 Проверка понимания</h2>
    <div class="card card-accent">
      <p><strong>Вопрос 1:</strong> Какой AI лучше для 200-страничного договора?</p>
      <p><em>Ответ: Kimi (2M токенов) или Claude (100K+ слов).</em></p>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Загружайте документы, задавайте конкретные задачи (суммаризируй, найди риски, сравни), проверяйте критичные выводы. Экономия: 2-3 часа в день.</p>
    </div>
  </div>'''),
    
    ("1.5", "Практика: автоматизируй свою первую задачу", "🛠️ ФАЗА 1 · ВЛАДЕНИЕ ИНСТРУМЕНТАМИ", "60 минут", '''
  <div class="section">
    <h2>🎯 Задача урока</h2>
    <p>Выберите одну рутинную задачу из вашей работы и автоматизируйте её с помощью AI за 60 минут.</p>
    <div class="card card-accent">
      <strong>Примеры задач:</strong>
      <ul>
        <li>Еженедельный отчёт о закупках (суммаризация 10 писем)</li>
        <li>Проверка 5 договоров на рисковые пункты</li>
        <li>Сравнение 3 предложений поставщиков</li>
        <li>Написание 10 ответов клиентам по шаблону</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Пошаговая инструкция</h2>
    <div class="card card-success">
      <h3>Шаг 1: Выберите задачу (5 мин)</h3>
      <ul class="checklist">
        <li>Занимает > 30 минут в неделю?</li>
        <li>Повторяется регулярно?</li>
        <li>Связана с текстом (письма, отчёты, договоры)?</li>
        <li>Результат можно проверить?</li>
      </ul>
    </div>
    
    <div class="card card-success">
      <h3>Шаг 2: Напишите промпт (15 мин)</h3>
      <div class="example">
        <div class="example-label">ШАБЛОН</div>
        <p><strong>Роль:</strong> Ты — [ВАША РОЛЬ]</p>
        <p><strong>Контекст:</strong> [КОНТЕКСТ ЗАДАЧИ]</p>
        <p><strong>Задача:</strong> [ЧТО НУЖНО СДЕЛАТЬ]</p>
        <p><strong>Формат:</strong> [ТАБЛИЦА / JSON / ЧЕКЛИСТ]</p>
      </div>
    </div>
    
    <div class="card card-success">
      <h3>Шаг 3: Протестируйте (20 мин)</h3>
      <ul>
        <li>Прогоните 3-5 реальных примеров</li>
        <li>Сравните результат с ручной работой</li>
        <li>Замерьте время: AI vs ручная работа</li>
      </ul>
    </div>
    
    <div class="card card-success">
      <h3>Шаг 4: Документируйте (20 мин)</h3>
      <ul>
        <li>Сохраните промпт в общий доступ (Notion / Confluence)</li>
        <li>Напишите инструкцию: что делает, как проверить</li>
        <li>Поделитесь с коллегой — проверьте, понятно ли</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист завершения</h2>
    <ul class="checklist">
      <li>Задача выбрана и соответствует критериям?</li>
      <li>Промпт написан по формуле RCOF?</li>
      <li>Протестирован на 3+ примерах?</li>
      <li>Результат проверен экспертом?</li>
      <li>Промпт задокументирован и доступен команде?</li>
      <li>Время экономии > 50%?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Поздравляем!</h3>
      <p>Вы автоматизировали первую задачу. Следующий шаг — создать библиотеку из 10 промптов для вашей роли. Это сэкономит 5-10 часов в неделю.</p>
    </div>
  </div>'''),
    
    # Phase 2
    ("2.1", "RAG простыми словами: как подключить AI к базе знаний", "📄 ФАЗА 2 · ДАННЫЕ И ДОКУМЕНТЫ", "40 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>AI "знает" только то, что было в обучающих данных. Он не знает ваши внутренние процедуры, цены, историю клиентов. <strong>RAG решает эту проблему.</strong></p>
    <div class="card card-accent">
      <strong>Пример:</strong> Клиент спрашивает: "Какие у вас сроки доставки в Казань?" AI без RAG скажет "обычно 3-5 дней". AI с RAG скажет "согласно вашему договору №123 от 15.03, доставка в Казань — 2 дня, бесплатно от 50 000 руб."
    </div>
  </div>

  <div class="section">
    <h2>📚 Что такое RAG (без математики)</h2>
    <div class="example">
      <div class="example-label">💡 АНАЛОГИЯ</div>
      <p>Представьте, что AI — это новый сотрудник. RAG = <strong>его ознакомление с документами компании</strong>. Вы даёте ему папку с инструкциями, и он отвечает клиентам, используя эти инструкции.</p>
    </div>
    
    <div class="card">
      <h3>Как работает RAG (3 шага)</h3>
      <ol>
        <li><strong>Индексация:</strong> Ваши документы (PDF, Word, Excel) "загружаются" в базу знаний</li>
        <li><strong>Поиск:</strong> Когда приходит вопрос, AI находит релевантные документы</li>
        <li><strong>Генерация:</strong> AI отвечает, используя найденные документы + свои знания</li>
      </ol>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Когда RAG нужен, а когда нет</h2>
    <div class="card card-success">
      <h3>✅ Нужен RAG</h3>
      <ul>
        <li>Ответы на вопросы клиентов по продуктам/услугам</li>
        <li>Внутренний поиск по базе знаний (регламенты, инструкции)</li>
        <li>Анализ договоров с учётом типовых условий компании</li>
        <li>Обучение новых сотрудников (ответы на вопросы по процедурам)</li>
      </ul>
    </div>
    <div class="card card-warning">
      <h3>❌ Не нужен RAG</h3>
      <ul>
        <li>Творческие задачи (генерация идей, копирайтинг)</li>
        <li>Общие знания ("какая столица Франции?")</li>
        <li>Задачи, где важен "общий мир", а не конкретные документы</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>👨‍💻 Как поставить задачу разработчику</h2>
    <div class="card card-success">
      <pre style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px;">
"Нужно внедрить RAG для отдела [НАЗВАНИЕ].

Требования:
- Источники: [PDF/Word/Excel/1C/CRM]
- Объём: [N] документов, [N] страниц
- Пользователей: [N] человек
- Языки: [RU/EN]
- Обновление: как часто добавляются новые документы
- Конфиденциальность: [да/нет]

Прошу оценить:
1. Платформу (OpenWebUI / LangChain / готовое решение)
2. Стоимость внедрения и эксплуатации
3. Сроки POC
4. Требования к инфраструктуре"
      </pre>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>AI отвечает, ссылаясь на конкретные документы?</li>
      <li>Ответы точные (не выдумывает условия, которых нет в документах)?</li>
      <li>Новые документы появляются в поиске за < 1 часа?</li>
      <li>Пользователи могут работать без IT-шника?</li>
      <li>Есть статистика использования (какие вопросы задают чаще)?</li>
    </ul>
  </div>

  <div class="section">
    <h2>📝 Проверка понимания</h2>
    <div class="card card-accent">
      <p><strong>Вопрос 1:</strong> Что делает RAG?</p>
      <p><em>Ответ: Подключает AI к базе знаний компании, чтобы ответы были основаны на реальных документах.</em></p>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>RAG = AI + ваши документы. Нужен для точных ответов по продуктам, процедурам, договорам. Не нужен для творческих задач. Стоимость внедрения: $500-5000 в зависимости от масштаба.</p>
    </div>
  </div>'''),

    ("2.2", "Векторные базы: что спросить у IT", "📄 ФАЗА 2 · ДАННЫЕ И ДОКУМЕНТЫ", "35 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>RAG работает на "векторных базах". Это хранилище, где документы хранятся не как текст, а как "смыслы". Нужно понимать основы, чтобы говорить с IT.</p>
  </div>

  <div class="section">
    <h2>📚 Векторная база простыми словами</h2>
    <div class="example">
      <div class="example-label">💡 АНАЛОГИЯ</div>
      <p><strong>Обычная база данных = библиотечный каталог.</strong> Ищете по точному названию. "Договор с ООО Ромашка" — найдёт, "соглашение с цветочной компанией" — нет.</p>
      <p><strong>Векторная база = Google по смыслу.</strong> Ищете "как доставляем в Казань" — находит договор логистики, инструкцию по доставке, email от транспортной компании.</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Популярные векторные базы</h2>
    <div class="card">
      <h3>Для начинающих (без кода)</h3>
      <ul>
        <li><strong>Pinecone (облако)</strong> — managed, от $25/мес, не нужен сервер</li>
        <li><strong>Chroma (open-source)</strong> — бесплатно, но нужен разработчик</li>
        <li><strong>Qdrant</strong> — open-source, хорошая документация</li>
      </ul>
    </div>
    <div class="card">
      <h3>Для корпораций</h3>
      <ul>
        <li><strong>Weaviate</strong> — enterprise, поддержка, масштабирование</li>
        <li><strong>Milvus</strong> — от Alibaba, хорош для больших данных</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>👨‍💻 Что спросить у IT</h2>
    <div class="card card-success">
      <ul class="checklist">
        <li>Какую векторную базу рекомендуете под наш объём? (N документов, M запросов/день)</li>
        <li>Как происходит обновление данных? (ручное / автоматическое по расписанию)</li>
        <li>Какая точность поиска? (recall @ top-5)</li>
        <li>Сколько стоит хранение и поиск в месяц?</li>
        <li>Есть ли backup / disaster recovery?</li>
        <li>Можно ли перенести на другого провайдера? (vendor lock-in)</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Поиск находит релевантные документы (проверьте 10 запросов)?</li>
      <li>Скорость поиска < 2 секунд?</li>
      <li>Новые документы индексируются автоматически?</li>
      <li>Есть мониторинг (если база падает, кто узнает)?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Векторная база = хранилище "смыслов". Нужно для RAG, семантического поиска, рекомендаций. Спросите IT про объём, скорость, обновление, vendor lock-in. Стартовый бюджет: $25-100/мес.</p>
    </div>
  </div>'''),

    ("2.3", "Длинные документы: как не потерять контекст", "📄 ФАЗА 2 · ДАННЫЕ И ДОКУМЕНТЫ", "40 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>AI "забывает" начало документа, когда читает конец. Для договора на 100 страниц это критично. Нужно уметь работать с длинными текстами.</p>
  </div>

  <div class="section">
    <h2>📚 Проблема и решения</h2>
    <div class="card card-warning">
      <strong>Проблема:</strong> У модели есть "контекстное окно" — максимальный объём текста, который она может обработать за раз. ChatGPT — ~32K токенов (~50 страниц), Claude — ~200K (~300 страниц), Kimi — 2M (~3000 страниц).
    </div>
    
    <div class="card card-success">
      <h3>Решение 1: Чанкинг (разбиение на части)</h3>
      <p>Документ режется на куски по 1000 слов, каждый кусок анализируется отдельно, потом результаты объединяются.</p>
      <p><strong>Аналогия:</strong> Как если бы вы дали 10 стажёрам по 10 страниц, а потом свели их заметки в один отчёт.</p>
    </div>
    
    <div class="card card-success">
      <h3>Решение 2: Иерархическая суммаризация</h3>
      <ol>
        <li>Сначала суммаризируем каждую главу (10 страниц → 1 страница)</li>
        <li>Потом суммаризируем суммаризации (10 глав → 1 страница)</li>
        <li>Получаем "сжатую версию" всего документа</li>
      </ol>
    </div>
  </div>

  <div class="section">
    <h2>👨‍💻 Как поставить задачу разработчику</h2>
    <div class="card card-success">
      <pre style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px;">
"Нужно обработать документы до [N] страниц.

Требования:
- Модель: [Claude / Kimi / local]
- Метод: [чанкинг / иерархия / гибрид]
- Проверка: каждый результат сверяется с оригиналом
- Время: < [N] минут на документ

Прошу сделать демо на 3 реальных документах."
      </pre>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Суммаризация не потеряла ключевые пункты? (проверьте на 3 документах)</li>
      <li>Связи между разделами сохранены?</li>
      <li>Время обработки приемлемо?</li>
      <li>Есть процесс проверки для критичных документов?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Для длинных документов используйте чанкинг или иерархическую суммаризацию. Claude и Kimi — лучшие модели для больших текстов. Всегда проверяйте критичные выводы.</p>
    </div>
  </div>'''),

    ("2.4", "Суммаризация и редактирование: отчёты, договоры, акты", "📄 ФАЗА 2 · ДАННЫЕ И ДОКУМЕНТЫ", "45 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>Отчёт на 50 страниц → 1 страница за 5 минут. Договор на 20 страниц → чеклист рисков за 10 минут. AI экономит 90% времени на чтение.</p>
  </div>

  <div class="section">
    <h2>📚 Типы суммаризации</h2>
    <div class="card">
      <h3>Extractive (выделение главного)</h3>
      <p>AI выбирает самые важные предложения из оригинала. Без искажений, но может быть несвязно.</p>
      <p><strong>Используйте:</strong> для юридических документов, где важна точность формулировок.</p>
    </div>
    <div class="card">
      <h3>Abstractive (пересказ своими словами)</h3>
      <p>AI переписывает текст, объединяя идеи. Более читаемо, но риск искажения.</p>
      <p><strong>Используйте:</strong> для отчётов, презентаций, внутренних резюме.</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Шаблоны промптов для суммаризации</h2>
    <div class="card">
      <div class="example">
        <div class="example-label">ДЛЯ ОТЧЁТА</div>
        <p>"Суммаризируй отчёт в 1 страницу. Сохрани цифры и проценты. Формат: Проблема | Причина | Рекомендация | Ответственный."</p>
      </div>
    </div>
    <div class="card">
      <div class="example">
        <div class="example-label">ДЛЯ ДОГОВОРА</div>
        <p>"Извлеки из договора: стороны, предмет, сумма, сроки, неустойка, условия расторжения, приложения. Таблица: Параметр | Значение | Риск."</p>
      </div>
    </div>
    <div class="card">
      <div class="example">
        <div class="example-label">ДЛЯ АКТА</div>
        <p>"Суммаризируй акт приёмки. Выдели расхождения с договором. Формат: Параметр | По договору | По акту | Расхождение | Критичность."</p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист принятия результата</h2>
    <ul class="checklist">
      <li>Все цифры и даты сохранены точно?</li>
      <li>Ключевые условия не потеряны?</li>
      <li>Риски выделены корректно?</li>
      <li>Эксперт проверил критичные выводы?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Extractive для юридических документов (точность), abstractive для отчётов (читаемость). Всегда проверяйте цифры, даты, риски. Экономия: 2-3 часа на документ.</p>
    </div>
  </div>'''),
]

for lesson in all_lessons:
    generate_lesson(*lesson)

print("\nDone! Check generated lessons.")
