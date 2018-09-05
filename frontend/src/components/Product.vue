<template>
  <div class="product">
    <h1>Produtos</h1>
    <div class="pure-form">
      <fieldset>
        <input type="text" placeholder="Produto" v-model="name">
        <input type="number" placeholder="Preço" v-model="price" @keyup.enter="addProduct">
        <button type="submit" class="pure-button pure-button-primary" @click="addProduct">Adicionar</button>
      </fieldset>
    </div>
    <table class="pure-table">
      <thead>
        <tr>
          <th>Produto</th>
          <th>Preço</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products">
          <td style="text-align:left">{{ product.name }}</td>
          <td style="text-align:right">{{ product.price | formatPrice }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

import axios from 'axios';
import { formatPrice } from '../utils'

export default {
  data () {
    return {
      name: '',
      price: '',
      products: []
    }
  },
  methods: {
    getProducts(){
      axios.get('http://localhost:5000/product/')
      .then((result) => {
        this.products = result.data.data
      })
    },
    addProduct(){
      let data = {'name': this.name, 'price': this.price}
      axios.post('http://localhost:5000/product/add', data)
      .then((result) => {
        this.products.push(
          {
            name: this.name,
            price: this.price
          }
        )
        this.name = ''
        this.price = ''
      })
    }
  },
  filters: {
    formatPrice
  },
  mounted(){
    this.getProducts()
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
table {
  margin-left: auto;
  margin-right: auto;
}
</style>
