<template>
  <div class='header'>
    HI! Im header block.
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
  }
}
</script>

<style>
  .header {
    padding: 10px;
    background-color: lightgray;
  }
</style>
