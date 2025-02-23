Kod Açıklaması
fetch() Fonksiyonu

    Binance API'sinden son 50 dakikalık BTCUSDT verilerini çeker.

    Verileri işler ve aşağıdaki bilgileri döndürür:

        x: Zaman ekseni için aralık.

        height: Her bir mumun yüksekliği.

        low_point: Her bir mumun başlangıç noktası.

        color: Mumun rengi (yeşil veya kırmızı).

        highest: Her bir mumun en yüksek fiyatı.

        lowest: Her bir mumun en düşük fiyatı.

        volume: Her bir mumun işlem hacmi.

main() Fonksiyonu

    matplotlib kütüphanesini kullanarak mum grafiğini çizer.

    Yeşil renkli mumlar, kapanış fiyatının açılış fiyatından yüksek olduğunu (yükseliş) gösterir.

    Kırmızı renkli mumlar, kapanış fiyatının açılış fiyatından düşük olduğunu (düşüş) gösterir.


BTCUSDT Candlestick Chart
Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.

Not: Bu proje eğitim amaçlıdır ve herhangi bir yatırım tavsiyesi içermez. Kullanmadan önce kendi araştırmanızı yapın.
