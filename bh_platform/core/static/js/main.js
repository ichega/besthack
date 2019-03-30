const Home = { template: '<h1>Домашнаяя страница</h1>' }
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
const app = new Vue({
    el: "#app",
    router,
    methods: {
        change_location: function(path){
            location.pathname = path
        },
    },
})