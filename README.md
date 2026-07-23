# Morse Code Converter

Μια εφαρμογή μετατροπής κειμένου σε κώδικα Μορς και αντίστροφα, γραμμένη σε Python. Διαθέτει τόσο **desktop GUI** (Tkinter) όσο και **web διεπαφή** (Flask).

## Χαρακτηριστικά

- Κωδικοποίηση (**encode**) κειμένου σε κώδικα Μορς
- Αποκωδικοποίηση (**decode**) κώδικα Μορς σε κείμενο
- Υποστήριξη γραμμάτων, αριθμών και σημείων στίξης
- Διαχωρισμός λέξεων με `/` ή τριπλό κενό
- Γραφικό περιβάλλον (GUI) με Tkinter
- Web εφαρμογή με Flask

## Δομή του project

```
├── __init__.py
├── application.py   # Flask web εφαρμογή
├── encoder.py        # Λογική κωδικοποίησης κειμένου → Μορς
├── decoder.py         # Λογική αποκωδικοποίησης Μορς → κείμενο
├── gui.py             # Desktop εφαρμογή με Tkinter
└── requirements.txt
```

## Προαπαιτούμενα

- Python 3.10 ή νεότερη έκδοση
- Για το GUI σε Linux, ίσως χρειαστεί να εγκαταστήσετε ξεχωριστά το Tkinter:
  ```bash
  sudo apt install python3-tk
  ```

## Εγκατάσταση

1. Κλωνοποιήστε το repository:
   ```bash
   git clone <URL_του_repository>
   cd <όνομα_φακέλου>
   ```

2. Δημιουργήστε virtual environment (προαιρετικό αλλά συνιστάται):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Εγκαταστήστε τις εξαρτήσεις:
   ```bash
   pip install -r requirements.txt
   ```

## Εκτέλεση

### Web εφαρμογή (Flask)

```bash
python application.py
```

Η εφαρμογή θα τρέχει στο `http://127.0.0.1:5000`.

### Desktop εφαρμογή (Tkinter GUI)

```bash
python gui.py
```

## Παράδειγμα χρήσης

```python
from encoder import encode
from decoder import decode

encode("SOS")        # → "... --- ..."
decode("... --- ...") # → "SOS"
```

## Άδεια χρήσης

Το project διανέμεται ελεύθερα για εκπαιδευτικούς σκοπούς.
