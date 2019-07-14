<template>
  <main>
    <h1 class="syllabus-title">Syllabus</h1>

    <div class="syllabus-container">
      <syllabus-button class="home-button" :link="link" v-for="link in links" :key="link.name" />
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      links: [
        { name: "講義", url: "/subject" },
        { name: "先生", url: "/teacher" },
        { name: "分類", url: "/category" },
        { name: "分野", url: "/field" }
      ]
    };
  }
};
</script>

<style lang="scss">
.home {
  &-button {
    font-size: 2rem;
    margin: 1rem;
  }
}
</style>
