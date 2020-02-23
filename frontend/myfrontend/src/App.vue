<template>
  <div id="app">
    {{msg}}
  <Header />
    
  </div>
</template>


<script>
import Header from './components/Header';
export default {
  name: 'App',
  components: {
    Header
  },
  data() {
return{
    msg:'HelloWorld',
  }
  }
}
</script>




<style>

</style>
