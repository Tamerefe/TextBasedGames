import java.util.Scanner;

public class storyturkish {
    public static void startGameTurkish(Scanner scanner) {

        System.out.println("\033[1;33mAdınız nedir?\033[0m");
        System.out.print(">> ");
        String playerName = scanner.nextLine();

        System.out.println("\n\033[1;32mMerhaba, " + playerName
                + ". Karanlık bir ormanda kim olduğunuzu hatırlamadan uyanıyorsunuz.\033[0m");
        System.out.println("\033[1;32mÖnünüzde iki yol var: biri sisli bir patika, diğeri eski bir taş köprü.\033[0m");
        System.out.println("\033[1;33mHangi yolu seçiyorsunuz?\033[0m (1: Sisli Patika / 2: Taş Köprü)");

        System.out.print(">> ");
        int choice = scanner.nextInt();
        scanner.nextLine();

        if (choice == 1) {
            mistyPathTurkish(scanner);
        } else if (choice == 2) {
            stoneBridgeTurkish(scanner);
        } else {
            System.out.println("\033[1;31mGeçersiz seçim. Gölgeler sizi yutuyor...\033[0m");
        }
    }

    public static void mistyPathTurkish(Scanner scanner) {
        System.out.println("\033[1;32mSisli patikada yürüyorsunuz, çevrenizi zar zor görebiliyorsunuz.\033[0m");
        System.out.println(
                "\033[1;32mAniden, karşınıza eski bir kulübe çıkıyor. İçeri girmek ister misiniz?\033[0m (1: Evet / 2: Hayır)");

        System.out.print(">> ");
        int choice = scanner.nextInt();

        if (choice == 1) {
            System.out.println(
                    "\033[1;32mKulübeye adım atıyorsunuz ve eski bir kitap buluyorsunuz. Kitabı açtığınızda, anılarınız geri gelmeye başlıyor...\033[0m");
            System.out.println(
                    "\033[1;32mKitap, ormanın kalbinde gizli bir tapınaktan bahsediyor. İpuçlarını takip ediyor musunuz?\033[0m (1: Evet / 2: Hayır)");
            System.out.print(">> ");
            choice = scanner.nextInt();

            if (choice == 1) {
                System.out.println(
                        "\033[1;32mOrmanın derinliklerine doğru yolculuk yapıyorsunuz, garip semboller ve harabelerle karşılaşıyorsunuz.\033[0m");
                System.out.println(
                        "\033[1;32mTapınağı buluyorsunuz, ancak gölgeli bir muhafız girişini engelliyor.\033[0m");
                System.out.println(
                        "\033[1;33mMuhafıza meydan mı okuyorsunuz yoksa gizlice geçmeye mi çalışıyorsunuz?\033[0m (1: Meydan Oku / 2: Gizlice Geç)");
                System.out.print(">> ");
                choice = scanner.nextInt();

                if (choice == 1) {
                    System.out.println(
                            "\033[1;32mCesurca savaşıyorsunuz ve muhafızı yeniyorsunuz. İçeride, ailenizin resimlerini buluyorsunuz ve kimliğinize dair yazılmış yazılar olduğunu görüyorsunuz bu ipuçlarını takip edecek misiniz?\033[0m (1: Takip Et / 2: Resimleri Yakınız)");
                    System.out.print(">> ");
                    choice = scanner.nextInt();
                    if (choice == 1) {
                        System.out.println(
                                "\033[1;32mIpuçları sizi bir adaya götürüyor, kayıp anılarınızı ve kimliğinizi buluyorsunuz. Kazandınız!\033[0m");
                        System.out.println("\033[1;32mKazandınız!\033[0m");
                    } else {
                        System.out.println(
                                "\033[1;31mResimleri yakıyorsunuz ve tapınak yıkılıyor. Gölgeler sizi yutuyor ve sonsuza kadar kayboluyorsunuz...\033[0m");
                        System.out.println("\033[1;31mOyun Bitti.\033[0m");
                    }
                } else {
                    System.out.println(
                            "\033[1;31mGizlice girmeye çalışıyorsunuz ama başarısız oluyorsunuz. Muhafız sizi gölgelere sürgün ediyor...\033[0m");
                    System.out.println("\033[1;31mOyun Bitti.\033[0m");
                }
            } else {
                System.out.println(
                        "\033[1;31mİpuçlarını görmezden geliyorsunuz ve kulübeyi terk ediyorsunuz. Gölgeler sonunda sizi buluyor...\033[0m");
                System.out.println("\033[1;31mOyun Bitti.\033[0m");
            }
        } else {
            System.out.println(
                    "\033[1;31mİçeri girmemeye karar veriyorsunuz ve uzaklaşıyorsunuz. Ancak, gölgeler sizi yutuyor...\033[0m");
            System.out.println("\033[1;31mOyun Bitti.\033[0m");
        }
    }

    public static void stoneBridgeTurkish(Scanner scanner) {
        System.out.println("\033[1;32mEski taş köprüyü geçerken, ortasında gölgeli bir figür beliriyor.\033[0m");
        System.out
                .println("\033[1;32mFigür size kim olduğunuzu soruyor. Yanlış cevap verirseniz, köprü çökecek.\033[0m");
        System.out.println("\033[1;33mCevabınız nedir?\033[0m (1: Bilinmeyen Gezgin / 2: Gölge Avcısı)");

        System.out.print(">> ");
        int choice = scanner.nextInt();

        if (choice == 1) {
            System.out.println(
                    "\033[1;32mGölge, sizi tanıyormuş gibi başını sallıyor ve kayboluyor. Köprüyü güvenle geçiyorsunuz ve unutulmuş bir köy buluyorsunuz.\033[0m");
            System.out.println(
                    "\033[1;32mKöylüler sizi tanıyor gibi görünüyor. Sizi geçmişinizi açıklayan bir yaşlıya götürüyorlar.\033[0m");
            System.out.println(
                    "\033[1;33mDaha fazla bilgi edinmek için kalıyor musunuz yoksa yolculuğunuza devam mı ediyorsunuz?\033[0m (1: Kal / 2: Devam Et)");
            System.out.print(">> ");
            choice = scanner.nextInt();

            if (choice == 1) {
                System.out.println(
                        "\033[1;32mYaşlı, Gölge Diyarının kayıp muhafızı olduğunuzu ortaya çıkarıyor! Bu yetenekleriniz ile ne yapacaksınız?\033[0m (1: Koru / 2: Yok Et)");
                System.out.print(">> ");
                choice = scanner.nextInt();
                if (choice == 1) {
                    System.out.println(
                            "\033[1;32mKöyü koruyorsunuz ve halk size minnettar. Kayıp kimliğinizi buluyorsunuz ve gerçek bir kahraman oluyorsunuz!\033[0m");
                    System.out.println("\033[1;32mKazandınız!\033[0m");
                } else {
                    System.out.println(
                            "\033[1;31mKöyü yok ediyorsunuz ve gölgeler sizi yutuyor. Sonsuza kadar kayboluyorsunuz...\033[0m");
                    System.out.println("\033[1;31mOyun Bitti.\033[0m");
                }
            } else {
                System.out.println(
                        "\033[1;31mYolculuğunuza devam ediyorsunuz ama gerçek bir sır olarak kalıyor. Sonsuza kadar gölgelerde yaşıyorsunuz...\033[0m");
                System.out.println("\033[1;31mOyun Bitti.\033[0m");
            }
        } else {
            System.out.println(
                    "\033[1;31mGölge sizi bir tehdit olarak algılıyor ve köprüyü parçalıyor! Uçuruma düşüyorsunuz...\033[0m");
            System.out.println("\033[1;31mOyun Bitti.\033[0m");
        }
    }
}