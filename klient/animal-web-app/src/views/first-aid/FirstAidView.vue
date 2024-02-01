<script setup lang="ts">
import { ref, computed } from "vue";

const searchTerm = ref("");

const foreignBodies = [
  {
    id: 1,
    title: "Zatrucie",
    text:
      "W przypadku połknięcia przez zwierzaka szkodliwych substancji, natychmiast kontaktuj się z weterynarzem.\n" +
      "Podaj zwierzakowi węgiel aktywny na zalecenie weterynarza i szybko jedź do lecznicy.\n" +
      "Zabierz opakowanie trującej substancji oraz zabezpiecz wymiociny zwierzaka, używając gumowych rękawic.\n" +
      "Nie wywołuj wymiotów u zwierzaka.\n" +
      "W przypadku pogorszenia stanu zwierzaka, niezwłocznie zawieź go do weterynarza.\n" +
      "Podczas transportu otul zwierzaka ciepłym kocem i zadbaj o jego bezpieczeństwo, szczególnie w przypadku drgawek.",
  },
  {
    id: 2,
    title: "Rany kłute",
    text:
      "Jeśli zwierzak dozna urazu przez gałąź, szprychę rowerową czy patyk, na przykład przebicia żeber, natychmiast uspokój go i sprawdź, co się stało, trzymając go na smyczy.\n" +
      "Nie próbuj samodzielnie usuwać ciała obcego, aby uniknąć poważnego krwawienia i ryzyka wykrwawienia zwierzaka.\n" +
      "W niektórych przypadkach zabezpiecz uraz bandażem lub torbą.\n" +
      "W przypadku wstrząsu ułóż zwierzaka w bezpiecznej pozycji bocznej, przykryj termicznym kocem i szybko skonsultuj się z weterynarzem lub udaj się do kliniki.",
  },
  {
    id: 3,
    title: "Połknięcie ciała obcego",
    text:
      "Jeśli zwierzak połknął zabawkę lub inny przedmiot, natychmiast skontaktuj się z weterynarzem i zawieź zwierzaka do lecznicy.\n" +
      "Nie próbuj samodzielnie wywoływać wymiotów u zwierzaka, ponieważ może to pogorszyć sytuację lub doprowadzić do zadławienia się zwierzęcia.",
  },
];

const fracturesAndSprains = [
  {
    id: 4,
    title: "Złamanie lub pęknięcie",
    text:
      "W przypadku upadku zwierzaka z wysokości lub wypadku, który może spowodować złamania lub pęknięcia kończyn, zwróć uwagę na silną kulawiznę i nietypowe ułożenie nogi.\n" +
      "Jeśli podejrzewasz złamanie, staraj się jak najmniej ruszać kontuzjowaną kończynę. W razie potrzeby zastosuj prowizoryczną szynę.\n" +
      "Przenoś zwierzaka ostrożnie, tak aby kontuzjowana kończyna była od Ciebie odwrócona. Jeśli zwierzak jest w stanie iść samodzielnie, zrób nosidło, które ułatwi mu poruszanie się.\n" +
      "Po dotarciu do samochodu, połóż zwierzaka i niezwłocznie zawieź go do weterynarza na prześwietlenie i dalsze leczenie.",
  },
  {
    id: 5,
    title: "Złamanie otwarte",
    text:
      "W przypadku złamania otwartego, gdzie kość przerywa ciągłość skóry, skoncentruj się na zatamowaniu silnego krwawienia, najlepiej z użyciem opaski uciskowej.\n" +
      "Nie aplikuj szyny na otwarte złamanie, aby uniknąć dodatkowego bólu.\n" +
      "Uspokój zwierzaka i w przypadku objawów wstrząsu, ułóż go w pozycji bocznej bezpiecznej.\n" +
      "Zastosuj sterylny opatrunek i luźno załóż bandaż, aby ochronić ranę przed zabrudzeniem.\n" +
      "Przenoś zwierzaka tak, aby kontuzjowana kończyna była zwrócona od Ciebie i mogła swobodnie zwisać.",
  },
];

const wounds = [
  {
    id: 6,
    title: "Opatrzenie rany bez obfitego krwawienia",
    text:
      "W przypadku lekkich ran lub skaleczeń, które nie krwawią lub krwawią nieznacznie, przyłóż sterylny opatrunek i zabandażuj ranę, unikając stosowania maści.\n" +
      "Zastosuj specjalne opatrunki dostosowane do lokalizacji urazu, na przykład na łapę w przypadku uszkodzeń pazurów lub opuszek.\n" +
      "Używaj prostych technik, aby łatwiej założyć opatrunek, szczególnie przy mniejszych urazach.\n" +
      "U psów krótkowłosych, bandaż na ogon może być potrzebny do ochrony zranionej końcówki ogona przed wizytą u weterynarza, zwłaszcza jeśli wystąpią rany tłuczone lub cięte spowodowane silnym merdaniem ogonem.",
  },
  {
    id: 7,
    title: "Opatrzenie rany z obfitym krwawieniem",
    text:
      "W przypadku krwawiących urazów, delikatnie uciskaj miejsce rany, aby zatrzymać krwawienie z mniejszych naczyń.\n" +
      "Jeśli rana jest duża lub obejmuje większe naczynia, zastosuj opatrunek uciskowy.\n" +
      "W przypadku intensywnie krwawiących ran kończyn lub ogona, użyj opaski uciskowej.\n" +
      "Dla krwawiących ran na uszach, należy zaaplikować specjalny opatrunek, który zapewni stabilność i efektywną hemostazę.",
  },
  {
    id: 8,
    title: "Rany po ukąszeniu",
    text:
      "Rany kąsane mogą być poważniejsze i głębsze niż wyglądają, zwłaszcza jeśli doszło do potrząsania przez gryzącego zwierzaka.\n" +
      "Oczyść powierzchownie ranę, zabezpiecz ją opatrunkiem.\n" +
      "Szybko zabierz zwierzaka do weterynarza, który oceni głębokość obrażeń i zdecyduje o potrzebie zabiegu chirurgicznego.",
  },
  {
    id: 9,
    title: "Urazy oczu",
    text:
      "Urazy oczu są zawsze pilnym przypadkiem i wymagają natychmiastowej konsultacji z weterynarzem.\n" +
      "Opóźnienie wizyty u lekarza może skutkować utratą wzroku zwierzaka.\n" +
      "Nigdy nie stosuj domowych środków przy urazach oczu.",
  },
];

const apathy = [
  {
    id: 10,
    title: "Silna apatia, śpiączka lub paraliż",
    text:
      "W przypadku paraliżu lub śpiączki u zwierzaka, najpierw zatamuj ewentualne krwawienia.\n" +
      "Połóż zwierzę w bezpiecznej pozycji bocznej, zabezpieczając jego drogi oddechowe.\n" +
      "Okryj zwierzaka kocem, aby zapobiec utracie ciepła.\n" +
      "Niezwłocznie zawieź zwierzę do najbliższego gabinetu weterynaryjnego lub kliniki.",
  },
  {
    id: 11,
    title: "Zatrzymanie oddechu",
    text:
      "Zachowaj spokój, gdy pies przestanie oddychać po wypadku.\n" +
      "Usiądź przed zwierzakiem, zwracając jego nos w Twoją stronę.\n" +
      "Zamknij jego pysk jedną ręką, a drugą utwórz pierścień wokół nosa.\n" +
      "Delikatnie wdmuchuj powietrze do nozdrzy, obserwując podnoszenie się klatki piersiowej. Poproś kogoś o pomoc w tej obserwacji.\n" +
      "Wdmuchuj powietrze co trzy sekundy, wykonując 20 do 30 oddechów na minutę.\n" +
      "Co trzeci oddech sprawdzaj, czy pies wznowił oddychanie.\n" +
      "Regularnie sprawdzaj puls psa, aby monitorować jego krążenie.",
  },
  {
    id: 12,
    title: "Zatrzymanie akcji serca",
    text:
      "Rozpocznij reanimację tylko jeśli serce zwierzaka przestało bić. Nigdy nie ćwicz na zdrowym zwierzaku.\n" +
      "Upewnij się, że:\n" +
      "\n" +
      "Brak pulsu lub wyczuwalnych uderzeń serca.\n" +
      "Klatka piersiowa nie porusza się.\n" +
      "Pysk lub język są nieruchome.\n" +
      "Zwierzak nie reaguje na głos.\n" +
      "Zwierzak nie reaguje na bodźce bólowe, np. szczypanie ucha.\n" +
      "Jeśli występują wszystkie te objawy, rozpocznij masaż serca:\n" +
      "Ułóż zwierzaka płasko na prawym boku w bezpiecznej pozycji.\n" +
      "Wyciągnij głowę zwierzaka, tworząc przedłużenie kręgosłupa i otwórz jego pysk.\n" +
      "Połóż obie ręce na klatce piersiowej w okolicy serca, tuż za lewym łokciem dla większych zwierzaków. U mniejszych zwierzaków lub szczeniąt, użyj dwóch lub trzech palców, lub jednej ręki.\n" +
      "Uciskaj klatkę piersiową raz na sekundę, następnie zwolnij nacisk.\n" +
      "U dużych zwierzaków wtłaczaj powietrze co dziesiąty ucisk. U mniejszych, samo uciskanie klatki piersiowej może dostarczyć powietrze do płuc.",
  },
];

const filteredFracturesAndSprains = computed(() => {
  return fracturesAndSprains.filter(
    (item) =>
      item.title.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
      item.text.toLowerCase().includes(searchTerm.value.toLowerCase()),
  );
});

const filteredForeignBodies = computed(() => {
  return foreignBodies.filter(
    (item) =>
      item.title.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
      item.text.toLowerCase().includes(searchTerm.value.toLowerCase()),
  );
});

const filteredWounds = computed(() => {
  return wounds.filter(
    (item) =>
      item.title.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
      item.text.toLowerCase().includes(searchTerm.value.toLowerCase()),
  );
});

const filteredApathy = computed(() => {
  return apathy.filter(
    (item) =>
      item.title.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
      item.text.toLowerCase().includes(searchTerm.value.toLowerCase()),
  );
});
</script>

<template>
  <div
    class="bg-[#F1F1F1] h-screen w-screen p-10 flex flex-col overflow-y-auto"
  >
    <div class="flex">
      <v-text-field
        label="Wyszukaj pomocy "
        variant="outlined"
        bg-color="#fff"
        v-model="searchTerm"
      ></v-text-field>
    </div>
    <div
      class="p-4 bg-sky-200 border rounded-2xl flex flex-col w-full shadow-xl"
    >
      <p class="font-extrabold text-sky-900">
        Wskazwówki pierwszej pomocy dla zwierząt
      </p>
      <ul class="list-disc px-4 py-3 text-sky-900 font-semibold">
        <li class="py-1">Zachowaj spokój</li>
        <li class="py-1">Miej pod ręką numer do weterynarza</li>
        <li class="py-1">Zabezpiecz zwierzę smyczą</li>
        <li class="py-1">
          Zabezpiecz siebie - załóż zwierzęciu prowizoryczny kaganiec
        </li>
        <li class="py-1">Uspokój zwierzę</li>
      </ul>
      <p>
        Źrodło informacji :
        <a
          href="https://www.zooplus.pl/magazyn/psy/zdrowie-pielegnacja-psa/pierwsza-pomoc-dla-psa"
          >https://www.zooplus.pl</a
        >
      </p>
    </div>
    <div>
      <p class="text-[22px] font-bold pt-4 text-sky-800">
        Ciała obce w ciele zwierzęcia
      </p>
      <v-expansion-panels class="pt-3">
        <v-expansion-panel
          v-for="item in filteredForeignBodies"
          :key="item.id"
          :title="item.title"
          :text="item.text"
          class="font-semibold"
        >
        </v-expansion-panel>
      </v-expansion-panels>
      <p class="text-[22px] font-bold pt-8 text-sky-800">
        Złamania lub pęknięcia
      </p>
      <v-expansion-panels class="pt-3">
        <v-expansion-panel
          v-for="item in filteredFracturesAndSprains"
          :key="item.id"
          :title="item.title"
          :text="item.text"
          class="font-semibold"
        >
        </v-expansion-panel>
      </v-expansion-panels>
      <p class="text-[22px] font-bold pt-8 text-sky-800">
        Zwierze jest nieprzytomne
      </p>
      <v-expansion-panels class="pt-3">
        <v-expansion-panel
          v-for="item in filteredApathy"
          :key="item.id"
          :title="item.title"
          :text="item.text"
          class="font-semibold"
        >
        </v-expansion-panel>
      </v-expansion-panels>
    </div>
  </div>
</template>
