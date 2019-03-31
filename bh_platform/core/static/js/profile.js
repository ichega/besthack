Vue.component('page-profile',{
    template: `
    <v-container grid-list-md  >
      <v-layout row wrap justify-center>
        <v-flex md8 xs12>
          <v-card light>
            <v-layout row wrap>
              <v-flex md6 xs12>
                <v-img src="https://cdn.vuetifyjs.com/images/cards/foster.jpg" contain style="padding-left:10px" ></v-img>
              </v-flex>

              <v-flex md6 xs12>
                <v-card-title primary-title>
                  <v-flex class="text-wrap" style=" word-wrap: break-word;" >
                    <h3>Пользователь: <span>{{who_is_profile}}</span> </h3>
                    <h3>ФИО: <span>sdfsdf</span> </h3>
                    <h3>Физическое лицо</h3>
                    <h3>ИНН: 123123012381</h3>
                    <h3>Веб-сайт: <a href="#" style="text-decoration: none">что-то.ру</a></h3>
                    <h3>Краткое описание: такой то такой то</h3>
                    <h3>E-mail: lol@gmail.com</h3>
                    <h3>Телефон: +79201218940</h3>
                  </v-flex>
                </v-card-title>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    `,
    data: () => ({
      who_is_profile: 'Админ',
      img_of_profile: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
      FIO_of_profile: 'Кирилл Бебнев',

    })
});


// new Vue({
//   el: '#app',
//     data: () => ({

//     })
// })
