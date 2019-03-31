var STATE_WAIT = 0
var STATE_RUNNING = 1
var STATE_DONE = 2

var CanbanTask = {
    props: [
        "id",
        "title",
        "event_title",
        "event_image",
        "description",
        "perfomer",
        "perfomer_image",
        "partner",
        "partner_image",
        "deadline"
    ],
    data: function(){
        return {
            dialog3: false,
        }

    },
    methods: {

    },
    computed: {

    },

    template: `
    <v-card width="100%" class="mb-1 ml-1 mr-1 mt-1">

        <v-card-title >
            <v-layout column wrap>
                  <template>

                    <v-layout row justify-center>
                      <v-dialog v-model="dialog3" persistent max-width="600px" >

                        <template v-slot:activator="{ on }">
                            <v-btn small light style="padding: 0px; text-transform: none;" v-on="on">изменить</v-btn>
                        </template>
                        <v-card light>
                            <v-card-title>
                              <span class="headline">Изменение задачи</span>
                            </v-card-title>
                            <v-card-text class="pt-0 pb-0" >
                              <v-container grid-list-md>
                                <v-layout wrap>

                                  <v-flex xs12 sm6>
                                    <v-text-field label="Наименование задачи" v-model="title" ></v-text-field>
                                  </v-flex>

                                  <v-flex xs12 sm6>
                                    <v-text-field label="Наименование мероприятия" v-model="event_title" ></v-text-field>
                                  </v-flex>

                                  <v-flex xs12 sm12>
                                    <span style="font-weight:bold">Конец</span>
                                  </v-flex>

                                  <v-flex xs12>
                                    <v-text-field label="Время" v-model="deadline"></v-text-field>
                                  </v-flex>

                                  <v-flex xs12>
                                        <v-textarea
                                          label="Поле"
                                          v-model="description"
                                          hint="Hint text"
                                        ></v-textarea>
                                  </v-flex>

                                  <v-flex xs12 sm6>
                                    <v-select
                                      label="Исполнитель"
                                      v-model="perfomer"
                                      :items="['Лол Кеков', 'Трол Морфинов', 'Фемистокл Рыжий']"
                                    ></v-select>
                                  </v-flex>

                                  <v-flex xs12 sm6>
                                    <v-select
                                      label="Партнер"
                                      v-model="partner"
                                      :items="['Лол Кеков', 'Трол Морфинов', 'Фемистокл Рыжий']"
                                    ></v-select>
                                  </v-flex>

                                </v-layout>
                              </v-container>
                            </v-card-text>
                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn color="blue  darken-1" flat @click="dialog3 = false">Закрыть</v-btn>
                              <v-btn color="red darken-1" flat @click="dialog3 = false">Сохранить</v-btn>
                            </v-card-actions>

                        </v-card>
                      </v-dialog>

                    </v-layout>
                  </template>


                    <v-layout row wrap>
                        <v-flex md5 xs12>
                            <span class="title" style="text-align: center;">{{ title }}</span>
                        </v-flex>
                        <v-flex md5 xs12>
                                <v-avatar size="36px" >
                                    <img :src="event_image" alt="Avatar" >
                                </v-avatar>
                                <span> {{ event_title }}</span>
                        </v-flex>
                    </v-layout>
                <v-flex>
                <div class="subheading">Постановка:</div>
                <div class="caption">
                {{ description }}
                </div>
                </v-flex>
                <v-flex>
                    <v-layout row wrap>
                        <v-flex xs12 md6>


                            <div class="subheading">Исполнитель:</div>
                            <v-avatar size="36px" >
                                <img :src="perfomer_image" alt="Avatar" >
                            </v-avatar>
                            <span>{{ perfomer }}</span>
                        </v-flex>
                        <v-flex xs12 md6>
                            <div class="subheading">Партнер:</div>
                            <v-avatar size="36px" >
                                <img :src="partner_image" alt="Avatar" >
                            </v-avatar>
                            <span> {{ partner }}</span>
                        </v-flex>

                    </v-layout>
                </v-flex>


                </v-flex>
                <v-flex>
                    <v-layout row wrap>
                        <v-flex md6 >

                            <span class="subheading">До:</span>
                            <v-chip color="red" text-color="white"> {{ deadline }}</v-chip>
                        </v-flex>
                        <v-flex md2>
                            <v-btn color="blue" fab small dark @click="$emit('state_change',{id: id, state:0})">
                                <v-icon>fa fa-clock</v-icon>
                            </v-btn>
                        </v-flex>
                        <v-flex md2 >
                            <v-btn color="orange" fab small dark @click="$emit('state_change',{id: id, state:1})">
                                <v-icon>fa fa-cogs</v-icon>
                            </v-btn>
                        </v-flex>

                        <v-flex md2>
                            <v-btn color="green" fab small dark @click="$emit('state_change',{id: id, state:2})">
                                <v-icon>fa fa-check-double</v-icon>
                            </v-btn>
                        </v-flex>
                    </v-layout>

                </v-flex>


            </v-layout>







        </v-card-title>


    </v-card>



    `

}


Vue.component('canban-task', CanbanTask);

var CanbanComponent = {

    data: function(){
        return {
            tasks: [
                {
                    id: 1,
                    state : STATE_WAIT,
                    title:"Задача 1",
                    event_title:"Мероприятие 1",
                    event_image:"https://www.crucial.com.au/blog/wp-content/uploads/2014/12/events_medium.jpg",
                    description:`Difficulty on insensible reasonable in.
                    From as went he they.
                    Preference themselves me as thoroughly partiality considered on in estimating.
                        Middletons acceptance discovered projecting so is so or.
                        In or attachment inquietude remarkably comparison at an.
                        Is surrounded prosperous stimulated am me discretion expression.
                        But truth being state can she china widow. Occasional preference fat remarkably now projecting uncommonly dissimilar.
                        Sentiments projection particular companions interested do at my delightful.
                        Listening newspaper in advantage frankness to concluded unwilling.`,
                    perfomer:"Имя исполнителя",
                    perfomer_image:"https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
                    partner:"Имя партнера",
                    partner_image:"https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
                    deadline:"31.03.2019 10:00",
                },
                {
                    id: 2,
                    state : STATE_DONE,
                    title:"Задача 2",
                    event_title:"Мероприятие 2",
                    event_image:"https://www.crucial.com.au/blog/wp-content/uploads/2014/12/events_medium.jpg",
                    description:`Difficulty on insensible reasonable in.
                    From as went he they.
                    Preference themselves me as thoroughly partiality considered on in estimating.
                        Middletons acceptance discovered projecting so is so or.
                        In or attachment inquietude remarkably comparison at an.
                        Is surrounded prosperous stimulated am me discretion expression.
                        But truth being state can she china widow. Occasional preference fat remarkably now projecting uncommonly dissimilar.
                        Sentiments projection particular companions interested do at my delightful.
                        Listening newspaper in advantage frankness to concluded unwilling.`,
                    perfomer:"Имя исполнителя",
                    perfomer_image:"https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
                    partner:"Имя партнера",
                    partner_image:"https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
                    deadline:"31.03.2019 10:00",

                },
                {
                    id: 3,
                    state : STATE_DONE,
                    title:"Задача 3",
                    event_title:"Мероприятие 2",
                    event_image:"https://www.crucial.com.au/blog/wp-content/uploads/2014/12/events_medium.jpg",
                    description:`Difficulty on insensible reasonable in
                        Listening newspaper in advantage frankness to concluded unwilling.`,
                    perfomer:"Имя исполнителя",
                    perfomer_image:"https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
                    partner:"Имя партнера",
                    partner_image:"https://avatars0.githubusercontent.com/u/9064066?v=4&s=460",
                    deadline:"31.03.2019 10:00",

                }
            ]
        }

    },
    methods: {
        task_change_state: function(data){
            console.log(data)
            for (var i = 0; i < this.tasks.length; i++){
                if (this.tasks[i].id == data.id){
                    this.tasks[i].state = data.state;
                    break;
                }
            }
            // data.task.state = data.state;
        },
    },
    watch: {

    },
    computed: {

    },
    template: `

            <v-layout wrap row style='height:100%;'  >
                <v-flex md4 xs12 lg4 >

                <v-card height="100%"  style="background-color:#ddf">
                <v-alert
                :value="true"
                color="#ff5555ff">
                    <span class="title" style="display: flex; justify-content: center;">Поставлены</span>
                </v-alert>
                    <v-card-title primary-title>

                        <canban-task v-for="task in tasks"
                            v-if="task.state == 0"
                            :id="task.id"
                            :title="task.title"
                            :event_title="task.event_title"
                            :event_image="task.event_image"
                            :description="task.description"
                            :perfomer="task.perfomer"
                            :perfomer_image="task.perfomer_image"
                            :partner="task.partner"
                            :partner_image="task.partner_image"
                            :deadline="task.deadline"
                            @state_change="task_change_state($event)"
                        ></canban-task>

                    </v-card-title>


                </v-card>

                </v-flex>

                <v-flex md4 xs12 lg4>



                <v-card height="100%" style="background-color:#ffd">
                <v-alert
                :value="true"
                color="#ff5555ff">
                    <span class="title" style="display: flex; justify-content: center;">В работе</span>
                </v-alert>

                <v-card-title primary-title>

                <canban-task v-for="task in tasks"
                        v-if="task.state == 1"
                        :id="task.id"
                        :title="task.title"
                        :event_title="task.event_title"
                        :event_image="task.event_image"
                        :description="task.description"
                        :perfomer="task.perfomer"
                        :perfomer_image="task.perfomer_image"
                        :partner="task.partner"
                        :partner_image="task.partner_image"
                        :deadline="task.deadline"
                        @state_change="task_change_state($event)"
                    ></canban-task>

                </v-card-title>


            </v-card>

                </v-flex>

                <v-flex md4 xs12 lg4>

                <v-card height="100%" style="background-color:#dfd">
                <v-alert
                :value="true"
                color="#ff5555ff">
                    <span class="title" style="display: flex; justify-content: center;">Завершены</span>
                </v-alert>

                    <v-card-title primary-title>

                    <canban-task v-for="task in tasks"
                        v-if="task.state == 2"
                        :id="task.id"
                        :title="task.title"
                        :event_title="task.event_title"
                        :event_image="task.event_image"
                        :description="task.description"
                        :perfomer="task.perfomer"
                        :perfomer_image="task.perfomer_image"
                        :partner="task.partner"
                        :partner_image="task.partner_image"
                        :deadline="task.deadline"
                        @state_change="task_change_state($event)"
                    ></canban-task>

                    </v-card-title>


                </v-card>

                </v-flex>
            </v-layout>




    `

}

Vue.component('canban', CanbanComponent);
