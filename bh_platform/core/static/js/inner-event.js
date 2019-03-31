Vue.component('blockorganizer', {
  props: ['img_of_organizer', 'name_of_organizer'],
  template: `
  <div>
    <v-avatar size="36px" >
      <img :src="img_of_organizer" alt="Avatar" >
    </v-avatar>
    <span>&nbsp {{ name_of_organizer }}</span>
    </div>
  `
});


Vue.component('page-innerevent', {
  template: `
  <v-container grid-list-md  >
    <v-layout row wrap justify-center>
      <v-flex md8 xs12>
        <v-layout row wrap justify-center>
          <v-flex md11 xs12 >
            <v-card dark style="background-color:rgba(255,0,0,0.7)">
              <v-layout row wrap justify-center>

              <v-flex md6 xs12 >
                <div style="display:flex; justify-content: center; padding: 15px;">
                  <span  style="font-weight: bold;">Название:</span>
                  <span>&nbsp{{name_of_event}}</span>
                </div>
              </v-flex>

              <v-flex md6 xs12>
                <div style="display:flex; justify-content: center; padding: 5px;">

                  <template>
                 
                    <v-layout row justify-center>
                      <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
                      
                        <template v-slot:activator="{ on }">
                          <v-btn small light style="padding: 0px; text-transform: none;" v-on="on">


                            <span style="font-weight: bold">Задачи:&nbsp</span>
                            <v-icon small >fa-tasks</v-icon>
                          </v-btn>
                        </template>
                        
                        
                          
                          <v-toolbar dark style="background-color:#ff5555ff">
                            
                            <v-toolbar-title ><v-icon>fa fa-tasks</v-icon> Доска задач</v-toolbar-title>
                            
                            <v-spacer></v-spacer>
                            <v-toolbar-items>
                              <v-btn icon dark @click="dialog = false">
                                <v-icon>close</v-icon>
                              </v-btn>
                            </v-toolbar-items>
                          </v-toolbar>
                          
                       
                          <canban></canban>
                        
                        
                       
                      </v-dialog>
                      
                    </v-layout>
                    
                  </template>

                </div>
              </v-flex>

              </v-layout>
            </v-card>
          </v-flex>

          <v-flex md11>
            <v-card light>
              <v-card-title primary-title>
                <div>
                  <h3 class=" mb-0" style="font-weight: bold">Поле</h3>
                </div>
                {{field_of_event}}
              </v-card-title>
            </v-card>
          </v-flex>

          <v-flex md11>
            <v-card light>
              <v-card-title primary-title>
                <div>
                  <span class=" mb-0" style="font-weight: bold">Начало: </span>
                  <span>Время: {{time_start_of_event}} |</span>
                  <span>Дата: {{date_start_of_event}}</span>
                </div>
              </v-card-title>
            </v-card>
          </v-flex>

          <v-flex md11>
            <v-card light>
              <v-card-title primary-title>
                <div>
                  <span class=" mb-0" style="font-weight: bold">Конец: </span>
                  <span>Время: {{time_end_of_event}} |</span>
                  <span>Дата: {{date_end_of_event}}</span>
                </div>
              </v-card-title>
            </v-card>
          </v-flex>

          <v-flex md11>
            <v-card light>
                <div style="padding: 15px;">
                  <span class="mb-0" style="font-weight: bold">Организатор: </span>
                  <v-btn dark style="background-color:rgba(255,0,0,0.7)">
                    <v-avatar size="32px" >
                      <img src="https://avatars0.githubusercontent.com/u/9064066?v=4&s=460" alt="Avatar" >
                    </v-avatar>
                    <span style="text-transform: none">&nbsp {{name_organizer_of_event}}</span>
                  </v-btn>
                </div>
            </v-card>
          </v-flex>

      </v-layout>
    </v-flex>


    <v-flex md4 xs12 >
      <v-layout row wrap justify-center>

        <v-flex md10 xs12 >
          <v-card dark style="background-color:rgba(255,0,0,0.7)">
            <v-layout row wrap >
              <v-flex md6 xs12 >
                <div style="padding: 15px;">
                  <span  style="font-weight: bold; ">Спонсоры:</span>
                </div>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>

        <v-flex md10 v-for="item in list_of_organizers">
          <v-card light>
            <a href="#" style="text-decoration: none; color: black; display:flex; justify-content: center; padding: 10px; align-items: center">
              <blockorganizer
              :img_of_organizer="item.img_of_organizer"
              :name_of_organizer="item.name_of_organizer"
              ></blockorganizer>
            </a>
          </v-card>
        </v-flex>

      </v-layout>
    </v-flex>

            </v-layout>
          </v-container>
  `,

  data: () => ({
    dialog: false,
    notifications: false,
    sound: true,
    widgets: false,

    name_of_event: "Мероприятие 1",
    field_of_event: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat  non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",

    time_start_of_event: "15:90",
    date_start_of_event: "19.06.2948",

    time_end_of_event: "98:34",
    date_end_of_event: "06.11.1765",

    name_organizer_of_event: "Иван Иванов",

    list_of_organizers: [
      {
        img_of_organizer: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
        name_of_organizer: "Петя Петров"
      },
      {
        img_of_organizer: "https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
        name_of_organizer: "Кеша Петров"
      },
    ]

  })
});

// new Vue({
//   el: '#app',
//     data: () => ({

//     })
// })
