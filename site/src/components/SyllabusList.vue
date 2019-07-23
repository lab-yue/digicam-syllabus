<template>
  <ul class="syllabus-list">
    <li class="syllabus-list-item" v-for="item in items" :key="item.id">
      <g-link class="syllabus-button-link" :to="item.url">{{item.name}}</g-link>
    </li>
  </ul>
</template>

<script>
export default {
  props: ["items"]
};
</script>


<style lang="scss">
.syllabus-list {
  &-item {
    transition: 0.3s all ease-in-out;
    font-size: 1.2rem;
    border-bottom: 1px solid $theme-pale-green;
    a {
      display: block;
      padding: 2rem;
    }
    &:hover {
      background-color: $theme-pale-green;
    }
  }
}
</style>
