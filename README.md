# Порівняння алгоритмів сортування

Цей документ містить аналіз ефективності трьох алгоритмів сортування: сортування вставками, сортування злиттям та Timsort (вбудований в Python).

## Вихідні дані для тестування

Тестування було проведено на трьох наборах даних різного розміру:

- Малий набір: 100 елементів (випадкові числа в діапазоні від 0 до 1,000)
- Середній набір: 1,000 елементів (випадкові числа в діапазоні від 0 до 10,000)
- Великий набір: 10,000 елементів (випадкові числа в діапазоні від 0 до 100,000)

## Результати (секунди)

| Algorithm            | Small                | Medium               | Large                |
| -------------------- | -------------------- | -------------------- | -------------------- |
| Insertion Sort       |              0.00027 |              0.02358 |              2.27540 |
| Merge Sort           |              0.00124 |              0.01638 |              0.20603 |
| Timsorted            |              0.00001 |              0.00006 |              0.00057 |
| Timsort              |              0.00001 |              0.00006 |              0.00055 |

## Висновки

За результатами замірів часу виконання різних алгоритмів сортування на масивах різного розміру, ми можемо зробити наступні висновки:

- **Insertion Sort** показує хороші результати на малих наборах даних, але його продуктивність швидко знижується зі збільшенням розміру масиву. 
Це пов'язано з тим, що часова складність алгоритму є \(O(n^2)\) у найгіршому та середньому випадках.

- **Merge Sort** має більш стабільну продуктивність незалежно від розміру масиву, завдяки своїй часовій складності \(O(n \log n)\). 
Це робить його значно більш ефективним на великих наборах даних порівняно з Insertion Sort.

- **Timsort**, вбудований алгоритм сортування Python (який використовується у функціях `sorted()` та методі `.sort()`), показує найкращу продуктивність у всіх випробуваннях. 
Це підтверджує його високу ефективність для широкого спектру розмірів даних. Timsort є гібридним алгоритмом, який використовує принципи Merge Sort та Insertion Sort, 
оптимізований для реальних даних, які часто містять вже відсортовані секції.

Ці результати підтверджують, що поєднання стратегій сортування, як у Timsort, робить його набагато ефективнішим, особливо на реальних даних, де можливі частково відсортовані секції.
 Саме тому програмісти часто віддають перевагу використанню вбудованих алгоритмів сортування Python, які забезпечують високу продуктивність без необхідності самостійної реалізації складних алгоритмів.
