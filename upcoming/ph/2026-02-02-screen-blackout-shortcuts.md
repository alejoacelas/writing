# Screen blackout shortcuts to support focus

*Source: https://wow.pjh.is/journal/screen-blackout-shortcuts*  ·  *Published: 2026-02-02*

---

Multi-agent workflows can be very distracting. I often have 3–5 agents running with several more awaiting review, spread across [four screens](https://wow.pjh.is/journal/llm-screen). It's like managing a team on Slack—but your directs are checking in every few minutes, rather than every few hours.

But then: chunks of my day also require deep, focussed work. And having all my agent terminals visible—running, or waiting for review—is a big distraction.

So I made some shortcuts to toggle screen visibility:

- **CAPS LOCK + 2** — Black out all screens except my primary monitor (toggle)
- **CAPS LOCK + 3** — Black out the screen under my mouse cursor (toggle)
- **CAPS LOCK + 4** — Restore all blacked-out screens [1](#user-content-fn-1)

This uses [Hammerspoon](https://www.hammerspoon.org/). Install it with:

```bash
brew install hammerspoon

```

Then add this to your `~/.hammerspoon/init.lua`:

```lua
-- =============================================================================
-- Screen Blackout Feature
-- =============================================================================

local blackoutCanvases = {}  -- Table to store black canvases, keyed by screen ID

-- Change this to your primary screen name (find it via hs.screen.allScreens() in Hammerspoon console)
local primaryScreenName = "DELL S2725QC"

local function blackoutScreen(screen)
    local screenId = screen:id()
    if blackoutCanvases[screenId] then
        return false
    end

    local frame = screen:fullFrame()
    local canvas = hs.canvas.new(frame)
    canvas:appendElements({
        type = "rectangle",
        action = "fill",
        fillColor = { black = 1.0, alpha = 1.0 },
        frame = { x = 0, y = 0, w = frame.w, h = frame.h }
    })
    canvas:level(hs.canvas.windowLevels.screenSaver)
    canvas:show()

    blackoutCanvases[screenId] = canvas
    return true
end

local function restoreScreen(screen)
    local screenId = screen:id()
    if blackoutCanvases[screenId] then
        blackoutCanvases[screenId]:delete()
        blackoutCanvases[screenId] = nil
        return true
    end
    return false
end

local function toggleBlackoutScreenUnderMouse()
    local mouseScreen = hs.mouse.getCurrentScreen()
    if not mouseScreen then return end

    if blackoutCanvases[mouseScreen:id()] then
        restoreScreen(mouseScreen)
    else
        blackoutScreen(mouseScreen)
    end
end

local function toggleBlackoutAllExceptPrimary()
    local screens = hs.screen.allScreens()
    local anyBlackedOut = false

    for _, screen in ipairs(screens) do
        if screen:name() ~= primaryScreenName and blackoutCanvases[screen:id()] then
            anyBlackedOut = true
            break
        end
    end

    for _, screen in ipairs(screens) do
        if screen:name() ~= primaryScreenName then
            if anyBlackedOut then
                restoreScreen(screen)
            else
                blackoutScreen(screen)
            end
        end
    end
end

local function restoreAllScreens()
    for _, canvas in pairs(blackoutCanvases) do
        canvas:delete()
    end
    blackoutCanvases = {}
end

-- Bind hotkeys (Hyper = Cmd+Ctrl+Alt+Shift, or use whatever modifier you prefer)
hs.hotkey.bind({"cmd", "ctrl", "alt", "shift"}, "2", toggleBlackoutAllExceptPrimary)
hs.hotkey.bind({"cmd", "ctrl", "alt", "shift"}, "3", toggleBlackoutScreenUnderMouse)
hs.hotkey.bind({"cmd", "ctrl", "alt", "shift"}, "4", restoreAllScreens)

```

After saving, reload your config (click the Hammerspoon menu bar icon → Reload Config).

## Footnotes

1. If you've not already [made CAPS LOCK into a hyperkey](https://manual.raycast.com/hyperkey), I strongly recommend doing so. Otherwise, update the Hammerspoon script to use different shortcuts. [↩](#user-content-fnref-1)
