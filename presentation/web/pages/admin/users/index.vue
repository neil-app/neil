<template>
  <div class="sections">
    <div class="container">
      <div class="columns is-multiline">
        <div class="column is-half" v-for="user in users" :key="user.id">
          <div class="card">
            <div class="card-content">
              <div>
                  {{ user.name }}
                  {{ user.email }}
                <a href="#" class="button is-normal" @click="deleteUser(user)">削除</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
//   data() {
//     return {
//       isEdit: false,
//       phoneNumber: "",
//       password: "",
//     }
//   },
  async asyncData({app, error}) {
    try {
      const { data } = await app.$axios.get(`/api/users`)
      return {
        users: data.users,
      }
    } catch (err) {
      return {
        statusCode: err.response.status,
        message: err.response.statusText,
      }
    }
  },
//   computed: {
//     name: function() {
//       return this.user.name
//     }
//   },
  methods: {
    deleteUser(user) {
      this.$axios.delete(`/api/users/${user.id}`)
    },
  }
}
</script>

<style lang="scss" scoped>
</style>