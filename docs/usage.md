# Verwendung des Disk Management Tools

## Disk-Analyse

Um eine Disk-Analyse durchzuführen, verwenden Sie das Modul `disk_analyzer.py`:

```python
from src.disk_analyzer import analyze_disk, list_partitions

# Verfügbare Partitionen anzeigen
print("Verfügbare Partitionen:", list_partitions())

# Analyse der Haupt-Partition durchführen
print(analyze_disk())

# Analyse einer spezifischen Partition durchführen
print(analyze_disk("/path/to/partition"))
```

Die Funktion `analyze_disk()` gibt Informationen über den Gesamtspeicher, den verwendeten Speicher und den freien Speicher der angegebenen Partition zurück.