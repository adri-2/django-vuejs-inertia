<template>
 
    <div>
      <h1>{{events }} ...</h1>
      
    </div>
  </template>
  
  <script setup>
  // import { onMounted } from 'vue';


  
  const props = defineProps({
    events: String
  })

 
//   onMounted(() => {
//   document.title = "Ma page Vue.js";
// });
  </script>
  