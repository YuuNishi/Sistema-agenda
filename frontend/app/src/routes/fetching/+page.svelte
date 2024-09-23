<script>
  import {onMount} from "svelte";
  let patients =[]
  let url='http://127.0.0.1:8000/patient'
  onMount(async()=>{
    const data = await fetch(url)
    patients = await data.json()

  })
</script>

<h1>Hello, World!!!</h1>
{#each patients as patient(patient.id)}
  <h3>id: {patient.id} nome: {patient.name}</h3>
{/each}