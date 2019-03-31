const Home = { template: '<edit-button caption="Kek"></edit-button>' }
const Profile = { template: '<page-profile></page-profile>' }
const Events = { template: '<page-events></page-events>'}
const Event = { template: '<page-innerevent></page-innerevent>'}
const NotAuth = { template: 'Not authenticated'}

// 2. Определяем несколько маршрутов
// Каждый маршрут должен указывать на компонент.
// "Компонентом" может быть как конструктор компонента, созданный
// через `Vue.extend()`, так и просто объект с опциями компонента.
// Мы поговорим о вложенных маршрутах позднее.
const routes = [
  { path: '/', component: Home },
  { path: '/index', component: Home },
  { path: '/home', component: Home },
  { path: '/events', component: Events },
  { path: '/event', component: Event },
  { path: '/profile', component: Profile },
  { path: '/canban', component: CanbanComponent},
]

// 3. Создаём экземпляр маршрутизатора и передаём маршруты в опции `routes`
// Вы можете передавать и дополнительные опции, но пока не будем усложнять.
var router = new VueRouter({
  routes // сокращённая запись для `routes: routes`
})

// 4. Создаём и монтируем корневой экземпляр приложения.
// Убедитесь, что передали экземпляр маршрутизатора в опции
// `router`, чтобы позволить приложению знать о его наличии.

const store = new Vuex.Store({
    state: {
      email: "",
      is_auth: false,
      avatar: "https://img.icons8.com/ios/2x/user.png",
    },
    mutations: {
        set_profile: function(state, profile){
            console.log(profile)
            state.email = profile.email
            state.is_auth = (profile !== undefined)
            state.avatar = profile.avatar
        }
    }
  })


const app = new Vue({
    el: "#app",
    router,
    store,
    data: () => ({
        drawer: false
      }),
    computed: {
        user: function (){
            var profile = load_profile();
            return profile
        }
    },
    created() {
        var profile = load_profile();
        this.$store.commit('set_profile', profile);
        

    },
    methods: {
        change_location: function(path){
            location.pathname = path
        },
        
    },
})


