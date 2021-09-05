<script>
  import {
    Header,
    HeaderUtilities,
    HeaderGlobalAction,
    Icon,
    TooltipDefinition
  } from "carbon-components-svelte";
  import Login20 from "carbon-icons-svelte/lib/Login20";
  import Logout20 from "carbon-icons-svelte/lib/Logout20";
  import { Link,navigate } from "svelte-routing";
  import { user, token } from "./store";

  let isSideNavOpen = false;

  $: isUser = $user;

  let logout = (e) => {
    e.preventDefault();
    $user = null;
    $token = null;
    navigate("/", { replace: true });
  }
</script>

<Header platformName="Clinical Decision System" bind:isSideNavOpen>
  <HeaderUtilities>
    {#if isUser === null}
      <TooltipDefinition tooltipText="Login/Sign Up" align="end">
        <Link to="/authuser"><HeaderGlobalAction aria-label="Login" icon={Login20} /></Link>
      </TooltipDefinition>
    {:else}
      <TooltipDefinition tooltipText="Logout" align="end">
        <HeaderGlobalAction aria-label="Logout" icon={Logout20} on:click={logout} />
      </TooltipDefinition>
    {/if}
  </HeaderUtilities>
</Header>