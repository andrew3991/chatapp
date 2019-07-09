// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

Vue.use(Buefy)

Vue.config.productionTip = false
Vue.component('my-model', {
  data: function () {
    return {
      checkedNames: [],
      title: ''
    }
  },
  props: ['users'],
  template: `
  <div class="modal is-active">
  <div class="modal-background"></div>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">Modal title</p>
      <button class="delete" aria-label="close" @click="$emit('close')"></button>
    </header>

    <section class="modal-card-body">
    <b-field label="Title">
      <b-input v-model="title" v-show="checkedNames.length > 1"></b-input>
    </b-field>
    <b-field label="Users">
        <b-select
            multiple
            native-size="10"
            expanded="true"
            v-model="checkedNames"
            >
            <option v-for="user in users" :key="user.id">{{user}}</option>
        </b-select>
    </b-field>
    </section>
    <footer class="modal-card-foot">
      <button class="button is-info" @click="sendMessageToParent">Start chatting</button>
    </footer>
  </div>
</div>
  `,
  methods: {
    sendMessageToParent () {
      this.$emit('messageFromChild', this.checkedNames, this.title)
    }
  }
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
