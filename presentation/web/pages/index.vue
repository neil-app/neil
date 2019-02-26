<template>
  <div>
    <div class="main-image">
      <img src="https://66.media.tumblr.com/1dda85efab4eea20137c6fd0b48514c9/tumblr_piufjzc4Hq1ucje5do3_640.jpg">
    </div>
    <div class="title">Nails Online</div>
    <link href="https://fonts.googleapis.com/css?family=Indie+Flower" rel="stylesheet">
    <div class="links">
      <nuxt-link :to="{path: `/users/8`}">home</nuxt-link>
      <nuxt-link :to="{path: `/admin/users`}">admin</nuxt-link>
      <a href="http://www.aoyama-eye-clinic.com/cl_info/">About</a>
      <a href="https://www.shuminoengei.jp/m-pc/a-page_p_detail/target_plant_code-350">Works</a>
      <a href="https://beauty.hotpepper.jp/kr/slnH000286231/blog/W000225989/">Blog</a>
      <a href="https://yumeg.com/shopdetail/000000001572/">Shop</a>
      <a href="https://beauty.hotpepper.jp/CSP/kr/reserve/?storeId=H000286231&staffId=W000225989">Contact</a>
    </div>
    <div class="images">
      <img v-for="image in images" :key="image.id" :src="image.image_url" class="image">
    </div>
  </div>
</template>

<script>
export default {
  head: {
    title: "nails online",
  },
  async asyncData({app, error}) {
    try {
      const { data } = await app.$axios.get(`/api/images`)
      return {
        images: data.images,
      }
    } catch (err) {
      return {
        statusCode: err.response.status,
        message: err.response.statusText,
      }
    }
  },
}
</script>

<style lang="scss" scoped>
.main-image {
  margin-top: 2rem;
  text-align: center;
  img {
    width: 125px;
    height: 150px;
  }
}
.title {
  margin-top: 2rem;
  text-align: center;
  font-family: "Indie Flower", cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: 15;
  font-size:50px;
}
.links {
  text-align: center;
  margin-bottom: 2rem;
  a {
    color: #777777;
  }
}
.images {
  width: 60%;
  margin: auto;
  display: flex;
  text-align: center;
  vertical-align: middle;
}
.image {
  width: 80px;
  height: 80px;
}

</style>
