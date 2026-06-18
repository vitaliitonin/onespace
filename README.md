# Onespace

> Україномовна платформа для пошуку фільмів та мультфільмів — з поділом на дитячий та дорослий контент, рейтингами IMDb і темним кінематографічним інтерфейсом.

Не стрімінг. Знайшов — перейшов на Netflix/Kino UA.

---

## Структура репо

| Папка | Що всередині |
|-------|-------------|
| [`research/`](./research/) | Аналіз конкурентів, аудиторії, інсайти; скриншоти референсів у `screens/` |
| [`wireframes/`](./wireframes/) | Lo-fi wireframes Desktop → Mobile |
| [`concept/`](./concept/) | Visual concept, moodboard, напрямок стилю |
| [`tokens/`](./tokens/) | Дизайн-токени: колір, типографіка, відступи, тіні |
| [`components/`](./components/) | Специфікації UI-компонентів |
| [`design-system/`](./design-system/) | Зібрана дизайн-система (посилання на Figma / експорт) |
| [`handoff/`](./handoff/) | Матеріали для розробки: аннотації, redlines, assets |

Повний продуктовий бриф → [`CLAUDE.md`](./CLAUDE.md)

---

## Прогрес

### Discovery
- [x] Продуктовий бриф
- [ ] Research & аналіз конкурентів
- [ ] Аудиторні інсайти

### Design
- [ ] Wireframes (Desktop)
- [ ] Visual concept
- [ ] Дизайн-токени
- [ ] UI-компоненти
- [ ] Дизайн-система

### Handoff
- [ ] Специфікації для розробки
- [ ] MVP scope затверджений

---

## Ключові рішення

- **Дані**: TMDB API + IMDb datasets
- **Режими**: Дорослий / Дитячий з PIN-перемикачем
- **Freemium**: пошук безкоштовно → watchlist + дитячий режим платно
- **Стек**: Next.js 14 · Tailwind · PostgreSQL · Prisma · NextAuth · Vercel
- **Платформа**: Desktop → Mobile
