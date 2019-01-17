<template>
  <section class="section">
    <div class="container is-centered">
      <div class="card">
        <div class="card-content">
          <div class="content">
            <form @submit.prevent="login">
              <div class="field">
                <div class="control">
                  <input class="input" type="email" placeholder="メールアドレス" v-model="inputEmail" required>
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <input class="input" type="password" placeholder="パスワード" v-model="password" required>
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <button class="button is-primary login-button" type="submit">
                    ログイン
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// import { mapGetters } from "vuex"
export default {
  data() {
    return {
      inputEmail: "",
      password: "",
    }
  },
  head() {
    return {
      title: `ログイン`,
    }
  },
  // computed: {
  //   ...mapGetters({
  //     user: "user",
  //     email: "email",
  //   }),
  // },
  // fetch({ store, redirect }) {
  //   if (store.state.auth.user) {
  //     redirect("/")
  //   }
  // },
  mounted() {
    this.inputEmail = this.email
  },
  methods: {
    async login() {
      try {
        // await this.$store.dispatch("setEmail", "")
        await this.$auth.loginWith("local", {
          data: {
            email: this.inputEmail,
            password: this.password,
          },
        })
        await this.$store.dispatch("setEmail", this.inputEmail)
      } catch (error) {
        let message = "エラーが発生しました。しばらくたってからお試しください"
        if (error.response.data.message) {
          message = error.response.data.message
        }
        this.$toast.open({
          message: message,
          type: "is-danger",
        })
      }
    },
  },
}
</script>

<style scoped>
.section {
  padding-top: 1.5rem;
}

.card {
  margin-left: auto;
  margin-right: auto;
  max-width: 400px;
}

.card-content {
  margin-top: 100px;
}

.control input{
  margin-bottom: 1rem;
}

.login-button {
  width: 100%;
}

.field-reregistration {
  margin-top: 0.5rem;
}
</style>
