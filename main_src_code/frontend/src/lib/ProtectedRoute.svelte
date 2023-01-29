<script>
	import { Route, Link } from 'svelte-routing';
	import { user } from './store';
	import AccessDenied from "./AccessDenied.svelte";
	
	export let path;
	export let component;

	$: isUser = $user;

</script>

{#if isUser !== null}
	<Route path={path} component={component} />
{:else }
	<Route path={path} component={AccessDenied} />
{/if}