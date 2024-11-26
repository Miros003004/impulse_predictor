Impulse.Predictor - это современный инструмент расчёта удельного импульса ракетного двигателя. Данный инструмент поможет ускорить работу в области проектирования ракетных двигателей и создания новых топлив для ракетно-космической техники. Impulse.Predictor  характеризуется простотой в использованиии и высокой точностью предсказанных им значений.  
Для предсказания удельного импульса программе нужны всего лишь 2 параметра: химический состав топлива и коэффициент объёмного расширения рабочего тела. Получая на вход состав топлива, Impulse.Predictor преобразует эти данные в структуру SMART. Далее в работу вступает модель на основе алгоритмов машинного обучения Random Forest Regressor,  которая по исходным данным предсказывает значение удельного импульса ракетного двигателя. Абсолютная погрешность предсказаний данной модели составляет 20,02 секунды.
В процессе разработки Impulse.Predictor была составлена база данных ракетных топлив, опробованы 3 модели:
1. Random Forest Regressor;
2. Cat Boost Regressor;
3. KNeighbors Regressor
и 2-е комбинации дискрипторов:
1. "Fingerprint + коэффициент удельного расширения"
2. "RDKit + коэффициент объёмного расширения"
Лучший результата показала модель Random Forest Regressor, работающая на первой комбинации дискрипторов. Именно эта модель используется в Impulse.Predictor.

Данные сайт и модель созданы в рамках выполнения научно-исследовательской работы для олимпиады школьников "Шаг в будущее" секции "Инженерное дело".
Работу выполнил: Мирославлев Илья
Научный руководитель: Луканов Михаил
Сайт сверстал: Невмятуллин Руслан

Литература, использлованная в работе:
1. Алемасов В.Е. Теория ракетных двигателей.
2. Добровольский М.П. Житкостные ракетные двигатели. Основы проектирования.
3. Штехер М.С. Топлива и рабочие тела ракетных двигателей.
4. Паушкин Я.М. Ракетные топлива.
5. Егорычев В.С. Топлива химических ракетных двигателей.
6. Мелькумов Т.М. Ракетные двигатели.
7. Васильев А.П. Основы теории и расчёта жидкостных ракетных двигателей.