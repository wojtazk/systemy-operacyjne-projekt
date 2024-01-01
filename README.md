# Systemy Operacyjne - symulacja algorytmów planowania czasu procesora i zastępowania stron

by Wojciech Kowal

---

# Wybrane algorytmy

## Algorytmy planowania czasu procesora

### First Come First Serve (FCFS)

Algorytm First Come First Serve to jeden z najprostszych algorytmów planowania czasu procesora. W tym algorytmie procesy są wykonywane w kolejności, w jakiej zgłosiły się do systemu operacyjnego. Proces, który przybył jako pierwszy, zostaje wykonany jako pierwszy.

Algorytm FCFS nie uwzględnia priorytetów ani długości trwania procesów. Oznacza to, że jeśli jeden długi proces przybył jako pierwszy, to inne, krótsze procesy, które przybyły później, będą musiały czekać na swoją kolej, co może prowadzić do długiego czasu oczekiwania.

Ten algorytm jest prosty i łatwy do zrozumienia, ale może prowadzić do niesprawiedliwego podziału zasobów i długiego czasu oczekiwania dla niektórych procesów.

### Round-Robin (RR)

Algorytm Round-Robin to algorytm planowania czasu procesora, który przydziela każdemu procesowi określony czas procesora, zwany również "kwantem czasu" lub "kwantem czasu wykonywania". Zasada działania tego algorytmu polega na cyklicznym przypisywaniu kwantów czasu procesom w kolejności ich przybycia.

Kiedy proces otrzymuje swój kwant czasu, może być wykonywany przez ten określony czas. Jeśli proces nie zostanie zakończony po upływie kwantu czasu, jest przenoszony na koniec kolejki procesów gotowych, a następny proces otrzymuje swój kwant czasu.

Algorytm Round-Robin jest szczególnie przydatny w przypadku, gdy mamy wiele procesów o podobnym priorytecie i chcemy zapewnić sprawiedliwy podział zasobów. Dzięki temu żaden proces nie jest faworyzowany, a każdy proces otrzymuje okazję do wykonania.

Jeśli dobrany kwant czasu będzie zbyt długi to algorytm Round-Robin będzie w zasadzie działał jak FCFS. Dlatego trzeba go dobrać rozsądnie.

Algorytm Round-Robin jest szeroko stosowany w systemach operacyjnych ze względu na swoją prostotę i możliwość zapewnienia sprawiedliwego podziału czasu procesora.

## Algorytmy zastępowania stron

### First In, First Out (FIFO)

Algorytm First In, First Out to jeden z najprostszych algorytmów zastępowania stron w systemach operacyjnych. Zasada działania tego algorytmu polega na tym, że strona, która została załadowana jako pierwsza do pamięci fizycznej, zostaje wydalona jako pierwsza w przypadku konieczności zastąpienia strony.

Kiedy system operacyjny potrzebuje załadować nową stronę do pamięci fizycznej, ale nie ma już dostępnego miejsca, wybierana jest strona, która była w pamięci fizycznej najdłużej. Ta strona zostanie usunięta, aby zrobić miejsce dla nowej strony.

Algorytm FIFO nie uwzględnia żadnych czynników takich jak popularność strony czy jej ważność. Oznacza to, że strona, która jest używana intensywnie lub jest ważna dla działania programu, może zostać zastąpiona, nawet jeśli to może prowadzić do spadku wydajności.

Mimo pewnych wad, algorytm FIFO jest wciąż szeroko stosowany ze względu na swoją prostotę i przewidywalność działania.

### Least Frequently Used (LFU)

Algorytm Least Frequently Used to jeden z algorytmów zastępowania stron w systemach operacyjnych. Zasada działania tego algorytmu polega na zastępowaniu stron, które są używane najrzadziej.

Kiedy system operacyjny potrzebuje załadować nową stronę do pamięci fizycznej, ale nie ma już dostępnego miejsca, wybierana jest strona, która była używana najrzadziej. Oznacza to, że strony, do których liczba odwołań jest mała , są bardziej podatne na zastąpienie.

Algorytm LFU uwzględnia częstotliwość używania stron. Strona, do której jest więcej odwołań, ma większe szanse na pozostanie w pamięci fizycznej, ponieważ jest uznawana za ważniejszą.

W przypadku, gdy kilka stron ma taką samą najmniejszą częstotliwość używania, algorytm LFU może zastosować inne kryteria, takie jak czas, w którym strona została ostatnio użyta.

Algorytm LFU ma zaletę w przypadku, gdy niektóre strony są używane bardzo często, a inne bardzo rzadko. Dzięki temu możliwe jest skuteczne zarządzanie pamięcią fizyczną, aby utrzymać w niej najczęściej używane strony.

Jednak algorytm LFU ma pewne wady. Jeśli strona była używana często w przeszłości, ale przestała być używana, nadal może zajmować miejsce w pamięci fizycznej, ponieważ algorytm nie uwzględnia zmian w częstotliwości używania stron w czasie. Ponadto, algorytm LFU może być bardziej skomplikowany do zaimplementowania niż inne algorytmy zastępowania stron.

Mimo pewnych wad, algorytm LFU jest szeroko stosowany w systemach operacyjnych, szczególnie w przypadku, gdy ważne jest utrzymanie w pamięci fizycznej najczęściej używanych stron.

# Struktura plików projektu

- cpu_scheduling → folder z implementacjami algorytmów planowania czasu procesora
  - FCFS.py
  - Round_Robin.py
- page_replacement → folder z implementacjami algorytmów zastępowania stron
  - FIFO.py
  - LFU.py
- models → folder z klasami (modelami) Procesu i Strony
  - Process.py
  - Page.py
- simulation_sample_data → folder z danymi wejściowymi do symulacji
  - cpu_scheduling_sample_data.txt
  - page_replacement_sample_data.txt
- simulation_results → folder z wynikami symulacji algorytmów
  - FIFO_simulation_results.txt
  - Round-Robin*simulation_results_time_slice*[time_slice].txt
  - [algorithm]_simulation_results_page_frames_[page_frames] → dla FIFO i LFU
- simulation_results_calc → folder z obliczeniami do wyników symulacji
  - cpu_scheduling.xlsx
  - page_replacement.xlsx
- simulation_results_charts → folder z wykresami do wyników symulacji
  - [chart].png
- generateSampleData.py → plik źródlowy zawierający funkcje generujące dane testowe
- loadSampleData.py → plik źródłowy zawierający funkcje wczytujące dane testowe z plików
- helpers.py → plik źródłowy z funkcjami pomocniczymi
- main.py → główny plik programu
- README.md → sprawozdzanie w wersji markdown
- .gitignore

# Symulacja planowania czasu procesora

## Procedura testowania algorytmów

Liczba próbek: 100_000

Maksymalny czas wystąpienia procesu: 10_000

Maksymalny czas potrzebny do wykonania procesu: 5000

Kwanty czasu dla algorytmu Round-Robin: 10, 100, 1000, 4000

### Dane Wejściowe

Przykładowe dane wejściowe:

| Process | Arrival Time | Burts Time |
| ------- | ------------ | ---------- |
| P1      | 0            | 5          |
| P2      | 8            | 7          |

- `Process` → nazwa procesu (w mojej implementacji nazwa procesu będzie pominięta, nie jest niezbędna do symulacji)
- `Arrival Time` → czas wystąpienia procesu
- `Burst Time` → ilość czasu potrzebna do wykonania procesu przez CPU

Dane wejściowe bedą wygenerowane przez funkcję z generateSampleData.py i zapisane do pliku cpu_scheduling_sample_data.txt, w folderze simulation_sample_data.

### Dane wyjściowe

- `Arrival Time`
- `Burst TIme`
- `Completion Time` → czas, w którym proces skończył się wykonywać
- `Turn Around Time` →czas przez jaki process istnieje w systemie (Różnica między `Completion Time` i `Arrival Time`)
  - (`Turn Around Time` = `Completion Time` - `Arrival Time`)
- `Waiting Time` → czas w którym proces oczekiwał na wykonanie (Róźnica między `Turn Around Time` i `Burst Time`)
  - (`Waiting Time` = `Turn Around Time` - `Burst Time`)

Wyniki symulacji bedą wygenerowane przez funkcje z plików FCFS.py oraz Round-Robin.py i zapisane do plików FCFS*simulation_results.txt oraz Round-Robin_simulation_results_time_slice*[time_slice].txt, w folderze simulation_results.

### Porównywane Parametry

Pomiędzy algorytmami First Come First Serve **i** Round-Robin \*\*\*\*będą porównywane:

- `Turn Around Time`
- `Waiting Time`

Dla Round-Robin zmieniany będzie kwant czasu (`Time Slice` → cząstka czasu procesora przydzielana procesowi)

Obliczenia, wykresy i tabele będą znajdowały się w pliku: cpu_scheduling.xlsx, w folderze

simulation_results_calc

## Opracowanie wyników eksperymentów

| Algorithm                   | Turn Around Time avg | Turn Around Time median | Turn Around Time std | Waiting Time avg | Waiting Time median | Waiting Time std |
| --------------------------- | -------------------- | ----------------------- | -------------------- | ---------------- | ------------------- | ---------------- |
| FCFS                        | 125401118.2          | 125515211.5             | 72405869.24          | 125398610        | 125512171           | 72405869.12      |
| Round-Robin time slice 10   | 167543659.9          | 188895747               | 74780253.49          | 167541151.8      | 188893230.5         | 74778857.2       |
| Round-Robin time slice 100  | 167528446.1          | 188905632               | 74772360.63          | 167525937.9      | 188903088           | 74770964.87      |
| Round-Robin time slice 1000 | 165844759.1          | 186299549.5             | 74804966.61          | 165842250.9      | 186297219.5         | 74803626.03      |
| Round-Robin time slice 4000 | 145464683.8          | 150490709.5             | 79943773.96          | 145462175.6      | 150488564           | 79943149.21      |

![Turn Around Time chart](/simulation_results_charts/turn_around_time.png)

![Waiting Time chart](/simulation_results_charts/waiting_time.png)

### Wnioski

`Round-Robin` ma większy zarówno `Turn Around Time` jak i `Waiting Time`, co oznacza że procesy czekają dłużej na ich całkowite wykonanie niż w przypadku `FCFS`.

Średni czas oczekiwania procesów w `Round-Robin` dla kwantów czasu (`Time Slice`) 10, 100, 1000 był gorszy od średniego czasu oczekiwania w `FCFS` o około 33%, dla większych kwantów czasu ta różnica maleje bardziej maleje. Nie jest to ogromna różnica biorąc pod uwagę, że jeden długi proces w `Round-Robin` nie blokuje innych procesów.

W `Round-Robin` im kwant czasu jest większy tym bardziej zaczyna on przypominać `FCFS`. W moich danych testowych czas wykonywania procesu może być równy co najwyżej 5000, co za tym idzie jeśli ustawilibyśmy w `Round-Robin` kwant czasu na 5000, wtedy wyniki byłyby identyczne z wynikami `FCFS`. A więc dla odpowiednio dużego kwanty czasu `Round-Robin` będzie zachowywał się tak samo jak `FCFS`. To zachowanie widoczne jest na obu wykresach, im większy kwant czasu tym bardziej słupki `Round-Robina` przypominają te z `FCFS`.

Kiedy popatrzymy na dane wynikowe, to zaobserwujemy że w `FCFS` procesy które wykonały się jako pierwsze to te które wystąpiły jako pierwsze. Natomiast w przypadku `Round-Robin` faworyzowane są procesy wykonujące się w krótkim czasie.

`FCFS` (10 procesów które skończyły się wykonywać jako pierwsze)

| Arrival Time | Burst Time |
| ------------ | ---------- |
| 1            | 1797       |
| 1            | 1657       |
| 1            | 1196       |
| 1            | 2863       |
| 1            | 3864       |
| 1            | 4918       |
| 1            | 2875       |
| 1            | 4857       |
| 1            | 2558       |
| 1            | 33         |

<br>

`Round-Robin` time slice 100 (10 procesów które skończyły się wykonywać jako pierwsze)

| Arrival Time | Burst Time |
| ------------ | ---------- |
| 1            | 33         |
| 8            | 38         |
| 11           | 43         |
| 14           | 35         |
| 15           | 16         |
| 18           | 100        |
| 22           | 10         |
| 23           | 20         |
| 29           | 65         |
| 35           | 16         |

Ciężko jest jednoznacznie określić który algorytm jest lepszy. Wybór między First Come First Serve a Round-Robin zależy od tego co jest dla nas bardziej korzystne. `FCFS` jest prosty w implementacji i ma minimalne koszty, ale może prowadzić do długiego czasu oczekiwania dla procesów, które przybywają później. Z drugiej strony, `RR` zapewnia lepsze czasy odpowiedzi dla krótkich procesów i jest wygodny w użyciu w systemach typu time-sharing. Jednak ma on wyższe koszty ze względu na potrzebę rejestrowania upływu czasu i przełączanie procesów, co może powodować pogorszenie wydajności, gdy w systemie występuje wiele procesów.
Podsumowując, jeśli system wymaga prostego algorytmu planowania z minimalnymi kosztami, `FCFS` jest dobrym wyborem. Jednak jeśli system musi zapewnić lepsze czasy odpowiedzi dla krótkich procesów i jest zaprojektowany do time-sharingu, `RR` jest lepszym wyborem.

---

# Symulacja algorytmów zastępowania stron

## Procedura testowania algorytmów

Liczba próbek: 100_000

Pojemność pamięci: 1000, 2000, 5000, 10_000

Ilość stron: 10_000

### Dane wejściowe

Przykładowe dane wejściowe:

| Page Reference Number |
| --------------------- |
| 4                     |
| 7                     |
| 3                     |
| 4                     |

- `Page Reference Number` → numer strony która chcemy odczytać z pamięci

Każda strona na start ma częstotliwość występowania równą 0.

Dane wejściowe bedą wygenerowane przez funkcję z generateSampleData.py i zapisane do pliku page_replacement_sample_data.txt, w folderze simulation_sample_data.

### Dane wyjściowe

- `Page Faults` → ilość wczytań strony do pamięci

Wyniki symulacji bedą wygenerowane przez funkcje z plików FIFO.py oraz LFU.py i zapisane do plików [algorithm]_simulation_results_page_frames_[page_frames].txt, w folderze simulation_results.

### Porównywane Parametry

Pomiędzy algorytmami First In First Out i Least Frequenty Used \*\*\*\*będą porównywane:

- `Page Faults`

Podczas symulacji obu algorytmów zmieniana będzie pojemność pamięci (`Memory Capacity` → ilość stron mogących zmieścić się w pamięci)

Obliczenia, wykresy i tabele będą znajdowały się w pliku: page_replacement.xlsx, w folderze

simulation_results_calc

## Opracowanie wyników eksperymentów

| Algorithm              | Page Faults avg | Page Faults median | Page Faults std |
| ---------------------- | --------------- | ------------------ | --------------- |
| FIFO page frames 1000  | 9.0001          | 9                  | 2.724243012     |
| LFU page frames 1000   | 9.0064          | 9                  | 3.824390022     |
| FIFO page frames 2000  | 8.0194          | 8                  | 2.299091916     |
| LFU page frames 2000   | 8.0133          | 8                  | 4.192269446     |
| FIFO page frames 5000  | 5.1429          | 5                  | 1.186203857     |
| LFU page frames 5000   | 5.1281          | 4                  | 4.228769371     |
| FIFO page frames 10000 | 1               | 1                  | 0               |
| LFU page frames 10000  | 1               | 1                  | 0               |

![Page Faults chart](/simulation_results_charts/page_faults.png)

| Algorithm              | Page references | Page faults | Page hits | Page fault percentage |
| ---------------------- | --------------- | ----------- | --------- | --------------------- |
| FIFO page frames 1000  | 100000          | 90001       | 9999      | 90.001%               |
| LFU page frames 1000   | 100000          | 90064       | 9936      | 90.064%               |
| FIFO page frames 2000  | 100000          | 80194       | 19806     | 80.194%               |
| LFU page frames 2000   | 100000          | 80133       | 19867     | 80.133%               |
| FIFO page frames 5000  | 100000          | 51429       | 48571     | 51.429%               |
| LFU page frames 5000   | 100000          | 51281       | 48719     | 51.281%               |
| FIFO page frames 10000 | 100000          | 10000       | 90000     | 10.000%               |
| LFU page frames 10000  | 100000          | 10000       | 90000     | 10.000%               |

![Page Faults vs Page Hits chart](/simulation_results_charts/page_faults_page_hits.png)

![Page Faults Percentage chart](/simulation_results_charts/page_faults_percentage.png)

### Wnioski

W moich danych testowych, strony które chcemy wczytać występują mniej więcej z tą samą częstością, nie ma stron które byłyby dużo bardziej popularne od reszty. Może być to główną przyczyną dla której oba algorytmy mają wręcz identyczne wyniki. `LFU` powinien mieć przewagę nad `FIFO` jeśli procesy występowały by z różnymi częstościami.

Z wyników symulacji widać, że dla pamięci która mieści 1000 stron, w ok 90% przypadków strona nie była obecna w pamięci i trzeba było ją wczytać. Sytuacja zmienia się dla większej pojemności pamięci, wraz ze wzrostem pojemności pamięci spada ilość przypadków odwołań do strony której nie ma w pamięci. Jeśli pojemność pamięci jest równa lub większa niż liczba wszystkich stron to wtedy każda strona w momencie odwołania się do niej zostaje zapisana w pamięci i już tam zostanie, ponieważ nie trzeba zwalniać pamięci aby załadować nową stronę. Taka sytuacja drastycznie obniża liczbę przypadków, w których strona w momencie odwołania nie była obecna w pamięci. Dobrze ilustrują to wyniki dla obu algorytmów dla `page frames` równego 10_000, czyli pojemność pamięci jest równa maksymalnej liczbie wszystkich stron.

Ciężko jest jednoznacznie określić który algorytm jest lepszy. `FIFO` jest łatwiejszy do zaimplementowania, jednak nie bierze pod uwagę częstotliwości dostępu strony lub inncyh kryteriów mogących być ważne w pewnych sytuacjach. `LFU` wymaga prowadzenia “dzienniczka” z częstością stron, co może wykorzystywać dodatkowe zasoby systemu.

Nie ma uniwersalnej odpowiedzi, który algorytm jest lepszy, wybór często wiąże się z eksperymentowaniem i analizą, aby określić odpowiedni algorytm dla konkretnego systemu.

# Źródła

- [https://www.guru99.com/fcfs-scheduling.html](https://www.guru99.com/fcfs-scheduling.html)
- [https://www.geeksforgeeks.org/program-for-fcfs-cpu-scheduling-set-1/](https://www.geeksforgeeks.org/program-for-fcfs-cpu-scheduling-set-1/)
- [https://www.geeksforgeeks.org/program-for-fcfs-cpu-scheduling-set-2-processes-with-different-arrival-times/](https://www.geeksforgeeks.org/program-for-fcfs-cpu-scheduling-set-2-processes-with-different-arrival-times/)
- [https://www.guru99.com/round-robin-scheduling-example.html](https://www.guru99.com/round-robin-scheduling-example.html)
- [https://www.geeksforgeeks.org/program-for-round-robin-scheduling-for-the-same-arrival-time/](https://www.geeksforgeeks.org/program-for-round-robin-scheduling-for-the-same-arrival-time/)
- [https://www.geeksforgeeks.org/round-robin-scheduling-with-different-arrival-times/](https://www.geeksforgeeks.org/round-robin-scheduling-with-different-arrival-times/)
- [https://www.javatpoint.com/round-robin-program-in-c](https://www.javatpoint.com/round-robin-program-in-c)
- [https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/](https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/)
- [https://www.geeksforgeeks.org/page-faults-in-lfu-implementation/](https://www.geeksforgeeks.org/page-faults-in-lfu-implementation/)
- [https://www.javatpoint.com/lru-vs-lfu-page-replacement-algorithm](https://www.javatpoint.com/lru-vs-lfu-page-replacement-algorithm)
