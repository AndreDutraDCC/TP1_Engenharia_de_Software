<template>     
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-card-title class="white--text primary darken-4">
     <v-icon class="white--text mx-2">mdi-magnify</v-icon> {{title}}

      <v-spacer></v-spacer>
        <v-tooltip left>
        <template v-slot:activator="{ on, attrs }">
            <v-btn
                color="white"
                class="text--primary"
                fab
                small
                v-bind="attrs"
                v-on="on"
            >
                <v-icon>mdi-plus</v-icon>
            </v-btn>
        </template>
        <span>Adicionar Todas</span>
        </v-tooltip>

    </v-card-title>

    <v-card-text class="pt-4">
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quasi nobis a at voluptates culpa optio amet! Inventore deserunt voluptatem maxime a veniam placeat, eos impedit nulla quos? Officiis, aperiam ducimus.
    </v-card-text>

    <v-divider></v-divider>

    <v-virtual-scroll
      :items="teste"
      :item-height="100"
      height="500"
    >
    <template v-slot:default="{ item }">
        <Music/>
        <!-- <Music :music="item"/> -->
    </template>
    </v-virtual-scroll>
  </v-card>
</template>

<script>
import Music from '@/components/Music'

export default {
    name: 'MusicList',
    props: ["title"],
    components: {
      Music,
    },
    data: () => ({
        teste: [
            {color: '#2196F3', fullName: 'Oliver Smith', initials: 'OS'},
            {color: '#90CAF9', fullName: 'Jake Anderson', initials: 'JA'},
        ]
    //   colors: ['#2196F3', '#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5', '#1976D2', '#1565C0', '#0D47A1', '#82B1FF', '#448AFF', '#2979FF', '#2962FF'],
    //   names: ['Oliver', 'Jake', 'Noah', 'James', 'Jack', 'Connor', 'Liam', 'John', 'Harry', 'Callum', 'Mason', 'Robert', 'Jacob', 'Jacob', 'Jacob', 'Michael', 'Charlie', 'Kyle', 'William', 'William', 'Thomas', 'Joe', 'Ethan', 'David', 'George', 'Reece', 'Michael', 'Richard', 'Oscar', 'Rhys', 'Alexander', 'Joseph', 'James', 'Charlie', 'James', 'Charles', 'William', 'Damian', 'Daniel', 'Thomas', 'Amelia', 'Margaret', 'Emma', 'Mary', 'Olivia', 'Samantha', 'Olivia', 'Patricia', 'Isla', 'Bethany'],
    //   surnames: ['Smith', 'Anderson', 'Clark', 'Wright', 'Mitchell', 'Johnson', 'Thomas', 'Rodriguez', 'Lopez', 'Perez', 'Williams', 'Jackson', 'Lewis', 'Hill', 'Roberts', 'Jones', 'White', 'Lee', 'Scott', 'Turner', 'Brown', 'Harris', 'Walker', 'Green', 'Phillips', 'Davis', 'Martin', 'Hall', 'Adams', 'Campbell', 'Miller', 'Thompson', 'Allen', 'Baker', 'Parker', 'Wilson', 'Garcia', 'Young', 'Gonzalez', 'Evans', 'Moore', 'Martinez', 'Hernandez', 'Nelson', 'Edwards', 'Taylor', 'Robinson', 'King', 'Carter', 'Collins'],
    }),

    computed: {
      items () {
        const Length = this.teste.length
        // const namesLength = this.names.length
        // const surnamesLength = this.surnames.length
        // const colorsLength = this.colors.length

        return Array.from({ length: 10000 }, (k, v) => {
          const name = this.names[this.genRandomIndex(namesLength)]
          const surname = this.surnames[this.genRandomIndex(surnamesLength)]

          return {
            color: this.colors[this.genRandomIndex(colorsLength)],
            fullName: `${name} ${surname}`,
            initials: `${name[0]} ${surname[0]}`,
          }
        })
      },
    },

    methods: {
      genRandomIndex (length) {
        return Math.ceil(Math.random() * (length - 1))
      },
    },
}
</script>

<style>

</style>