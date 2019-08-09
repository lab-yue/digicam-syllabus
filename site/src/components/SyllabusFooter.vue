<template>
  <footer class="syllabus-footer">
    <span>
      updated:
      <time>{{updateTime}}</time>
    </span>
    <span>
      edit on
      <a
        class="syllabus-footer-link-github"
        href="https://github.com/rainy-me/digicam-syllabus"
        rel="noopener"
        target="_blank"
      >github</a>
    </span>
  </footer>
</template>

<script>
export default {
  computed: {
    updateTime() {
      const offset = new Date().getTimezoneOffset() * 60 * 1000;
      return new Date(Date.now() - offset)
        .toISOString()
        .split(".")[0]
        .replace("T", " ");
    }
  }
};
</script>


<style lang="scss">
.syllabus-footer {
  margin-top: 5rem;
  align-items: center;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  height: 3rem;
  background-color: #f2f6f5;
  &-link {
    &-github {
      color: slategrey;
      text-decoration: underline;
    }
  }
}
</style>
