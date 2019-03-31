Vue.component('event', {
  props: ["id",'img_event', 'date_event', 'name_event', 'text_event'],
  template: `
      <v-card height="400px" style="overflow: hidden;">
        <v-img :src="img_event" aspect-ratio="2.75" height=200px></v-img>

        <v-card-title primary-title>
          <div>
          
            <h4 style="font-weight: normal"><v-icon small>fa-calendar-alt</v-icon>&nbsp{{date_event}}</h4>
            <h3 class="headline mb-0">{{name_event}}</h3>
            
            <div v-html="text_event"></div>
          </div>
        </v-card-title>

      </v-card>
  `
});

Vue.component('page-events', {
  template: `

    <v-container grid-list-md  >
      <v-layout row wrap justify-center>

        <v-flex md12 xs12 >
          <v-layout row wrap >

            <v-container grid-list-md >

              <span class="headline mb-2">Мероприятия:</span>

              <v-layout row wrap>

                <v-flex md4 xs12 v-for="item in events">
                  <a style="text-decoration: none" @click="$router.push('/event'); $store.commit('set_current_event', item.id);">
                   <event
                    :id="item.id"
                    :img_event="item.image"
                    :date_event="item.dt_start"
                    :name_event="item.name"
                    :text_event="item.snippet"
                    
                  ></event> 
                  <!--<event
                    
                    :img_event="item.img_event"
                    :date_event="item.date_event"
                    :name_event="item.name_event"
                    :text_event="item.text_event"
                    
                  ></event>-->
                  </a>
                </v-flex>

              </v-layout>

            </v-container>

          </v-layout>
        </v-flex>

      </v-layout>
    </v-container>

  `,
  data: () => ({
    events: [
      {
        "img_event": "https://cdn.vuetifyjs.com/images/cards/desert.jpg",
        "date_event": "11.06.1998",
        "name_event": "Мероприятие 1",
        "text_event": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod temporLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor"
      },
      {
        "img_event": "https://cdn.vuetifyjs.com/images/cards/desert.jpg",
        "date_event": "11.06.2008",
        "name_event": "Мероприятие 2",
        "text_event": "Loreing elit, sed do eiusmod temporLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor"
      }
    ],
  }),
  created() {
    this.events = this.load_events();
    
  },
  methods: {
    //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ДОРАБОТАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    load_events: function (){
      var self = this;
      var xhr = new XMLHttpRequest();
      var url = "/get_events/";
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
      return response.events
    }
  },
});

// new Vue({
//   el: '#app',
//     data: () => ({})
// })
