<template>
  <div class="product">
    <h1>Produtos</h1>
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
export default {
  data () {
    return {
      products: []
    }
  },
  methods: {
    getProducts(){
      axios.get('http://localhost:5000/product/').then((result) => {
        console.log(result)
      this.products = result.data
      })
    }
  },
  filters: {
    formatPrice(value) {
      let val = (value/1).toFixed(2).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    }
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
