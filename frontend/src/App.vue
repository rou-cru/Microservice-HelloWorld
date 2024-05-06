<template>
  <div class="card text-center m-3">
    <div class="card-body">Name: {{hostname}}</div>
  </div>
</template>

<script>
export default {
  name: "get-request",
  
  data() {
    return {
      hostname: null
    }
  },

  created() {
      fetch("/api/hostname", {
          method: 'GET'
      })
      .then(response => response.json())
      .then(data => (this.hostname = data.hostname));
  }
}
</script>