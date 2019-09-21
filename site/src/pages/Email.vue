<template>
  <syllabus-layout>
    <v-card width="1500" class="mx-auto email-title">
      <v-card-title>
        All
        <span class="email-length">{{ $page.allEmail.totalCount }}</span>
        Records
        <v-switch class="simplify-switch" v-model="simplify" label="Simplify" />
        <v-spacer />
        <v-text-field v-model="searchText" append-icon="search" label="名前検索"></v-text-field>
      </v-card-title>
      <v-simple-table fixed-header>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="email in emails" :key="email.id">
            <td class="email-linkstyle">
              <g-link
                class="email-linkstyle"
                :to="`/teacher/${email.teacher.id}`"
              >{{ email.teacher.name }}</g-link>
            </td>

            <td class="email-padding-left-0">
              <v-col v-for="(address,id) in email.addresses" :key="id">
                <a class="email-linkstyle" :href="`mailto:${address.link}`">{{address.link}}</a>
                <span v-if="!simplify">
                  <g-link :to="`/subject/${address.subject.id}`">
                    <v-btn
                      class="ma-2 email-substyle"
                      tile
                      outlined
                      color="primary"
                    >{{address.subject.title}}</v-btn>
                  </g-link>
                </span>
              </v-col>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
    </v-card>
  </syllabus-layout>
  <!--
  <syllabus-layout>
    <h2 class="syllabus-page-title">
      All
      <span class="syllabus-page-title-count">{{ $page.allEmail.totalCount }}</span>
      Records
    </h2>
    <input placeholder="名前検索" class="syllabus-input" v-model="searchText" />
    <div class="email-simplify-wrapper">
      <label class="email-simplify-label" for="simplify">simplify</label>
      <input type="checkbox" name="simplify" v-model="simplify" />
    </div>
    <ul class="syllabus-list">
      <li class="syllabus-list-item" v-for="email in emails" :key="email.id">
        <g-link class="syllabus-button-link email-teacher" :to="`/teacher/${email.teacher.id}`">
          {{
          email.teacher.name
          }}
        </g-link>
        <div class="email-wrapper">
          <span class="email-item" v-for="(address,id) in email.addresses" :key="id">
            <a :href="`mailto:${address.link}`" class="email-address">{{address.link}}</a>
            <span v-if="!simplify" class="email-subject">
              <g-link :to="`/subject/${address.subject.id}`">({{address.subject.title}})</g-link>
            </span>
          </span>
        </div>
      </li>
    </ul>
  </syllabus-layout>
  -->
</template>

<page-query>
query {
  allEmail {
    totalCount
    edges {
      node {
        teacher {
          id
          name
        }
        addresses {
          link
          subject {
            id
            title
          }
        }
      }
    }
  }
}

</page-query>

<script>
export default {
  data() {
    return {
      searchText: "",
      simplify: false
    };
  },
  computed: {
    emails() {
      let emails = JSON.parse(
        JSON.stringify(this.$page.allEmail.edges.map(({ node }) => node))
      );

      if (this.simplify) {
        emails = emails.map(item => {
          const addressLinks = [];

          const addresses = item.addresses.filter(address => {
            if (!addressLinks.includes(address.link)) {
              addressLinks.push(address.link);
              return true;
            }
          });
          item.addresses = addresses;
          return item;
        });
      }
      if (this.searchText) {
        emails = emails.filter(item => {
          return item.teacher.name.includes(this.searchText);
        });
      }

      return emails;
    }
  }
};
</script>

<style lang="scss" scoped>
.email {
  &-title {
    padding: 30px 40px;
  }
  &-length {
    margin: 5px;
    font-size: 1.2em;
    color: rgb(0, 147, 226);
  }
  &-linkstyle {
    color: #000;
    font-size: 1.1em;
  }
  &-substyle {
    font-size: 0.8em;
    letter-spacing: -0.5px;
  }
  &-padding-left-0 {
    padding-left: 0;
  }
}
.simplify {
  &-switch {
    margin-left: 20px;
  }
}
/*
.email {
  &-teacher {
    width: 40%;
  }
  &-wrapper {
    width: 60%;
    text-align: left;
  }
  &-simplify {
    &-label {
      color: slategrey;
    }
    &-wrapper {
      font-weight: bold;
      padding: 1rem;
      font-size: 1.6rem;
    }
  }
  &-item {
    display: flex;
    width: fit-content;
    align-items: center;
    flex-wrap: wrap;
  }
  &-address {
    text-decoration: underline;
    color: inherit;
    width: fit-content;
  }
  &-subject {
    font-size: 0.8rem;
    color: #888;
  }
}
@media screen and (max-width: 640px) {
  .syllabus {
    &-list {
      &-item {
        flex-wrap: wrap;
      }
    }
  }
  .email {
    &-teacher {
      width: 100%;
    }
    &-wrapper {
      width: 100%;
    }
  }
}
*/
</style>