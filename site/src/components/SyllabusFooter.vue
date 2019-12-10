<template>
  <v-footer class="syllabus-footer-root" padless color="#fafafa">
    <v-col class="syllabus-footer" cols="12">
      <span>
        updated:
        <time>{{updateTime}}</time>
      </span>
      <span>
        edit on
        <a
          href="https://github.com/koorimizuw/digicam-syllabus-material-ui"
          rel="noopener"
          target="_blank"
        >github</a>
      </span>
    </v-col>
  </v-footer>
  <!--
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
  -->
</template>

<script>
const { updateTime } = require("../../../data/update.json");
export default {
  data() {
    return {
      updateTime
    };
  }
};
</script>


<style lang="scss">
.syllabus-footer {
  display: flex;
  justify-content: space-between;
  &-root {
    margin-top: 10px;
  }
}
/*
.syllabus-footer {
  margin-top: 3rem;
  align-items: center;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  height: 3rem;
  background-color: #f2f6f5;
  color: slategrey;
  &-link {
    &-github {
      text-decoration: underline;
    }
  }
}
*/
</style>
