<template>
  <div>
  <button class="button" @click="showAddChatModal=true">Show</button>
  <my-model v-show="showAddChatModal" @close="showAddChatModal=false"></my-model>
<div class="dropdown">
  <button class="btn bmd-btn-icon dropdown-toggle" type="button" id="ex1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    <i class="material-icons">more_vert</i>
  </button>
  <div class="dropdown-menu dropdown-menu-left" aria-labelledby="ex1">
    <button class="dropdown-item" type="button">Action</button>
    <button class="dropdown-item disabled" type="button">Another action</button>
    <button class="dropdown-item" type="button">Another action</button>
  </div>
</div>
  </div>
</template>


<script>
export default {
  data () {
    return {
      showAddChatModal: false
    }
  }
}
</script>


