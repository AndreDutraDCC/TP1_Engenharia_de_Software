<template>
<v-row :class="rowClass">
    <v-col v-for="item in inputs" :key="item.label" 
    :cols="colsCols(item.columns, 'cols')"
    :xs="colsCols(item.columns, 'xs')"
    :sm="colsCols(item.columns, 'sm')"
    :md="colsCols(item.columns, 'md')"
    :lg="colsCols(item.columns, 'lg')"
    :xl="colsCols(item.columns, 'xl')"
    >
        <AutoInput
        :ref="item.key"
        v-model="value1[item.key]"
        :key="item.key"
        :key2="item.key"
        :type='item.type'
        :label='item.label'
        :rules='item.rules'
        :outlined='item.outlined'
        :placeholder='item.placeholder'
        :hint='item.hint'
        :persistentHint='item.persistentHint'
        :prependIcon='item.prependIcon'
        :prependInnerIcon='item.prependInnerIcon'
        :prependOuterIcon='item.prependOuterIcon'
        :appendIcon='item.appendIcon'
        :appendInnerIcon='item.appendInnerIcon'
        :appendOuterIcon='item.appendOuterIcon'
        :color='item.color'
        :trackColor="item.trackColor"
        :thumbColor="item.thumbColor"
        :thumbLabel="item.thumbLabel"
        :thumbValue="item.thumbValue"
        :min="item.min"
        :max="item.max"
        :step="item.step"
        :value='item.value'
        :hideDetails='item.hideDetails'
        :items='item.items'
        :chips='item.chips'
        :multiple='item.multiple'
        :dense='item.dense'
        :doubt='item.doubt'
        :callbackAction='item.callbackAction'
        :background='item.background'
        :monetary='item.monetary'
        :loading='item.loading'
        :filter='item.filter'
        :cnpj='item.cnpj'
        :disabled='item.disabled'
        :counter='item.counter'
        :ratio='item.ratio'
        :readonly='item.readonly'
        :prefix='item.prefix'
        :suffix='item.suffix'
        :bucket='item.bucket'
        :subfolder='item.subfolder'
        :maxWidth='item.maxWidth'
        :autoGrow="item.autoGrow"
        :rows="item.rows"
        :rowConfig="item.rowConfig ? item.rowConfig : {}"
        @update="update"
        @onChange="onChange"
        @action="$emit('action', item.key)"
        :stylization="item.stylization"
        v-if="!item.hide"
        />
    </v-col>
</v-row>
</template>
<script>
import AutoInput from "@/components/forms/Input";

export default {
    name: 'autoForm',
    components: {
        AutoInput,
    },
    data(){
        return{
            value1: {}
        }
    },
    methods:{
        colsCols(cols, size){
            if(cols){
                if(typeof cols == 'object') return cols[size]
                else return cols
            }else return 12
        },
        update(key) {
            this.$emit('input', this.value1)
            this.$emit('update', key)
        },
        onChange(key) {
            // console.log(this.rowClass)
            this.$emit('input', this.value1)
            this.$emit('onChange', key)
        },
        start() {
            this.inputs.forEach(item => {
                this.value1[item.key] = this.value[item.key] ? this.value[item.key] : ''
                this.$refs[item.key][0].start()
            });
        }
    },
    beforeMount(){
        this.inputs.forEach(item => {
            this.value1[item.key] = this.value ? ( this.value[item.key] ? this.value[item.key] : '') : ''
        });
    },
    computed: {
        rowClass1(){
            console.log("aaaaa ", this.rowClass)
            return this.rowClass
        }
    },
    props: ['inputs','value', 'rowClass']
}
</script>