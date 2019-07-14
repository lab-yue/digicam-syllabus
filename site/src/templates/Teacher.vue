<template>
  <pre>{{JSON.stringify($page.teacher,null,4)}}</pre>
</template>

<page-query>
query Teacher($id: String!){
  teacher: teacher (id: $id) {
    name
    subjects{
      id
      title
    }
  }
}
</page-query>

<script>
export default {};
</script>

<style lang="scss" scoped>
</style>
