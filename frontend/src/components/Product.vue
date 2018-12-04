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
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products">
          <td style="text-align:left">{{ product.name }}</td>
          <td style="text-align:right">{{ product.price | formatPrice }}</td>
          <td>
            <!-- <span class="dropdown-item" style="cursor:pointer;padding-right:10px" click="edit(item)"><i class="fa fa-edit" style="color:#20a8d8"></i></span> -->
            <span class="dropdown-item" style="cursor:pointer" @click="remove(product)"><i class="fa fa-close" style="color:red"></i></span>
          </td>
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
      editProduct: {
        name: '',
        price: ''
      },
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
      axios.post('http://localhost:5000/product/', data)
      .then((result) => {
        this.products.push(
          {
            id: result.data.data.id,
            name: result.data.data.name,
            price: result.data.data.price
          }
        )
        this.name = ''
        this.price = ''
      })
    },
    remove: function(product) {
      axios.delete('http://localhost:5000/product/' + product.id + '/delete/')
      .then((response) => {
        var idx = this.products.indexOf(product)
        this.products.splice(idx, 1)
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
