<template>
  <div>
    <div class="yumeka">
      <img src="https://imgbp.hotp.jp/CSP/IMG_SRC_K/14/49/C007371449/C007371449_164-219.jpg">
    </div>
    <div class="title">yumeka online</div>
    <div class="links">
      <nuxt-link :to="{path: `/users/8`}">home</nuxt-link>
      <nuxt-link :to="{path: `/admin/users`}">admin</nuxt-link>
      <a href="http://www.aoyama-eye-clinic.com/cl_info/">About</a>
      <a href="https://www.shuminoengei.jp/m-pc/a-page_p_detail/target_plant_code-350">Works</a>
      <a href="https://beauty.hotpepper.jp/kr/slnH000286231/blog/W000225989/">Blog</a>
      <a href="https://yumeg.com/shopdetail/000000001572/">Shop</a>
      <a href="https://beauty.hotpepper.jp/CSP/kr/reserve/?storeId=H000286231&staffId=W000225989">Contct</a>
    </div>
    <div class="images">
      <img v-for="image in images" :key="image.id" :src="image.image_url" class="image">
    </div>
  </div>
</template>

<script>
export default {
  head: {
    title: "yumeka online",
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
.yumeka {
  text-align: center;
  img {
    width: 125px;
    height: 150px;
  }
}
.title {
  margin-top: 1rem;
  text-align: center;
  font-family: cursive;
  font-weight: 50;
  font-size:24px;
}
.links {
  text-align: center;
  margin-bottom: 2rem;
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
