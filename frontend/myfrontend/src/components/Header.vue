<template>
 <div class="container">
    <button v-on:click="django_import">Import</button>

     <div class="left">

        <h1>
            {{header}}
        </h1>
        <form class="form_group" @submit.prevent="post1">
    
            <div class="form-element">
            <label for="name">name</label>
            <input type="text" name="name" v-model="name">

            </div>

            <div class="form-element">
                
            <label for="description">description</label>
            <input type="text" name="description" v-model="description">
            </div>


            <div class="form-element">

            <label for="price">price</label>
            <input type="text" name="price"  v-model="price">
                
            </div>

            <button type="submit">Submit</button>

            {{message}}
        </form>

    
     </div>

     <div class="right">
         <ul>
        <li v-bind:key=todo v-for="todo in Todos">
            {{todo.name}} -{{todo.price}}
            <!-- {{todo.id}} -{{todo.title}} -->
        </li>
    </ul>

     </div>


 </div>
</template>

<script>
import axios from 'axios';
export default {
name:"Header",
data(){
    return{
        header:"Form 60",
        name:'',
        price:'',
        description:'',
        Todos:[],

        message:'',
    }

},
methods:{
django_import(){
    // axios.get('https://jsonplaceholder.typicode.com/todos')
    axios.get('http://127.0.0.1:8000/')
          .then(res =>{this.Todos=res.data;})
},

post1(){
axios({
  method: 'post',
  url: 'http://127.0.0.1:8000/',
  data: {
    name :this.name,
    description :this.description,
    price :this.price,
  }
})
.then(() => {
    this.name='';
    this.description='';
    this.price='';
    this.django_import();
    // this.message = "post submitted"
    })
}




}

}
</script>   

<style scoped>
.container{
    
    width:1200px;
    margin:auto;
    display:flex;
    justify-content: space-between;
    align-items:center;
    height:80vh;
}


button{
    flex:none;
}

.right ,.left{
    width:500px;
    height:100%;
    border:1px solid red;
    overflow:auto;
    /* flex:1; */

}

.form_group{

    display:flex;
    justify-content: space-evenly;
    align-items: flex-start ;
    flex-direction: column;
    width:100%;
}

.form-element{
    margin:30px;
    /* display: */
    flex-direction: row;
    justify-content:space-evenly; 
} 

</style>