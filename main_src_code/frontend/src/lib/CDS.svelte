<script>
	import {
		Tile,
		MultiSelect,
		Tag,
		Button,
		InlineNotification,
		UnorderedList,
		ListItem,
	} from "carbon-components-svelte";
	import symp from "../assets/symp.json";
	import { token } from "./store";

	let sel_arr = [];
	let sel_ind = [];
	$: predictions = {};

	let symp_selected = (e) =>{
		const det = e.detail
		sel_arr = det.selected
		sel_ind = det.selectedIds
		predictions = {};
	}

	let but_click = (e) => {
		fetch("/predict", {
			method: 'POST',
			headers: {
				'Content-Type': "application/json",
				'x-access-token': $token
			},
			body: JSON.stringify(sel_ind),
		}).then(resp => resp.json())
		.then(data => {
			predictions = data;
		})
		.catch((error) => console.log(error));
	}
</script>

<Tile>
	<h2 class="heading"> AI Symptoms Checker </h2>
	<br />
	<h6> Please search for your Symptom </h6>
	<br />
	<MultiSelect 
	spellcheck = "false"
	filterable
	placeholder = "Filter Symptom Names"
	items={symp}
	size="xl" on:select = {symp_selected}
	/>
	<br />
	<h6> Symptoms selected </h6>
	{#if sel_arr.length !== 0}
	{#each sel_arr as symp}
	<Tag type="blue">{symp.text}</Tag>
	{/each}
	{:else}
	<Tag type="red">None</Tag>
	{/if}
	<br />
	<div class="but_align">
		<Button disabled={(sel_arr.length === 0)} size="lg" on:click = {but_click}>Analyse</Button>
	</div>
	<div>
		{#if Object.keys(predictions).length !== 0 && sel_arr.length !== 0}
		<InlineNotification hideCloseButton lowContrast
		kind={predictions["code"]}
		title={predictions["msg"]} 
		/>
		<Tile>
			{#if predictions["code"] === "success"}
			{#if predictions["high_rec"].length !== 0}
			<h4> Most Probable diagnosis suggestions </h4>
			<UnorderedList>
				{#each predictions["high_rec"] as item}
				<ListItem>{item}</ListItem>
				{/each}
			</UnorderedList>
			{/if}
			{#if predictions["rec"].length !==0}
			<h4> Less Probable diagnosis suggestions </h4>
			<UnorderedList>
				{#each predictions["rec"] as item}
				<ListItem>{item}</ListItem>
				{/each}
			</UnorderedList>
			{/if}
			{:else}
			{#if predictions["inconclusive"].length !== 0}
			<h4> Inconclusive </h4>
			<UnorderedList>
				{#each predictions["inconclusive"] as item}
				<ListItem>{item}</ListItem>
				{/each}
			</UnorderedList>
			{/if}
			{/if}
		</Tile>
		{/if}
	</div>
</Tile>