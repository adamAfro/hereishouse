# hereishouse

## Różne parametry

Dane `train.csv` mają zmienne parametry w jakimś tam formacie. W pliku `parse_params.py` jest funkcja
`parse`, która zwraca ramkę z tymi parametrami i `id`, 

```py
from pandas import read_csv
import params

df = read_csv("dane/train.csv")
df_parametry = params.parse(df)
```

Ewentualnie można bezpośrednio z pliku: `params.from_file("dane/train.csv")`

### Uwagi

Niektóre parametry są zerojedynkowe, np.: `heating_types_gas`, czyli ogrzewania gazowe, a samo
ogrzewanie jest też oddzielną zmienną kategoryczną `heating`. 

Czyli w teorii(!) może być tak, że 
- ogrzewanie `heating` jest zaznaczone jako gazowe, a jednocześnie są inne ogrzewania, np. `heating_types_coal` = 1
- ogrzewanie `heating` jest nie zaznaczone, ale są inne ogrzewania np. `heating_types_gas`
- ogrzewanie `heating` jest nie zaznaczone, i wyklucza inne ogrzewania `heating_types_` - wszystkie muszą być 0
- ogrzewanie `heating` jest wykluczone, bo są inne ogrzewania `heating_types_`

I nie dotyczy to samego `heating`, bo mogą być (chyba, nie patrzyłem) też inne zmienne `cośtam_types_`, 
które mają też po prostu odpowiednik `cośtam`.