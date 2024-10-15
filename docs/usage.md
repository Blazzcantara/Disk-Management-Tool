# Verwendung des Disk Management Tools

## Grafische Benutzeroberfläche (GUI)

Um die grafische Benutzeroberfläche zu starten, führen Sie die Datei `main.py` aus:

```
python main.py
```

In der GUI können Sie:
1. Eine Partition aus dem Dropdown-Menü auswählen.
2. Auf "Analyze Disk" klicken, um die Analyse durchzuführen.
3. Die Ergebnisse im Textfeld anzeigen lassen.

## Kommandozeilen-Nutzung

Für eine Analyse über die Kommandozeile können Sie das Modul `disk_analyzer.py` direkt verwenden:

```python
from src.disk_analyzer import analyze_disk, list_partitions

# Verfügbare Partitionen anzeigen
print("Verfügbare Partitionen:", list_partitions())

# Analyse der Haupt-Partition durchführen
print(analyze_disk())

# Analyse einer spezifischen Partition durchführen
print(analyze_disk("/path/to/partition"))
```