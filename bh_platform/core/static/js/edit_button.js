Vue.component('edit-button', {
    props: [
        "caption"
    ],
    data: () =>({
        dialog: false,
    }),
    methods: {
        
    },
    template: `
    <span>
    <v-btn
      color="primary"
      dark
      @click.stop="dialog = true"
    >
      Open Dialog
    </v-btn>    
    <v-dialog
        v-model="dialog"
        max-width="290"
    >
        <v-card>
        <v-card-title class="headline">Редактирование</v-card-title>

        <v-card-text>
        <v-text-field
            :label="caption"
        ></v-text-field>
        </v-card-text>

        <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn
            color="green darken-1"
            flat="flat"
            @click="dialog = false"
            >
            Disagree
            </v-btn>

            <v-btn
            color="green darken-1"
            flat="flat"
            @click="dialog = false"
            >
            Agree
            </v-btn>
        </v-card-actions>
        </v-card>
    </v-dialog>
    </span> 
    `

});