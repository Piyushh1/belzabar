<template>
  <div class="container">
    Dashboard panel {{message}}
  </div>
</template>
<script>
  export default {
    name: 'dashboard',
    data () {
      return {
        message: 'Dashoboard message goes here.......'
      }
    }
  }
</script>
<style>
  .container {
    padding: 10px;
  }
</style>
