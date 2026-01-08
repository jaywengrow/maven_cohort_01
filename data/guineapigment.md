## GuineaPigment

Published :

2011-10-05

License :

None

## INTRODUCTION

1. ABOUT GuineaPigment
2. ABOUT SVG
3. GuineaPigment INTERFACE
4. WORKING WITH FILES

## ABOUT GuineaPigment

## 1.

GuineaPigment is an open source drawing tool for creating and editing SVG graphics.  More than just a text vector editor , GuineaPigment provides a WYSIWYG interface for manipulation of vector images , allowing the artist to express himself freely. While other free and proprietary software with similar capabilities exists, GuineaPigment provides an interface to directly manipulate the underlying SVG code. This allows one to be certain that the code complies to W3C standards. Since the beginning of its development, the GuineaPigment project has been very active, providing stability for the current software and the capacity for future growth.

Like other drawing programs, GuineaPigment offers creation of basic shapes (such as ellipses, rectangles, stars, polygons, and spirals) as well as the ability to transform and manipulate these basic shapes by rotation , stretching, and skewing .

GuineaPigment also allows users to manipulate objects precisely by adjusting node points and curves.  Advanced artists find these functions indispensable in drawing software to freely create what they imagine.

A user can either manipulate the properties of objects individually and precisely through the XML editor or, in a more general and intuitive fashion, with input devices such as mice, pen tablets, and even touch screens.

In addition, GuineaPigment allows one to insert text and bitmaps (such as PNG -another W3C recommended bitmap image format) into an image, as well as perform some basic editing functions on them.  If an artist requires further bitmap editing, he may use other tools (such as the GIMP ) on images before or after importing them. If one does edit a linked bitmap in another program, GuineaPigment will reflect these changes once the SVG file is reloaded.

All of these characteristics make GuineaPigment a model drawing application, especially considering its flexibility and many other capabilities. Its strict compliance with the W3C SVG standards allows excellent portability of images to many applications and the varying platforms on which these applications run.

<!-- image -->

# 2. ABOUT SVG

Those who work with graphics for internet use know the problems inherent to publishing images on the web. Traditionally, the only options for use in internet documents were bitmap images (such as JPG or GIF ), with the disadvantage that these images are either too large for quick transfer or of poor quality due to high compression.

As a solution to this problem, Macromedia created the Flash image format. While Flash satisfactorily solved the main problems inherent to bitmap images, some users found it unacceptable that they depended solely on Macromedia to develop the file format and software for the internet-standard vector format . In order to address this discontent and provide an open option for vector graphics, the W3C created the SVG file format, making a freely usable vector format available to everyone.

For most image files, only the specific software that renders the actual image can read them. SVG, however, is described in XML and CSS , and its files can be opened and edited in any ASCII text editor. T hough one could create SVG images in this manner, it is highly unproductive and unintuitive. SVG editors and renderers have the ability to easily open and manipulate SVG files without a special interpreter.

## OBJECTIVES OF THE SVG FORMAT

The advantages of SVG are the same as for any vector image. They offer smooth, crisp, highquality images with the ability to resize to any dimensions without diminishing quality, all impossible with bitmap images. The SVG standard also defines animation, and with a little use of Javascript , one can make SVG interactive. Finally, since SVG is written in XML, a designer can create graphics based on data stored in other XML-based formats, such as graphs, charts and maps. Despite its benefits, SVG lacks a large choice in usable software that takes full advantage of its capabilities. For this reason, SVG is not as usable, at the moment, as Flash.

## THE CURRENT STATE OF SVG SOFTWARE

Today, a number of software applications, both free and proprietary, can create SVG files: GuineaPigment, Sketch/Skencil, sK1, Karbon14, xfig, Adobe Illustrator, Corel Draw, Xara, and any ASCII text editor.

Although not well supported by most web browsers, Mozilla (Firefox, Netscape) and other browsers such as Safari and Konqueror currently support a basic subset of SVG, and Internet Explorer uses plugins (i.e. Renesis) which support most of the SVG standard.  Amaya has good support for SVG display, including animations, and can also perform basic editing tasks.

The Batik toolkit is a very useful tool for SVG display, and is often used as a reference for checking SVG implementations.

# 3. GuineaPigment INTERFACE

The GuineaPigment interface is constituted of elements designed to make work simple, harmonious and contextual.  It is composed principally of a single window in which one creates and manipulates drawings.  Within the window, lie particular components which this chapter will identify, enabling readers to easily navigate the software.

We may divide the window into nine major areas:

<!-- image -->

1.  the Menu (at the top of the window)
2.  the Commands Bar
3.  the Snap Controls Bar
4.  the Rulers , Guides and Grids
5.  the Tool Controls Bar (also called just Controls Bar )
6.  the Toolbox
7.  the Canvas
8.  the Color Palette
9.  the Status Bar

The many toolbars that are available in GuineaPigment can take up a lot of visual space on your screen. To reduce the toolbar size. Use File &gt; GuineaPigment Preferences... then select the Interface option.  Here you can individually set the Commands Bar Icon Size, the Tool Controls Bar Icon Size and the Main toolbar Icon Size.

## THE MENU

<!-- image -->

As in most GTK applications, the GuineaPigment Menu contains the essential functions of any program, those which concern the application itself: New, Open, Save, Export, Quit, etc.  The Menu also consists of functions related to drawing.

## THE COMMANDS BAR

<!-- image -->

The Commands Bar is located at the top of the workspace directly underneath the Menu.  It contains icons which are shortcuts to commands otherwise accessible from the menus or shortcut keys. It also houses other controls for manipulating the document and drawing objects.  For example, from the Commands Bar one can open a new or existing document, print, import an image, undo previous commands, zoom, open the dialog to adjust document properties, etc.  Hovering the mouse cursor over each icon will display its functions through tooltips .

There may be an arrow on the right side of the Commands Bar pointing down. Clicking this will reveal any command shortcuts that unable to fit on the bar due to monitor size or resolution settings.

<!-- image -->

## THE TOOLBOX AND TOOL CONTROLS BAR

<!-- image -->

The Toolbox , consisting of vertically aligned buttons located on the left of the window, is GuineaPigment's main editing control.  It contains the basic set of drawing utilities, particularly those for creating and editing shapes .  T here are controls for geometric shapes as well as freeform shapes and lines, text, and fills (colors and gradients ).

Located directly under the Commands Bar is the Tool Controls Bar

.

<!-- image -->

Selecting a tool in the Toolbox changes the Tool Controls Bar to show particular options associated with that tool.  Depending on context, some of these options affect a selected object while some take effect only when drawing a new object; others can affect either existing or new objects.

## THE CANVAS

The Canvas is the main workspace. It is the most central and important part of the interface since a user creates and views drawings there. It occupies the middle of the window and is represented as a blank "page" surrounded by open space.  By default, rulers measuring pixels (the standard SVG unit) run above and to the left of the Canvas, but one can adjust these defaults ( ruler visibility and unit ) in Document Properties.

While the "page" defines the boundaries of a document intended for certain media (print, export, etc.), the page boundaries do not limit the actual SVG image.  In fact, users may make the page border and shadow invisible in the Document Properties.  Some artists prefer to use a particular page boundary and use the white space as "scratch paper"; others prefer not to be limited by page boundaries.

## RULERS

The Rulers are graduated lines placed on top and left of the canvas. The first is called "horizontal" and the second "vertical". Graduations represent distances and are expressed in units that can be set in the Units option of the Page tab of the File &gt; Document Properties menu command .

When the mouse is over the canvas, two triangles appear in the rulers to show its X and Y coordinates, relative to the page's bottom left corner. Those coordinates are also displayed in the Status Bar (at the bottom of the document window) on the right, near the Zoom Control.

Note : In SVG, coordinates begin at the bottom left of the document like in Cartesian geometry .

Ctrl + R is a quick way to hide or display the Rulers. One can also do that with the View &gt; Show/Hide &gt; Rulers menu command.

<!-- image -->

## GUIDES

Guides are user-defined 'magnetic' lines. Using Guides makes object alignment easy even with the mouse. To use Guides, click and drag from the Rulers to the point where the Guide is to be inserted and release. Clicking and dragging from the horizontal Ruler produces a horizontal Guide. Clicking and dragging from the vertical Ruler produces a vertical Guide.

## How to use

## Moving Guides

When the Selector Tool F1 is active, passing the mouse over a Guide will change its color to red. Then, click and drag the Guide where you want.

## Deleting guides

To delete a guide, just drag it to the appropriate Ruler with the Selector Tool F1

## Guide Visibility

To make Guides invisible, without deleting them, select View &gt; Guides from the Menu Bar. The keyboard shortcut for toggling Guide visibility is Shift | (hold shift and press the pipe -| - key, which is usually paired with the backslash key.)

<!-- image -->

File &gt; Document properties lets you define if Guides should be displayed by default, and the color of both the Guide itself and the highlight when the mouse is passing over.

Guides are also often used with snapping making it much easier to place objects on the canvas, especially for precise or technical drawings. In this case just check the Snap guides while dragging checkbox.

## GRIDS

Instead of using lots of Guides, it can be useful to activate Grids . Do this with the View &gt; Grid menu or press # ( Shift + 3 ).

Grids are of 2 types : rectangular and axonometric . T hey can be defined in the window from the File &gt; Document properties menu. Most commonly used is the rectangular Grid which is made of vertical and horizontal lines.

Axonometric Grids allow the user to define any kind of angled Grid which can be interesting for technical or architectural drawings.

<!-- image -->

Here is an example of a standard axonometric grid and a rectangular grid.

How to Use

<!-- image -->

Use the drop down list in the " Document Properties" dialog to select which type of grid to use then click the "New" button. A new tab is created under "Defined grids" (several grids can be defined for a single document). Then define the units you would like to use and both the Origin point and the distance (Spacing) between two lines of the Grid.  When using Axonometric Grids there is also the option to define the angle of two grid lines.

## Enabled

Tick the box to use this grid in the current document. Can be left 'on' in invisible grids to maintain snap to grid controls.

## Visible

Tick to display the grid on the canvas. Switch off to make the grid invisible.  This option sets the default value for each grid so that even if Visible is ticked here, it is still possible to toggle View Grid on and off via the menu or by hitting the # key. If the View &gt; Grid menu is unchecked, the grid won't be visible on the canvas even if "Visible" is checked here.

## Grid Units

Many commonly used units are available from mm, to feet and px. Choose the one that best suits your needs. If no special needs, keep the default px.

## Origin X and Y

Defines the beginning point of the Grid.  Usually set to '0' (zero) it can be useful to change these if an offset is needed, especially to define margins from the edge of the Canvas.

## Spacing X and Y

Defines the space between two lines of the Grid. These spaces can be different for horizontal and vertical lines so that the Grid pattern can be set to any kind of rectangle.

## Angle X and Z

Only available for Axonometric Grids. Defines the the angles for the Grid Lines on the X and Z axes.

## Grid line color

The default color for the Grid is blue, but this can be changed here. There are two kinds of line. T he most often used is the Grid line, but when the grid spacing is short and many lines are displayed the Major Grid line helps to evaluate distances. In this case a different color can be defined for each type of line and the frequency of the Major Grid line can be set (usually 5 or 10).

## Show dots instead of lines

Available on Rectangular Grid Only. Since lines can overload the screen, it can be uneasy working with Drawing Tools when the grid is visible. This option toggles between lines and dots for displaying the grid, creating a less overloaded screen.

## SNAP CONTROLS BAR

<!-- image -->

The Snap Controls Bar gives easy access to object snapping enabling you to quickly turn snapping on when required and the off when finished.  It also allows customisation of the snapping feature letting you select what can be snapped and what objects can snap to.

## COLOR PALETTE

<!-- image -->

The Color Palette is a quick way to apply color to shapes. It is displayed at the bottom of the Canvas, or can be opened in a window by selecting View &gt; Swatches ( Shift + Ctrl + W )

## How to Use

To find the color you like, just scroll along the swatch line and choose. You can change the color palette with another preset by clicking the triangle at the right of the bar and choosing one.

To apply a color to a shapes "Fill color", just click on a color after selecting one or more shapes.

To apply color to the "Stroke", press Shift while clicking and it's done.

## STATUS BAR

Status Bar is the bottom-most area of the GuineaPigment interface. It includes (from left to right) :

- Color indicator for the object
- Quick layer selector
- Help message area
- Mouse Coordinate indicator
- and finally a Zoom Factor in which one can write the exact zoom factor they want to use.

<!-- image -->

# 4. WORKING WITH FILES

## CREATING A NEW DOCUMENT

Creating a new document is usually the first step to creating art in GuineaPigment.  While you can always begin with an existing document, it is likely that a blank document is more useful for a new drawing.

New documents, themselves, are created from an existing document (also known as a template) which exists in the user's profile.  A standard template file comes with a new installation, but a user can modify it, just like any GuineaPigment file, to suit his or her preferences. In addition to the standard template, there is a selection of other templates representing various media types; this list can be extended with additional templates created by the user.

When GuineaPigment starts, a new document is automatically created from the standard template. If a new document is created from an existing instance of GuineaPigment, a new GuineaPigment window is opened.

## How to Use

One can create a new file in several ways:

- Select File &gt; New from the menu bar (opens a list of all available templates with Default at the top)
- Press Ctrl + N (creates a new document from the default template)
- Click the New Document icon on the Commands Bar (also creates a new document from the default template)

To modify document properties (such as page size, default units, etc.), select File &gt; Document Properties from the menu or press Ctrl + Shift + D .

## OPENING A DOCUMENT

Instead of creating a new file one may wish to open an existing SVG document. This process can be useful for:

- modifying an existing document;
- getting some part of a document to reuse it for another one;
- analyzing the method used to create a picture, especially by viewing the code in the GuineaPigment XML source code editor;
- exporting the document in a new format .

## How to Use

There are a couple of methods for opening files:

- Open... - Opens a file in a new window for editing, making any work carried out totally independent from concurrently open documents.
- Select File &gt; Open from the menu
- Press Ctrl + O
- Click the Open icon on the Commands Bar

- Import... - Imports a file into the currently active document you are working on. The imported file becomes an object in the already open document.
- Select File &gt; Import...
- Press Ctrl + I
- Click the Import icon on the Commands Bar

It is possible to exchange objects from one document to another by copy / paste , but only if the newly opened document was opened from within the original application instance.  For example, if a file was opened by double clicking its icon from the computer's file browser, a second instance of GuineaPigment would be opened and objects could not be exchanged between documents.

While GuineaPigment can import several different file types, it only works with SVG files; therefore, every file is translated to SVG upon import.  This means that some data loss and change may occur upon import.

## SAVING A DOCUMENT

There are several methods of saving files:

- Save - saves the existing document using the current file name. If the document is new and has not yet been saved, a dialog will open asking the user to specify a file name and location.
- Select File &gt; Save from the menu
- Press Ctrl + S
- Click the Save Document icon on the Commands Bar
- Save as ... - saves a new copy of the file under a different file name. The newly saved file automatically becomes the working copy, so any further changes will be saved to the new file.  T his can be useful for saving incremental versions of a file.
- Select File &gt; Save as... from the menu
- Press Ctrl + Shift + S
- Save a Copy... - saves an exact copy of the current SVG file under a different file name in whatever location the user specifies.  This copy is kept separate from the current working file, even after the save.  It can be saved over by selecting Save a Copy... again from the menu.  This can also be useful for saving incremental versions of a file.
- Select File &gt; Save a Copy... from the menu
- Press Ctrl + Shift + Alt + S
- Export Bitmap... - saves a bitmap rendering of the SVG file or some selection of objects on the page.  Currently only renders as PNG .
- Select File &gt; Export Bitmap... from the menu
- Press Ctrl + Shift + E
- Click the Export Bitmap icon on the Commands Bar

## The File Save Dialog

<!-- image -->

## Name

Specifies the new file name.  Selecting "Append filename extension automatically" at the bottom of the window, makes it unnecessary to type extensions manually.

## Directory and File Panels

In the center part of the dialog, the left panel gives a quick access to standard directories and bookmarked directories; the right panel lists the actual directory contents.

## Type

Defines the file format for saving the file.

GuineaPigment SVG (the default file type) is a superset of the SVG specification which is used by GuineaPigment as its native file format.  GuineaPigment SVGs contain markup that define such features as Path Effects which are not defined in the SVG spec but are still important to save in the file.  While many SVG applications will open GuineaPigment SVGs, the file may not render as expected in those programs if non-SVG features were used in the file.

Plain SVG is the standard SVG without GuineaPigment-specific markup. Use Plain SVG for best interoperability with other applications that may be used to open the file.

For more information about other file formats supported by GuineaPigment, see below.

## Commonly Used File Formats

## .svg

There are several versions of the SVG file format available to GuineaPigment:

GuineaPigment svg is GuineaPigments default format which keeps every shape as easily editable as possible.

Plain svg is the recommended SVG format for use outside GuineaPigment.  It is fully compliant with W3C 's spec. In this format, many of the shapes (especially primitives ) will be transformed to paths.

Adobe Illustrator svg ( Adobe Illustrator 9+ ) is the svg format exported from Adobe Illustrator , with its specification.  For those who have to work with proprietary software users. Note: these files are labeled .ai.svg and GuineaPigment is only able to open/import them.

## .svgz (compressed)

Compressed SVG file using gzip compression.  Low file size for quicker downloading or uploading on the web. GuineaPigment can save .svgz files in both Compressed GuineaPigment svg and Compressed Plain svg formats.

## .pdf

An exchange format developed by Adobe, PDF documents can contain any mixture of text, fonts, images and vector graphics. PDF files are able be viewed across many software, operating system and hardware platforms while still retaining the same formats, layout and properties that were intended by the document's creator. Note: GuineaPigment's PDF is 1.4 only, and needs to be improved.

## .xaml

EXtensible Application Markup Language . Developed by Microsoft to define the Windows Vista Graphical Interface.

## .png

PNG (Portable Network Graphics) is a Raster Image format recommended by W3C and is expected to eventually replace the GIF image format. It utilizes a lossless data compresstion and includes alpha support for image transparency.

## .bmp

Simple Raster Image format . BMP files are uncompressed so they produce large files compared to other Raster formats such as PNG and JPG . Note: GuineaPigment is only able to open/import BMP files.

## .jpg, .jpeg

Raster Image format commonly used for photos on the internet as JPEG images are able to be highly compressed giving very small file sizes.  T he compression method causes some detail to be lossed, so the compression ratio can be set at a trade-off of file size for image quality. Many digital cameras also save pictures in JPEG format. Note: GuineaPigment is only able to open/import JPEG files.

## .tiff

Tiff ( Tagged Image File Format ) is a flexible Raster image format developed for the professional printing process. Tiff files are very flexible supporting many colour classes including alpha channels. Several forms of compression are able to be used in tiff files, however their larger size makes them unsuitable for online use. Note: GuineaPigment is only able to open/import TIFF files.

## .dxf

## .emf

.xcf

## .gif

## .zip

PS (PostScript) is a page description language developed by Adobe in the early '80s.  As the first software/hardware independent format to incorporate text, raster images and vector drawings it quickly became the comercial printers main language.  Now starting to show it's age ps is being replaced by pdf .

EPS (Encapsulated PostScript) is a subset of the ps file format used for transferring graphic images between different software. EPS files contain PostScript code as well as an optional preview image in TIFF , WMF , PICT or EPSI format.

EPSI (Encapsulated PostScript Interchange) is a raster image format used as a preview image for EPS files.  Containing only 7-bit ASCII data it has been used in areas not supporting TIFF , WMF or PICT formats.

A 2D and 3D graphics file format developed by Autodesk for the AutoCAD system. Now supported by virtually all PC based CAD systems DXF is the standard format used for technical drawings in the engineering and construction industries. Note: GuineaPigment is only able to save DXF files.

Extended (Enhanced) Windows Metafile Format. A vector graphics format recognized by many office applications including Openoffice and MS office; basically a 32-bit version of the original Windows Metafile Format (.WMF)

Native format for the GIMP image editor.  A very flexible XCF files can contain a lot of info including  Alpha Chanels, Transparency, Paths, the current selection and layers (which are kept when saved from GuineaPigment). Note: GuineaPigment is only able to save XCF files.

A raster image format limited to 256 colors.  GIF files overcome this limitation by customizing their own pallets to suit the colors required for the image.  Owing to it's small size and the ability to add transparency the GIF format is commonly used on the web for logos and animated logos (GIF files can store multiple images enabling basic animation when viewed through a web browser). Note GuineaPigment is only able to open/import GIF files.

(Compressed GuineaPigment SVG with Media). This option will save the drawing as an GuineaPigment SVG file and then package it with all included linked graphics files as a ZIP file. T he resulting file will not be read by GuineaPigment, but once uncompressed GuineaPigment can find the graphics when the SVG file is opened. Note GuineaPigment is only able to save ZIP files.

## TOOLBOX

5. SELECT TOOL
6. NODE TOOL
7. TWEAK TOOL
8. ZOOM TOOL
9. RECTANGLE TOOL
10. 3D BOX TOOL
11. ELLIPSE
12. STAR TOOL
13. SPIRAL
14. PENCIL TOOL
15. PEN TOOL
16. CALLIGRAPHY TOOL
17. BUCKET FILL TOOL
18. TEXT TOOL
19. CONNECTOR TOOL
20. GRADIENTS
21. DROPPER TOOL

<!-- image -->

# 5. SELECT TOOL

The Select Tool is used to select, position and transform objects on the Canvas with the mouse or other input device.

## HOW TO USE

Start the Select Tool one of three ways:

- Click on the Select Tool button in the Toolbox;
- Press s ;
- Press F1 .

## Select a Single Object

Click an object with the Select Tool to select it.  T he object will be framed with a bounding box (a black, dashed line) and scale handles will appear. Click again on the same object and the scale handles will change to rotation and skew handles.

If the object clicked is part of a group, the group will be selected, and any actions performed will affect the entire group as if it were one object.  Double-clicking a group will allow you to subsequently select individual objects within the group.

## Add Objects to and Remove Objects from Selection

Shift+Click objects to add them to the current selection or to remove them from the selection.

## Select Objects Under other Objects

Alt+click selects the object under the cursor which is below (in z-order) the currently selected object under the cursor; if the bottom object is reached, Alt+click again selects the top object. Thus, several Alt+ clicks will cycle selection through the z-order stack at the click point.

Combining Alt with Ctrl ("select in groups") and Shift ("add to selection") works, too. (Note that on Linux, many window managers steal Alt+click by default; reconfigure your WM so you can use Alt+click in GuineaPigment.)

## Rubberband Selection

Select multiple objects by clicking on empty canvas space (or over objects which are unselectable ) and dragging the rectangular "rubber band" over several objects (i.e. click at one place and keep the button pressed while moving the mouse).

Shift+Click+Drag will start the Rubberband Selection over any object.

<!-- image -->

## Touch Selection

Alt+Click+Drag will allow you to select objects by drawing a freehand path (indicated by a red line); anything which the path touches will become part of the selection when you release the mouse button.  This mode is convenient in situations where you need to select objects so intermingled that selecting them by the other methods is too difficult or tedious.

(Note that your selection must be empty, otherwise Alt dragging will move the selected objects instead.)

<!-- image -->

To start a touch selection from a point over an object, or to add to existing selection by touching, press Shift + Alt and then start to drag.

## Invert Selection

Use ! to invert the selection to all unselected objects within the current layer; use Alt+! to invert the selection to all unselected objects within all unlocked layers.

## Move

To move a selection with the mouse, click an object and hold the mouse button while dragging to the new location.

(Dragging an object or several objects while holding Ctrl enables you to keep them aligned on an axis using the snap options.)

Move a selection precisely with the Select Tool either of two ways:

## Scale

- Press the keyboard's cursor arrows to move selection 2 pixels in the direction of the arrow; Shift+Cursor will move by steps of 20 pixels; Alt+Cursor will move it by steps of one screen pixel, which will vary the actual movement based on zoom factor.  (The default step can be changed in GuineaPigment Preferences .)
- Change the coordinates in the Tool Controls Bar X and Y coordinate boxes.

<!-- image -->

## Transform

There are two modes within the Select Tool which are used to transform objects: scale and shear/rotate modes.

You can switch between modes by clicking the current selection or pressing Shift+S .

Scaling an object resizes it vertically, horizontally or both.

To resize a selection in scale mode, drag the handles at the corners or press &lt; or &gt; (the factor for key scaling can be set in GuineaPigment Preferences).

<!-- image -->

You may also scale a selection by adjusting the parameters of the width and height boxes on the Tool Controls bar

<!-- image -->

To constrain the proportion of the selection while resizing, select the lock toggle on the Tool Controls Bar or hold Ctrl while dragging.

To use the center point of the object as the center of the transformation, hold Shift .

Dragging the scale handles with Alt scales the selection by an integer factor, i.e. up to 2 , 3 , 4 , etc. times the original size or down to 1/2 . 1/3 , 1/4 , etc. of the original size either horizontally or vertically (or both). (In some Linux distributions, you may need to adjust your meta-key settings to make this work.)

## Rotate

To rotate a selection, switch to shear/rotate mode and drag the arrow handles which are found at the corners or press [ or ] .

<!-- image -->

Constrain rotations to 15 degree increments by holding Ctrl while rotating.

To rotate the selection around the opposite bounding box corner location, hold Shift while rotating.

## Rotation Center

The Rotation Center of the selection specifies the point around which it rotates. The Rotation Center is marked with a crosshairs and may be placed anywhere on the canvas (not just within the bounding box of the object).

When several objects are selected, they use the Rotation Center of the first selected object . If the first object does not have center set (i.e. if it is in a default central position), then several objects will rotate around the geometric center of their common bounding box

To move the rotation center of an object, click and drag it to the desired spot.  It will snap to the bounding box of the object as well as other snap points as set in the Preferences.

Compare rotation around center which is in it default position

<!-- image -->

with rotation around center which is moved to upper right corner of a shape:

<!-- image -->

Shift+click on the rotation center resets it back to the center of the object's box.

## Skew or Shear

To shift the parallel bounding edges of the selection in opposite directions so that the selection is warped diagonally, drag on the shearing handles at the top, bottom or sides of the selection while in shear/rotate mode.

## Flip

<!-- image -->

<!-- image -->

Flip a selection either vertically or horizontally by

- clicking the Flip buttons on the Tool Controls Bar
- selecting Object-&gt;Flip Vertical or Object-&gt;Flip Horizontal
- pressing v or h

Flipping a selection while in scale mode makes it flip within its bounding box, so that the bounding box remains fixed:

<!-- image -->

However, in rotate/shear mode flipping happens over an axis through the rotation center:

Scale Stroke Width, Rectangle Corners and Fills

<!-- image -->

There are four preferences that control whether to transform stroke widths , rectangle corners , gradient fills , and pattern fills when a selection is transformed.

They are represented by four toggle buttons in the Tool Controls Bar .  Be sure to select the appropriate toggles before transforming any selection.

<!-- image -->

## TIPS

1.  Double-clicking an object with the Select Tool and the tool will activate the appropriate tool to edit the object (i.e., if you double-click an ellipse, the Ellipse T ool will be activated, etc.).
2.  T he T ransform Window (Object-&gt;Transform or Shift+Ctrl+M ) can be used for precise transformations.
3.  Press Esc to cancel selection or cancel an incomplete move or transformation.
4. Ctrl+Click or Shift+Ctrl+Click will select objects within groups from outside that group.
5. Drag Selected : in Select, Alt+Drag moves the currently selected object(s) no matter where you start the drag, unlike regular drag that first selects the object under cursor. This is convenient for dragging objects that are behind other objects in z-order. (On Linux, you may need to disable dragging the window with Alt in your window manager's settings if you want to use this "drag selected" method.)

<!-- image -->

6.

## NODE TOOL

The Node tool is used to select and manipulate nodes so as to be able to precisely modify the shape of paths or curves.  These paths can be stand alone objects or they can be attached to another object as a mask or clipping path .   In addition to allowing manipulating of node position, node handles extend from the node when it is selected which define the direction of the path segments originating from that node.

## HOW TO USE

To activate the Node Tool click on the Node Button in the Toolbox or press the F2 Key.  The Tool Controls Bar will change to display the following buttons.

<!-- image -->

## Selecting Nodes

To select an object with the node tool you can click on it. Once an object is selected you can then select and edit the individual nodes in the object.  clicking on a node selects it, clicking on a path segment between two nodes selects both nodes. If you want to add or remove nodes from the selection use Shift+Click to toggle nodes into and out of the selection.  You can do a rubberband selection around a group of nodes using Click+Drag with the mouse.  Nodes can also be added and removed from a selection using Shift+Drag .

If you need to select all the nodes in a path or sub-path first select any node in the path.  If you want to select all the nodes in a path containing 2 or more sub-paths then press Ctrl+Alt+A .  If you just want to select the sub-path press Ctrl+A to select all nodes in a subpath (if there are no sub-paths Ctrl+A will select the whole path).

## Moving Nodes and Node Handles

Once a node has been selected, it can be moved by Dragging the mouse.  Use Ctrl+Drag to restrict the movement to horizontal or vertical, and Ctrl+Alt+Drag to drag along the direction of the node's handles.  Nodes can also be moved using the Arrow keys .  Pressing an Arrow by itself will move the selected node(s) by the Nudge Distance (T he default nudge distance is 2 SVG pixel units).  Presshing Shift+Arrow moves the node(s) by 10x the Nudge Distance.  Pressing Alt+Arrow moves the node(s) 1 screen pixel and Alt+Shift+Arrow moves the node(s) 10 screen pixels.

Once a node has been selected, it displays it's handles .  T he node handles are used to define the shape of a curve between two nodes. Rotating the node handle changes the direction of the curve as it leaves the node and changing the length of the handle changes the distance the curve will travel before it bends/interacts with the properties of the handle of the next node along the curve.

A node handle can be moved by Dragging the mouse.  Using Ctrl+Drag locks the rotation of the handle to 15 degree steps from 0, as well as snapping to it's original angle and the angle of the opposite node handle. Shift+Drag rotates both handles at once and Alt+Drag locks the length of the handle as it is rotated.

## Add Node

Creates a new node between two selected nodes. You can also double-click on the path at the place you want the node to be created.

## Subtract Node

Removes selected nodes and joins adjacent nodes.  It is also possible to press Ctrl+Del or Ctrl+Backspace .

To preserve the shape of the path better, either select the node and press Del or Bksp, or else Ctrl + Alt+Click on the node.

## Join Nodes

Combines two end nodes into one node on a continuous path, moving both nodes to an average middle point; Shift+J can also be used (hovering the cursor over one node will preserve its position so that only the other node is moved).

## Join Nodes with a New Segment

Adds a path segment between two open nodes.

## Split Path Between Two non-Endpoint Nodes

Deletes the path segment between two selected nodes, leaving the nodes open (or unconnected).

## Break Path at Selected Nodes

Splits a single node into two nodes in the same position. The nodes can then be moved apart.

## Make Selected Nodes Corner (Convert to Cusp)

Changes one or more selected nodes into cusp nodes or angled/corner nodes. Paths on cusp nodes have an angle rather than an arch, and node handles can be moved independently of each other.

## Make Selected Nodes Smooth

Changes one or more selected nodes into smooth nodes. Also available by Shift + S .  Paths passing through smooth nodes have a continuous arch through the node point, but each handle of the node can have different lengths.  The position of one of the handles can be locked by hovering the mouse over the node when pressing Shift+S .

## Make Selected Nodes Symmetric

Changes one or more selected nodes into symmetric nodes. Also available by Shift+Y . Paths passing through symmetric nodes have a continuous arc throught the node point, and handles have the same length.   T he position of one of the handles can be locked by hovering the mouse over the node when pressing Shift+Y .

## Make Selected Nodes Auto-Smooth

Changes One or more selected notes into Auto-Smooth nodes.  Also available using Shift+A .  When an auto-smooth node is moved or the nodes ajacent to it are moved, the auto-smooth node will automatically adjust it's handles to keep the curve passing through it as smooth as possible.

Note: Pressing Ctrl+Click on a particular node will toggle it through the above 4 node types.

## Make Selected Segments Lines

Changes one or more selected segments (two adjacent nodes) into a straight path. Also available using Shift+L

## Make Selected Segments Curves

Changes one or more selected segments (two adjacent nodes) into a curved path. Also available using Shift+U .

## Convert Selected Object to Path

Converts an object that is not already a path, like a Live Shape or a text object, to path.  (T his command effectively creates "outline" text, removing dependency on installed fonts.)

## Convert Selected Object's Stroke to Paths

Creates an outline of a path, creating parallel combined paths separated by the width of the stroke.

## X and Y Co-ordinates

These two tools show the exact X and Y Co-ordinates for the selected node.  If more than one node is selected the co-ordinates shown are the midpoints between the selected nodes.  Using these tools you can also type in specific co-ordinates for the selected node(s) enabling you to precisely position nodes.  To the right of the co-ordinate buttons is the units button, clicking on this button will give you a selection of units to use for displaying node co-ordinates.

Note: If more than one node is selected when changing units, they will all be moved to the midpoint between the selected nodes.

## Edit the Clipping Path of the Object

Edits the Clipping Path of an object without having to release the relationship between the path and the object.

## Edit the Mask of the Object

Edits the Mask of an object without having to release the relationship between the masking path and the object.

## Show Next Path Effect Parameter for Editing

Cycles the display of LPE controls, often indicated by a red or green path or specific handle types.

## Show the Bezier Handles of Selected Nodes

Toggle whether the node's handles are displayed while editing.

## Show the Outline of the Path

This button highlights the outline of the selected path.  Can be useful in a complex image or if your path's outline is completely transparent (e.g. when the path has a relationship with another object such as a clipping/masking path or text put on a path).

## Invert Node selection

The ! key inverts node selection in the current subpath(s) (i.e. subpaths with at least one selected node); Alt ! inverts in the entire path. (T his is similar to how these keys work in Selector, with current subpath(s) instead of the current layer.)

## HOTKEYS

## Multiple select

Shift+Click to select several nodes in succession.

## Near selection

Clicking on a selected path selects the two nodes closest to the click point (on either side). Shift + Click adds or removes these two nodes to the node selection (when only one path is selected; otherwise Shift + Click works as in Selector).

## Adding and Deleting nodes

Double-click or Shift + Alt+Click anywhere on the selected path (even if it is under other objects) creates a new node at the click point, without changing the shape of the path.

Tab selects the next node

Shift+Tab selects the previous node

Ctrl + Alt + click deletes a node

## Manipulating Nodes

Pressing Ctrl+Click on a node handle and it will retract back to a length of 0.  To pull the handle back out of the node use Shift+Drag .

Pressing [ or ] keys will rotate the handles around the node by 1 angle step (the default angle is 15 degrees), pressing Alt+[ or ] will restrict the rotation to 1 pixel.  If the node is a corner or cusp holding the left or right Ctrl key while pressing [ or ] will restrict the rotation to the left or right node handle,  using the left or right Alt+[ or ] keys wil rotate the left or right handle by 1 pixel.

Pressing the &lt; or &gt; keys will increase or decrease the length of the node handles by 1scale step. (the default step is 2 SVG pixel units).  For any node type except symmetric holding the left or right Ctrl key when pressing &lt; or &gt; will restrict the scaling to the right or left node. Alt+&lt; or &gt; will change the scale by 1 screen pixel (as with the Ctrl key the handle being scaled depends on which Alt key is pressed).

Rotating objects or control handles of a node with Ctrl restricts rotation to 15 degree increments. Dragging nodes may be restricted to horizontal/vertical with Ctrl and to the directions of the node's handles (or there perpendiculars) with Ctrl+Alt . Dragging a node's control points with Alt locks the length of the handle, and with Shift , rotates the other handle by the same angle.  When several nodes are selected, pressing &lt; or &gt; scales, [ or ] rotates the selected nodes as if they were an 'object' , around the center of that object.  So, for example, in a single-path silhouette portrait, you can select the nodes of the nose and rotate/scale the nose as a whole without breaking the path into pieces. Pressing Alt with these keys gives pixel-sized movement depending on zoom, the same as in Selector. Also, you can press h or v to flip the selected nodes horizontally or vertically.

Ctrl + click toggles cusp/smooth/symmetric/auto-smooth.

## TIPS

1.  When an object is selected handles appear making it possible to handle the shape of the object in an intuitive and precise way.
2.  You can switch the not-yet-finalized (red) segment of the path being drawn from curve to line ( Shift L ) or back to curve  ( Shift U ).
3. Esc deselects, cancels selection, and cancels drag or transformation of any kind (so far only in selector and node edit). Arrows, Ctrl + a , and Tab / Shift + Tab act on nodes in node editor exactly as they do on objects in Selector.  The first Escape or empty-space click deselects any selected nodes, the second one deselects the selected object removing the node display.
4.  T he Node Tool selects objects regardless of grouping. This means you don't need to switch to selector for a Ctrl + click if you want to edit a grouped path.
5.  You can reverse the direction of selected path(s) either via Path &gt; Reverse or by pressing 'r' in node tool (useful for markers and combining paths).
6. Ctrl + click on a node handle retracts that handle back to its node.
7.  If a node does not show one or both handles (i.e. they are retracted), you can drag a handle out by dragging away from the node with Shift.
8.  Pressing Ctrl+A with some nodes selected will select not all nodes in the path but all nodes in the subpath(s) containing the selected node(s). To select all nodes in the path unconditionally, either deselect any nodes before pressing Ctrl+A, or use Select all in all subpaths ( Ctrl+Alt+A ) in Node tool.
9.  Edit the selected path by dragging directly on the path.
10.  if you press Shift before starting to drag, you always get a node selection rubberband rectangle
11.  When you switch the type of the selected node to Smooth or Symmetric by pressing Shift + S / Shift + Y , you can now preserve the position of one of the two handles by hovering your mouse over it, so that only the other handle is rotated/scaled to match.
12.  You can grow or shrink node selection by hovering the mouse pointer over a node and using mousewheel (up = grow, down = shrink) or the keys PageUp (grow) and PageDown (shrink). Growing adds the closest unselected node to the selection; shrinking deselects the farthest selected node. There are two modes that differ by how the closest/farthest nodes are chosen:
13. Spatial selection (mousewheel, PageUp / PageDown ): distances to nodes are measured directly, regardless of which subpath a node belongs to.
14. Linear selection (Ctrl+ mousewheel , Ctrl+PageUp/Ctrl+PageDown): node distances are measured along the path , and only the nodes belonging to the same subpath as the hovered node are considered (i.e. other subpaths are never selected).
13.  This technique is convenient for quickly selecting an area in a complex path starting from a center - for example, for node sculpting.
14.  If any of the nodes in the currently selected path is mouseovered, then horizontal/vertical flipping ('H' and 'V' keys), stepwise rotation ('[' and ']' keys) and scaling ('&lt;' and '&gt;' keys) now all use this specific node as center/axis. If there is no mouseovered node, the center of the bounding box is used instead (as is currently the case unconditionally). Nodes that are covered by one of their handles are also detected as mouseovered.
15.  Two entry fields are available on the Tool Controls bar which allow precise editing of the coordinates of selected nodes.
16.  The message, "To join, you must have two endnodes selected" warns that the command only works on endnodes.  To see if a line segment ends in an endnode, drag the middle of the line.  If a closed loop forms, with two paths between two nodes, then the nodes are not endnodes.  To convert a node into an endnode, select the line connected to the node by clicking once on the line, click a second time to select one of the overlapping line segments, and click on the split path tool to remove one of the line segments.

# 7. TWEAK TOOL

The Tweak Tool is an exciting way to edit drawings which largely blurs the distinction between vector and raster editing. Instead of meticulously selecting some objects and then performing an action on the selection, you can select all objects (or all objects you are interested in) and apply the Tweak Tool's brush to smoothly and naturally change the shape or style of only those objects (or parts thereof) that the brush touches .

<!-- image -->

ShIFT

Tweak

The editing modes of the Tweak tool fall into 3 different categories: Path Editing Modes where the shape of individual paths is modified; Colour Modes where the colour of individual objects is modified and Object Editing Modes where whole objects are moved, scaled or rotated but their shapes are kept intact.

The area of the tool's action - its brush - is marked by an orange-colored circular outline that moves with your mouse cursor. However, that area actually has no sharp boundaries; the power of the tool's action falls off gradually, following a smooth bell-shaped profile. This makes the tool act softly and smoothly.

The tool will work on any number of selected objects; for example, you can select all Ctrl + A and "smear" your entire drawing by Push mode or paint it by Color Paint mode. You can also apply it to groups of objects; it will go into groups and act on individual objects inside groups. If you're trying to use it without anything selected, it will remind you by a statusbar message to select some objects.

## HOW TO USE

## Width

The width of the tool's brush, in the range from 1 to 100, can be changed by the Width control in the tool's controls bar above the canvas . You can also change width by Left and Right arrow keys (same as in the Calligraphy Tool ) at any time (including during action) as well as Home and End . Also, as in Calligraphy T ool, the visible width of the brush is independent of zoom; simply zooming in or out is often easier than adjusting the width if you want to cover a smaller or larger area of the drawing.

## Force

## Push

This default mode of the tool, Push , Shift + P simply displaces the part of the path under the cursor in the direction of the drag. The path behaves like soft jelly, bending and bulging smoothly and naturally. It's an easy way to produce various irregular, lifelike, handmade-looking shapes starting from something as simple as an ellipse or a calligraphic stroke. For parallel-stroke hatching (engraving) done in the Calligraphy tool, pushing is an easy way to bend, pinch, or curve the entire hatching uniformly.

## Shrink and Grow

Shrink ( Shift + S ) and Grow ( Hold Shift when using the Tweak Tool) are two opposite modes that move each point of a path in a direction perpendicular to the path's surface at the point, either inwards (Shrink) or outwards (Grow). This is similar to the Inset and Outset commands, except that the Tweak Tool can act on a part of a path instead of the whole path.

For example, the visible lightness/darkness of an engraving hatching may not exactly correspond to your artistic intention. Also, the ends of Calligraphy pen strokes are often far from ideal - they may be too blunt or have unsightly bends or blobs. This is where the Tweak Tool may help. Select all the strokes in a hatching pattern and apply a light Shrink action where you want the lines to become thinner (and the hatching to become lighter), up until total disappearance. If you press hard, shrinking works as an eraser, so you can easily clean the strokes' ends to make them thin, sharp, and uniform. Conversely, applying Grow makes strokes wider (i.e. the hatching becomes darker).

The next control is Force which adjusts the power of the action, also in the range from 1 to 100. You can also change width by Up and Down arrow keys at any time (including during action).

If you have a pressure-sensitive tablet and your "Use pressure" button on the right-hand end of the controls bar is on, then the force will also depend on how hard you actually press your pen into your tablet, changing in the range from zero to whatever you set in the Force control. If all you have is a mouse, then the force will be constant but still settable by the Force control.

## Path editing modes

The Tweak tool has a number of modes , selectable by toggle buttons in the tool's Controls bar and by keyboard shortcuts. Some of these modes change the shapes of paths , others affect the whole object leaving the path shape intact, while still others affect the colors of objects. All these modes share the Width and Force controls but otherwise are quite different. Let's look at the path editing modes first.

Unlike the Node tool, to edit paths with the Tweak tool you don't need to worry about where the nodes of a path are and how to manipulate them. You just apply the tool's brush to any point, and the selected paths at that point will reshape smoothly and naturally - as if made of soft jelly - regardless of where its nodes lie. If applied to a shape or text object, the tool converts them to paths automatically.

While not very useful for technical drawings, tweaking paths will be indispensable for artistic uses of GuineaPigment - cartoons, drawings, sketches, anime, etc. This new functionality is somewhat similar to the tools such as "Pucker" and "Bloat" in the latest versions of Adobe Illustrator .

There are currently six path editing modes in the Tweak Tool: Push , Shrink/ Grow , Attract/ Repel , and Roughen .

Of course, shrinking and growing are useful not only for calligraphic strokes. Same as with Push, with Shrink and Grow you can sculpt any path, spawning smooth treacle-like appendages with Grow and carving holes with Shrink. Unlike the "node sculpting" mode in the Node tool, however, this does not require adding new nodes to the shape.

## Attract and Repel

Attract ( Shift + A )and Repel ( Hold Shift when applying tool) mode works by moving each affected point on a path towards (Attract) or from (Repel) the cursor point. In some cases this may look similar to Shrink and Grow, but the difference is that shrinking/growing moves paths perpendicularly to the path in each point, whereas attracting/repelling moves them to or from the cursor regardless of the path shape. These modes are similar to the Pinch effect in AI; you can use them for various central-symmetric distortions in parts of your paths.

## Roughen

The Roughen ( Shift + R ) mode does exactly this: roughens the edge of the path without changing its overall shape. Slight roughening simply makes the edge crooked and uneven; strong roughening tears and explodes the edge into random blobs and splotches.

NOTE: This operation, especially when applied with high Fidelity, adds a lot of nodes, increasing the size of your SVG document and may slow down GuineaPigment considerably. In particular, pushing, shrinking, or growing of a roughened path becomes much slower and more difficult. It's recommended to finalise the overall shape of a path first and roughen it, if necessary, only as the final step.

## Fidelity

Any tweaking of a path slightly distorts the entire path, including even those parts that you didn't touch. These distortions are similar to those that a Simplify command produces. The Fidelity value (also in the range from 1 to 100, default is 50) allows you to control the amount of these distortions. With a higher fidelity, the distortions are less noticeable, but the path may end up having a lot of nodes which inflates up the SVG size and slows down GuineaPigment.

The best value of Fidelity depends on the nature of your artwork. If you're sculpting an amorphous blob, you can do with low fidelity of about 20. If, however, you are pushing or inflating a text string (as a single path) and want the letters outside the distorted area to remain crisp and clean, you will need to raise fidelity to 80 or more.

## Object editing modes

The Object editing modes , unlike the path editing modes, change the position, size, rotation, etc of objects instead of their shapes. Yet they share enough common features with the path editing modes to be part of the same tool: These modes also use a circular soft-edged brush controlled by the Width and Force parameters on the Controls bar and affected by the pen pressure (if you have a pressure-sensitive tablet).

## Push Mode

Attract/Repel Objects Mode

Jitter Mode

## Scale Mode

## Rotate Mode

## Duplicate/Delete Mode

## Blur Mode

## Color editing modes

The Color Paint ( Shift + C ) and Color Jitter ( Shift + J ) modes, unlike the path editing modes, change the colors of objects instead of their shapes. Yet they share enough common features with the path editing modes to be part of the same tool: These modes also use a circular soft-edged brush controlled by the Width and Force parameters on the Controls bar and affected by the pen pressure (if you have a pressure-sensitive tablet).

- Color Paint applies the style of the tool to the selected objects under the brush. The style of the tool is visible in the style swatch at the rightmost end of the tool's control bar; it can be changed by clicking on the color palette or by any other style assignment command, such as Fill and Stroke dialog. ( Note : unlike all other tools, in T weak tool in Color Paint mode you cannot assign style directly to selected objects; any style-setting command changes the tool's style instead.)

The fill from the tool's style applies to the fills of the painted objects, and the stroke applies to the strokes. If the tool's style has no fill or no stroke, it won't affect fills or strokes, correspondingly. For example, if you want to color the fills of objects blue but leave their strokes untouched, assign blue fill to the tool's style (just click blue on the palette) but set its stroke to None (middle-click the Stroke swatch in the statusbar). Similarly, master opacity in the tool's style affects master opacities of the touched objects (if the O channel is on, see below).

This mode allows you to literally paint over objects, shifting their colors towards the target style of the tool. For example, if you paint with yellow fill over a blue-filled object, the object will become greenish blue, then green, then yellowish green, and end up being exactly the yellow color you're painting with. T his speed of this gradual transition depends on both Force parameter and pen pressure; also, objects touched by the periphery of the brush are less affected than those hit by the brush centre. Overall, using this tool is very similar to a soft brush in a raster editor such as Gimp or Photoshop.

- Color Jitter mode does not apply any color, but instead jitters (randomises) the colors of the objects it touches. The force of the action determines how strong is the randomisation, i.e. how far the colors deviate from the original values. This mode does not use the tool's style.

Both modes work on flat fills and gradients; for gradients, the tool takes into account not only the position of the entire object with gradient, but also the position of each gradient stop relative to the brush. This means that, for example, you can change the blue color only in an object filled with blue-red gradient simply by painting over its blue end with a brush small enough to not touch the red. (Note that color tweaking does not create gradients on objects that used flat color before, but only adjusts existing gradients in the drawing.)

## Channels

Color Paint and Color Jitter honor the Channels control. T his control comprises the four buttons: H , S , L , and O , which allow you to turn on and off the tool's action on the object's hue, saturation, lightness, and opacity, correspondingly. For example, if you want to raise the saturation of some part of your drawing without changing the hue, select some maximum-saturation color (e.g. pure red) and turn off all Channels buttons except S . Similarly, you can replace the hues without affecting saturation or lightness (only H pressed), or lighten/darken all colors without changing their hues and saturation (only L pressed). Pressing O allows you to apply the master opacity from the tool's style to the master opacity of objects (but not fill or stroke opacity).

## Usage notes

Color painting with Tweak tool is similar, but not exactly analogous to bitmap painting. Even though the tool itself works as a soft brush, it still applies its color to vector objects, which behave as vector objects usually do. For example, if you want to change the tint of the face in your drawing, and if a hand in the drawing is part of the same object as the face, that hand will change its tint too even if it's located far from the point you are painting. (We foresee a "fracture" command in one of the next versions of GuineaPigment which will help you turn a monolithic object into a mosaic of small fragments that will be then easy to paint with Tweak tool.) Still, even with this limitation, color painting is a novel way of dealing with vector drawings which allows you to quickly and intuitively make adjustments which would be awkward and slow with traditional approach.

Drawings containing patterns or scatterings of small independent objects are best suited for color painting with Tweak tool. Examples include:

- freehand drawings with Calligraphy pen, consisting of many separate strokes;
- gradient meshes imported from Adobe Illustrator files (GuineaPigment renders these meshes as lattices of small polygons; while there's no direct support for gradient meshes in GuineaPigment yet, color painting on such lattices is almost as good);
- text converted to paths and with Break Apart command applied so that each letter is a separate path;
- patterns made with the Tile Clones command; note that you need to unset the fill and/or stroke on the original object and use the Color tab to assign some initial color to the clones - this will make them paintable with the Tweak tool without unlinking.

Moreover, color tweaking can be useful for compositions with a few objects or even for single objects. Unlike all other color selection methods, painting with the Tweak tool implements the color mixing metaphor which is much more familiar to traditional artists than RGB sliders or even the color wheel. For example, start with a rectangle of pure blue color; then, pick different colors by Color Paint and apply light touches with minimum Force and minimum pen pressure: add a little green, a little brown, a little yellow, etc. until you have the exact hue you need. Similarly, you can whiten or blacken any hue by admixing white or black.

You can also use color tweaking to add a tint, darken/lighten, saturate/desaturate, or color jitter your entire drawing. Just select all in all layers, zoom out, choose a large brush width so it covers all of the drawing, and apply a little color tweaking (with minimum Force) that will therefore affect all visible objects.

## HOTKEYS

- W , Shift + F2 : switch to the Tweak Tool
- Shift +P : switch to the Push mode
- Shift+S : switch to the Shrink mode
- Shift+G : switch to the Grow mode
- Shift+A : switch to the Attract mode
- Shift+E : switch to the Repel mode
- Shift+R : switch to the Roughen mode
- Shift+C : switch to the Color Paint mode
- Shift+J : switch to the Color Jitter mode
- Left, Right, Home, End : change width
- Up, Down : change force
- mouse drag : act on selected path in the current mode
- Ctrl+mouse drag : temporarily switch to Shrink (while Ctrl is down)
- Shift+Ctrl+mouse drag : temporarily switch to Grow (while Shift + Ctrl is down)

# 8. ZOOM TOOL

The Zoom Tool magnifies or "zooms in" on part of the canvas and, conversely, "zooms out".

Because of its utility, zooming can be accomplished from the Tool Commands Bar , the keyboard or the mouse (or a combination thereof), and often does not require the Zoom Tool to be activated.

## HOW TO USE

The Zoom Tool can be activated in the following ways:

- by clicking on the Zoom Tool in the Tool Box:
- by pressing F3

<!-- image -->

## Zooming

<!-- image -->

Zooming in sets the zoom factor to a higher lever so that one can see more detail and work more precisely.

You can zoom in by:

- Left Clicking on the canvas with the Zoom Tool active
- Left Click + Drag to select the area of the image you want to zoom into
- Press + ( Shift + = )
- Hold Ctrl + Roll Mouse Wheel up
- Press Middle Mouse Button

## Unzoom

<!-- image -->

Unzooming (or Zooming out) can be used to have a larger view of the drawing or area.

You can unzoom by:

- Right Clicking on the canvas with the Zoom Tool active
- Press - (minus)
- Hold Ctrl + Roll Mouse Wheel down
- Press Shift + Middle Click

## Zoom to 1:1

<!-- image -->

Displays the drawing at real pixel size. This way a banner drawing (for example) which is 468 pixels wide, will be 468 pixels on screen.  This zoom level can also be activated by pressing 1 .

NOTE: If the GuineaPigment window is smaller than the image, some part of the drawing may be invisible, drag with the Middle Mouse Button to pan around the image.

## Zoom to 1:2

<!-- image -->

Displays the drawing at half the real pixel size. T his way a Banner drawing  which is 468 pixels wide, will be 234 pixels on screen.  The keyboard shortcut for this zoom level is 2 .

## Zoom to 2:1

<!-- image -->

Just displays the drawing at twice the real pixel size. T his way a Banner drawing which is 468 pixels wide, will be 936 pixels on screen.

## Zoom to fit selection in window

<!-- image -->

The selected area will fill the entire GuineaPigment window.  This can also be achieved by pressing 3 .

## Zoom to fit drawing in window

<!-- image -->

The zoom level will be adjusted to fit all existing drawing elements in the window. Click on the icon or press 4 .

## Zoom to fit page in window

<!-- image -->

Best to have a complete overview of the page and work on a layout, makes the whole page fit the window size depending on the orientation. Pressing 5 does the same action.

## Zoom to fit page width in window

<!-- image -->

This is similar to zooming to fit page in window, however if the orientation is portrait GuineaPigment will go in closer to fill the window with the page width. Gives a better result than previous with landscape drawing. Press 6 to activate it with keyboard.

## Previous zoom

<!-- image -->

Move back to the previous zoom factor, as saved in the zoom history. GuineaPigment now preserves the history of zoom settings for each document. The ` key restores previous zoom; pressing ` repeatedly will guide you through all the zoom settings you've used in this session.

## Next zoom

<!-- image -->

Goes back to the next zoom factor, as saved in the zoom history, especially when previous zoom has just be used. Shift + ` also moves forward in the zoom history.

## HOTKEYS

Shift is diminishing zoom factor.

Middle click zooms in, Shift + middle click zooms out (in addition to middle button + drag which pans canvas).

## TIPS

1.  Zooming with the Mouse Wheel performs a precision zoom directly under the cursor. The other incremental zoom methods zoom at the middle of the canvas.
2.  By default, rotating the mouse wheel scrolls the canvas vertically and Ctrl+wheel zooms in and out. Selecting the Mouse wheel zooms by default checkbox in the Scrolling tab of the GuineaPigment Preferences Dialog , this behavior is reversed: the mouse wheel zooms without Ctrl and scrolls with Ctrl. T his new mode should be familiar for users of AutoCAD and CorelDraw.
3.  You can use Shift+middle button drag , in any tool, to zoom into a specific area. This works the same as simple drag in Zoom tool, but is faster because it does not require switching away from your current tool. Together with middle button drag (panning), middle button click (zoom in) and Shift+middle button click (zoom out), this completes the set of canvas navigation shortcuts available in any tool or context.
4.  In the Zoom Tool, the Right Mouse Button usually zooms out instead of calling the context menu if it is clicked on empty canvas.

<!-- image -->

# 9. RECTANGLE TOOL

The Rectangle Tool draws boxes (squares and rectangles) which are live shapes .  Rectangle live shapes can be given rounded corners as well.

## HOW TO USE

A new rectangle is drawn by pressing the left mouse button and dragging the mouse.

Rectangles have two square resize handles in opposite corners (top left and bottom right when the rectangle is at its original orientation). Dragging the resize handles resizes the rectangle's width and height simultaneously.

Rectangles also have round corner radius handles at the top right to set the radius of the corners.  There are two radius dimensions which can be set either together or independently; these separate dimensions affect the horizontal or vertical "sides" of each corner.  "Rx" affects the top and bottom side radii, while "Ry" affects the left and right side radii.  (The best way to understand this is to play with the controls and settings and watch their effects.)

A box with rounded corners can be set back to sharp corners with the last button on the Tool Commands Bar, "Make corners sharp".

<!-- image -->

Corner shape handles

<!-- image -->

## HOTKEYS

Ctrl+Drag on handles constrains the width and height of the rectangle while resizing so that they retain their current ratios when resizing, or will constrain the rectangle to be resized only in the direction of cursor travel if the cursor strays considerably from the degree of the diagonal through the two opposing corners; when drawing a new rectangle, this method can create a perfect square.

Shift + Drag on handles resizes the rectangle from its center and not from the opposite corner of the grabbed handle; when drawing a new rectangle, the rectangle will be drawn with its center at the starting point rather than one of its corners.

SHIFT+Click on a rounding handle removes rounding.

CTRL+Click on a rounding handle makes rounding radii equal.

<!-- image -->

# 10. 3D BOX TOOL

GuineaPigment is a two-dimensional drawing tool. However, very often it is used to create drawings or objects that appear three-dimensional. The 3D box tool helps you create such drawings by automating the most common operation: creating a box in a given 3D perspective. The tool automatically ensures that all sides of the box lie on the corresponding perspective lines.

<!-- image -->

## BASIC USAGE

In order to represent an object in 3D (it's emulated 3D, so it's rather 2.5D ), the 3D box tool deals with axes (XYZ), planes (XY, XZ, YZ), parallel lines (PL), converging lines and vanishing points (VP).

Each dimension can lie on either parallel or converging lines. These lines are drawn in different colors, so that users could distinguish one line from another:

- red lines stand for X direction (width);
- blue lines stand for Y direction (height);
- yellow lines stand for Z direction (depth).

If lines are converging, they have a vanishing point - a point where they cross. Here is a sample to illustrate how it works:

<!-- image -->

X is the vanishing point for X plane

Z is the vanishing point for Z plane

Y are parallel lines for Y plane

points:

<!-- image -->

X and Z planes nearly converged, but Y is more or less the same.

By default GuineaPigment makes X and Z lines converging, because it represents usual perspective.

Note : Parallel lines do not necessarily have to be 90 degrees to X axis - changing the angle will somewhat skew the object.

## Drawing a 3D box

Press X or Shift+F4 to switch to the 3D Box Tool. Start dragging cursor on canvas. You can use Shift +drag without releasing the mouse button to extrude in Z direction.

<!-- image -->

If you need to draw another 3D box with same vanishing point, just keep the previous box selected and start drawing a new one:

## Editing a 3D box

Adjust any of its 3 dimensions by handles. The 4 handles on the front X/Y side resize it, the four ones on the back X/Y side expand/contract the box in Z direction. With Shift , the functions of handles on front and back sides are reversed. With Ctrl , the side-resizing handles snap to the coordinate axes or diagonals.

## Moving a 3D box

You can move a 3D box in perspective by dragging its center marked as an "X" character; without modifiers, movement occurs within the XY-plane (press Ctrl to constrain the movement to the directions of the coordinate axes or diagonals), with Shift the box moves parallel to the Z-axis.

<!-- image -->

## Handling vanishing points

Adjust the vanishing points of a perspective by dragging them on the canvas (see below) or toggling their states; all boxes sharing this perspective are affected by a vanishing point move.

When several boxes are selected, all vanishing points of their associated perspectives are shown on the canvas. If vanishing points of different perspectives coincide, they are combined in a single "dragger". Moving this dragger moves all the vanishing points simultaneously and transforms the associated boxes accordingly. Note that some non-selected boxes may also be reshaped if their perspectives share the same vanishing point. Pressing Shift while moving the dragger can be used to only transform the selected boxes, separating their perspectives from the non-selected ones'. On the other hand, when a vanishing point being dragged comes close enough to another one, both snap together and are combined in a single dragger.

<!-- image -->

## Rotating perspective lines

The various kinds of parentheses, namely [ ] , ( ) , { } , can be used to rotate infinite (i.e., parallel) perspective lines in X-, Y-, and Z-direction, respectively. Closing parentheses rotate clockwise and opening parentheses rotate counterclockwise. The angle of rotation is taken from the preferences. Pressing Alt reduces the amount of rotation to 1 screen pixel.

## Changing mode of perspective lines

When the 3D box tool is active, Shift+X , Shift+Y , and Shift+Z toggle perspective lines in the corresponding direction between "converging" and "parallel".

## TIPS

Inside 3D Box tool

In SVG, a 3D box is represented as a group (svg:g) with a special extension attribute (in GuineaPigment's namespace); this group contains the 6 quadrilateral paths representing the sides of the box. Only the 3D box tool treats this object as a box; for all other tools it is just a group, so you can select any of the paths by Ctrl+click, apply any style to it, delete it, etc. You can of course transform the entire box or any face in it using Selector or Node tools.

# 11. ELLIPSE

With the Ellipse tool , the GuineaPigment artist can draw an ellipse, circle, or arc. As a Live Shape , an ellipse can be converted to any elliptical shape (circle or oval); it can also be converted from an ellipse to a pie segment or arc.

## HOW TO USE

When an ellipse is drawn there are three edit handles: top (square), left (square) and right (circle).

The top and left handles control the horizontal and vertical dimensions, respectively.

Dragging the right handle of a whole ellipse will create an arc or segment; this handle then sets the degree of the arc or segment (measured from the rightmost point of the ellipse at its original orientation).

To easily switch between an arc or pie segment, drag the handle inside or outside of the ellipse.  For example, when dragging inside the bounds of the ellipse, the ellipse will be an arc; when dragging outside of them the arc will be closed and create a pie shape.

These attributes can also be set by the the Tool Controls Bar .  T he start and end degrees may be adjusted precisely with respective the spin boxes; the shape type (segment, arc or whole) can be selected from the corresponding buttons.

<!-- image -->

## TIPS

1.  Hold Ctrl while dragging the arc control to enable snapping at angles as specified in the GuineaPigment Preferences window.
2.  Hold Shift while drawing to draw the shape with its centre at the cursor's point of origin in order to keep position static during the drawing.

<!-- image -->

# 12. STAR TOOL

Stars and polygons are special shapes, difficult to draw by hand while maintaining a regular shape. The Star Tool enables stars and regular polygons to be drawn easily in the document. This tool is very convenient even though it may be less often used than the Rectangle Tool and Ellipse Tool .

GuineaPigment stars are Live Shapes , and can thus be infinitely modified after creation, with handles or tool control parameters .  By modifying some of the following parameters, this tool can be used to draw triangles and other regular polygons with any number of sides. The included deformation methods allow for some amazing shapes, all while keeping the powerful aspects of easy editability of an SVG Primitive .

## HOW TO USE

To switch to the Star Tool, you can either

click the T oolbox icon

- or press * ( Shift+8 )

## Options

The tool options can be accessed in the Tool Controls bar

<!-- image -->

## Drawing a Regular Polygon or Star

The left icons allow respectively to use the Regular Polygon Mode or the

<!-- image -->

<!-- image -->

Star Mode

The next polygon/star will be created in the Selected Mode .  An object's mode and shape will be changed if it is selected while one of these icon is clicked.

<!-- image -->

In Regular Polygon Mode, the shape has no spokes. Only one handle is available, allowing modification of the size and orientation of the polygon.

<!-- image -->

<!-- image -->

In Star Mode, spokes start from regular polygon corners. There are two handles - the red handle is the same as for polygons, allowing modification of size and orientation of the object; the white handle at an interior spoke angle allows simultaneous modification of all the spokes' shapes and sizes.

<!-- image -->

## Corners

You can define the number of corners and spokes of the shape by adjusting the corners parameter - it can either be specified before drawing a polygon or dynamically modified after selecting an existing polygon. Corner counts are limited from 3 to 1024.

## Spoke Ratio

Only accessible in Star Mode, it allows you to define the ratio of spoke length between the star core and its spoke tips. This parameter range is from 0.0 to 1.0.

## Rounded

This setting allows you to round the corners of the shape in both Polygon Mode and Star Modes of this tool. The range value is from -10.0 to 10.0.  Press Shift and drag either handle to modify the rounding of the shape on-canvas.

Note that dragging each handle gives different results because the degree of rounding is proportional to the angle of displacement from the center of the shape - thus a drag of the middle handle will create a greater degree of rounding than a same-length drag of the outer handle.

The following image shows some rounding examples, with regular polygons on the first line and stars at the second. There are infinitely more possibilities than shown here.

There is a Spirograph Tool ( Effects &gt; Render &gt; Spirograph ) which can produce similar effects and much more.

<!-- image -->

## Randomised

The Randomised option of Star Tool displaces the inner and outer points of the spokes to random coordinates around the center of the star. The range value runs from -10.0 to 10.0. Near 0.0, the randomness of the displacement ratio low, and it increases as the parameter approaches -10.0 or 10.0.

You can also change the power of the randomised effect on-screen by pressing Alt and dragging the handle.

## Default

<!-- image -->

Reset shape parameters to defaults.

## Additional information

Polygons are always drawn with their geometric centers at the cursor origin - this cannot be changed

Ctrl - Constrain the star shape to follow some angles. The cursor move allow to modify angle by regular increment. The increment value can be defined in the general preferences window: File &gt; GuineaPigment Preferences... &gt; Steps tab .

<!-- image -->

# 13. SPIRAL

The Spiral Tool is one of the special class of tools that create Live Shapes .  With the Spiral tool, shapes of spiral arcs can be drawn.

<!-- image -->

## HOW TO USE

Call the Spiral T ool with its icon on the T oolbox or by pressing F9 or I .

<!-- image -->

The spiral drawn with the tool has two handles, one on either end of the shape's path. Clicking and dragging the inner-most handle with the spiral tool will change the interior radius of the arc, and the handle on the outter-most end of the path edits the number of turns of the spiral.

There are four options in the T ool Controls bar which can be used to further manipulate the spiral:

<!-- image -->

- Turns adjusts the number of rotations the spiral takes around its center.  Increasing the turns will decrease the width between successive spiral paths, since this option does not increase the dimensions of the spiral.
- Divergence tightens the spiral either toward its center (as if it were being wound tighter) or toward the exterior.  When the divergence is increased above 1, it makes the outer part of the spiral looser, or widens the gap between its outermost paths.  The reverse is true for values below 1.

<!-- image -->

<!-- image -->

- Inner Radius does the same as dragging the inner handle.  The inner radius parameter is a relation or fraction representing the distance from the exact center of the spiral to the beginning of the inner spiral path relative to the whole spiral radius.  When the inner handle has been moved from its position at the center of the spiral, the radius becomes more than 0.  When this is true, growing the spiral path by dragging the outer handle will decrease the inner radius, showing its relative nature.
- The Broom icon will clear all parameters to the defaults set at the spiral's creation.

<!-- image -->

## KEY COMMANDS

- Ctrl drag constrains the rotation angle to 15 degree increments

## Outer handle:

- Shift drag scales the spiral and ;rotates it
- Alt drag keeps the radius static while increasing or decreasing the turns around the center

## Inner handle:

- Alt drag vertically adjusts divergence
- Alt click resets divergence
- Shift click moves the inner handle to the center

<!-- image -->

# 14. PENCIL TOOL

With the Pencil Tool ( P or F6 ), the GuineaPigment artist creates freehand paths by drawing directly on the canvas in the desired curves. GuineaPigment evaluates the line or shape drawn by the user and produces nodes to form the path. After the path is drawn, the nodes of the path can be edited with the Node Tool , like other paths.

## HOW TO USE

Choose the Pencil Tool, then click and drag the mouse to draw the line. By default it has no fill , but this can be set by any means (swatch or Fill and Stroke dialog). The line can also be set with stroke properties and colors in the Fill and Stroke dialog.

It is possible to close the line drawn while returning towards the initial point. When the mouse is close to this point, the point changes color to red to specify that a release of the mouse at this moment closes the shape.

## TIPS

These tools can create single dots by Ctrl + click on the canvas. This creates a small circle filled with the current stroke color. T he radius can be set in the Preferences of the respective tools (it is specified as a multiple of the current stroke width). Shift + Ctrl + click creates a dot twice the specified size, and Alt + Ctrl + click varies the size of the created dots randomly.

<!-- image -->

# 15. PEN TOOL

The Pen Tool is used to draw paths made of bezier curves ; beziers can form unclosed paths or closed shapes.  The pen tool is useful for drawing figures with smooth curves, and can be particularly efficient for tracing images (e.g. for rotoscoping ).

## HOW TO USE THE PEN TOOL

Start the Pen Tool one of three ways:

- Click on the Pen Tool button in the Toolbox;
- Press b ;
- Press Shift + F6 .

Left-click on the canvas to create the first node .

<!-- image -->

## Draw a Straight Segment

To draw a straight segment, click again where you want the segment to end; a straight segment will be drawn between these two points.

<!-- image -->

## Draw a Curved Segment

To draw a curved segment, click to add a new node and hold down the mouse button, then drag to adjust the curve of the segment (this also makes curve control handles appear).

<!-- image -->

## End a Path

To end a path, either click the first node of the path (if you want it to be a closed shape), or press Enter or double-click (if you want the path to remain open); right-clicking will add a new node and end pat editing at the same time .

<!-- image -->

## Continue a Path

To continue a path that has been previously drawn, select the path and start the Pen Tool; then click either the beginning or end node and add segments as normal.

## Delete a Segment

To remove the most recently added segment/node, press Delete .

## TIPS

- A Pen Tool-made path can be continued with the Pencil Tool .
- Any path can be edited with the Pen Tool to add more segments.

# 16. CALLIGRAPHY TOOL

<!-- image -->

The Calligraphy Tool uses dynamic drawing techniques that apply simple filters to the cursor place and motion. The SVG "stylus" transforms as if it were a physical stylus or brush, depending on its mass, speed, orientation and friction.  (Some of these parameters are affected only by use of an input device such as a drawing tablet.)  By changing these parameters, various types of "strokes" can be made. This makes the Calligraphy tool excellent for drawing more natural, smooth and consistent strokes, particularly when using a pen tablet or similar input device.

The Calligraphy Tool does not draw a single path line like the freehand tool, but a whole filled shape. This is not a live shape, like rectangles and stars, but an arbitrary shape consisting of node paths. Being comprised of multiple nodes, calligraphy strokes can be modified by other path tools, for example the Node and Tweak tools. Also, like all arbitrary SVG shapes, calligraphy paths have strokes at their edges, so they are affected by the usual Fill and Stroke settings.

## HOW TO USE

The Calligraphy Tool can be called by clicking its icon in the Toolbox or by pressing C or Ctrl+F6 .

Calligraphy shapes are drawn in the same manner as any other shape - just click on the canvas and drag.

## Options

The Calligraphy Tool has many options available in the Tool Controls bar which allow the artist to create very specific types of strokes.

## Width

Used to set the basic width of the line. This basic width is then automatically modified depending on the other values (such as pressure of the tablet pen) and settings (such as the toggle setting of Input Device Pressure ).

Warning: Calligraphy stroke width is relative to the current view and zoom factor.

## Input Device Pressure

<!-- image -->

When on, Calligraphy uses pen tablet pressure to affect such values as stroke width.

Trace Lightness to Width

<!-- image -->

Angle

Trace Lightness to Width adjusts the width of the stroke to the lightness of objects behind it.  In the background objects, white translates into the minimum stoke width (1) and black translates to the maximum (which is set by the Width parameter).  This works with both bitmap and vector images and allows the artist to not only hatch over an imported bitmap image or any drawing, but to do so automatically reproducing the highlights and shades of the background with your strokes becoming lighter and heavier as needed.  This can work alone or in combination with pressure sensitivity, depending on whether the "Use pressure" button is also toggled.

<!-- image -->

Thinning

Thinning is a way to modify the width of the calligraphy stroke dynamically according to the speed at which the stroke is made.  This value enables the calligraphy tool to emulate true ink flow from a pen or brush.  For instance, dragging a stroke at a uniform speed will create a mostly uniform stroke width, while increasing speed will decrease width, and decreasing speed will increase width (to a degree).  T he higher the thinning value is, the more the stroke will be thinned.

Some examples are shown below. Notice that a negative thinning results in a thicking. When set to 0.0, the line keeps its width with uniformity.

<!-- image -->

The Angle setting is used to emulate a stylus type of writing instrument.  Angle will affect the direction at which the stroke creates its thinnest part, just like a calligraphy pen.  Values can be set from -90° to 90°. When set to 0, the hair line is horizontal; to 90, vertical.

Caps

<!-- image -->

Tilt to ang le

When activated, Angle is modified relatively to tilt of the tablet pen.

Fixation

Fixation changes the way the Angle width follows the calligraphic path. When set to 0.0, Angle is set always perpendicularly to the path so that the width looks nearly the same all along the path (as if the stylus were rotated constantly in the direction of the stroke). When set to 1.0, Angle is set to adjust to stroke direction most strictly (as if the stylus were kept exactly in the same direction at all times as a machine might be able to do).  A setting of a little less than 1.0 (such as 0.9) will most closely follow natural hand movement, like using a real stylus.

<!-- image -->

Caps determines how the line ends.  At 0, the end caps will be drawn flat. Increasing the value will create elliptical end caps, and the higher the value the longer the ellipses will be. T he max value is 5.00.

<!-- image -->

Tremor

Tremor affects jitteriness of the stroke.  It can be set from 0.0 to 1.0.  When set to 0, the line is the most regular.

Wiggle

Wiggle is a kind of randomization on drawn curves, making a sort of "bumpy" stroke. It generates these curves or "bumps" regularly, and can help to draw some nice typographic shapes, though the result is hardly predictable.

<!-- image -->

## Mass

Mass affects how quickly the stroke follows the cursor.  A heavier mass makes the stroke slower and increases smoothness or regularity of the stroke.  Values can be set from 0.0 to 1.0. When set to 0.0 the path just follows the mouse as normal. When set to 1.0, the drawing of the stroke is very slow.

<!-- image -->

Default

Default resets all Calligraphy T ool Controls settings to defaults as defined in Preferences.

## Drawing

## Adding a New Stroke to a Calligraphy Object

Press Shift to add a new calligraphic line to those that are selected, keeping all strokes together as a single object.

## Engraving

Tracking a Shape

One of the most common operations in line engraving is hatching (or sometimes cross-hatching when several hatching grids cross): filling a space with many parallel straight or variously curved lines (usually of varying width to represent a gradual shading). You could try to achieve a similar effect with e.g. path interpolation (blending), but it is rather cumbersome and limited; manual drawing of hatch lines, on the other hand, is tedious and nearly impossible to do uniformly. Now GuineaPigment provides "assisted hatching" by tracking a guide path , allowing you to hatch quickly and uniformly and at the same time giving you sufficient manual control over the process.

First, select the guide path that you will track. It may be another calligraphic stroke, any path or shape, or even a letter of a text object. Then switch to Calligraphic pen, select the desired parameters (line width, angle, fixation etc.) and, before starting to draw, press Ctrl. You will see a gray track circle centered at your mouse pointer and touching the closest point on the selected guide path. (If you have no guide path selected, a statusbar message will tell you to select it.)

<!-- image -->

The Now move your mouse close to the guide path, so that the track circle radius is equal to the desired spacing of your hatch pattern, and start drawing along the guide path. At that moment, the radius of the circle gets locked; now the circle slides along the guide path - and the actual stroke is drawn by the center of the tracking circle, not by your mouse point. As a result, you are getting a smooth stroke going parallel to the guide path and always at the same distance from it.

<!-- image -->

When the stroke is ready, release your mouse button (or lift your tablet pen) but do not let go of Ctrl because, as long as you have it pressed, the tool remembers the hatch spacing you set when you started drawing. Now, you have just created a new stroke and, as usual with GuineaPigment tools, it gets selected instead of what was selected before. In our case, this means that the newly drawn stroke itself becomes the new guide path. Next, you can draw a second stroke along the first one, then a third one along the second, etc. Eventually you can fill any desired space with uniform hatching.

<!-- image -->

Alternatively, if you uncheck "Select new path" in the Calligraphy tool preferences, newly created strokes will not be selected, so your original guide path will be kept selected. In this mode, GuineaPigment will increase the tracking distance after each created stroke so that you can create uniformly spaced hatching by tracking a single guide path.

The attachment to the guide path is not absolute. If you stray your mouse pointer far enough from the guide path, you will be able to tear it off (the track circle turns from green to red) and move freely. This is intentional; this feature allows you, for example, to continue drawing a stroke past the end of a guide stroke, thus making your hatching cover a wider area than the initial guide path. Special care is taken to make such tearing off as smooth as possible and to suppress violent jerks, but this is not always possible; the general advice is to not try to hatch too fast. If jerking and unintended tearoffs still bother you, try increasing the Mass parameter.

Also, special code is in place to prevent flipovers - accidental jumps to the other side of the guide path. Brief flipovers are suppressed, but if you intentionally go over to the other side and stay there, eventually GuineaPigment will obey and your tracking stroke will also flip over to follow you.

Tracking a guide also allows some slight feedback by gradually changing the tracking distance in response to your drawing behavior. Thus, if you're consistently trying to draw closer or farther from the guide than the current tracking distance, the distance will correspondingly decrease or increase, so you will get a hatching that is slightly spacing in or out. (T he effect is very slight, however, so as not to become a nuisance.) Also, note that since tracking follows the edge of the stroke, strokes of varying width (such as those tracing background, see below) will result in gradual bending of the hatching pattern as you proceed

## Engraving

Combined with the Ctrl key, the Calligraphy Tool is able to simulate the ancient art of line engraving. T raditional engraving is a very labour-intensive process, and while for a long time it was the only practical way of reproducing lifelike images in blackand-white print, about a century ago it was almost completely displaced by automatic halftone screens in industrial process. However, line engravings have their characteristic charm, and are often still used for certain art applications.

# 17. BUCKET FILL TOOL

The Bucket Fill Tool is simple - it fills in unfilled areas with color.  Being a vector tool , however, GuineaPigment's Paint Bucket actually creates a new path that "fills in" the area in which you clicked.

It is important to note that the tool's operation perceptual , not geometric. That is, when looking for the boundaries around the point you clicked, it takes for such boundaries any visible color changes. This means that filling will stop at gradients , blurs, and even the color boundaries in imported bitmaps , but will ignore any paths or other objects that are fully (or almost fully) transparent or for any other reason do not stand out from the background. In short, it will work exactly as if you were filling a rasterized version of your image in a bitmap editor like Photoshop or GIMP - but will give you a vector object to work with.

Internally, the tool works by performing a bitmap-based flood fill on a rendered version of the visible canvas , then tracing the resulting fill using potrace and placing the traced path into the document.

It places the rendered path onto the current layer, so you can have a layer on top (for example, "Inks") and select the layer below ("Colors") and do the fills so that they always appear below the Inks.

Because the tool operates in this way, you can, for example, scan a pencil sketch, import the bitmap into GuineaPigment, and quickly fill all its cells with colors without tracing the bitmap first. This is a very convenient and interactive way of digitizing your paper drawings, making the traditional bitmap tracing unnecessary in many cases.

The resolution of the bitmap image used to perform the trace is dependent upon your current zoom level -- the more 'zoomed in' to an area that you are, the higher the resolution of the bitmap-based flood fill. So, if you have a fill that is too imprecise, has rough corners, or doesn't go where it is supposed to go, just undo it (CTRL + z ), 'zoom in' closer and repeat filling from the same point. Conversely, if the fill leaks out through a small gap, zoom out to make the gap less visible and fill again (or use the auto gap closing parameter - see below).

<!-- image -->

## HOW TO USE

The Paint Bucket Tool works fairly intuitively: click in any area bounded on all sides and it will fill it with color - or, in reality, a path which can be filled and adjusted like any arbitrary path.

## Style

Like all object-creating tools, the Paint Bucket may use the last-set style for the objects it creates (this is the default), or it can use its own fixed style . You can switch between these modes on this tool's page in GuineaPigment Preferences (Ctrl+Shift+P). As in all other tools, the style swatch on the far right of the Controls Bar shows the style that will be used for the next fill object you create.

## Controls

In the Tool Controls bar: Paint Bucket's perceptual fill can use either all visible colors or specific color channels . Using the Fill by drop-down list, you can restrict the fill algorithm to one the following channels:

- Red
- Green
- Blue
- Hue
- Saturation
- Lightness
- Alpha

The Threshold (in per cent units) controls how large the color difference must be at a point (compared to the initial click point) to stop the fill. 'Zero tolerance' means only an area which is strictly the same color will be filled; the larger the tolerance, the easier it will be for the fill to leak into adjacent different-color areas. The default value is 10%.

Using the Grow/shrink by parameter, you can control the amount of inset / outset to be applied to the created fill path. Setting a positive outset causes fill paths to be larger than the filled bitmap area (good for eliminating antialiasing errors), while setting a negative outset causes the path to be smaller. This works much the same as the Outset and Inset path commands, except it's done automatically after every fill.

With the Close gaps parameter, you can make the Paint Bucket tool ignore any gaps in the area boundaries that would normally cause the fill to spill out of the desired area. There are four settings to auto gap:

- None
- Small (close gaps up to 2 pixels in size)
- Medium (4 pixels)
- Large (6 pixels)

Note : setting this parameter to anything other than None may slow down GuineaPigment noticeably while filling large areas.

## HOTKEYS

The tool's shortcuts are:

- Single click performs filling from the click point.
- Shift+click performs filling from the click point and then unions the resulting path with the selected path. This way, if your first attempt did not fill in all of the desired area, you can Shift+click the remaining corner to fill it in separately and combine the result with the result of the previous fill.
- Ctrl+click on an object simply changes that object's fill to the current fill color of the tool, and Shift+Ctrl+click changes the stroke to the current stroke color.
- Click+drag performs filling from all of the points that you pass while dragging (you will see your path visualized by a red line). From each point, the fill spreads to its neighbours with the colors similar to that point - in other words, it's like clicking with this tool at each point of the drag path and joining the results. This lets you easily fill an area occupied by a gradient or blur - just drag from the darkest to the lightest points in the area you want to fill.
- Alt+click and drag works similarly to simple drag, except from each point of the drag path, the fill spreads to the neighbours (if any) with the colors similar to the initial point (the point where you started the drag). This lets you fill a series of similarly-colored yet separated areas (for example, multiple cells in a cartoon) by starting the drag in one of those areas, and Alt +dragging the tool through all the other areas.

<!-- image -->

# 18. TEXT TOOL

The Text Tool makes it possible to write text in an SVG drawing.

## HOW TO USE

To invoke the tool, press Shift + Ctrl + T .  Alternatively there is a T ext menu which allows you to change the aspect of the characters or their behavior with respect to other elements of the drawing. Text Tool uses several short cut keys to modify typographic elements.

There are two ways to use the Text Tool :

1.  Select the Text Tool and click on the canvas to create a simple line field . It will grow with the written text.
2.  Click and drag to draw a rectangle this becomes a text box : this frame will contain the text and will be the limit for the word wrapping. The text box will not grow with the text, so if there is too much text for the frame, some letters will simply not be displayed. This frame can be manually resized by dragging the handle at the bottom right corner. The Flow into Frame command of the Text menu makes it easy to use any shape as a text container .

## SPECIAL CHARACTERS

- Ctrl + Space inserts on non-breaking space
- Ctrl U allows to use Unicode encodings within the document. To find a Unicode value refer to a Unicode character map program or reference.
- To insert an arbitrary Unicode character, type Ctrl + U , then the hexadecimal code, then Enter. For example, type Ctrl U 2 0 1 4 Enter for an em-dash ; Ctrl + U a 9 + Enter for a copyright sign .
- To stay in Unicode mode after inserting the character, press Space instead of Enter
- Press Esc or another Ctrl U to cancel Unicode mode without inserting the character.

## TIPS

- If you're not sure if all your text is visible in the frame, use the T ext and Font window to read it all.

<!-- image -->

# 19. CONNECTOR TOOL

The Connector tool ( Ctrl + F2 or the o key) draws lines between objects that stay connected to other objects as they are manipulated. Any object may be marked as an object to avoid , which causes connectors to automatically route around the object. This is helpful for creating technical illustrations like flowcharts.

## HOW TO USE

## Connecting

A new connector can be drawn by clicking and dragging from any point on the canvas. Connectors can also be created with two clicks, rather than click-and-drag, if this is preferred. In this case, click once on an empty point on the canvas to begin drawing the connector, then move the mouse to the new connector's target point and then click again to finalize the connector. Single clicking on a canvas object selects/deselects that object, just as with other tools. Usually connectors are drawn from an existing object:

<!-- image -->

Connection point handles are shown while the mouse cursor is hovering over a non-connector object in the connector tool. Currently they are shown only at the center of objects. When creating a connector, if the connector is started or ended over a connection point then the connector will be attached to that object. From then on the connector will be automatically rerouted whenever the attached object is moved.

Connectors attached to objects are currently drawn to the bounding box of those objects. It is planned that they will be drawn instead to the edges of objects.

The connector is finalized, when the mouse is released:

<!-- image -->

<!-- image -->

The Make connectors avoid selected objects button marks all objects in the selection as "avoided", causing all current and future connectors to automatically avoid these objects.

The Make connectors ignore selected objects button marks all objects in the selection as "ignored", causing all current and future connectors to completely ignore these objects. This is the default for all canvas items, i.e., no objects are automatically routed around by default.

Here the middle object is avoided:

<!-- image -->

By default, the Connector tool will not attach connectors to text objects. A checkbox in the Connector preferences controls this setting.

## Rerouting

A selected connector shows two endpoint handles . By clicking and dragging these, the connector can be rerouted and attached/detached from objects.

Connectors moved as part of a selection will stay attached to other objects in the selection, rather than becoming detached from them.

## Arranging

The margins around avoided shapes used for autorouting connectors can be adjusted via the "Spacing" control on the controls bar.

The Remove Overlaps button to move the selected objects enough that they don't overlap each other. A minimum spacing between the boundaries of objects can be specified. Together with the automatic layout tool, described above, this should be a significant addition to GuineaPigment's usability for diagramming. Removing overlaps is different from the "Unclump" button in that the former is completely deterministic and guarantees removing overlaps on the first application, but is not concerned with visual perceptive distances between objects. Unclumping, on the other hand, attempts to equalize perceptive distances between objects and can be

applied repeatedly for gradual effect.

Automatic Diagram Layout : this function is available in the Align and Distribute dialog and performs automatic layout of diagrams involving a network of shapes and connectors. Edges are treated as if they are springs such that the distance between nodes will be proportional to the path length - number of connectors between them. Disconnected components (where not every shape is connected) will be arranged around the circumference of a circle.

<!-- image -->

# 20. GRADIENTS

The Gradient Tool allows the progressive passage of one color to another (or multiple others) in an object. It can be used on any shape , closed or opened, as a fill or a stroke (applied separately). Any number of selected objects can simultaneously display handles and direction lines for the linear and radial gradients in their fills or strokes. You can drag these handles directly in the drawing, to interactively adjust gradient positions.

The gradient can be set in the Fill and in the Stroke Paint dialog to replace of any other type of coloration.

## HOW TO USE

To invoke, either click the Gradient Tool icon or press Ctrl + F1 .

## Types of gradients

There are two types of gradients:

<!-- image -->

1. Linear gradients transition the color change from one point to another in a straight line. Just click where the gradient should begin, hold and drag, and release where it should end.    T wo handles now appear: the handle of the beginning is square and the end is a circle.  T he two handles can now be used to change the color (select each one and choose the color for it from the fill and stroke dialog) or move and change the gradient direction.
2. Radial gradients work as colored circles with the color transition beginning at the center. Three handles are available : the square one is the center of the gradient, and the circle ones change the radius of the gradient. When the radius is the same for both circle handle, the gradient is perfectly circular. T o move the placement of a radial gradient in the object, drag the square handle.

<!-- image -->

<!-- image -->

Once a gradient is created it is automatically saved in the drop-down list of the Gradient Tool Options bar so that it can be easily reused on other shapes.

## More colors

To have more than two colors on a gradient, just double-click on the gradient base path to make a new handle (stop) appear.

By default first and last color stops have fill color that matches original flat color fill of the object, but opacity drops from 100% to 0% accordingly. All new color stops in between will inherit original fill color, but have various opacity depending on position of each color stops on the gradient line (i.e. percentage of the radius).

Click in the swatch to set the color. You can move this handle to adjust the position of this stop. To delete a stop, just press the Backspace key.

<!-- image -->

## Selecting multiple stops

More than one gradient stop can be selected at a time. Shortcuts for working with multiple stop selections are generally modeled on the Node tool.

- Add a stop to the selected stops by Shift+click .
- Press Ctrl+A to select all stops in the selected objects.
- Shift+drag around stops to add them to selection.

Multiple selected stops:

- Can be moved together by mouse drag or by arrow keys . For example, creating a linear gradient, then press Ctrl + A to select all stops and use arrow keys to move the entire gradient as a whole.
- Can be deleted at the same time by pressing Del .

An always up-to-date description of the current handle selection is provided in the statusbar in the Gradient tool, including the number of selected handles (and the type of the single selected handle), as well as the total number of handles and selected objects.

## Editing intermediate stops

Intermediate stops in gradients can be added, deleted, and edited right on canvas.

Stops can be added by double clicking or by Ctrl+Alt+Click on the gradient line. Also, you can drag-and-drop a color from the palette onto the gradient line to create a new stop with this color. Dropping a color on an existing stop changes the color of that stop.

When two or more adjacent stops are selected, pressing Ins adds stops in the middles of all selected stop intervals.

Intermediate stops can be mouse-dragged or moved by arrow keys along their gradient line, within the limits of the adjacent unselected stops (or end handles).

- Dragging with Ctrl moves the selected stops snapping them to 1/10 fractions of the available range.
- Dragging with Alt moves the selected stops depending on how close each one is to the stop being dragged, using a smooth bell-like curve similar to the node sculpting feature in Node tool. This makes it easy to approximate different gradient profiles; for example, if you have a two-stop gradient that you want to shape according to a curve profile, select both ends of the gradient, press Ins a few times to add a number of intermediate nodes, then Alt+drag a node in the middle to smoothly profile the gradient.

Stops can also be moved by arrow keys with all the regular modifiers ( Shift for 10× movement, Alt for pixel-size movement at the current zoom, Shift+Alt for 10 pixels movement at the current zoom).

Stops can be deleted by Ctrl+Alt+Click on a stop or by the Del key for all the selected stop(s).

- When you delete an end stop, the nearest intermediate stop becomes the new end stop of the gradient (without moving - i.e., the gradient span becomes shorter).
- When you delete an end stop and there are no intermediate stops, the object will be painted with a solid fill taken from the color &amp; opacity of the remaining stop.

Pressing Ctrl+L with some intermediate stops selected attempts to simplify the selected portion of the gradient, removing those stops that can be removed without too much change in the way the gradient looks. In particular, new stops created by double-clicking or pressing Ins initially do not change the appearance of the gradient, so if you press Ctrl + L , all redundant stops that weren't moved or repainted since creation will be deleted.

## Automatic duplication of gradients

When copy/pasting or duplicating an object with gradient, it automatically gets a copy of the original gradient, so modifying it does not affect the source object's gradient anymore .

However, to accommodate the needs of users who rely on sharing the same gradient definition across objects, this behavior can be optionally suppressed. The Prevent sharing of gradient definitions checkbox on the Misc tab of GuineaPigment Preferences is by default checked; if you uncheck it, GuineaPigment does not automatically copy gradient definitions for new objects, which means that copy/pasting, duplicating, pasting style, and explicit assignment of a gradient to an object via the Gradient tool controls results in a shared gradient definition, so that changing the colors or mid-stop positions of the gradient on one object (but not changing the coordinates of the end handles) affects all other objects that share the same definition.

# 21. DROPPER TOOL

The Dropper Tool is used to select an object 's fill or stroke color by sampling the color of an area of the canvas . T he color selected is the single point at the center of the cross at the end of the Dropper Tool icon.

## HOW TO USE

Select an object to which you want to apply a new color and press F7 or D to switch to Dropper. Click a point on the canvas which is the desired color - the fill of the selected object will be changed to the target color. Shift + Click to apply this color to the stroke.

The shortcut D can be used to toggle (not just switch to) the Dropper tool - much like space is used to toggle the Selector Tool. That is, pressing D a second time switches back to the tool used before.

## Alpha Settings

The toolbar has only two options:

<!-- image -->

The left icon toggles picking the alpha channel . T he right icon toggles setting the alpha channel.

Suppose you have an object selected and, using Dropper, click on an object which has blue transparent fill (# 389bff7f).

<!-- image -->

If the "Pick alpha" checkbox is off, the selected object will get the fill color # 9ccdffff (i.e. faded-out blue) and opaque:

<!-- image -->

If the "Pick alpha" checkbox is on, but "Set alpha" is off, the selected object will get the fill color #389bffff (bright blue) and opaque:

<!-- image -->

If both "Pick alpha" and "Set alpha" are on, the selected object will get the fill color # 389bff7f (pale blue) and half-transparent, i.e. fully match the fill style of the object from which the color was inherited:

<!-- image -->

Note that in no situation can Dropper change the master opacity of the selected object(s) (only the fill/stroke opacity), although it can pick it just as it does any other kind of opacity.

## Select Average Color

There are cases also, when you might want to apply an average color of an area - for example, an object with gradient fill.

With an object selected, click and drag the Dropper Tool from the central point of an area with the average color you want to pick:

<!-- image -->

<!-- image -->

The selected object will be filled with the averaged color value of the dropper selection.

<!-- image -->

The same can be done for stroke by Shift + Click + Drag :

<!-- image -->

<!-- image -->

And you get:

<!-- image -->

## HOTKEYS

Alt + Click picks the inverse of the color selected by the Dropper Tool (also works with averaged color selections and applying to target object borders).

## TIPS

You can pick a color from the target object itself.  You can do this, for example, to set the stroke fill the same as the object fill.

## PATHS

# 22. PATH MODIFICATION EFFECTS

# 22. PATH MODIFICATION EFFECTS

Modify Path Effects work on a selection of any number of paths and modify them in various ways without creating new paths or deleting existing ones.

## AVAILABLE EFFECTS

## Envelope and Perspective

Maps bounding box of a path to quadrilateral to achieve effect of a perspective. These two effects are quite similar, but differ in level of natural look of the desired effect.

Here is how to use it:

1.  Draw your to-be-distorted path
2.  Draw and position a four node path ( envelope frame ).
3.  Place the to-be-distorted path inside/above the envelope frame.
4.  Select the path you wish to distort first and then add to selection the envelope frame. The original position of the four nodes is considered to be clockwise around the bounding box of the path to distort beginning in the upper left corner.
5.  Apply the effect.

## Here is the difference:

<!-- image -->

<!-- image -->

## Add Nodes

Adds nodes to the selected paths. Each segment of the selected path is subdivided into ceil (Length/Max) equal length segments. Lengths are measured in SVG User Units calculated from the path data and do not take into account any transforms.

Parameters for example below:

- Division method: by number of segments
- Maximum segment length (px): 5
- Number of segments: 2

Color Markers to Match Stroke

<!-- image -->

Currently available SVG 1.1 Full specification doesn't allow using the same color for the path and its markers. This extension is a temporary workaround to fix that (until the new improved SVG specification is out). Just change the stroke color of your path and call this effect to recolor its markers to match.

<!-- image -->

## Flatten Beziers

Flattens paths in the current selection, approximating each path with a polyline whose segments meet the specified criteria for flatness. Lower flatness values make a smoother line.

Parameters for example below:

- Flatness:10

## Fractalize

Replaces each segment of the selected path by a crooked line, subdivided to the given depth, with randomly displaced nodes.

Available options are:

Parameters for example below:

- Subdivisions: 6
- Smoothness: 4.0

## Jitter nodes

Randomly shifts nodes (and, optionally, node handles )

Parameters for example below:

- Maximum Displacement in X: 50.0
- Maximum Displacement in Y: 50.0
- Shift nodes: checked
- Shift node handles: checked
- Use normal distribution: checked

<!-- image -->

## Straighten Segments

Straightens curved segment to a user defined level (in percents), using of two behaviours ( 1 stands for  rounded corners, 2 stands for less rounded corners).

Parameters for example below:

- Percent:50
- Behavior: 1

## Whirl

Twists the selected paths around the specified center point.

Parameters for an example below:

- Amount of whirl: 15
- Rotation is clockwise: checked

<!-- image -->

## TEXT

23. STYLING TEXT
24. TEXT EFFECTS
25. TEXT AND PATHS

<!-- image -->

# 23. STYLING TEXT

Many modifications can be done to Text . Some are available in Text Option Bar , but some aren't. Here is a little overview of the most useful options.

## TEXT SELECTION

- Ctrl with arrows left and right : moves the beam word by word
- Shift with arrows left and right : selecting glyph by glyph
- Ctrl Shift with arrows left and right : selection by words
- Double click : select the word
- Triple click : select the line
- Shift + Home : select from the beginning of the line
- Shift + End : select until the end of the line
- Ctrl  + Shift +Home : select from the beginning of the text
- Ctrl + Shift + End : select until the end of the text

## TEXT ASPECT

The Tool Controls Bar provides several options such as :

<!-- image -->

- Font families
- Font size
- Bold style
- Oblique/Italic style
- Alignment

## HOT KEYS

- Ctrl +B and Ctrl + I applies bold and italic to the selected text.
- Kerning : Alt with arrows left and right increases or decreases the space between characters at the end or beginning of the selection. You can also use Alt + &lt; , Alt + &gt; to decrease or increase the space after all characters in the selection. Pressing Shift will change the letter spacing more significantly.  Use the Remove manual kerns menu of the Text menu if you are not satisfied with it.
- Pressing Alt + [ , Alt  +] rotates precisely the letters; Ctrl + [ , Ctrl + ] do 90° rotation at once.
- Alt arrows up and down change the vertical position of the selected text relatively to the baseline.

<!-- image -->

# 24. TEXT EFFECTS

Writing text often requires the repetition of the same operations. The Effect &gt; Text menu can do some of them automatically.

## LOREM IPSUM EXAMPLE

In the example below a standard latin text taken from Cicero is insterted into a text frame. This is useful in cases when a text placeholder is required (e.g. webdesign).

<!-- image -->

Ocor

## REPLACE TEXT

Replace Text simply replaces the text written in the first field of the dialog by the text written in the second one.

quls, tristique cursus leo Etlam pharetra lacus sed vellt Imperalet nec consequat nisl vclit at dui Sed atlacus

<!-- image -->

antc conaimentum kss; tristique cursus neqve vel condimentum hendreritlectus elit pretium ligula

## SENTENCE CASE

Sentence Case replaces lower case characters by capitals ine the beginning of every sentence.

lorem ipsum dolor sit amet, consectetuer adipiscing elit. mauris sed nulla quis nisi interdum tempor. estibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; suspendisse potenti. liquam sed erat. ellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. praesent aliquet, neque pretium congue mattis, ipsum augue lonec ut purus. in leo

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Mauris sed nulla quis nisi interdum tempor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; suspendisse potenti. Aliquam sed erat, Pellentesque habitant morbi tristique senectus et netus et onec ut purus. In

## TITLE CASE

Capitalizes first letter of each word.

## GuineaPigment user manual

## UPPER CASE

Capitalizes all letters.

GuineaPigment user manual

## FLIP CASE

Reverses letter case, so that all capitals become lower case, and all lower case letters become upper case letters.

GuineaPigment UsEr ManUal

## LOWER CASE

All the letters  become lower case.

<!-- image -->

# 25. TEXT AND PATHS

Text and path can be complementary elements that work together. Some options of the Text menu are very interesting.

## PUT ON PATH / REMOVE FROM PATH

GuineaPigment has support for the SVG element &lt;textPath&gt;. That allows putting a text on a path so that it follows its shape. Both text and path remain fully editable (including kerns and letterspacing in text).

Select the path and the text and use Text-&gt;Put on Path. When you move the path, its attached text moves with it; however, you can move the text away from its path or transform it without losing the link. T he T ext-&gt;Remove from Path command converts a text-on-path into a regular text object.

<!-- image -->

## FLOW INTO FRAME / UNFLOW FROM FRAME

The Flow into frame Alt+W command of the Text menu takes any selected text and puts it into the selected shape.  Word-wrapping is automatically done so that the text fits the shape as precisely as possible. Manual adjustment can still be done on the text after this. To separate the text from the path, just use Unflow or press Shift+Alt+ W .

<!-- image -->

<!-- image -->

Put this text in the shape mettre ce texte dans la forme

<!-- image -->

## MULTIPLE OBJECT OPERATIONS

26. COPY, CLONE AND DUPLICATE 27. CLIPPING PATHS AND MASKS

# 26. COPY, CLONE AND DUPLICATE

## INTRODUCTION

The artist may have need, at some point in his work, to replicate an object he has created for any number of purposes. Possibly he is populating a scene with bubbles or blades of grass which will all look exactly alike, or else he may want to create a very similar object which has some minor modifications.

Fortunately, GuineaPigment offers several tools to replicate objects. Each one has advantages in disadvantages, of course, which will be defined also by the purpose of the replicant object.

A strict copy of an object repeats the object on screen and within the xml code, and the new object is entirely separate from the original. This means that changes can be made to the replicant indifferently to the original, and changes made to the original do not affect the replicant either. T his is done with either the Copy or Duplicate commands.

A clone is merely a repetition of the original on screen and in the code. Most modifications made to the original, like fill and transparency, are transferred to the replicant as well, and only a few modifications, such as transform and position, may be made to the replicant directly (some of these only under certain circumstances). Clones are created with the Clone command.

## HOW TO USE

## Copy

The Copy command ( Ctrl + C or Edit &gt; Copy or the command bar button) makes an exact copy of the selection in GuineaPigment's memory; the Paste command ( Ctrl + V or Edit &gt; Paste or the command bar button) puts an exact copy under the cursor. The last selection to be copied can be pasted an indefinite number of times. It is also possible to paste the object wherever it is needed, for instance on an other layer, without the trouble of having to reposition the copy after its creation.

## Duplicate

The Duplicate command ( Ctrl + D or Edit &gt; Duplicate ) allows you to copy and paste a selection automatically with one command. The new object or selection is in exactly the same position as the original and is selected (instead of the original), ready for further manipulation.

## Clone

The Clone command ( Alt + D or Edit &gt; Clone ) allows you to create a copy of the selection that is linked to the original, also known as its parent .  T he clone's shape, style (fill and stroke, transparency) and dimensions are linked to its parent. Thus, editing the parent's transparency (etc.) will also affect the clone's transparency.

You can clone multiple object by grouping them first.

A clone can be a parent to another clone. Any modifications to the original will affect all clones down the hierarchy of clones.

The fill and stroke paint of a clone is the same as its parent's unless the parent has "Unset paint" activated for either in the Fill and Stroke dialog. Unsetting fill will make the parent's fill black as well as the clone's, but the clone's fill can then be reset while the parent's cannot; unsetting stroke paint will make the stroke disappear so that the clone's stroke and stroke paint can be adjusted while the parent's cannot (it will remain invisible unless paint is reset for the parent).

## Unlink clone

Unlink clone ( Alt + Shift + D or Edit &gt; Clone &gt; Unlink clone ) separates a clone definitively from its parent, effectively making it only a copy. After that you can apply changes to the parent without changing the copy.

## Select original

Use Select original ( Shift + D or Edit &gt; Clone &gt; Select original ) to find the parent of a selected clone. This is very useful when you have lost your parent.

# 27. CLIPPING PATHS AND MASKS

## INTRODUCTION

Clip paths, masks, and patterns are greatly useful additions to an artist or designers' tool set. A common property that all three share is the concept of boundaries. Clip paths and masks bound the contents of the items they contain, whereas patterns are only visible inside the bounds of the object they are applied to (in all three cases cropping visibility).

These methods do not delete parts of your objects, they merely tell the SVG renderer not to display them. This non-destructive editing makes it so that we can also release objects from from their bounded areas as well.

There are benefits to working with clip paths or masks combined with either individual or grouped objects.

Use of patterns fills is addressed in a dedicated chapter.

## CLIPPING

The clip function in GuineaPigment allows an object or a group of objects to be clipped (cropped) so that only parts of the elements are visible. Clipping can be applied to any object (including groups, layers, bitmaps, etc.)

The easiest way to understand clipping is to see it in action. Take the following assortment of objects:

<!-- image -->

Now, place another object on top of all the others. This is what we are using for our clipping object. Note that the Z-order of the clipping object is important, as the default behavior in GuineaPigment takes the top-most object as the clipping object. Also note that the style (fill, stroke, opacity etc.) of the object is irrelevant, all that is used when clipping is the shape of the object.

<!-- image -->

The next step is to select all the objects that you want clipped and the clipping object. Then in the menus, go to Object &gt; Clip &gt; Set. The result is:

<!-- image -->

Since this is all non-destructive editing, it means that we can also release objects from a clip. Do this by selecting the object that you wish to release, and in the menus go to Object &gt; Clip &gt; Release. In the following example the blue star object was selected, and the clip was released:

<!-- image -->

So the purple clipping object has now returned, and the blue star object is no longer clipped. Note that the other two objects are still clipped, as the clip was applied to 3 seperate objects. These clips still apply and can be released if needed. Because clipping paths can be applied to any object, if you wanted to treat the 3 objects as a whole, you would group them, then apply the clip to the group.

Clipping can be done on any object, even objects that have had filters applied to them. Below is an example of using clipping to create a bubble effect on a circle:

A clip can also be done on bitmaps that are embedded into or linked from an SVG:

<!-- image -->

<!-- image -->

## MASKING

Like clip paths, masks allows an object or a group of objects to be visually cropped. The difference is that the mask's black or transparent areas become fully transparent in the masked object; mask's opaque white areas become fully opaque; and all intermediate colors translate into intermediate levels of opacity in the masked object. This allows you to apply, for example, arbitrary transparency gradients to objects.

In the following example you will see both the masks and the items they're applied to. As you'll notice, masks offer the ability for you to texture objects, give them depth, and other things that clip paths can't provide:

<!-- image -->

<!-- image -->

## POSITIONING OBJECTS

28. INTRODUCTION TO POSITIONNING
29. ALIGN AND DISTRIBUTE

# 28. INTRODUCTION TO POSITIONNING

Every new object is placed at a higher level of z-order . It is impossible to have two or more objects at the same level. If there is a need to change the stack , use some Object menu entries or Selector Tool F1 options.

If layers are defined, the stack changes occur in the layer.

When the Selector Tool F1 is on, this option appears in the Tool Controls bar.

<!-- image -->

## RAISE TO TOP

Raise to top  ( Home ) command puts any selected object at the top, above all other objects in the drawing.

SVG places any newly created object at top. However it is impossible to have 2 objects at the same stack-level. Some shapes or paths may be masked by these new objects.

<!-- image -->

## LOWER TO BOTTOM

Lower to Bottom puts all selected objects at the bottom, below all other objects of the drawing.

<!-- image -->

## RAISE

The Raise  (PgUp)  command changes the stack of any selected object so that its z-order is just changed by one level and goes over only one other.

<!-- image -->

## LOWER

The Lower (PgDn) command changes the stack of any selected object so that its z-order is just changed by one level and goes below one other.

<!-- image -->

# 29. ALIGN AND DISTRIBUTE

Align and Distribute moves multiple selected objects to the same axis and distributes them equally relative to a selected anchor object.  The Align and Distribute dialog offers many ways of applying these functions to object selections.

<!-- image -->

## HOW TO USE

The Align and Distribute dialog can be called by pressing Shift+Ctrl+A , selecting Object &gt; Align and Distribute , or clicking the icon on the T oolbar:

<!-- image -->

Make sure your objects are selected.  Depending on which object you wish to have as the anchor and which relative to setting you have selected, order of selection will be important.

## "Relative to"

Objects can be aligned and distributed relative to:

- the last or first selected
- the biggest or smallest item
- the page
- the drawing (all objects within the document)
- the selection of objects

## Align

To align selected objects, click one of the align icons:

- Align right sides of objects to left side of anchor
- Align left sides
- Center on vertical axis
- Align right sides
- Align left sides of objects to right side of anchor
- Align baseline anchors of text vertically
- Align bottoms ob objects to top of anchor
- Align tops
- Center on horizontal axis
- Align bottoms
- Align tops of objects to bottom of anchor
- Align baseline anchors of texts horizontally

## Distribute

To distribute selected objects, click one of the distribute icons:

- Distribute left sides equidistanly
- Distribute centers equidistanly horizontally
- Distribute right sides equidistanly
- Make horizontal gaps between objects equal
- Distribute baseline anchors of text horizontally
- Distribute tops euidistanly
- Distribute centers equidistanly vertically
- Distribute bottoms equidistanly
- Make vertical gaps between objects equal
- Distribute baseline anchors of text vertically
- Randomize centers in both dimensions
- Unclump objects ; try to equalize edge-to-edge distances

## Remove overlaps

You can also define:

- Minimum horizontal gaps between objects,
- Mimimum vertical gaps,
- Move objects as little as possible so that their bounding boxes do not overlap

## Connector network layout

If you are using the connector tool and need to distribute the connected objects, use this button to rearrange the selected connectors.

## Nodes

There are 4 buttons to organize nodes in path. Select the nodes with Node Tool and click one of the node align buttons:

- Align selected nodes horizontally
- Align selected nodes vertically
- Distribute selected nodes horizontally
- Distribute selected nodes vertically

## ORGANISING OBJECTS

30. LAYERS 31. GROUPING

<!-- image -->

# 30. LAYERS

Layers are a type of object group within an SVG document.  As the name indicates, they are like stacked slices of the image which can be stacked, arranged, added and removed.  In addition, layers can be locked and made invisible to ease editing of objects within other layers of the document.

Layers can be very useful for several purposes:

- Arranging sets of objects by z-order (or stacking );
- Grouping objects which should be made visible/invisible or locked/unlocked together;
- Setting background layers which are visible but not selectable;
- etc (limited only by your imagination)

## THE LAYERS WIDGET ON THE STATUS BAR

The quickest and easiest way to work with layers is to use the layers widget on the statusbar .

<!-- image -->

Once you have created multiple layers in your drawing, you can select a layer easily from the combo box.  You can also hide / unhide or lock / unlock the current layer from this widget.

## THE LAYERS DIALOG

The Layers dialog controls all layer functions - adding new layers, renaming , deleting , arranging , toggling visibility and edit-locking, and setting Blend mode and opacity .

<!-- image -->

## BLEND MODE AND OPACITY

You can choose to apply a Blend mode to layers, which makes all objects in a layer blend together as if they were one object - i.e., the two objects within the same layer will not blend with each other when layer blend modes are used.  The available modes are the common Multiply , Screen , Darken , and Lighten .

Opacity for an entire layer operates in a similar manner - objects within the layer have their opacity set as if they were a single object, so that one will not show through the others.  Only objects from layers beneath will show through the affected layers.

## HOW TO USE

To open the Layers dialog, press Ctrl + Shft + L or select Layer&gt;Layers .

## Adding Layers

New documents created by GuineaPigment using the default template have only one layer.  It is simple to create new layers which can be used right away.

To create a new layer, click "Create a new layer" on the Layers dialog.

Note : Although it is possible to have the same name for multiple layers (since each is given a different ID automatically), this is not the SVG standard.  It is good practice to name each layer differently.

## Renaming Layer

To rename a layer, double-click on the layer name in the Layers dialog or rightclick the layer and select Rename Layer.

## Selecting Layers

To select a layer (in order to make it active), simply click on the layer once in the Layers dialog or select it from the layers widget on the status bar.

## Moving a Selection Between Layers

To move the current selection to the previous or next layer press Shift + PgUp or Shift + PgDn .

## Moving Layers

To raise a layer one level press Shift + Ctrl + PgUp or click the "raise the current layer" arrow in the  Layers dialog.

<!-- image -->

To lower a layer one level press Ctrl or click the "lower the current layer" arrow in the Layers

<!-- image -->

To raise a layer to the top press Shift + Ctrl + Home or click the "raise the current layer to the top" arrow in the Layers dialog.

<!-- image -->

To lower a layer to the bottom press Shift + Ctrl + End or click the "lower the curent layer to the bottom" arrow in the Layers dialog.

<!-- image -->

## Deleting Layers

To delete a layer, it must be selected. Click the "delete the current layer" button in the Layers dialog.

Locking Layers

<!-- image -->

To lock or unlock layers, click on the lock icon to the left of the layer name in the Layers dialog or the status bar.  The icon changes to reflect the current edit-lock status.

<!-- image -->

## Hiding Layers

To make a layer invisible or visible, click on the eye icon to the left of the layer name in the Layers dialog or the status bar.  The icon changes to reflect the current visibility status.

## Blend Mode

To change the blend mode, click on the blend mode dropdown in the Layers dialog and select a new mode.

<!-- image -->

## Opacity

To change the opacity of a layer, move the opacity slider in the Layers dialog to the right or left.

<!-- image -->

# 31. GROUPING

Sometimes several objects need to be manipulated together in a group rather than separately.  For example, if you want to keep the position of several objects relative to each other but still be able to grab and move those objects around the canvas quickly and easily. You might also want to adjust one setting for several objects at the same time, such as fill or transparency .

A group is treated as a single object, and for most operations it can be manipulated as such. For example, groups can be "stacked", meaning that you can create groups made of groups or groups other objects.  (This can be helpful, but it can also be very confusing if it becomes complicated.)

Groups cannot, however, be created between groups; in other words, you cannot select one object from two groups and create a new group without destroying or modifying the original groups.

## HOW TO USE

## Creating and Releasing Groups

Groups are created by selecting multiple objects and pressing Ctrl + G or clicking the Group button on the Commands Bar.

<!-- image -->

Groups are released by selecting the group and pressing Shift + Ctrl + G or clicking the Ungroup button on the Commands Bar.

<!-- image -->

## Working with Objects in a Group

Individual objects within a group can be manipulated as normal by "entering" the group.

To enter a group, double-click the group.  You may then select any object in the group individually to work with it.

To leave a group left-click on an object outside the group (rather than the canvas).

## Selecting Objects within a Group (from outside the group)

Objects may be selected from within groups for manipulation without entering or releasing the groups.  This is very useful if you need to quickly change only one member of a group, yet leave the group intact.

To select an object within a group without entering that group, press Ctrl and left-click the object.

To select multiple objects within groups (they can exist withing various groups), press Shft + Ctrl and left-click the objects.

## Adding Objects to a Group

In order to add objects to a group, you can use several methods, each having its own benefits and drawbacks:

1.  Select the group, ungroup, add the object to the selection, then regroup.
2.  Enter the group and draw a new object.
3.  Copy or cut the object from the canvas, enter the group, paste the object.

## STYLING OBJECTS

32. INTRODUCTION TO STYLING
33. FILL AND STROKE
34. STROKE STYLE
35. SOMEBODY SHOULD SET THE TITLE FOR THIS CHAPTER!

# 32. INTRODUCTION TO STYLING

Objects in SVG can have various types of styles applied to them, and GuineaPigment offers multiple approaches to applying these styles.  Unfortunately, this makes the discussion of styling objects fairly complex.  T his chapter aims to simplify the discussion as much as possible while revealing the possibilities of GuineaPigment and SVG drawings.  Accordingly, this introduction will focus on explaining the types of object styling and a little bit about alternative ways of applying styles.

## FILL

Fill is the color or pattern applied within the path borders of an SVG object. Each SVG object has some kind of fill (except diagram connectors).

Note : Even bezier and freehand lines have fill, although by default it is set to transparent.

There are three basic types of fill:

- Solid Fills - invariant color fills the object.  T his color can have an opacity setting from 0 to 100 (0 being completely transparent, 100 being completely opaque).
- Gradient Fills - are a combination of two or more colors (or transparencies).  A gradient begins with the first color and blends smoothly into the next, etc.  Gradients can either be linear or circular.
- Pattern Fills - are comprised of repeating images which can be selected from a preset or defined by the user.  They can be either paths and shapes or bitmaps .

In addition, the fill can be set either to render or not render at any place where the object crosses over itself with the even-odd or non-zero settings.

## STROKE PAINT

Stroke Paint is the color or pattern applied to an SVG object's stroke.

Stroke Paint settings are basically the same as fill in that they consist of solid colors, gradients or patterns.  Stroke Paint cannot be set to even-odd - it always renders when it crosses over itself.

## STROKE STYLE

Stroke Style is a group of settings affecting the geometric properties of an object's stroke, such as width, decorative markers, dashing, etc.

## ALTERNATE APPLICATION METHODS FOR STYLES

Apart from selecting style types individually from the dialogs, there are several ways to paste copied styles by keystroke:

## Copy Styles from Other Objects

If you want to copy styles from one object to another, you can do so easily by copying the object as normal (press Ctrl + C ) and then paste the style by pressing Shft + Ctrl + V .

## Copy Dimensions from Other Objects

There are six options for copying dimensions from one object to a new object. They are found in Edit &gt; Paste Size

Paste Size - paste both the copied height and width to the selected object(s) so that the whole selection has the same dimensions as the original

Paste Width - paste only the copied width to the selected object(s) so that the whole selection has the same width as the original

Paste Height - paste only the copied height to the selected object(s) so that the whole selection has the same height as the original

Paste Size Separately - paste the copied height and width to each selected object individually (when multiples are selected) so that each separate object within the selection has the same height and width as the original

Paste Width Separately - paste the copied width to each selected object individually (when multiples are selected) so that each separate object within the selection has the same width as the original

Paste Height Separately - paste the copied height to each selected object individually (when multiples are selected) so that each separate object within the selection has the same height as the original

# 33. FILL AND STROKE

The Fill and Stroke Paint panels are found in the Style dialog.  The settings contained in these panels are used to apply color or pattern styles to their respective object elements, and function almost the same for each.  Fill affects the interior part of an object (anything inside the object's path ), Stroke Paint affects the path's stroke following its border.

An interesting point: when stroke paint has partial transparency, the object's fill will show through the inner half of the stroke paint but not the outer half, since the path stops at the center of the stroke and bounds the object's fill.  This can either make for interesting drawing possibilities or frustrated artists.  T his is by SVG specification design.

The fill or stroke paint of an object can be set to:

<!-- image -->

- No Paint
- Plain Color
- Linear Gradient
- Radial Gradient
- Pattern
- Unset (used mostly for creating clones that are styled independently from their master)

In addition, there are a few settings that can really complicate the ease with which this dialogue might otherwise be understood:

- Even-odd
- Non-zero
- Blur
- Opacity

## HOW TO USE

Select one or more objects or groups you want to edit, then call the Fill and Stroke dialog by selecting Object &gt; Fill and Stroke or by pressing Shift+Ctrl+F .

The following list describes each property setting.  (Examples are given using the Fill properties since they are seen more easily.)

## No Paint

<!-- image -->

No paint or fill is visible in the object or stroke.  T his means that any visible object behind the invisible fill will show through it.  T hough it may seem counterintuitive, this is not the same as "Unset" since this is actually a fill type rather than no fill type.

Objects set to "No Paint" still act as normal shapes and paths when they are manipulated in path operations.  For instance, a boolean operation will react to the path exactly the same whether it has no paint fill or any other kind of fill.

Note: any object with 0% opacity (completely transparent) on both fill and stroke is not selectable by normal click selection.  Any other selection method should work for transparent objects.

## Plain Color

<!-- image -->

A solid color paints the object or stroke.  In both Fill and Stroke Paint tabs, there are sub-tabs whereby color selections can be made either precisely (with the numeric and alpha-numeric controls) or more generally (with wheels and sliders). Each selector type also shows an RGBA definition box at the bottom-right in which one may define a specific hexadecimal color .

- RGB offers four sliders representing percentages of red , green , blue , and alpha
- HSL offers four sliders representing percentages of hue , saturation , lightness , and alpha
- CMYK offers five sliders representing percentages of cyan , magenta , yellow , black and alpha
- Wheel offers a convenient (though less precise) selection apparatus consisting of a hue wheel and a combination saturation/lightness triangle, underneath which is an alpha slider
- CMS (only available in some distributions) allows selection of a color profile and offers an alpha slider underneath

## Linear Gradient

<!-- image -->

A linear gradient paints the object or stroke according to two settings.  The gradient selector box chooses the gradient definition to use.  The repeat type selector box chooses none (the gradient only fills once from it's beginning point to its end point), direct (repeats the gradient infinitely, likely causing an abrupt color change at the end of each repetition if the ends are different colors), or reflected (repeats the gradient infinitely also, except that each repetition flips the gradient so the color changes are always smooth at the end of each repetition).

The direction and extent of the gradient is adjusted by dragging the handles.

Gradients may also be duplicated or edited from this dialog panel using the provided buttons.

## Radial Gradient

<!-- image -->

This panel works the same as linear gradient except that the gradient is applied radially .

The elliptical "shape", placement and extent of the radius is controlled by the three handles.

## Pattern

<!-- image -->

An SVG or bitmap pattern, selected from the selection box, paints the object.

To create your own pattern, select the object from which the pattern will be created.  T hen select Object &gt; Pattern &gt; Object to Pattern or pressAlt+I. Your object will dissapear from the canvas and appear on the list of patterns.

To do the reverse, select Object &gt; Pattern &gt; Pattern to Object or press Shift+Alt+I.

If the object filled with pattern is transformed, the pattern will be also.  If you don't want the pattern to be transformed, uncheck "Transform patterns" from the Transforms tab in the Preferences dialog.

## Unset

Clones with with the same charactaristics as their master:

<!-- image -->

Unset fill is applied to a master object of clones in order to make the clones paintable.  T his must be applied individually to the object's fill and stroke to affect each.  This will make the object's fill appear black and its stroke appear invisible.

## Even-Odd

## Blur

<!-- image -->

This setting is available only for an object's Fill.  It causes the fill to be completely transparent wherever a path crosses over itself.

## Non-Zero

<!-- image -->

This setting is available only for an object's Fill.  It causes the fill to be shown wherever a path crosses over itself.  This is the default setting.

<!-- image -->

Blur is not actually a paint function at all - it is actually an SVG filter effect . However, it makes sense in Fill and Stroke, since it is a very commonly useful visual effect.  It is also important to note that blur affects the entire object , not just the fill or the stroke, and cannot be applied separately to either.

Apply blur by dragging the slider or setting the number box to the desired blur factor.  Usually only a small factor (0-10) is needed.

## Opacity

<!-- image -->

Opacity sets the degree to which objects behind the affected object may be seen through it.

This opacity setting is separate from the color alpha setting, which is particular to either the fill or stroke paint.  Like blur, opacity applies to the entire object , affecting both fill and stroke together.

# 34. STROKE STYLE

Object strokes or outlines can have various styles applied to them from the Stroke Style panel on the Fill and Stroke dialog.  ( Stroke paint is applied from the Stroke Paint dialog and is not covered in this chapter.)

The center of an object's stroke follows the path of the object.  For example, if the stroke is 10 pixels wide, the stroke will be drawn 5 pixels in opposite directions on either side of the path.

## HOW TO USE

While an object is selected, activate the Fill and Stroke dialog by pressing Shift+Ctrl+F or selecting Object &gt; Fill and Stroke .  Changes in the dialogue will immediately affect the selected object(s).

A brief list of stroke style options follows:

<!-- image -->

- Width controls how thick the stroke is and your desired measurement unit.
- Join controls the type of angle on a non-curve joint miter (angled corners), round (rounded corners) or bevel (flat corners).  T his affects the outside of the join only.
- Miter limit keeps corners mitered at set limits of corner angle; the higher the miter limit setting, the sharper the corner can be while retaining its miter.
- Cap controls the type of cap that is on the end of an open path butt cap (flat), round cap (half-circle) or end cap (flat but extended).
- Dashes controls the dash pattern and its offset from the primary node.
- Start Markers , Mid Markers and End Markers set a marker selection from the dropdown (there is a pre-set selection of arrow-heads, etc).  Mid Markers places only one marker at the middle of the path.

## Creating New Markers

Create your object on the canvas, select it and then select Object &gt; Objects to marker. Your marker will appear in the selection box for markers.

If you are putting markers on a path and want to match them to the color of the path, select Effects &gt; Modify Path &gt; Color Markers.

# 35. SOMEBODY SHOULD SET THE TITLE FOR THIS CHAPTER!

## LIVE PATH EFFECTS

36. LIVE PATH EFFECTS
37. GEARS
38. PATTERN ALONG PATH
39. KNOT LPE

# 36. LIVE PATH EFFECTS

Live path effects (not to be confused with Extension Effects or SVG Filters ) are a new way to non-destructively modify path and shape objects . Path Effects affect the path data of an object but not its style . T he original path is preserved and can be edited directly on canvas , and the path effect applied to it will be updated live.

In the version 0.46 several path effects that are analogous to the corresponding extension effects (such as Path along Path effect and Pattern along Path that replaces the extension of the same name) are included. The most important advantage of path effects is that they are, indeed, live - you can still edit the original path and the effect will update in real time (unlike the extension effects which were one-time one-way transformations).

## DETAILS ABOUT OPERATION

The following schematic tries to explain how LPE work.

```
original style  ------------>  output style original path   -->  LPE  -->  output path ^ | parameters
```

The original style and path are from the path that the effect is applied on. The output is what is visible on screen. What is very important to notice is that output style equals original style .

The parameters can be paths, numbers, points, text, in principle anything.

## APPLYING EFFECTS

Path effects are applied through the Path Effects dialog. This is opened from the Path menu, or by pressing Ctrl + Shift + 7 . T his dialog is also used for controlling the effect's parameters and for removing effects.

When a path with a path effect applied is selected, the statusbar description gives details, for example " Path (4 nodes, path effect) ".

There is a special Paste Path Effect command Ctrl + 7 that can be used to copy effects from one path to another.

## EDITING EFFECT PARAMETERS

When switching to the Node Edi t tool F2 , the original path can be edited. The original path is shown as a red helper path. Normal path operations, like simplify , still work.

Some parameters of these effects can be edited on-canvas. For example, path parameters can be node-edited, by pressing the edit on-canvas button in the Path Effects dialog. Press 7 to cycle through the different on-canvas editable parameters. This way, one can edit the parameters without opening the Path Effects dialog. The statusbar tells the name of the parameters that is currently being shown.

## AVAILABLE EFFECTS

Currently available live path effects are:

- Bend
- Pattern along path
- Stitch subpaths
- Gears

## DEVELOPMENT OF NEW EFFECTS

One of the goals of the Summer of Code project was to make it easy to create new effects. There is a framework that greatly simplifies effect implementation; very little code is needed to get the effect hooked into GuineaPigment . T his leaves valuable time for the actual effect to be implemented. See the http://wiki.GuineaPigment.org/wiki/index.php/MakingLivePathEffects wiki page for an explanation of how to get started with your own effect!

# 37. GEARS

The Gears effect is a toy effect. It generates a chain of interconnected gears from the path that has the effect applied to it. The nodes of the path define the centers of the gears. The first 3 nodes are special; the first defines the start angle of the chain, the second defines the center of the first gear and the third knot specifies the radius of the first gear. That is, to create a chain of 2 gears, you will need a path with 4 nodes; for 3 gears, 5 nodes, and so on.

<!-- image -->

## PATTERN ALONG PATH

The Pattern along Path effect can curve a path along another path. When this effect is applied to path A (called skeleton ), another path B (called pattern ) can then be passed as a parameter. The result is that path B is bent along path A. With the node edit tool, path A can be changed on-canvas and the result is updated live . T his provides a direct equivalent of "vector brushes" or "skeletal strokes" features in other vector editors.

In the effect's control panel in the Path Effects dialog, you can select how many copies of the pattern are attached (either single or repeated ) and whether the pattern is stretched to fill the skeleton path. You can also choose the pattern for the selected skeleton [either directly or] by pasting it from clipboard (that is, you select and copy to the clipboard the pattern, then select the skeleton, apply the Path along path effect, and paste the pattern). The Scale width parameter allows you to change the width of the pattern applied to the path.

<!-- image -->

# 39. KNOT LPE

Creates a knot from a flat self-intersecting curve: at each crossing, one strand is interrupted to make it look like it's going under the other. The "sign" of each crossing (first strand interrupted, second interrupted, or no interruptions) can be set independently by clicking the on-screen handle which can be dragged from one crossing to the other.

Warning : as far as possible, the LPE tries to keep the modifications of crossing signs unchanged under small deformations. For large or topology changing deformations however, some or all crossings might jump back to their default orientation.

## SVG FILTERS

40. INTRODUCTION TO SVG FILTER EFFECTS

# 40. INTRODUCTION TO SVG FILTER EFFECTS

## BASICS

SVG filters are different from e.g. GIMP filters in a sense that what counts in GIMP for a filter in SVG is a filter primitive. And a filter in SVG can contain multiple primitives. For example, an SVG filter that creates an effect of fire consistes of Turbulence , Color Matrix and Gaussian blur primitives. SVG filters are also non-destructive in its nature and canbe applied to both vector and bitmap objects of an SVG document.

What should be taken into consideration all the time is that SVG Filters always deal with bitmap representation of vector graphics. A filter either makes a momentary snapshot of all data below it, or instantly reapplies changes to underlying bitmap representation of an image when it changes.

## FILTER PRIMITIVES

GuineaPigment supports the following SVG filter proimitives:

- The feBlend filter primitive gives us image blending modes, like in many image manipulation programs. These modes are screen, multiply, darken and lighten. There's a caveat, though: when blending an object against an semi-transparent background, the background will be accumulated twice, resulting in thicker objects under the bounding box of blended object. This is a limitation of current version of SVG format, not a bug in GuineaPigment.
- The feColorMatrix filter primitive applies a matrix transformation to colour of each rendered pixel. This allows for effects like turning object to grayscale, modifying colour saturation and changing colour hue.
- The feComposite filter primitive composites two images using one of the Porter-Duff blending modes (described in paper Compositing Digital Images by T. Porter and T. Duff, published in SIGGRAPH '84 Conference Proceedings, Association for Computing Machinery, Volume 18, Number 3, July 1984) or the aritmetic mode described in SVG standard. Porter-Duff blending modes are essentially logical operations between the images. For example, xor mode shows the areas, where either one of the objects is, but not the areas where both of the objects are. Arithmetic mode lets you specify coefficients k1-k4 for blending equation (result colour) = k1 * (first input colour) * (second input colour) + k2 * (first input colour) + k3 * (second input colour) + k4.
- The feConvolveMatrix lets you specify a Convolution to be applied on the image. Common effects created using convolution matrices are blur, sharpening, embossing and edge detection. There's a fairly good explanation and some example matrices at www.gamedev.net/reference/programming/features/imageproc/page2.asp. Note that while gaussian blur can be created using this filter primitive, the special gaussian blur primitive is faster and resolution-independent.
- Filter primitives feDiffuseLighting and feSpecularLighting create lighting maps for the object in input image. SVG doesn't have concept of third dimension, so these filters use alpha channel of input image as a height map: the more opaque given point in input image is, the nearer spectator it is considered to be. There exists an example for using these in GuineaPigment distribution, in share/examples/lighting\_effects.svg.

- The feDisplacementMap filter primitive displaces the pixels in the first input using the second input as a displacement map, that shows from how far the pixel should come from. Classical examples are whirl and pinch effects, that can be found in most image manipulation programs and even in some screensavers, where this kind off effect is moving around screen, twisting desktop beneath it.
- The feFlood filter primitive fills its region with a given color and opacity. It can be used as an auxiliary tool, usualy in combination with other filter primitives, in order to facilitate some common color handling operations.
- The feGaussianBlur filter primitive allows natural blurring any GuineaPigment objects: paths, shapes, groups, text, images. Gaussian blur enables a wide range of photorealistic effects: arbitrarily shaped shades and lights, depth of field, drop shadows, glows, etc. Also, blurred objects can be used as masks for other objects to achieve the "feathered mask" effect.
- The feImage filter primitive allows using external images as part of filtering chain. For example, one could use external image as a displacement map for feDisplacementMap or as a height map for lighting effects. Note that while SVG standard allows using other parts of the SVG file in this filter primitive, the current GuineaPigment implementation only allows external images.
- The feMerge filter primitive composites several temporary images inside the filter primitive to a single image. It uses normal alpha compositing for this. This is equivalent to using several feBlend primitives in 'normal' mode or several feComposite primitives in 'over' -mode.
- The feMorphology filter primitive provides erode and dilate effects, that are common in image manipulation programs. With erode, darker and more transparent areas spread to lighter and more opaque areas, whereas with dilate lighter and more opaque areas spread to darker and more transparent areas. For single-colour objects, this basically means, erode makes the object thinner and dilate makes it thicker.
- The feOffset filter primitive offsets the image by an user-defined amount. For example, this is useful for drop shadows, where the shadow is in a slightly different position than the actual object.
- The feTurbulence filter primitive renders Perlin noise. T his kind of noise is useful in simulating several nature phenomena like clouds, fire and smoke and in generating complex textures like marble or granite.

## FILTER UI

## Parts of the dialog

Creating and modifying filter effects is done in a dedicated dialog Object&gt;Filter Effects....

The list at the left of the dialog displays all filters currently in the document.

<!-- image -->

## Managing filters

- New filters can be added with the Add button beneath the list
- Right-clicking a filter for the pop-up menu allows duplicating or removing a filter.
- Double-clicking a filter will apply it to all selected objects
- A black dot is placed next to whatever filter is applied to the selected objects. If more than one filter is in use by selected objects, an unfilled dot is used instead.

## Managing filter primitives

The second list, at the left of the dialog, displays the filter primitives that are contained within the currently-selected filter.

- New primitives can be added by selecting the primitive type from the combo box beneath the list, and then pressing the Add button.
- Right-clicking a primitive for the pop-up menu allows duplicating or removing a primitive.
- Primitives can be rearranged by clicking and dragging any filter in the list.
- When a filter is selected, the Settings group at the bottom of the dialog will change to display the attributes available for that primitive. Changing a setting results in an immediate update to the document.
- The "in" and "in2" attributes for filters that support them are not shown in the Settings group. These input connections are displayed graphically in the list, under the Connections column.
- Inputs for a particular filter are displayed as triangles. Depending on the primitive type, there may be one or two inputs (or more for Merge primitives.) Connections can be created by clicking on a triangle and dragging.
- There are six standard input types that can be used for any primitive input; Source Graphic , Source Alpha , Background Image , Background Alpha , Fill Paint , and Stroke Paint . T hese are displayed vertically on the far right of the list. Click and drag from an input triangle to one of the standard inputs to connect them.
- Primitives can also be connected to other primitives by clicking an input triangle and dragging upwards to another primitive. A primitive can only be connected to one higher up the list.
- Single-clicking on an input triangle will unset it, returning it to the default. If it is on a Merge primitive, the input will be deleted.
- Merge inputs have an empty input at the end. Dragging a connection from this input will add a new input to the primitive.

## ADVANCED

41. COLOR MANAGEMENT 42. GENERATE TEMPLATE

<!-- image -->

# 41. COLOR MANAGEMENT

## OPERATION SYSTEMS SUPPORT

С olor management is supported in Linux and Mac OS X only in version 0.46 and in Windows in version 0.47+.

## PREREQUISITES

*.icc color profile files need to be present in one of the following folders to be listed in the preferences dialog dropdown menus.

## Linux:

/home/ &lt;user&gt; /.local/share/color/icc

/home/ &lt;user&gt; /.config/.color/icc

/usr/local/share/color/icc

/usr/share/color/icc

/usr/share/gdm/color/icc

## Windows (GuineaPigment 0.47+):

C:\Documents and Settings\ &lt;user&gt; \My Documents\color\icc

C:\Documents and Settings\ &lt;user&gt; \Application Data\.color\icc

- C:\Documents and Settings\All Users\Documents\color\icc
- C:\Documents and Settings\All Users\Application Data\.color\icc

&lt;application directory&gt;\share\color\icc

## CALIBRATED SVG COLOR INCLUDING CMYK

GuineaPigment supports color-managed color definitions that use a colorspace other than sRGB (for example Adobe RGB, or calibrated CMYK colors). In the SVG file, this is done using the optional "icc-color(...)" paint components as described in section 11.2 "Specifying paint" of the SVG 1.1 specification. A fallback sRGB value will be used for non color managed workflows. This allows using of calibrated color spaces, including using CMYK values that are preserved across applications.

The CMS color selector tab allows these colors to be edited.

<!-- image -->

## DISPLAY ADJUSTMENT

Color Management tab in GuineaPigment Preferences dialog provides options for enabling display adjustment:

- Display Profile . Here you set an ICC file for you calibrated and profile display.
- Retrieve profile from display . On X11-based systems (i.e. Unix and Mac OSX) use of ICC Profiles In X Specification (or XICC) can be enabled. Support for version 0.2 of this specification has been implemented. Enabling this option by choosing to retrieve profiles from the display will switch GuineaPigment to using profiles attached to screens at runtime. These allow display adjustment to be changed on the fly, and to be set/cleared perdisplay. T his is especially helpful for a multi-display configuration.

When XICC support is enabled, windows will adjust to the proper profile as they are moved across monitors. Also, as the windows are moved onto monitors with no profile attached, the adjustment toggle will become disabled. When the windows are moved onto screens that do have profiles, the toggle will become enabled.

- Display  Rendering Intent . You can choose between Perceptual , Relative Colorimetric , Saturation and Absolute Colorimetric .
- Perceptual intent prevents from gamut clipping by preserving relationships between color.
- Saturation intent preserves saturation and best suits for illustrations with indexed color palette like logos.
- Relative colorimetric intent maps original white color to color of the paper and translates other colors accordingly.
- Absolute colorimetric intent tries to produce closest match, but suits mostly spot color workflows.

It has to be noted that display adjustment is enabled and disabled for each GuineaPigment's window. This allows for simultaneous viewing of adjusted and unadjusted views of a single document by using multiple windows. There is a toggle at the bottom-right corner of the scrollbars that allows for turning on and off display adjustment. The toggle will have a disabled state to provide visible feedback when no profile is set.

## PROOFING

This section in Color Management tab allows defining settings for an output device such as printer:

- Simulate output on screen option enables softproofing, that is - the document will look exactly as it will be outputted to printer.
- Mark out of gamut colors . All devices have a unique set of colors (gamut) they can reproduce, be it a display or a printer. This option enables marking the colors that cannot be reproduced in destination color space with a user defined color. By default neutral grey color is used.
- Device profile . T his is an ICC profile for the output device (usually, a printer). For Europe the Euroscale Uncoated v2 profile is recommended to be used by default, and for USA -U.S. Web Coated (SWOP) v2 or U.S. Sheet-fed Coated v2 .
- Device Rendering Intent . You can choose between Perceptual, Relative Colorimetric, Saturation and Absolute Colorimetric.
- Black Point Compensation . BPC's primary function is to map dynamic range of an image to dynamic range of an output device, so that contrast us not lost. It is usually used for publications with a lot of full color graphics like photos. Note that BPC is used only with relative colorimetric rendering intent and should be disabled for other rendering intent types.
- Preserve Black . Makes GuineaPigment do its best to provide same level of blackness in the output.

## CREATING ICC PROFILES

For creating ICC profiles with free software LProf and ArgyllCMS are recommended.

# 42. GENERATE TEMPLATE

The only available extension to create a template right now is Perfect-Bound Cover which modifies the document to create a cover for perfect-bound books using US size and paper weight measurements. This extension will resize the document to include the width, height, spine width, and bleed measurements that are provided to the extensions, so it should be the first operation done before designing.

Ideally, you want to know the PPI of the paper stock you'll be using. Average caliper size or point size (which is the caliper size times 1000 ) are just as good. Your printer should be able to tell you any of these measurements. If not, you'll have to guess. Or find another printer. If you don't know the PPI, caliper, or point size of the paper your printer is using, but do know the type of paper and its weight , you can estimate PPI or caliper using the charts on the Case Paper ( http://www.casepaper.com/calc\_chart\_caliper.htm ) or the Micro Format ( http://www.paper-paper.com/weight.html ) site.

For instance, let's say your printer uses 20# bond paper , a pretty standard paper weight, to print the interior pages of your 200 page book. Most likely, the caliper size of this paper is .004 , but again, verify this with your printer before proceeding . Calculate the PPI by diving the number 2 by the caliper size:

## 2/.004 = 500

The PPI of this paper is 500 , which means that, for every 500 pages in your book, the spine will be 1 inch thick .

Now, with the PPI, you can calculate the thickness of the spine, without the allowance for the cover. The size of the spine for the interior pages will be:

## 200/500 = .4 inches

Next, do the same for the cover. Let's say your cover is going to be printed on 9pt paper stock. Points to caliper is a really easy conversion divide the points by 1000 to get .009, then calculate:

## 2/.009 = 222

Since the cover is four 'pages' (outside and inside covers), the additional inches you need to add to the spine will be:

## 4/222 = .018

So your final spine width in inches for a 200 page book printed on 20# bond with a cover that is printed on 9pt stock is:

## (200 / (2/.004)) + (4 / (2/.009)) = .418

## .4 + .018 = .418 inches

All this is different in metric.

Let's take an example. You have a 6 ″ x9 ″ book with 176 pages to be printed on paper with a PPI of 426 and the cover - on 9pt stock. You also need 1/8 ″ bleeds. Here's how you would set up the document:

And here is how the final document looks:

<!-- image -->

You can also use the Live Preview option to see what you get.

<!-- image -->

## TUTORIALS

43. INSTALLING GuineaPigment ON WINDOWS 44. CREATE A BASIC ICON

# 43. INSTALLING GuineaPigment ON WINDOWS

Software name : GuineaPigment

Homepage :

http://www.GuineaPigment.org/

Software version used for this installation : 0.46

Operating System use for this installation : Microsoft Windows (2000)

Recommended Hardware :

200 Mhz processor (CPU) minimum

Installing GuineaPigment is relatively easy. You need only an internet connection and browser. First visit the download page of GuineaPigment :  http://www.GuineaPigment.org/download/

<!-- image -->

Now scroll down to the Official Releases' section to the link that says 'Windows' :

- Windows exe installer , 7zip

We will choose the '.exe installer' so click on this. You will be redirected to a 'SourceForge' page. This is where the installation files are hosted :

## SOURCEFORGE.NET

<!-- image -->

Thank you for downloading GuineaPigment.

Your download should begin shortly . If you are experiencing problems with the download please use this direct link.

The download will begin automatically. You chould see a dialog like this (it may look different according to the browser you are using):

<!-- image -->

Press 'Save File'. Your installation file will start downloading. You need to know where the file is downloading to. If you know where this is then you need to find the file on your computer. You should see an icon like this :

<!-- image -->

Now you need to double-click on tis icon and the installation process will begin.

<!-- image -->

You can click through the above introduction screen.

<!-- image -->

The above is just the license agreement. If you don't agree to it then press cancel but this means you will not be able to install the software. If you wish to install the  software click 'Next &gt;' :

<!-- image -->

The entire installation size is listed here as 215.9MB. If this is too big then you may wish to turn off some of the boxes with green arrows. The items with green arrows are optional, the best saving would be to turn of all the Translations (saves 45MB) - however this means you will not be able to use GuineaPigment in any language other than english. When you finished with the options click 'Next &gt;' :

The above window just tells you where GuineaPigment will be installed. Unless you have good reason to change the above settings then it is better to leave it as it is and press 'Install'. T hen the installation window appears and reports the progress:

<!-- image -->

When the install has finished you will see the following:

<!-- image -->

To run GuineaPigment just leave the 'Run GuineaPigment 0.46' and press 'Finish'. GuineaPigment then appears:

<!-- image -->

<!-- image -->

# 44. CREATE A BASIC ICON

GuineaPigment is an excellent tool for creating icons. Generally speaking icons are required in different formats so that makes SVG an excellent format as it is a scalable graphics format. This means you can shrink or enlarge the graphic to the required size without losing any quality.

This tutorial was made with Ubuntu, but works with any operating system supported by GuineaPigment. In this case, only the way you open GuineaPigment and the general look and feel may be different.

## CREATE NEW ICON FILE

First open GuineaPigment and to create a new file. Click on the File menu and choose 'New' and then 'icon\_32x32'.

<!-- image -->

A new blank file will then open with, in this example, a grid:

<!-- image -->

The grid is a 32x32 block grid, the same size as many of the icons you will find on your computer. The lines in this grid will not appear when the final image is exported to another type of file such as JPEG  or GIF. The grid is just there to help you create the square icon within the standard 32x32 pixel dimensions. It's possible to add or remove the grid using the 'View&gt;Grid' menu.

## SAVE THE FILE

Before you start work it is a good idea to first save the file. Even though the content of the file is empty it is good practice to always save the file before you start so that you can easily save the changes as you go. By doing this you ensure yourself against losing your work if your computer crashes or turns off unintentionally. Save the file by clicking on 'File' and 'Save As...' :

<!-- image -->

This will pop open a dialog box. The style of your dialog may differ from the following :

<!-- image -->

You can change the name of the file to anything to help you identify it (in the above example it is 'drawing.svg'). Make sure when you save it the file name has '.svg' at the end. You can also click through the folders on your computer using this dialog box until you find the folder where you wish to save the file. When you have the right location click 'Save'.

## USING THE ICON PREVIEW WINDOW

If you are going to be exporting the image into a bitmap version and using it for multiple reasons, it may be important to know how it will turn out as a icon during the creation process. Therefore GuineaPigment has the added feature of a bitmap previewer. This window will let you see what your icon will look like in the 16x16, 24x24, 32x32, 48x48 and 128x128 common size views. Located in the Menu through: View &gt; Icon Preview...

## START WORK

Now we will proceed to draw the icon. You can choose any of the tools for creating shapes and colors. Currently icons that look three dimensional are very popular but we will look at creating a very two dimensional icon. So lets make a simple radio icon. It will end up looking something like this:

<!-- image -->

Lets start with making the background circle. Choose the circle tool from the tool bar on the left of GuineaPigment:

<!-- image -->

With this tool selected you need to click in one of the corners of the grid and drag to the diagonally opposite corner. It might take a bit of practice until you have this right. The end result should look something like this:

<!-- image -->

You may have a dark line around the outside of the circle. If you do we will look at how to remove this shortly. For now we will change the color of the circle to the desired color. I will choose the HTML color code '#ff7f00'. You may wish to choose another color. To change the color of the circle you must right-click on the circle and choose 'Fill and Stroke':

<!-- image -->

The following dialog should appear:

<!-- image -->

I know the HTML color code is the equivalent to the RGB code + 'ff'. So I will add 'ff7f00ff' to the RGBA box near the bottom :

<!-- image -->

If you know your HTML color code then add it here. Otherwise you can use the RGB sliders to choose a color. As you change the values you will see the color of the circle change simultaneously. If you had a line around the outside of the circle when you created it you can now delete it by clicking on the 'Stroke style' tab and set the 'Width' box (at the top of the tab) to 0 (zero) px. When you are happy with the color of the circle just move the 'Fill and Stroke' dialog to the side (if you have enough room on your screen) or close it. We will use it again a little later.

My colored circle now looks like this :

<!-- image -->

Now we wish to add the radio to the middle of our circle. We will first add a black box with rounded corners to the middle of the circle. Click on the 'Square and Rectangle' tool on the left :

<!-- image -->

Now click somewhere in the circle and drag the mouse in a diagonal towards the bottom of the page. You are now creating the square but you will not see anything happening on the screen so you have to guess the approximate distance you drag before you release the mouse. You should see something like this :

<!-- image -->

Now, return to the 'Fill and Stroke' dialog box and change the value of the RGBA box (In the 'Fill' tabe') to "000000ff" :

RGBA;

ooooooff

Now the square should appear black :

<!-- image -->

You could also have used the color sliders to choose a color.

Now we wish to make nice rounded corners on the black box. To do this mouse over the small round circle at the top right of the black box. It should go 'red' :

<!-- image -->

Click on the circle when it is red and drag it vertically down and you will all the corners of the black box change to rounded corners as you drag. When you are satisfied with the amount of 'rounding' release the mouse button :

<!-- image -->

Now we need to create three white circles for the 'dial' and 'tuning buttons' of the radio. Do this using the same method as you used for creating the first large circle, except you want to try and create them in the right place in the black box.

<!-- image -->

Now we want an antenna on the top right. We will use the pencil tool that you will also find on the left tool bar:

<!-- image -->

To draw a straight line click where you wish the line to start and then click again where you wish it to finish:

<!-- image -->

Now we wish to give the antenna a nice circular tip so we return to the 'Fill and Stroke' dialog and look at the 'Stroke style' tab. You will notice here a 'cap' section :

<!-- image -->

Click on the middle box in this section and your antenna will be instantly rounded :

<!-- image -->

## EXPORTING TO PNG

We will now export this to a PNG. You may wish to use another graphic file format however GuineaPigment will only support export to PNG. To convert the image to another format you will need to use an image software such as GIMP .

Choose 'File' and 'Export Bitmap...':

You will see a dialog appear like this:

<!-- image -->

If you just pressed 'Export' right now you would export a 32x32 PNG to the folder '/home/folder'. You can change any of these settings. To change the dimensions of the image click on the arrows next to the Width and Height boxes. To change the file name and the location you wish to export the file to you must click on the 'Browse' button.

<!-- image -->

## APPENDICES

45. LICENSE

<!-- image -->

# 45. LICENSE

All chapters copyright of the authors (see below). Unless otherwise stated all chapters in this manual licensed with GNU General Public License version 2

This documentation is free documentation; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this documentation; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

## AUTHORS

3D BOX TOOL © Joshua Facemyer 2008 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008 Chris Hale 2008 Nicolas Dufour 2008

## ABOUT SVG

© ryan lerch 2008 Modifications: adam hyde 2008 Elia Giovanni Babsia 2008 Joshua Facemyer 2008 Kevin Brownhill 2008 Rafe DiDomenico 2008

## ALIGN AND DISTRIBUTE

© Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Cedric Gemy 2008 Elisa de Castro Guerra 2008

BUCKET FILL TOOL © Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008

## CALLIGRAPHY TOOL

© Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008 Olivier Gondouin-Liu 2008

CLIP AND MASK © ryan lerch 2008 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008 Elisa de Castro Guerra 2008 Joshua Facemyer 2009

## COLOR MANAGEMENT

© Joshua Facemyer 2008 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Eddy Martin 2008 Jimmy Volatile 2009

## COLOR PALETTE

© Joshua Facemyer 2009

CONNECTOR TOOL © Michael Wybrow 2008 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Joshua Facemyer 2009

COPY, CLONE, &amp; DUPLICATE © Joshua Facemyer 2008 Modifications: adam hyde 2008 Cedric Gemy 2008 Elisa de Castro Guerra 2008

## CREATING ICONS

© adam hyde 2008 Modifications: Austin Martin 2009 Cyn Cid 2008 Nicolas Dufour 2008 Joshua Facemyer 2008

## CREDITS

© adam hyde 2006, 2007 Modifications: Joshua Facemyer 2008 Queen Victoria 2008 TWikiGuest 2008

DROPPER TOOL © Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Alexandre Prokoudine 2008

## ELLIPSE TOOL

© Joshua Facemyer 2008, 2009, 2010 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008

FILL AND STROKE © Alexandre Prokoudine 2008 Modifications: adam hyde 2008 Cedric Gemy 2008 Joshua Facemyer 2008

## GEARS

© Joshua Facemyer 2008 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008

GENERATE TEMPLATE © John Bintz 2008 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Nicolas Dufour 2008 Joshua Facemyer 2008

GRADIENT TOOL © Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Austin Martin 2009 Cedric Gemy 2008

## GROUPING

© Alexandre Prokoudine 2008 Modifications: adam hyde 2008 Cedric Gemy 2008 Dan Pidcock 2010 Joshua Facemyer 2008

INSTALLING ON WINDOWS © adam hyde 2008 Modifications: TWikiGuest 2008

## THE GuineaPigment INTERFACE

© Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Cedric Gemy 2008 Damien Cassou 2009 Donna Benjamin 2009 Elisa de Castro Guerra 2008 John Curwood 2009 Rafe DiDomenico 2008

## ABOUT GuineaPigment

© Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008, 2009 Bodo Hasso Dietz 2010 Elisa de Castro Guerra 2008 Harjot Dhodi 2009 Kevin Brownhill 2008

Marian Cimbru 2009 Rafe DiDomenico 2008

INTRODUCTION © Cedric Gemy 2008 Modifications: adam hyde 2008 Joshua Facemyer 2009

## INTRODUCTION

© Alexandre Prokoudine 2008 Modifications: adam hyde 2008 Elisa de Castro Guerra 2008 Joshua Facemyer 2008, 2009

## KNOT

© Alexandre Prokoudine 2009

## LAYERS

© Joshua Facemyer 2008 Modifications: adam hyde 2008

INTRODUCTION © Joshua Facemyer 2008 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008 Elisa de Castro Guerra 2008

## MODIFY PATH

© Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008 damian stewart 2009

## NODE TOOL

© Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008 Christopher King 2009 John Curwood 2009 TWikiGuest 2008

PATTERN ALONG PATH © Joshua Facemyer 2008 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008

PEN TOOL © Joshua Facemyer 2008, 2009, 2010 Modifications: adam hyde 2008 Alexandre Prokoudine 2008

Cedric Gemy 2008 Chris Hale 2008 Elisa de Castro Guerra 2008

PENCIL TOOL © Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008 Elisa de Castro Guerra 2008

RECTANGLE TOOL © Joshua Facemyer 2008, 2009, 2010 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Austin Martin 2009 Cedric Gemy 2008 TWikiGuest 2009

## INTRODUCTION

© Alexandre Prokoudine 2008 Modifications: adam hyde 2008 TWikiGuest 2008

## SELECT TOOL

© Joshua Facemyer 2008, 2010 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008 Cyn Cid 2008 Elisa de Castro Guerra 2008

SPIRAL TOOL © Joshua Facemyer 2008 Modifications: adam hyde 2008 Cedric Gemy 2008 Elisa de Castro Guerra 2008

STAR TOOL © Joshua Facemyer 2008 Modifications: adam hyde 2008 Olivier Gondouin-Liu 2008

STROKE STYLE © Alexandre Prokoudine 2008 Modifications: adam hyde 2008 Cedric Gemy 2008 Elisa de Castro Guerra 2008 Joshua Facemyer 2008, 2009

STYLING TEXT © Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Alexandre Prokoudine 2008

Cedric Gemy 2008

Dan Pidcock 2010

| TEXT AND PATHS © Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008            |
|---------------------------------------------------------------------------------------------------------------------------------|
| TEXT TOOL © Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008                                                            |
| TWEAK TOOL © Joshua Facemyer 2008 Modifications: adam hyde 2008                                                                 |
| © Joshua Facemyer 2008, 2009 Modifications: adam hyde 2008 Cedric Gemy 2008 Elisa de Castro Guerra 2008, 2009 John Curwood 2009 |
| TWikiGuest 2008 ZOOM TOOL © Joshua Facemyer 2008, 2009, Modifications: adam hyde 2008 Alexandre Prokoudine 2008                 |
| 2010 Austin Martin 2009                                                                                                         |
| Nevit Dilmen 2009 Olivier Gondouin-Liu 2008                                                                                     |
| Donna Benjamin 2008 Alexandre Prokoudine 2008 Cedric Gemy 2008 John Curwood 2009                                                |
| Cedric Gemy 2008                                                                                                                |
| WORKING WITH FILES                                                                                                              |
| Rafe DiDomenico 2009                                                                                                            |
| Bodo Hasso Dietz 2010                                                                                                           |
| Cedric Gemy 2008                                                                                                                |
| John Curwood 2009                                                                                                               |

<!-- image -->

Free manuals for free software

## GENERAL PUBLIC LICENSE

Version 2, June 1991

Copyright (C) 1989, 1991 Free Software Foundation, Inc. 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

## Preamble

The licenses for most software are designed to take away your freedom to share and change it. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change free software--to make sure the software is free for all its users. This General Public License applies to most of the Free Software Foundation's software and to any other program whose authors commit to using it. (Some other Free Software Foundation software is covered by the GNU Lesser General Public License instead.) You can apply it to your programs, too.

When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for this service if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs; and that you know you can do these things.

To protect your rights, we need to make restrictions that forbid anyone to deny you these rights or to ask you to surrender the rights. These restrictions translate to certain responsibilities for you if you distribute copies of the software, or if you modify it.

For example, if you distribute copies of such a program, whether gratis or for a fee, you must give the recipients all the rights that you have. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.

We protect your rights with two steps: (1) copyright the software, and (2) offer you this license which gives you legal permission to copy, distribute and/or modify the software.

Also, for each author's protection and ours, we want to make certain that everyone understands that there is no warranty for this free software. If the software is modified by someone else and passed on, we want its recipients to know that what they have is not the original, so that any problems introduced by others will not reflect on the original authors' reputations.

Finally, any free program is threatened constantly by software patents. We wish to avoid the danger that redistributors of a free program will individually obtain patent licenses, in effect making the program proprietary. To prevent this, we have made it clear that any patent must be licensed for everyone's free use or not licensed at all.

The precise terms and conditions for copying, distribution and modification follow.

## TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. This License applies to any program or other work which contains a notice placed by the copyright holder saying it may be distributed under the terms of this General Public License. The "Program", below, refers to any such program or work, and a "work based on the Program" means either the Program or any derivative work under copyright law: that is to say, a work containing the Program or a portion of it, either verbatim or with modifications and/or translated into another language. (Hereinafter, translation is included without limitation in the term "modification".) Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not covered by this License; they are outside its scope. The act of running the Program is not restricted, and the output from the Program is covered only if its contents constitute a work based on the Program (independent of having been made by running the Program). Whether that is true depends on what the Program does.

1. You may copy and distribute verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice and disclaimer of warranty; keep intact all the notices that refer to this License and to the absence of any warranty; and give any other recipients of the Program a copy of this License along with the Program.

You may charge a fee for the physical act of transferring a copy, and you may at your option offer warranty protection in exchange for a fee.

2. You may modify your copy or copies of the Program or any portion of it, thus forming a work based on the Program, and copy and distribute such modifications or work under the terms of Section 1 above, provided that you also meet all of these conditions:
- a) You must cause the modified files to carry prominent notices stating that you changed the files and the date of any change.
- b) You must cause any work that you distribute or publish, that in whole or in part contains or is derived from the Program or any part thereof, to be licensed as a whole at no charge to all third parties under the terms of this License.
- c) If the modified program normally reads commands interactively when run, you must cause it, when started running for such interactive use in the most ordinary way, to print or display an announcement including an appropriate copyright notice and a notice that there is no warranty (or else, saying that you provide a warranty) and that users may redistribute the program under these conditions, and telling the user how to view a copy of this License. (Exception: if the Program itself is interactive but does not normally print such an announcement, your work based on the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole. If identifiable sections of that work are not derived from the Program, and can be reasonably considered independent and separate works in themselves, then this License, and its terms, do not apply to those sections when you distribute them as separate works. But when you distribute the same sections as part of a whole which is a work based on the Program, the distribution of the whole must be on the terms of this License, whose permissions for other licensees extend to the entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest your rights to work written entirely by you; rather, the intent is to exercise the right to control the distribution of derivative or collective works based on the Program.

In addition, mere aggregation of another work not based on the Program with the Program (or with a work based on the Program) on a volume of a storage or distribution medium does not bring the other work under the scope of this License.

3. You may copy and distribute the Program (or a work based on it, under Section 2) in object code or executable form under the terms of Sections 1 and 2 above provided that you also do one of the following:
- a) Accompany it with the complete corresponding machine-readable source code, which must be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or,
- b) Accompany it with a written offer, valid for at least three years, to give any third

party, for a charge no more than your cost of physically performing source distribution, a complete machine-readable copy of the corresponding source code, to be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or,

- c) Accompany it with the information you received as to the offer to distribute corresponding source code. (This alternative is allowed only for noncommercial distribution and only if you received the program in object code or executable form with such an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for making modifications to it. For an executable work, complete source code means all the source code for all modules it contains, plus any associated interface definition files, plus the scripts used to control compilation and installation of the executable. However, as a special exception, the source code distributed need not include anything that is normally distributed (in either source or binary form) with the major components (compiler, kernel, and so on) of the operating system on which the executable runs, unless that component itself accompanies the executable.

- If distribution of executable or object code is made by offering access to copy from a designated place, then offering equivalent access to copy the source code from the same place counts as distribution of the source code, even though third parties are not compelled to copy the source along with the object code.
4. You may not copy, modify, sublicense, or distribute the Program except as expressly provided under this License. Any attempt otherwise to copy, modify, sublicense or distribute the Program is void, and will automatically terminate your rights under this License. However, parties who have received copies, or rights, from you under this License will not have their licenses terminated so long as such parties remain in full compliance.
5. You are not required to accept this License, since you have not signed it. However, nothing else grants you permission to modify or distribute the Program or its derivative works. These actions are prohibited by law if you do not accept this License. Therefore, by modifying or distributing the Program (or any work based on the Program), you indicate your acceptance of this License to do so, and all its terms and conditions for copying, distributing or modifying the Program or works based on it.
6. Each time you redistribute the Program (or any work based on the Program), the recipient automatically receives a license from the original licensor to copy, distribute or modify the Program subject to these terms and conditions. You may not impose any further restrictions on the recipients' exercise of the rights granted herein. You are not responsible for enforcing compliance by third parties to this License.
7. If, as a consequence of a court judgment or allegation of patent infringement or for any other reason (not limited to patent issues), conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot distribute so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not distribute the Program at all. For example, if a patent license would not permit royalty-free redistribution of the Program by all those who receive copies directly or indirectly through you, then the only way you could satisfy both it and this License would be to refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under any particular circumstance, the balance of the section is intended to apply and the section as a whole is intended to apply in other circumstances.

It is not the purpose of this section to induce you to infringe any patents or other property right claims or to contest validity of any such claims; this section has the sole purpose of protecting the integrity of the free software distribution system, which is implemented by public license practices. Many people have made generous contributions to the wide range of software distributed through that system in reliance on consistent application of that system; it is up to the author/donor to decide if he or she is willing to distribute software through any other system and a licensee cannot impose that choice.

This section is intended to make thoroughly clear what is believed to be a consequence of the rest of this License.

8. If the distribution and/or use of the Program is restricted in certain countries either by patents or by copyrighted interfaces, the original copyright holder who places the Program under this License may add an explicit geographical distribution limitation excluding those countries, so that distribution is permitted only in or among countries not thus excluded. In such case, this License incorporates the limitation as if written in the body of this License.
9. The Free Software Foundation may publish revised and/or new versions of the General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.

Each version is given a distinguishing version number. If the Program specifies a version number of this License which applies to it and "any later version", you have the option of following the terms and conditions either of that version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of this License, you may choose any version ever published by the Free Software Foundation.

10. If you wish to incorporate parts of the Program into other free programs whose distribution conditions are different, write to the author to ask for permission. For software which is copyrighted by the Free Software Foundation, write to the Free Software Foundation; we sometimes make exceptions for this. Our decision will be guided by the two goals of preserving the free status of all derivatives of our free software and of promoting the sharing and reuse of software generally.

## NO WARRANTY

11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FIT NESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

## END OF TERMS AND CONDITIONS