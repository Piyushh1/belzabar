<template>
  <div class='header'>
    HI! {{ username }}
    {{message}}
  </div>
</template>

<script>
export default {
  name: 'header',
  data () {
    return {
      message: 'Hello interns!!!'
    }
  },
  props: [ 'username' ]
}
</script>

<style>
  .header {
    padding: 10px;
    background-color: lightgray;
  }
</style>
