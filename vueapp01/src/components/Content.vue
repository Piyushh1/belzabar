<template>
	<div>
		hello this is content file
		<div>
			<ul>
				<li v-for="todo in todos" class="todo">
					<div :class="{active: todo.completed }">
					{{ todo.text }}
					<button v-on:click="complete(todo)">Completed</button>
					<button v-on:click="deletetodo(todo.id)">Delete</button>
					</div>
				</li>
			</ul>
		</div>
	</div>
</template>

<script>
/* eslint-disabled */
export default {
  props: ['todos', 'deletetodo', 'complete'],
  data () {
    return {
      msg: 'message part'
    }
  }
}
</script>

<style>
	ul {
		list-style: none;
	}
	.todo {
		padding: 10px;
    background-color: #6a9de8;
    border: 1px solid #467fe6;
    margin-top: -1px;
    text-align: left;
	}
	.active {
		text-decoration: line-through;
	}
</style>
