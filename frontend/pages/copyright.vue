<template>
  <v-container>
    <v-container fluid>
      <v-card>
        <v-toolbar
          flat
          color="success"
        >
          <v-toolbar-title class="headline font-weight-regular white--text">
            <v-icon dark>
              mdi-copyright
            </v-icon>
            Для правообладателей
          </v-toolbar-title>
        </v-toolbar>
        <v-card-title>
          О сервисе
        </v-card-title>
        <v-card-text>
          Сервис
          <nuxt-link :to="'/'">manga-exchange.ru</nuxt-link>
          - это клуб любителей манги, где пользователи предоставляют свои переводы манги,
          получая
          возможность загружать и читать мангу и делится ею с другими членами клуба.
        </v-card-text>
        <v-card-title>
          Защита авторских прав
        </v-card-title>
        <v-card-text>
          Мы соблюдаем Закон о защите авторских прав в цифровую эпоху (DMCA) и другие действующие законы об авторских
          правах и
          быстро удаляем неправомерно размещенные переводы манги, получив соответствующее уведомление о нарушении прав.
        </v-card-text>
        <v-card-title>
          Уведомление о нарушении авторских прав
        </v-card-title>
        <v-card-text>
          Если вы считаете, что перевод манги на сайте <nuxt-link :to="'/'">manga-exchange.ru</nuxt-link> нарушает ваши авторские права, вы можете
          написать
          уведомление о нарушении прав и отправить его на адрес нашего агента
          <a href="mailto:copyright@manga-exchange.ru"></a>copyright@manga-exchange.ru и сервис
          <nuxt-link :to="'/'">manga-exchange.ru</nuxt-link>
          незамедлительно осуществит блокировку перечисленной в уведомлении манги.

          Часть 512(c) Акта об авторских правах (Digital Millennium Copyright Act) предъявляет определенные требования к
          форме
          этого уведомления. В соответствии с этим, оно должно быть предоставлено в письменном виде и обязательно
          содержать
          следующую информацию:
          <v-list two-line>
            <v-list-item>
              Материальную или электронную подпись лица, имеющего право представлять интересы человека, чьи авторские
              права на материал были нарушены.
            </v-list-item>
            <v-list-item>
              Указание на работы (материалы), в отношении которых нарушены права. В случае, когда уведомление сообщает о
              нарушениях авторского права на несколько таких материалов (текстов, изображений), в нем должны быть
              приведены указания на каждый из них.
            </v-list-item>
            <v-list-item>
              Указание на материал, нарушающий авторские права или являющийся субъектом поведения, нарушающего авторские
              права, каковой материал должен быть удален с серверов manga-exchange.ru
              или заблокирован для доступа. Вы также должны предоставить исходный адрес (URL) этого материала.
            </v-list-item>
            <v-list-item>
              Информация о том, как связаться с вами, например адрес электронной почты, почтовый адрес или номер
              телефона.
              Утверждение, что вы действительно считаете, что использование данного материала в таком виде не разрешено
              ни владельцем авторских прав, ни его агентом, ни законодательством США.
            </v-list-item>
            <v-list-item>
              Заявление, сделанное ввиду возможных штрафных санкций за предоставление ложных сведений, что
              представленные вами факты не содержат ошибок и искажений, и вы имеете право действовать от лица владельца
              авторских прав.
            </v-list-item>
          </v-list>
        </v-card-text>
        <v-card-title>
          Удаление или блокирование доступа к материалу
        </v-card-title>
        <v-card-text>
          После получения указанного выше уведомления о нарушнии в течение 3 (трех) рабочих дней сервис readmanga.ru
          либо
          предпринимает меры по ограничению доступа к спорным материалам, либо, если информации в требовании
          недостаточно
          или
          существуют сомнения в полномочиях заявителя, связывается с лицом, направившим уведомление, для получения
          дополнительной информации.

          При определенных обстоятельствах <nuxt-link :to="'/'">manga-exchange.ru</nuxt-link> прекращает предоставление сервиса владельцам аккаунтов,
          которые были
          замечены в многократных нарушениях авторских прав.
        </v-card-text>
        <v-card-title>
          Встречное уведомление
        </v-card-title>
        <v-card-text>
          Если после блокировки перевода манги на основании уведомления о нарушении прав, пользователь имеет претензии
          относительно такой блокировки и не согласен с ней и при этом считает себя владельцем прав на загруженную им,
          но
          заблокированную мангу, такой пользователь имеет право прислать Встречное уведомление на адрес
          copyright@readmanga.ru, после чего доступ к заблокированной манге может быть открыт.

          Часть 512(g) Акта об авторских правах требует, чтобы ваше встречное уведомление было предоставлено в
          письменном
          виде
          и обязательно включало в себя следующие элементы:
          <v-list>
            <v-list-item>
              Вашу материальную или электронную подпись.
            </v-list-item>
            <v-list-item>
              Указание на материал, который был удален или заблокирован для доступа, и исходный адрес (URL), по которому
              этот материал был опубликован до того, как в его отношении были предприняты меры.
            </v-list-item>
            <v-list-item>
              Заявление, что понимая ответственность за мошенничество, установленную законодательством Соединённых
              Штатов, вы добросовестно утверждаете, что материал был удален или заблокирован в результате ошибки или его
              неправильной идентификации.
            </v-list-item>
            <v-list-item>
              Ваше имя, адрес и номер телефона.
            </v-list-item>
            <v-list-item>
              Учтите, что часть 512(f) Акта об авторских правах указывает, что лицо, которое намеренно высылает ложную
              информацию
              о том, что материал был удален или заблокирован по ошибке или из-за неправильной идентификации, может быть
              привлечено к ответственности.
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </v-container>
    <v-container fluid>
      <v-card>
        <v-toolbar
          flat
          color="success"
        >
          <v-toolbar-title class="headline font-weight-regular white--text">
            <v-icon dark>
              mdi-copyright
            </v-icon>
            For copyright holders
          </v-toolbar-title>
        </v-toolbar>
        <v-card-text>
          It is our policy to respond to notices of alleged infringement that comply with the Digital Millennium
          Copyright
          Act (the text of which can be found at the U.S. Copyright Office Web Site,
          <a href="http://lcWeb.loc.gov/copyright/">http://lcWeb.loc.gov/copyright/</a>)
          and other applicable intellectual property laws, which may include removing or disabling access to material
          claimed to
          be the subject of infringing activity.

          If you are a copyright owner and believe that any User Submission or other content infringes upon your
          copyrights,
          you may submit a notification pursuant to the Digital Millennium Copyright Act ("DMCA") by providing our
          Copyright
          Agent with the following information in writing (see 17 U.S.C 512(c)(3) for further detail):
          <v-list>
            <v-list-item>
              A physical or electronic signature of a person authorized to act on behalf of the owner of an exclusive
              right that is allegedly infringed;
            </v-list-item>
            <v-list-item>
              Identification of the copyrighted work claimed to have been infringed, or, if multiple copyrighted works
              at a
              single online site are covered by a single notification, a representative list of such works at that site;
            </v-list-item>
            <v-list-item>
              Identification of the material that is claimed to be infringing or to be the subject of infringing
              activity and
              that is to be removed or access to which is to be disabled and information reasonably sufficient to permit
              the
              service provider to locate the material;
            </v-list-item>
            <v-list-item>
              Information reasonably sufficient to permit the service provider to contact you, such as an address,
              telephone
              number, and, if available, an electronic mail;
            </v-list-item>
            <v-list-item>
              A statement that you have a good faith belief that use of the material in the manner complained of is not
              authorized by the copyright owner, its agent, or the law;
            </v-list-item>
            <v-list-item>
              A statement that the information in the notification is accurate, and under penalty of perjury, that you
              are
              authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.
            </v-list-item>
          </v-list>
          <nuxt-link :to="'/'">manga-exchange.ru's</nuxt-link> Copyright Agent to receive notifications of claimed infringement is:
          <a href="mailto:copyright@manga-exchange.ru">copyright@manga-exchange.ru</a>.
          You acknowledge that if you fail to comply with all of the requirements of this Section 5(D), your DMCA notice
          may not be valid.
        </v-card-text>

      </v-card>
    </v-container>
  </v-container>
</template>

<script>
  export default {
    name: "copyright",
    head() {
      return {
        title: 'Copyright holders',
        meta: [
          {hid: 'copyright', name: 'description', content: 'Information for copyright holders page'}
        ]
      }
    },
  }
</script>

<style scoped>

</style>
