import matplotlib.pyplot as plt
import pandas as pd

# GraphicsHelper sınıfı, verilen verilerden grafikler oluşturmak için kullanılır.
class GraphicsHelper:
    def __init__(self, data):
        self.data = data
        self.status_counts = self.data['Status'].value_counts()
    
    # Görevlerin tamamlanma durumlarını gösteren bir pasta grafiği oluşturur.
    def PieGraphic(self):
        plt.pie(self.status_counts, 
                labels=self.status_counts.index.map({0: 'Tamamlanmadı', 1: 'Tamamlandı'}),
                autopct='%1.1f%%',  # Dilimlerin yüzdelerini bir ondalık basamakla gösterir.
                startangle=90,      # Grafiği 90 dereceden başlatır.
                colors=['red', 'blue'])
        plt.title('Görevlerin Tamamlanma Durumları - Pasta Grafiği')
        plt.show()

    # Görevlerin tamamlanma durumlarını gösteren bir histogram grafiği oluşturur.
    def HistogramGraphic(self):
        self.data['Status'].plot(kind='hist',
                                 bins=3,  # Kaç adet sütun olacağını belirler.
                                 color='blue', 
                                 alpha=0.7) # Sütunların saydamlığını belirler.
        plt.xticks(ticks=[0, 1], labels=['Tamamlanmadı', 'Tamamlandı'])
        plt.xlabel('Durum')
        plt.ylabel('Görev Sayısı')
        plt.title('Görevlerin Tamamlanma Durumları - Histogram Grafiği')
        plt.show()

    # Görevlerin tamamlanma durumlarını gösteren bir saçılma grafiği oluşturur.
    def ScatterGraphic(self):
        plt.scatter(self.data.index, self.data['Status'], color='b', alpha=0.7)
        plt.yticks(ticks=[0, 1], labels=['Tamamlanmadı', 'Tamamlandı'])
        plt.xlabel('Görev')
        plt.ylabel('Durum')
        plt.title('Görevlerin Tamamlanma Durumları - Saçılma Grafiği')
        plt.show()