<template>
  <syllabus-layout class="teacher">
    <h1 class="syllabus-page-title">{{ $page.category.name }}</h1>
    <p class="teacher-subjects-count">
      講義数
      <span class="syllabus-page-title-count">{{ subjects.length }}</span>
    </p>

    <syllabus-statistics :subjects="statistics" :keys="['teacher']" />

    <syllabus-list :items="subjects" />
  </syllabus-layout>
</template>

<page-query>
query Category($id: String!) {
  category: category(id: $id) {
    name
    subjects {
      node {
        id
        title
        teacher{
          name
        }
      }
    }
  }
}
</page-query>

<script>
export default {
  metaInfo() {
    return {
      title: this.$page.category.name
    };
  },
  computed: {
    statistics() {
      const node = this.$page.category.subjects.node.map(n => ({
        ...n,
        teacher: n.teacher.name
      }));

      return { node };
    },
    subjects() {
      let items = this.$page.category.subjects.node.map(({ title, id }) => {
        return {
          id,
          name: title,
          url: `/subject/${id}`
        };
      });
      return items;
    }
  }
};
</script>

<style lang="scss" scoped>
.teacher {
  &-subjects {
    &-count {
      color: $theme-green;
      text-align: center;
    }
  }
}
</style>
