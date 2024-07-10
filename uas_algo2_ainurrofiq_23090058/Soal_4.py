# Kelas Parent Buah
class Buah:
    def __init__(self, warna, rasa):
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f"Buah: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"
# Kelas Child Mangga
class Mangga(Buah):
    def __init__(self, warna, rasa, vitamin):
        super().__init__(warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        parent_info = super().information()
        return f"{parent_info}, Vitamin: {self.vitamin}"

mangga1 = Mangga(warna="Kuning", rasa="Manis", vitamin="Vitamin C")

mangga1.setNama("Mangga Harum Manis")

print(mangga1.information())
