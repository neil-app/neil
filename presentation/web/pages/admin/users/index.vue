<template>


    <div class="columns is-center">
        <table class="table is-fullwidth">
        </table>
    </div>



</template>



<script>

  methods: {
    get() {
      this.$axios.get(`/api/users/${this.userId}`, {
         name: this.user.name,
         email: this.user.email,
    })
      this.isEdit = false
    },
  }

</script>