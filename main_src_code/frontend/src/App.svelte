<script>
	import {Router, Route} from "svelte-routing";
	import ProtectedRoute from './lib/ProtectedRoute.svelte';
	
  	import Home from './lib/Home.svelte';
  	import LogSigPage from './lib/LogSigPage.svelte';
  	import Dashboard from './lib/Dashboard.svelte';

  	export let url = "";
</script>

<main>
	<Router url={url}>
		<Route path="/"><Home /></Route>
		<Route path="/authuser"><LogSigPage /></Route>
		<ProtectedRoute path="/dashboard" component={Dashboard}/>
	</Router>
</main>

<style>
	:global(.heading) {
		text-align: center;
	}
	:global(.container) {
		position: relative;
		height: 100vh;
	}
	:global(.concen) {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}
	:global(.but_align) {
		text-align: right;
	}
</style>