---
title: How to let users request Microsoft Edge extensions without losing control
tags:
  - Microsoft Edge
  - Edge for Business
  - Intune
  - Browser Extensions
---
If you want users to stay productive without turning extension management into a free-for-all, a request-based approach can be a good middle ground.

Instead of allowing every Microsoft Edge extension by default, you can block extensions broadly and let users request the ones they need. That gives IT a review step before an extension becomes available, which is useful when extensions can access browsing activity, page content, cookies, or other sensitive data.

This post walks through a practical way to set that up by using the Microsoft Edge management service and then explains what the user and admin experience looks like afterward.

## Why use a request-based model

An all-or-nothing model usually creates one of two problems:

- Users install too many unreviewed extensions
- IT blocks everything and creates friction for common work

A request workflow gives you a middle path. Users can still discover tools they want, but approval stays with the administrator. That is especially helpful when you want to evaluate extensions for security, privacy, and business fit before allowing them into the environment.

## What you need before you start

Before configuring requests, make sure you already have Edge managed in your tenant and that you know where extension management is being enforced today.

That matters because extension settings can overlap between Microsoft Intune and the Microsoft Edge management service. If you already enforce extension behavior elsewhere, review that first so you do not create conflicting policies.

## Step 1: Create a baseline policy that blocks extensions by default

In the Microsoft Edge management service, create or update a configuration policy for the users who should be covered by this workflow.

The goal of the baseline policy is simple:

- block extensions by default
- allow only the extension types you want
- block unmanaged or external extension paths if that fits your security posture

From there, the request feature becomes useful because blocked extensions can be surfaced for admin review instead of being silently unavailable.

## Step 2: Turn on extension requests

Once the blocking policy is in place, go to the Extensions area of the configuration policy and open the Requests tab.

Enable extension requests for the policy and, if you want, add email notifications so an administrator or shared mailbox receives new request summaries. A shared IT mailbox is often better than a personal inbox if more than one admin reviews browser requests.

At this point, the policy is no longer just blocking. It is now collecting demand from users in a controlled way.

## Step 3: Test the user experience

After policy sync, have a test user try to install an extension that is currently blocked.

The expected behavior is that the user sees an option to request access instead of receiving a hard stop with no path forward. That is the moment where the experience becomes much more sustainable for real users. They do not need to open a separate ticket first just to tell IT what they were trying to install.

When you publish this article for your own audience, this is a great place to include:

- one screenshot of the blocked-extension prompt
- one sentence explaining what justification users should provide

## Step 4: Review and approve requests as an admin

Back in the Microsoft Edge management service, open the Requests view for the same configuration policy.

From there, review the requested extension and decide whether to:

- allow it
- keep it blocked
- force or normally install it if that matches your standard

Your review should be more than "does the user want it?" A good approval check includes:

- what permissions the extension requires
- whether it accesses sensitive internal sites
- whether there is a safer alternative
- whether the extension is needed by more than one team

If you approve it, the user can install it after the policy refresh reaches their device and profile.

## A few gotchas worth calling out

This is the section that usually makes a post feel genuinely useful, so it is worth keeping in your version.

First, watch for policy conflicts. If Intune or another management path is already defining overlapping extension behavior, the results can be confusing.

Second, remember that browser extension management is not just about installation. Host access, blocked permissions, and forced installs can matter just as much as whether an extension is technically allowed.

Third, test with a small user group before rolling this out broadly. That helps you confirm both the request flow and the approval workflow without creating noise for your whole tenant.

## Recommended article structure for your own writing

If you want to write your own version in a way that feels original and useful, this outline works well:

1. Start with the business problem
2. Explain why a request workflow is safer than fully open installs
3. Show the setup at a high level
4. Show the user experience
5. Show the admin approval experience
6. End with gotchas, testing notes, and recommendations

That structure keeps the post practical while still sounding like your own point of view.

## What I would customize before publishing

To make this truly yours, replace the generic parts with your own environment and opinions:

- add screenshots from your tenant
- name the actual team or use case that needed extension requests
- explain what your approval criteria are
- mention whether you use Intune, Edge management service, or both
- add one short "what surprised me" section from your testing

Those details are what separate an inspired post from a copied one.

## Sources and further reading

This article was written as an original post for this site after reviewing Microsoft documentation and the overall structure of Peter van der Woude's post on the same topic.

- Microsoft Learn: [Extensions management](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-management-service-extensions)
- Microsoft Learn: [Manage Microsoft Edge extensions in the enterprise](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions)
- Inspiration for topic structure: [Allowing users to request the installation of browser extensions for Microsoft Edge](https://petervanderwoude.nl/post/allowing-users-to-request-the-installation-of-browser-extensions-for-microsoft-edge/)
