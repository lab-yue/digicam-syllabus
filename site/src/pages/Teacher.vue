<template>
  <div>
    <h2>Teachers</h2>
    <ul>
      <li v-for="edge in $page.allTeacher.edges" :key="edge.node.id">
        <g-link :to="`/teacher/${edge.node.id}`">{{ edge.node.name }}</g-link>
      </li>
    </ul>
  </div>
</template>

<page-query>
query {
  allTeacher {
    edges {
      node {
        id
        name
      }
    }
  }
}
</page-query>

<script>
export default {};
</script>


<style lang="scss" scoped>
</style>
