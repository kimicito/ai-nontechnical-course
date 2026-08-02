# HARNESS.md — AI для не ИТ-специалистов

## Контекст
- **Проект:** Курс «AI для не ИТ-специалистов» (ai-nontechnical-course)
- **URL:** https://kimicito.github.io/ai-nontechnical-course/
- **Языки:** RU, EN, FR, ZH
- **Технологии:** Static HTML, GitHub Pages, Pagefind (search)

## Архитектура

```
ai-nontechnical-course/
├── index.html              # RU главная
├── catalog.html            # RU каталог уровней
├── updates.html            # RU обновления
├── glossary.html           # RU термины
├── lessons/                # RU уроки (00-choose-model ... 17-5-agents)
│   └── NN-topic/index.html
├── en/                     # EN версия (зеркало структуры)
├── fr/                     # FR версия
├── zh/                     # ZH версия
└── pagefind/               # Поисковый индекс
```

## Структура уровней (после вставки Уровня 6)

| Уровень | Тема | Папки |
|---------|------|-------|
| 0 | База | 00-choose-model, 00-cloud-vs-onprem, 00-pricing, 00-what-is-llm |
| 1 | Промпты | 01-chain-prompts, 01-documents, 01-practice-task, 01-prompt-engineering, 01-structured-output |
| 2 | RAG | 02-long-docs, 02-rag-explained, 02-summarization, 02-vector-db |
| 3 | Автоматизация | 03-ai-processes, 03-monitoring, 03-nocode-automation, 03-simple-agents |
| 4 | Агенты | 04-agent-systems, 04-harness, 04-human-loop, 04-mcp, 04-multi-agent, 04-skills-hub, 04-what-is-agent |
| 5 | Внедрение | 05-pilot-project, 05-roi-calculator, 05-scaling |
| **6** | **Программирование** | **06-cursor-intro, 06-cursor-prompts, 06-cursor-website, 06-cursor-database** |
| 7 | Этика | 07-ai-policy, 07-confidential-data, 07-hallucinations |
| 8 | Закупки | 08-1-on-prem, 08-2-cloud, 08-3-hybrid, 08-5-agents |
| 9 | Строительство | 08-1-reality, 08-2-onprem, 08-3-cloud, 08-4-dev-agents, 08-5-agents |
| 10 | Аудит | 09-audit-construction-projects, 09-audit-procurement-sales, 09-compliance-fraud, 09-doc-check |
| 11 | PR | 10-1-reality, 10-2-onprem, 10-3-cloud, 10-4-dev-agents, 10-5-agents |
| 12 | ТОиР | 11-1-on-prem, 11-2-cloud, 11-3-hybrid, 11-5-agents |
| 13 | Логистика | 12-1-on-prem, 12-2-cloud, 12-3-hybrid, 12-5-agents |
| 14 | Продажи | 13-1-on-prem, 13-2-cloud, 13-3-hybrid, 13-5-agents |
| 15 | Юристы | 14-1-on-prem, 14-2-cloud, 14-3-hybrid, 14-4-summary, 14-5-agents |
| 16 | Комплаенс | 15-1-on-prem, 15-2-cloud, 15-3-hybrid, 15-4-summary, 15-5-agents |
| 17 | Безопасность | 16-1-on-prem, 16-2-cloud, 16-3-hybrid, 16-4-summary, 16-5-agents |
| 18 | HR | 17-1-on-prem, 17-2-cloud, 17-3-hybrid, 17-4-summary, 17-5-agents |

## Правила работы с курсом

### 1. План → Согласование → Выполнение
**При любой задаче по курсу:**
1. Показать план действий
2. Получить согласие пользователя
3. Только потом выполнять

### 2. Изменения во всех языках одновременно
- При добавлении урока/уровня — обновить RU, EN, FR, ZH
- При обновлении navigation — проверить все 4 языка
- При добавлении в glossary — добавить во все 4 glossary.html

### 3. Структурные изменения — проверять 404
После переименования папок или вставки уровня:
```bash
# Проверить все ссылки в catalog.html
bash /tmp/check_404.sh

# Проверить навигацию внутри уроков
grep -rn "href=\"../.." lessons/ | grep -v "style.css"
```

### 4. Pagefind переиндексация
После изменений HTML:
```bash
cd projects/ai-nontechnical-course
npx pagefind --source . --glob "**/*.html"
```

### 5. Git commit
```bash
git add -A
git commit -m "[course] Описание изменений"
git push origin gh-pages
```

## Типичные задачи

### Добавить новый уровень
1. Создать папки `lessons/NN-topic/` (RU)
2. Создать EN/FR/ZH версии
3. Обновить `catalog.html` (все языки)
4. Обновить `index.html` — карточка + статистика
5. Обновить `updates.html` (все языки)
6. Обновить навигацию «вперёд/назад» в соседних уроках
7. Переиндексировать Pagefind
8. Commit + push

### Исправить ошибку
1. Показать план исправления
2. Получить согласие
3. Исправить во всех затронутых файлах
4. Проверить 404
5. Commit + push

### Обновить термины
1. Добавить в `glossary.html` (все 4 языка)
2. Использовать простые объяснения (для не-IT)
3. Формат: `<h3>Термин</h3><div class="simple">Простое объяснение</div><p>Детали</p>`

## Критические проверки

| Проверка | Когда |
|----------|-------|
| `catalog.html` id секций | После вставки/удаления уровня |
| `index.html` ссылки `#levelN` | После изменения нумерации |
| `updates.html` записи | После добавления урока/уровня |
| `glossary.html` термины | При добавлении новой тематики |
| Пути `lessons/NN-*/` | После переименования папок |
| Навигация в уроках | После вставки уровня |
