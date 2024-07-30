Жадібний алгоритм:

1. Жадібний алгоритм починає з найбільшої монети і намагається взяти якомога більше таких монет.
2. Для кожного номіналу монет перевіряється, скільки разів цей номінал можна взяти, не перевищуючи залишок суми.
3. Це призводить до оптимального рішення в більшості випадків, але не завжди (наприклад, для монет [9, 6, 1] і суми 11).

Часова складність: O(n), де n — кількість монетних номіналів.
Продуктивність:
 - Жадібний алгоритм працює дуже швидко, оскільки просто перебирає номінали монет, починаючи з найбільшого, доки не буде досягнута потрібна сума.
 - Продуктивність на великих сумах також залишається високою, оскільки кількість ітерацій залежить тільки від кількості номіналів, а не від самої суми.
 - Жадібний алгоритм не завжди забезпечує оптимальне рішення для всіх наборів монет, що може бути його головним недоліком.

Динамічне програмування:

1. Створюється масив dp, де dp[i] зберігає мінімальну кількість монет для суми i.
2. Для кожної суми від 1 до amount, перевіряються всі номінали монет і вибирається мінімальна кількість монет, необхідна для досягнення цієї суми.
3. В кінці відновлюються використані монети, що дозволяє отримати оптимальне рішення з мінімальною кількістю монет.

Часова складність: O(n * amount), де n — кількість монетних номіналів, а amount — сума, для якої обчислюється видача решти.
Продуктивність:
 - Динамічне програмування використовує масив для зберігання мінімальної кількості монет для кожної суми до даної суми. Це гарантує оптимальне рішення.
 - Продуктивність може знизитися на дуже великих сумах, оскільки складність алгоритму залежить як від кількості номіналів, так і від величини суми.
 - Забезпечує правильний результат навіть у тих випадках, де жадібний алгоритм може не спрацювати оптимально.

    # Порівняння на великих сумах
    
Жадібний алгоритм залишається ефективним і швидким, але може давати неоптимальні результати для певних наборів номіналів.
Алгоритм динамічного програмування гарантує мінімальну кількість монет для видачі, але зростання суми значно впливає на час виконання алгоритму.

    # Висновок
Жадібний алгоритм підходить для швидких рішень з великою кількістю номіналів і великих сум, але його застосування обмежується його здатністю забезпечувати оптимальні результати. Алгоритм динамічного програмування, хоча й більш обчислювально затратний, гарантує оптимальність і забезпечує правильний результат для будь-якого набору номіналів.