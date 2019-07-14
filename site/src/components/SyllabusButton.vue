<template>
  <span class="syllabus-button">
    <g-link class="syllabus-button-link" :to="link.url">{{link.name}}</g-link>
  </span>
</template>

<script>
export default {
  props: ["link"]
};
</script>


<style lang="scss">
.syllabus-button {
  transition: 0.3s all ease-in-out;
  padding: 5px 1rem;
  font-size: 1rem;
  margin: 5px;
  border-radius: 5px;
  display: inline-block;
  background-color: $theme-pale-green;
  border-bottom: 2px solid $theme-light-green;
  cursor: pointer;
  &:hover {
    background-color: $theme-light-green;
  }
  &-link {
    color: $theme-grey;
  }
}
</style>
