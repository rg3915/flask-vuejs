<template>
  <div id="app">
    <img height="100px" src="./assets/flask-logo.png">
    <img height="100px" src="./assets/logo.png">
    <!-- <HelloWorld/> -->
    <Product/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import Product from './components/Product'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Product
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
