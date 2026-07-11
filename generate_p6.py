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

# Phase 6: Ethics
lessons_p6 = [
    ("6.1", "Конфиденциальные данные: что можно, что нельзя", "🛡️ ФАЗА 6 · ЭТИКА, БЕЗОПАСНОСТЬ, КОМПЛАЕНС", "35 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p><span class="highlight">Утечка данных = штрафы, репутационные потери, потеря контрактов.</span> GDPR — до 4% оборота. 152-ФЗ — до 500 млн руб. Нужно знать правила.</p>
  </div>

  <div class="section">
    <h2>📚 Классификация данных</h2>
    <div class="card card-danger">
      <h3>🔴 Категория 1: Категорически нельзя в облако</h3>
      <ul>
        <li>Персональные данные клиентов (ФИО, телефоны, паспорта)</li>
        <li>Коммерческая тайна (цены, поставщики, контракты)</li>
        <li>Стратегические планы (M&A, выход на рынки)</li>
        <li>Финансовая отчётность до публикации</li>
      </ul>
      <p><strong>Решение:</strong> On-premise (OpenWebUI + Qwen/Llama) или закрытая инфраструктура.</p>
    </div>
    
    <div class="card card-warning">
      <h3>🟡 Категория 2: Можно с ограничениями</h3>
      <ul>
        <li>Внутренние инструкции (без персональных данных)</li>
        <li>Обезличенные данные (анонимизированные)</li>
        <li>Публичные данные (сайт, каталог, прайс-лист)</li>
      </ul>
      <p><strong>Решение:</strong> Enterprise-версии AI (ChatGPT Enterprise, Claude for Business) с data processing agreement.</p>
    </div>
    
    <div class="card card-success">
      <h3>🟢 Категория 3: Можно в облако</h3>
      <ul>
        <li>Маркетинговые материалы</li>
        <li>Публичные тексты (пресс-релизы, посты)</li>
        <li>Общие знания ("как написать письмо")</li>
      </ul>
      <p><strong>Решение:</strong> Любые облачные AI (ChatGPT, Claude, Gemini).</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Чеклист безопасности</h2>
    <div class="card card-success">
      <ul class="checklist">
        <li>Все сотрудники подписали соглашение о конфиденциальности?</li>
        <li>Проведён аудит: какие данные уходят в облако AI?</li>
        <li>Есть DPA (Data Processing Agreement) с поставщиком AI?</li>
        <li>Данные не используются для обучения модели? (opt-out)</li>
        <li>Есть процесс реагирования на утечку?</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Не все данные можно отправлять в облако. Персональные данные, коммерческая тайна, стратегические планы — только on-premise. Публичные данные — любые облачные AI. Проведите аудит, подпишите DPA, настройте opt-out.</p>
    </div>
  </div>'''),

    ("6.2", "Галлюцинации: как проверять факты", "🛡️ ФАЗА 6 · ЭТИКА, БЕЗОПАСНОСТЬ, КОМПЛАЕНС", "40 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p><span class="highlight">AI "галлюцинирует" — выдумывает факты, цитаты, даты, законы.</span> Это не баг, а фича модели. Нужно уметь проверять.</p>
  </div>

  <div class="section">
    <h2>📚 Что такое галлюцинация</h2>
    <div class="example">
      <div class="example-label">💡 ПРИМЕР ГАЛЛЮЦИНАЦИИ</div>
      <p><strong>Вопрос:</strong> "Какая статья УК РФ регулирует неисполнение договора поставки?"</p>
      <p><strong>Ответ AI:</strong> "Статья 310 УК РФ предусматривает ответственность..." (выдумано — статьи 310 в УК нет)</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Методы проверки фактов</h2>
    <div class="card card-success">
      <h3>1. Первоисточник (для документов)</h3>
      <p>AI нашёл риск в договоре → проверьте по оригинальному тексту договора.</p>
    </div>
    <div class="card card-success">
      <h3>2. Перекрёстная проверка (для данных)</h3>
      <p>AI сказал "цена выросла на 15%" → проверьте по таблице цен за 3 месяца.</p>
    </div>
    <div class="card card-success">
      <h3>3. Экспертная проверка (для критичных)</h3>
      <p>AI нашёл юридический риск → проверьте юристом. AI нашёл риск качества → проверьте инженером.</p>
    </div>
    <div class="card card-success">
      <h3>4. RAG (для баз знаний)</h3>
      <p>Если AI использует RAG, он ссылается на конкретные документы. Проверьте цитату в оригинале.</p>
    </div>
  </div>

  <div class="section">
    <h2>🛠️ Чеклист: как не попасться на галлюцинацию</h2>
    <div class="card card-success">
      <ul class="checklist">
        <li>Для цифр: проверьте по первоисточнику</li>
        <li>Для дат: сверьтесь с календарём и документами</li>
        <li>Для законов: проверьте по официальным источникам (Консультант, Гарант)</li>
        <li>Для цитат: найдите оригинальный текст</li>
        <li>Для имен: проверьте по справочникам</li>
        <li>Если AI "уверенно" утверждает — проверьте дважды (уверенность ≠ правда)</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>Галлюцинации — нормальная особенность LLM. AI не врёт, он "предсказывает". Всегда проверяйте: цифры по первоисточнику, даты по календарю, законы по официальным базам, цитаты по оригиналу. Уверенность AI ≠ правда.</p>
    </div>
  </div>'''),

    ("6.3", "AI-политика компании: шаблон", "🛡️ ФАЗА 6 · ЭТИКА, БЕЗОПАСНОСТЬ, КОМПЛАЕНС", "45 минут", '''
  <div class="section">
    <h2>🎯 Зачем это бизнесу</h2>
    <p>Без политики — хаос. Один сотрудник использует ChatGPT для договоров, другой — нет. Один загружает конфиденциальные данные, другой — нет. <strong>Политика = единые правила для всех.</strong></p>
  </div>

  <div class="section">
    <h2>📚 Шаблон AI-политики компании</h2
    <div class="card card-success">
      <h3>1. Общие положения</h3>
      <ul>
        <li>Цель: регулирование использования AI в компании</li>
        <li>Область действия: все сотрудники, подрядчики, партнёры</li>
        <li>Ответственный: [ФИО, должность, контакт]</li>
      </ul>
    </div>
    
    <div class="card">
      <h3>2. Разрешённые инструменты</h3>
      <table>
        <thead>
          <tr><th>Инструмент</th><th>Для чего</th><th>Ограничения</th></tr>
        </thead>
        <tbody>
          <tr><td>ChatGPT Enterprise</td><td>Маркетинг, тексты, анализ</td><td>Без персональных данных</td></tr>
          <tr><td>Claude</td><td>Длинные документы</td><td>Без конфиденциальных данных</td></tr>
          <tr><td>OpenWebUI (on-premise)</td><td>Конфиденциальные данные</td><td>Только внутри компании</td></tr>
        </tbody>
      </table>
    </div>
    
    <div class="card">
      <h3>3. Запреты</h3>
      <ul>
        <li>❌ Загружать персональные данные клиентов в публичные AI</li>
        <li>❌ Использовать AI для юридически обязывающих заключений без проверки</li>
        <li>❌ Доверять AI цифры и даты без проверки</li>
        <li>❌ Использовать AI для принятия критичных решений (увольнение, штрафы)</li>
      </ul>
    </div>
    
    <div class="card">
      <h3>4. Процедуры</h3>
      <ul>
        <li>Все сотрудники проходят обучение перед использованием AI</li>
        <li>Каждый результат AI проверяется человеком для критичных задач</li>
        <li>Утечки данных фиксируются и расследуются в течение 24 часов</li>
        <li>Политика пересматривается каждые 6 месяцев</li>
      </ul>
    </div>
    
    <div class="card card-success">
      <h3>5. Ответственность</h3>
      <ul>
        <li>Сотрудник несёт ответственность за результат, использующий AI</li>
        <li>Руководитель отдела отвечает за обучение и контроль</li>
        <li>IT обеспечивает техническую безопасность</li>
        <li>Юрист проверяет соответствие законодательству</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>✅ Чеклист внедрения политики</h2>
    <ul class="checklist">
      <li>Политика согласована с юристом и HR?</li>
      <li>Все сотрудники подписали согласие?</li>
      <li>Проведено обучение (минимум 1 час)?</li>
      <li>Есть канал для вопросов и обратной связи?</li>
      <li>Политика доступна внутри компании (Confluence / Notion)?</li>
      <li>Назначен ответственный за обновление политики?</li>
    </ul>
  </div>

  <div class="section">
    <div class="card card-success">
      <h3>🎯 Главное из урока</h3>
      <p>AI-политика = единые правила для всех. Кто, что, какими инструментами, с какими ограничениями. Без политики — хаос и риски. С политикой — предсказуемость и контроль. Обновляйте каждые 6 месяцев.</p>
    </div>
  </div>'''),
]

for lesson in lessons_p6:
    generate_lesson(*lesson)

print("\nPhase 6 done! All phases completed!")
