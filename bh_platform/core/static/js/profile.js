Vue.component('page-profile',{
    template: `
    <v-container grid-list-md fluid >
      <v-layout row wrap justify-center>
        <v-flex md8 xs12>
          <v-card light>
            <v-layout row wrap>
              <v-flex md6 xs12>
                <v-img :src="profile.avatar" contain style="padding-left:10px" aspect-ratio="1"></v-img>
              </v-flex>

              <v-flex md6 xs12>
              
                <v-card-title primary-title>
                  <v-flex class="text-wrap" style=" word-wrap: break-word;" >
                  <v-layout column wrap>
                    <v-flex xs-12>
                      <v-layout row wrap>
                        <v-flex xs12 md6>
                          <h3>Пользователь:</h3> 
                        </v-flex>
                        <v-flex xs12 md6>
                          <span>{{profile.username}}</span> 
                        </v-flex>
                      </v-layout>
                    
                    </v-flex>

                    <v-flex xs-12>
                      <v-layout row wrap>
                        <v-flex xs12 md6>
                        <h3>ФИО:</h3> 
                        </v-flex>
                        <v-flex xs12 md6>
                        <span> {{profile.last_name}} {{profile.first_name }} {{profile.otch}}</span> 
                        </v-flex>
                      </v-layout>
                    
                    </v-flex>

                    <v-flex xs-12 v-if="profile.is_phys_face">
                      <v-layout row wrap>
                        <v-flex xs12 md6>
                        <h3 v-if="profile.is_phys_face">Физическое лицо</h3>
                        </v-flex>
                        
                      </v-layout>
                    
                    </v-flex>

                    <v-flex xs-12>
                      <v-layout row wrap>
                        <v-flex xs12 md6>
                        <h3>ИНН:</h3> 
                        </v-flex>
                        <v-flex xs12 md6>
                        <span>{{ profile.inn }}</span>
                        </v-flex>
                      </v-layout>
                    
                    </v-flex>
                    
                    <v-flex xs-12>
                      <v-layout row wrap>
                        <v-flex xs12 md6>
                        <h3>Веб-сайт: </h3>
                        </v-flex>
                        <v-flex xs12 md6>
                        <a href="#" style="text-decoration: none">{{ profile.site }}</a>
                        </v-flex>
                      </v-layout>
                    
                    </v-flex>

                    <v-flex xs-12>
                      <v-layout row wrap>
                        <v-flex xs12 md6>
                        <h3>Краткое описание: </h3>
                        </v-flex>
                        <v-flex xs12 md6>
                        <span>{{ profile.description }}</span>
                        </v-flex>
                      </v-layout>
                    
                    </v-flex>

                    <v-flex xs-12>
                      <v-layout row wrap>
                        <v-flex xs12 md6>
                        <h3>E-mail: </h3>
                        </v-flex>
                        <v-flex xs12 md6>
                        <span>{{ profile.email }}</span>
                        </v-flex>
                      </v-layout>
                    
                    </v-flex>

                    <v-flex xs-12>
                      <v-layout row wrap>
                        <v-flex xs12 md6>
                        <h3>Телефон: </h3> 
                        </v-flex>
                        <v-flex xs12 md6>
                        <span>{{ profile.phone }}</span>
                        </v-flex>
                      </v-layout>
                    
                    </v-flex>
                    
                    
                    
                    
                    
                    
                    
                    
                    </v-layout>
                  </v-flex>
                </v-card-title>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    `,
    created() {
      this.profile = this.load_profile();
    },
    methods: {
      load_profile: function (){
        var self = this;
        var xhr = new XMLHttpRequest();
        var url = "/get_profile/";
        xhr.open("POST", url, false);
        var response = "123"
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
  
                response = JSON.parse(xhr.responseText);
                // console.log(xhr.responseText)
                // console.log(json.email + ", " + json.password);
            }
        };
        var data = JSON.stringify({"page": "1"});
        xhr.send(data)
        
        // console.log(response)
        return response
      }
    },
    data: () => ({
      profile: {},
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
