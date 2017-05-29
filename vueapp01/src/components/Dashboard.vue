<template>
	<div class="container">
		<Header />
		<Aside />
		 <input v-model="newTodo" />
		 <button v-on:click="addTodo">Add</button>
		<Content
			v-bind:todos="todos"
      v-bind:deletetodo="deletetodo"
      v-bind:complete="complete"
		 />
	</div>
</template>

<script>
import Header from './Header'
import Aside from './Aside'
import Content from './Content'

export default {
  methods: {
    addTodo: function () { if (this.newTodo) this.todos.splice(0, 0, { id: this.todos.length + 1, text: this.newTodo, completed: false }); this.newTodo = undefined },
    deletetodo: function (id) { console.log(id); this.index = this.todos.findIndex(x => x.id === id); this.todos.splice(this.index, 1) },
    complete: function (todo) { todo.completed = true }
  },
  data () {
    return {
      msg: 'this is msg part',
      newTodo: undefined,
      todos: []
    }
  },
  components: {
    Header, Content, Aside
  }
}
</script>

<style scoped>
	.container {
		padding: 10px;
	}
</style>
