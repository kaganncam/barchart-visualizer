Kütüphaneler

    time: Zamanla ilgili işlemler için kullanılır (bu kodda kullanılmamış).

    binance.spot.Spot: Binance API'sine bağlanmak ve veri çekmek için kullanılır.

    matplotlib.pyplot: Grafik çizmek için kullanılır.

Değişkenler

    api_key: Binance API anahtarınız.

    api_secret: Binance API gizli anahtarınız.

    limit: Çekilecek mum (candlestick) sayısı (burada 50 olarak ayarlanmış).

fetch() Fonksiyonu

Bu fonksiyon, Binance API'sinden veri çeker ve bu verileri işler.

    Binance API Bağlantısı:
    python
    Copy

    client = Spot(api_key, api_secret)

        Spot sınıfı, Binance API'sine bağlanmak için kullanılır.

    Veri Çekme:
    python
    Copy

    data = client.klines("BTCUSDT", "1m", limit=limit)

        klines metodu, BTCUSDT çiftinin 1 dakikalık mum verilerini çeker.

        limit=50 parametresi, son 50 mum verisini alır.

    Veri İşleme:

        highest: Her bir mumun en yüksek fiyatı.

        lowest: Her bir mumun en düşük fiyatı.

        open_price: Her bir mumun açılış fiyatı.

        close_price: Her bir mumun kapanış fiyatı.

        volume: Her bir mumun işlem hacmi.

        height: Her bir mumun yüksekliği (açılış ve kapanış fiyatı arasındaki fark).

        low_point: Her bir mumun başlangıç noktası (açılış ve kapanış fiyatının minimumu).

        highest_lowest_difference: Her bir mumun en yüksek ve en düşük fiyatı arasındaki fark.

        x: Zaman ekseni için bir aralık (0'dan limit'e kadar).

        color: Mumun rengi (yeşil: kapanış > açılış, kırmızı: kapanış < açılış).

    Döndürülen Değerler:
    python
    Copy

    return x, height, low_point, color, highest, lowest, volume

main() Fonksiyonu

Bu fonksiyon, fetch() fonksiyonundan gelen verileri kullanarak grafik çizer.

    Veri Alma:
    python
    Copy

    x, height, low_point, color, highest, lowest, volume = fetch()

    Grafik Oluşturma:

        fig, ax = pyplot.subplots(): Grafik penceresi oluşturulur.

        ax.bar(): Mumların gövdesini çizer (renkler ve yükseklikler belirlenir).

        ax.vlines(): Mumların fitillerini (en düşük ve en yüksek fiyatlar arasındaki çizgiler) çizer.

        ax.set_ylim(): Grafiğin y ekseni sınırlarını belirler.

        ax.legend(): Grafiğe bir açıklama (legend) ekler.

        pyplot.show(): Grafiği gösterir.

Ana Program

    main() fonksiyonu çağrılarak program çalıştırılır.

Özet

Bu kod, Binance API'sinden BTCUSDT çiftinin son 50 dakikalık mum verilerini çeker ve bu verileri kullanarak bir mum grafiği (candlestick chart) çizer. Grafik, yeşil ve kırmızı renklerle yükseliş ve düşüşleri gösterir.
