<template>
  <div class="container">
    <Header></Header>
    <h1>Count {{ $store.state.count}}, isEven {{ evenOrOdd}}</h1>
    <div class="btn-container">
      <div class="btn btn-success" @click="increment">Increment</div>
      <div class="btn btn-error" @click="decrement">Decrement</div>
      <div class="btn btn-warning" @click="incrementIfOdd">IncrementIfOdd</div>
      <div class="btn btn-relative" @click="incrementAsync">Increment async</div>
    </div>
    <div class="github-container">
        Wanna look into github profile:<input class="zip" placeholder="Please enter github username" v-model="username"/>
        <div v-show="fetching">
          <img v-show="avtar" class="avtar" :src="avtar" />
          {{fetching}}
        </div>
    </div>
    <a :href="login" >Login</a>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'
import Header from './Header'
import axios from 'axios'

export default {
  name: 'hello',
  components: {
    Header
  },
  data () {
    return {
      login: '#dashboard',
      username: undefined,
      fetching: false,
      avtar: undefined
    }
  },
  computed: mapGetters([
    'evenOrOdd'
  ]),
  methods: mapActions([
    'increment',
    'decrement',
    'incrementIfOdd',
    'incrementAsync'
  ]),
  watch: {
    username: _.debounce(function () {
      if (this.username) {
        this.fetching = 'fetching....'
        axios.get(`https://api.github.com/users/${this.username}`)
          .then(response => {
            console.log('response ', response)
            this.fetching = response.data.name || response.data.login
            this.avtar = response.data.avatar_url
          })
          .catch(e => {
            this.fetching = 'No user found'
            this.avtar = undefined
            console.log('Error: ', e.msg)
          })
      }
    }, 1000)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
.container {
  border: 1px solid #e8e8e8;
  padding: 10px;
}

.avtar {
  width: 200px;
  vertical-align: top;
}

.btn-container {
  display: flex;
  flex-wrap: wrap;
}
.btn {
  padding: 10px;
  min-width: 200px;
  flex: 1;
  margin: 10px;
  color: white;
  cursor: pointer;
  border: 1px solid;
  border-radius: 2px;
}

.btn-success {
  background-color: #68c323;
  border-color: #0ba50b;
}

.btn-success:active {
  box-shadow: inset 2px 2px 10px #258a12;
}

.btn-error {
  background-color: #f14d4d;
  border-color: #d41515;
}

.btn-error:active {
  box-shadow: inset 2px 2px 10px #9c1616;
}

.btn-warning {
  background-color: orange;
  border-color: #da8d00;
}

.btn-warning:active{
  box-shadow: inset 2px 2px 10px #946b0d;
}

.btn-relative {
  background-color: #68b8f1;
  border-color: #3683b9;
}

.btn-relative:active{
  box-shadow: inset 2px 2px 10px #167ac1;
}

.zip {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #b9b7b7;
  border-radius: 4px;
}

.github-container {
  max-width: 400px;
  margin: 10px auto;
  border: 1px solid #cdcdcd;
  box-shadow: 1px 3px 10px #bbbaba;
  border-radius: 4px;
  padding: 20px;
  height: 275px;
  text-align: left;
}
</style>
